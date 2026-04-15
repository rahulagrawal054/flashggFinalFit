import ROOT
import os
import json
import logging
from optparse import OptionParser

# --- Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("BiasStudy")

def rooiter(x):
    """Iterator for RooFit collections."""
    iterator = x.iterator()
    ret = iterator.Next()
    while ret:
        yield ret
        ret = iterator.Next()

def get_options():
    parser = OptionParser(usage="usage: %prog [options]", description="Bias study wrapper for CMS Higgs Combine")

    # Input/Output Settings
    parser.add_option('--inputWSFile', dest='inputWSFile', default='Datacard.root',
                      help="Input workspace file (default: %default)")
    parser.add_option('--MH', dest='MH', default='125.38',
                      help="Higgs mass hypothesis (default: %default)")

    parser.add_option('--POI', dest='POI', default='r_ttH',
                      help="Parameter of interest (default: %default)")
    
    # NEW: Added POI Range argument to prevent boundary smashing!
    parser.add_option('--poiRange', dest='poiRange', default='-50,50',
                      help="Parameter ranges for POI, e.g., -800,800 (default: %default)")

    # Changed default seed to 12345 to match combine defaults safely
    parser.add_option('--seed', dest='seed', default='12345',
                      help="Random seed (default: %default)")

    # Physics Settings
    parser.add_option('--nToys', dest='nToys', default=20000, type='int',
                      help="Number of toys to generate/fit (default: %default)")

    # Execution Control
    parser.add_option('--mode', dest='mode', default="setup",
                      choices=['setup', 'generate', 'fixed', 'envelope'],
                      help="Operating mode: setup, generate, fixed, envelope")
    parser.add_option('--dryRun', dest='dryRun', action='store_true', default=False,
                      help="Print commands without executing them")

    return parser.parse_args()

class BiasRunner:
    def __init__(self, opt):
        self.opt = opt
        
        # UPGRADED: Added robustFit and Fallback algorithm for maximum stability
        self.common_rtd = (
            "--cminDefaultMinimizerStrategy 1 "
            "--cminFallbackAlgo Minuit2,0:0.1 "
            "--X-rtd MINIMIZER_freezeDisassociatedParams "
            "--X-rtd MINIMIZER_multiMin_hideConstants "
            "--X-rtd MINIMIZER_multiMin_maskConstraints "
            "--X-rtd MINIMIZER_multiMin_maskChannels=2"
        )

    def run_command(self, cmd):
        """Helper to log and execute shell commands."""
        logger.info(f"Executing: {cmd}")
        if not self.opt.dryRun:
            os.system(cmd)
        else:
            logger.info("Dry-run enabled: skipping execution.")

    def setup(self):
        logger.info("Starting Setup: Extracting PDF indices and performing initial fit.")
        f = ROOT.TFile.Open(self.opt.inputWSFile)
        w = f.Get("w")
        if not w:
            logger.error(f"Could not find workspace 'w' in {self.opt.inputWSFile}")
            return

        pdf_indices = [cat.GetName() for cat in rooiter(w.allCats()) if "pdfindex" in cat.GetName()]
        f.Close()

        if not pdf_indices:
            logger.warning("No PDF indices found in the workspace. Is the envelope method configured?")
        else:
            logger.info(f"Found {len(pdf_indices)} PDF indices: {', '.join(pdf_indices)}")

        pdf_index_str = ",".join(pdf_indices)
        
        # UPGRADED: Injected the --setParameterRanges here too
        cmd = (
            f"combine -m {self.opt.MH} -d {self.opt.inputWSFile} -M MultiDimFit "
            f"--robustFit 1 {self.common_rtd} "
            f"--setParameterRanges {self.opt.POI}={self.opt.poiRange} "
            f"--setParameters MH={self.opt.MH},{self.opt.POI}=0 "
            f"--freezeParameters allConstrainedNuisances,MH,{self.opt.POI} "
            f"-n _initial --saveWorkspace "
            f"--saveSpecifiedIndex {pdf_index_str}"
        )
        self.run_command(cmd)

        if self.opt.dryRun: return

        res_file = f"higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root"
        if not os.path.exists(res_file):
            logger.error(f"Fit output {res_file} not found.")
            return

        f_res = ROOT.TFile.Open(res_file)
        tree = f_res.Get("limit")
        tree.GetEntry(0)
        try:
            best_fits = {idx: getattr(tree, idx) for idx in pdf_indices}
            with open("pdfindex.json", "w") as jf:
                json.dump(best_fits, jf, indent=4)
        except AttributeError as e:
            logger.error(f"Failed to find expected branch: {e}")
        finally:
            f_res.Close()

    def generate(self):
        logger.info(f"Generating {self.opt.nToys} toys using POI: {self.opt.POI}")
        cmd = (
            f"combine -m {self.opt.MH} -d higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root "
            f"-M GenerateOnly "
            f"--setParameters MH={self.opt.MH},{self.opt.POI}=0 "
            f"--freezeParameters allConstrainedNuisances,MH "
            f"-n _toy_{self.opt.nToys} --saveToys --snapshotName MultiDimFit "
            f"-t {self.opt.nToys} -s {self.opt.seed} "
            f"--toysNoSystematics"
        )
        self.run_command(cmd)

    def run_significance(self, mode_type):
        logger.info(f"Running Significance: {mode_type.upper()} mode using POI: {self.opt.POI}")

        params = f"MH={self.opt.MH},{self.opt.POI}=0"
        freeze = "allConstrainedNuisances,MH"

        if mode_type == "fixed":
            with open("pdfindex.json", "r") as jf:
                pdf_bf = json.load(jf)
            pdf_params = ",".join([f"{k}={int(v)}" for k, v in pdf_bf.items()])
            pdf_freeze = ",".join(pdf_bf.keys())
            params += "," + pdf_params
            freeze += "," + pdf_freeze

        # UPGRADED: Fixed the seed bug and injected the POI Ranges!
        toy_file = f"higgsCombine_toy_{self.opt.nToys}.GenerateOnly.mH{self.opt.MH}.{self.opt.seed}.root"
        
        cmd = (
            f"combine -m {self.opt.MH} -d higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root "
            f"-M Significance --snapshotName MultiDimFit {self.common_rtd} "
            f"--setParameterRanges {self.opt.POI}={self.opt.poiRange} "
            f"--setParameters {params} --freezeParameters {freeze} "
            f"-n _{mode_type}_{self.opt.nToys} -t {self.opt.nToys} "
            f"--toysFile {toy_file} "
            f"--X-rtd ADDNLL_RECURSIVE=1 --toysNoSystematics"
        )

        self.run_command(cmd)

        if not self.opt.dryRun:
            self.run_command(f"mv higgsCombine_{mode_type}_* fit_{mode_type}.root")

if __name__ == "__main__":
    (options, args) = get_options()
    runner = BiasRunner(options)

    if options.mode == "setup":
        runner.setup()
    elif options.mode == "generate":
        runner.generate()
    elif options.mode in ["fixed", "envelope"]:
        runner.run_significance(options.mode)
