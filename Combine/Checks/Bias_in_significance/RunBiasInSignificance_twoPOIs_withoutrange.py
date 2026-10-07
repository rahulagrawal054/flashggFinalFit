import ROOT
import os
import json
import logging
from optparse import OptionParser

# The two named signal-strength POIs in this model. Fixed by the physics
# model, not user-configurable.
POIS = ['r_ttH', 'r_tHq']


def rooiter(x):
    """Iterator for RooFit collections."""
    iterator = x.iterator()
    ret = iterator.Next()
    while ret:
        yield ret
        ret = iterator.Next()


def get_options():
    parser = OptionParser(usage="usage: %prog [options]",
                           description="Two-POI bias study wrapper for CMS Higgs Combine (ttH/tHq)")

    # Input/Output Settings
    parser.add_option('--inputWSFile', dest='inputWSFile', default='Datacard.root',
                       help="Input workspace file (default: %default)")
    parser.add_option('--MH', dest='MH', default='125.08',
                       help="Higgs mass hypothesis (default: %default)")
    parser.add_option('--seed', dest='seed', default='12345',
                       help="Toy generation seed, fixed for reproducibility (default: %default)")
    parser.add_option('--nToys', dest='nToys', default=2000, type='int',
                       help="Number of toys to generate/fit (default: %default)")

    # Which POI to test (only meaningful for fixed/envelope modes)
    parser.add_option('--POI', dest='POI', default=None, choices=POIS,
                       help="POI to compute significance for in fixed/envelope mode: one of %s" % POIS)

    # Output folder naming: <outDir>/<label>_<nToys>toys/
    parser.add_option('--label', dest='label', default='allCats',
                       help="Identifier for this run (e.g. 'allCats' or a single category name), "
                            "used to name the output folder (default: %default)")
    parser.add_option('--outDir', dest='outDir', default='.',
                       help="Base directory under which the output folder is created (default: %default)")

    # Execution Control
    parser.add_option('--mode', dest='mode', default="setup",
                       choices=['setup', 'generate', 'fixed', 'envelope'],
                       help="Operating mode: setup, generate, fixed, envelope")
    parser.add_option('--dryRun', dest='dryRun', action='store_true', default=False,
                       help="Print commands without executing them")

    return parser.parse_args()


def setup_logging(out_dir, mode, seed):
    """Console logging plus a file handler inside the run's output folder,
    named per mode AND per seed - so parallel (condor) jobs running the same
    mode with different seeds never write to the same log file."""
    logger = logging.getLogger("BiasStudy")
    logger.setLevel(logging.INFO)
    logger.handlers = []  # avoid duplicate handlers if this is ever called twice in one process

    fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%H:%M:%S')

    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)

    log_path = os.path.join(out_dir, f"bias_study_{mode}_seed{seed}.log")
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger


class BiasRunner:
    def __init__(self, opt, out_dir, logger):
        self.opt = opt
        self.out_dir = out_dir
        self.logger = logger
        # Resolved once up front: everything below executes with out_dir as
        # the working directory, so any relative path given on the command
        # line (e.g. ../Datacard/foo.root) must be made absolute first.
        self.abs_ws_file = os.path.abspath(opt.inputWSFile)
        self.common_rtd = (
            "--cminDefaultMinimizerStrategy 0 "
            "--X-rtd MINIMIZER_freezeDisassociatedParams "
            "--X-rtd MINIMIZER_multiMin_hideConstants "
            "--X-rtd MINIMIZER_multiMin_maskConstraints "
            "--X-rtd MINIMIZER_multiMin_maskChannels=2"
        )

    def run_command(self, cmd):
        """Log and execute a command with out_dir as the working directory,
        so every file combine writes lands inside that one folder."""
        self.logger.info(f"Executing (in {self.out_dir}): {cmd}")
        if not self.opt.dryRun:
            os.system(f"cd {self.out_dir} && {cmd}")
        else:
            self.logger.info("Dry-run enabled: skipping execution.")

    def setup(self):
        """
        Extracts PDF indices from the workspace and runs an initial background-only
        MultiDimFit (both r_ttH and r_tHq frozen to 0) to establish the snapshot
        everything downstream is built from.
        """
        self.logger.info("Starting Setup: Extracting PDF indices and performing initial fit.")

        # 1. Open Workspace and find pdfindex categories
        f = ROOT.TFile.Open(self.abs_ws_file)
        w = f.Get("w")
        if not w:
            self.logger.error(f"Could not find workspace 'w' in {self.abs_ws_file}")
            return

        pdf_indices = [cat.GetName() for cat in rooiter(w.allCats()) if "pdfindex" in cat.GetName()]
        f.Close()

        if not pdf_indices:
            self.logger.warning("No PDF indices found in the workspace. Is the envelope method configured?")
        else:
            self.logger.info(f"Found {len(pdf_indices)} PDF indices: {', '.join(pdf_indices)}")

        # 2. Construct the Combine command (both POIs frozen to 0: background-only truth)
        pdf_index_str = ",".join(pdf_indices)
        poi_set = ",".join(f"{p}=0" for p in POIS)
        poi_freeze = ",".join(POIS)
        cmd = (
            f"combine -m {self.opt.MH} -d {self.abs_ws_file} -M MultiDimFit "
            f"{self.common_rtd} "
            f"--setParameters MH={self.opt.MH},{poi_set} "
            f"--freezeParameters MH,{poi_freeze} "
            f"-n _initial --saveWorkspace "
            f"--saveSpecifiedIndex {pdf_index_str}"
        )

        self.run_command(cmd)

        if self.opt.dryRun:
            self.logger.info("Dry-run mode: Skipping result extraction and JSON generation.")
            return

        res_file = os.path.join(self.out_dir, f"higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root")
        if not os.path.exists(res_file):
            self.logger.error(f"Fit output {res_file} not found. Check if the combine command failed.")
            return

        f_res = ROOT.TFile.Open(res_file)
        tree = f_res.Get("limit")
        if not tree or tree.GetEntries() == 0:
            self.logger.error("The limit tree is missing or empty. Fit may have failed to converge.")
            f_res.Close()
            return

        tree.GetEntry(0)
        try:
            best_fits = {idx: getattr(tree, idx) for idx in pdf_indices}
            pdfindex_path = os.path.join(self.out_dir, "pdfindex.json")
            with open(pdfindex_path, "w") as jf:
                json.dump(best_fits, jf, indent=4)
            self.logger.info(f"Successfully saved best-fit PDF indices to {pdfindex_path}")
        except AttributeError as e:
            self.logger.error(f"Failed to find expected branch in results file: {e}")
        finally:
            f_res.Close()

    def generate(self):
        """
        Generates background-only toys (r_ttH=0, r_tHq=0) from the setup() snapshot.
        With --toysNoSystematics, no profiling fit runs before sampling, so nothing
        else needs to be frozen here beyond MH.
        """
        self.logger.info(f"Generating {self.opt.nToys} toys (background-only: r_ttH=0, r_tHq=0)")

        initial_ws = os.path.join(self.out_dir, f"higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root")
        poi_set = ",".join(f"{p}=0" for p in POIS)

        cmd = (
            f"combine -m {self.opt.MH} -d {initial_ws} "
            f"-M GenerateOnly "
            f"--setParameters MH={self.opt.MH},{poi_set} "
            f"--freezeParameters MH "
            f"-n _toy_{self.opt.nToys} --saveToys --snapshotName MultiDimFit "
            f"-t {self.opt.nToys} -s {self.opt.seed} "
            f"--toysNoSystematics"
        )

        self.run_command(cmd)

    def run_significance(self, mode_type, target_poi):
        """
        Computes significance of target_poi on the background-only toys.
        The other POI is always profiled (floated), matching the real analysis's
        significance/limit commands, in both 'fixed' and 'envelope' mode.
        'fixed' additionally freezes pdfindex to setup()'s best-fit function per
        category; 'envelope' leaves pdfindex floating (discrete profiling).
        """
        other_poi = [p for p in POIS if p != target_poi][0]
        self.logger.info(
            f"Running Significance: {mode_type.upper()} mode, testing {target_poi} "
            f"(profiling {other_poi})"
        )

        initial_ws = os.path.join(self.out_dir, f"higgsCombine_initial.MultiDimFit.mH{self.opt.MH}.root")
        toys_file = os.path.join(
            self.out_dir, f"higgsCombine_toy_{self.opt.nToys}.GenerateOnly.mH{self.opt.MH}.{self.opt.seed}.root"
        )
        if not os.path.exists(toys_file):
            self.logger.error(f"Toys file not found: {toys_file}. Run --mode generate first.")
            return

        set_params = [f"MH={self.opt.MH}"]
        freeze_params = ["MH"]

        if mode_type == "fixed":
            pdfindex_path = os.path.join(self.out_dir, "pdfindex.json")
            if not os.path.exists(pdfindex_path):
                self.logger.error(f"{pdfindex_path} not found! Run --mode setup first.")
                return
            with open(pdfindex_path, "r") as jf:
                pdf_bf = json.load(jf)
            set_params.append(",".join(f"{k}={int(v)}" for k, v in pdf_bf.items()))
            freeze_params.append(",".join(pdf_bf.keys()))

        cmd = (
            f"combine -m {self.opt.MH} -d {initial_ws} "
            f"-M Significance --snapshotName MultiDimFit {self.common_rtd} "
            f"--redefineSignalPOI {target_poi} "
            f"--setParameters {','.join(set_params)} "
            f"--freezeParameters {','.join(freeze_params)} "
            f"-n _{mode_type}_{target_poi}_test_{other_poi}_profile_{self.opt.nToys}_seed{self.opt.seed} "
            f"-t {self.opt.nToys} --toysFile {toys_file} "
            f"--X-rtd ADDNLL_RECURSIVE=1"
        )

        self.run_command(cmd)


if __name__ == "__main__":
    (options, args) = get_options()

    if options.mode in ("fixed", "envelope") and options.POI is None:
        raise SystemExit(f"--POI is required for --mode {options.mode} (choose one of {POIS})")

    out_dir = os.path.join(options.outDir, f"{options.label}_{options.nToys}toys")
    os.makedirs(out_dir, exist_ok=True)
    out_dir = os.path.abspath(out_dir)  # so the "cd" in run_command is unambiguous

    logger = setup_logging(out_dir, options.mode, options.seed)
    logger.info(f"Output folder for this run: {out_dir}")
    logger.info(f"Mode: {options.mode}, MH: {options.MH}, seed: {options.seed}, nToys: {options.nToys}")

    runner = BiasRunner(options, out_dir, logger)

    if options.mode == "setup":
        runner.setup()
    elif options.mode == "generate":
        runner.generate()
    elif options.mode in ("fixed", "envelope"):
        runner.run_significance(options.mode, options.POI)
