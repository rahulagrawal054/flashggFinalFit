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

    parser.add_option('--seed', dest='seed', default='-1', 
                      help="seed (default: %default)")
    
    # Physics Settings
    parser.add_option('--initial-fit-param', dest='initial_fit_param', default='lumi_13TeV_uncorrelated_2016', 
                      help="Nuisance parameter to use for the initial fit (default: %default)")
    parser.add_option('--nToys', dest='nToys', default=2000, type='int', 
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
        self.common_rtd = (
            "--cminDefaultMinimizerStrategy 0 "
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
        """
        Extracts PDF indices from the workspace and runs an initial MultiDimFit 
        to determine the background-only best-fit state.
        """
        logger.info("Starting Setup: Extracting PDF indices and performing initial fit.")
        
        # 1. Open Workspace and find pdfindex categories
        f = ROOT.TFile.Open(self.opt.inputWSFile)
        w = f.Get("w")
        if not w:
            logger.error(f"Could not find workspace 'w' in {self.opt.inputWSFile}")
            return

        # Extract all category names containing 'pdfindex'
        pdf_indices = [cat.GetName() for cat in rooiter(w.allCats()) if "pdfindex" in cat.GetName()]
        f.Close()
        
        if not pdf_indices:
            logger.warning("No PDF indices found in the workspace. Is the envelope method configured?")
        else:
            logger.info(f"Found {len(pdf_indices)} PDF indices: {', '.join(pdf_indices)}")

        # 2. Construct the Combine Command
        # Using self.opt.POI ensures we fit the correct parameter (e.g., r_tH)
        pdf_index_str = ",".join(pdf_indices)
        cmd = (
            f"combine -m {self.opt.MH} -d {self.opt.inputWSFile} -M MultiDimFit "
            f"{self.common_rtd} "
            f"--setParameters MH={self.opt.MH},{self.opt.POI}=0 "
            f"--freezeParameters MH,{self.opt.POI} "
            f"-n _initial --saveWorkspace "
            f"--saveSpecifiedIndex {pdf_index_str}"
        )
        
        self.run_command(cmd)

        # 3. Handle Dry Run or missing output gracefully
        if self.opt.dryRun:
            logger.info("Dry-run mode: Skipping result extraction and JSON generation.")
            return

        res_file = f"higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root"
        if not os.path.exists(res_file):
            logger.error(f"Fit output {res_file} not found. Check if the combine command failed.")
            return

        # 4. Extract best fit values for the PDF Envelope
        f_res = ROOT.TFile.Open(res_file)
        tree = f_res.Get("limit")
        if not tree or tree.GetEntries() == 0:
            logger.error("The limit tree is missing or empty. Fit may have failed to converge.")
            f_res.Close()
            return

        tree.GetEntry(0)
        try:
            best_fits = {idx: getattr(tree, idx) for idx in pdf_indices}
            with open("pdfindex.json", "w") as jf:
                json.dump(best_fits, jf, indent=4)
            logger.info("Successfully saved best-fit PDF indices to pdfindex.json")
        except AttributeError as e:
            logger.error(f"Failed to find expected branch in results file: {e}")
        finally:
            f_res.Close()

    
    def generate(self):
        """
        Generates background-only toys based on the best-fit snapshot
        from the setup phase.
        """
        logger.info(f"Generating {self.opt.nToys} toys using POI: {self.opt.POI}")

        # 1. Build the command
        # Replace --expectSignal with explicit POI=0 in setParameters
        # Added --toysNoSystematics to handle the floating parameter error
        cmd = (
            f"combine -m {self.opt.MH} -d higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root "
            f"-M GenerateOnly "
            f"--setParameters MH={self.opt.MH},{self.opt.POI}=0 "
            f"--freezeParameters MH "
            f"-n _toy_{self.opt.nToys} --saveToys --snapshotName MultiDimFit "
            f"-t {self.opt.nToys} -s {self.opt.seed} "
            f"--toysNoSystematics"
        )

        # 2. Execute generation
        self.run_command(cmd)

        # 3. Rename output for consistency in the next steps
        # We check for dryRun here to avoid 'File Not Found' errors in the log
        if not self.opt.dryRun:
            None
            #self.run_command(f"mv higgsCombine_toy_* toys.root")
        else:
            logger.info("Dry-run: Skipping file rename (mv higgsCombine_toy_* toys.root)")

    def run_significance(self, mode_type):
        """
        Calculates significance for each toy. 
        'fixed' locks the background model; 'envelope' lets it float.
        """
        logger.info(f"Running Significance: {mode_type.upper()} mode using POI: {self.opt.POI}")
        
        # Base parameters: set the POI to 0 and freeze MH
        params = f"MH={self.opt.MH},{self.opt.POI}=0"
        freeze = "MH"

        # If 'fixed', we must also freeze the PDF index to the 'Best Fit' from data
        if mode_type == "fixed":
            if not os.path.exists("pdfindex.json"):
                logger.error("pdfindex.json not found! You must run --mode setup first.")
                return
            
            with open("pdfindex.json", "r") as jf:
                pdf_bf = json.load(jf)
            
            # Add the specific PDF indices to the command
            # e.g., pdfindex_tH_lep_1_13TeV=3
            pdf_params = ",".join([f"{k}={int(v)}" for k, v in pdf_bf.items()])
            pdf_freeze = ",".join(pdf_bf.keys())
            
            params += "," + pdf_params
            freeze += "," + pdf_freeze

        # Construct the final Combine command
        cmd = (
            f"combine -m {self.opt.MH} -d higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root "
            f"-M Significance --snapshotName MultiDimFit {self.common_rtd} "
            f"--setParameters {params} --freezeParameters {freeze} "
            f"-n _{mode_type}_{self.opt.nToys} -t {self.opt.nToys} --toysFile higgsCombine_toy_{self.opt.nToys}.GenerateOnly.mH125.38.12345.root "
            f"--X-rtd ADDNLL_RECURSIVE=1 --toysNoSystematics"
        )
        
        self.run_command(cmd)
        
        # Clean up the output filename
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
