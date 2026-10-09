# Background modelling for the ttH/tH CP analysis

This document describes the workflow configured in `config_ttH_tH_CP.py`. The upstream package documentation remains in `README.md`.

## Input and configuration

The input is `Trees2WS/workspaces/Data/allData.root`, containing the data workspace and category datasets. The config currently uses an absolute EOS path; update `inputWS` if the checkout or input location changes.

| Setting | Current value | Meaning |
| --- | --- | --- |
| inputWS | Trees2WS/workspaces/Data/allData.root (absolute path in config) | Data workspace |
| cats | auto | Read categories from the workspace |
| catOffset | 0 | Starting category index |
| ext | tth_th_analysis | Output directory suffix |
| year | combined | Combined-year luminosity from commonObjects |
| batch | local | Run category jobs sequentially on the current machine |
| queue | microcentury | Used for Condor; irrelevant for local execution |

The existing output contains 16 categories: `bkg_had`, `bkg_lep`, `tH_had_1–4`, `tH_lep_1–2`, `ttH_had_1–4`, and `ttH_lep_1–4`. Automatic category discovery follows the input workspace, so check the printed category list for each run.

## Environment and build

Run these commands in a new shell on a CERN machine with access to CVMFS and your CMSSW installation:

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src
eval "$(scram runtime -sh)"
cd flashggFinalFit
source setup.sh
cd Background
make -j2
```

Use your own CMSSW path if the installation moves. The build requires ROOT, RooFit, Boost, and HiggsAnalysis/CombinedLimit in the CMSSW environment. `source setup.sh` also adds the repository's common Python tools to `PYTHONPATH`.

`make -j2` compiles two targets at a time. Run it again after changing C++ sources or headers; unchanged targets are skipped. For a clean rebuild, run from `Background/`:

```bash
make clean
make -j2
```

The clean command removes build products, not the input workspace or analysis fit outputs.

### Generated build files

The makefile builds the library from `src/` and executables from `test/`. The active analysis executable is `bin/fTest`, compiled from `test/fTest.cpp`.

- `obj/*.o`: compiled model objects.
- `lib/libBackgroundProfileFitting.so`: shared library.
- `bin/`: executables, including `fTest`, `BiasStudy`, and `makeBkgPlots`.
- `RootDict.cxx`, `RootDict.o`, and `RootDict_rdict.pcm`: ROOT dictionary products.
- `lib/RootDict_rdict.pcm` and `bin/RootDict_rdict.pcm`: dictionary copies installed by the makefile for ROOT startup.

These files are ignored by Git and do not need committing. Compilation does not run fits or create new background workspaces.

### Check the build

Check that `make` finishes successfully, then test executable startup:

```bash
./bin/fTest --help
```

This should print the allowed options without a missing `RootDict_rdict.pcm` error. The current executable deliberately returns status 1 for `--help`; judge this check by the displayed options and startup messages.

The verified build produced compiler warnings, including unused variables and signed/unsigned comparisons. ROOT also printed duplicate-class warnings. These warnings did not prevent compilation or displaying help; a full fit must still be checked separately.

If ROOT reports a missing dictionary file with an older build, run `make clean` followed by `make -j2` so the updated makefile installs both PCM copies.

## Run the analysis

First inspect the generated category jobs:

```bash
python3 RunBackgroundScripts.py --inputConfig config_ttH_tH_CP.py --mode fTestParallel --printOnly
```

This prepares output directories and job scripts without executing fits. It replaces existing scripts in the corresponding jobs directory.

Run with the analysis logging wrapper:

```bash
bash rkumarag_fTest_v2.sh config_ttH_tH_CP.py
```

Or invoke the runner directly:

```bash
python3 RunBackgroundScripts.py --inputConfig config_ttH_tH_CP.py --mode fTestParallel
```

Despite the mode name, `batch: local` runs one category after another. Generated jobs call `runBackgroundScripts.sh`, which executes `bin/fTest`.

## Model selection and blinding

The active `test/fTest.cpp` uses a mass range of 100–180 GeV and fits the sidebands below 120 GeV and above 130 GeV. The 120–130 GeV region is excluded from the fit dataset.

The candidate families are Bernstein, exponential, Laurent, and power law. The F-test selects orders within each family. Envelope candidates are accepted when their goodness-of-fit probability exceeds 0.01 or their order is the selected truth order. Inspect fit failures and the per-category diagnostic plots before using the envelope.

The saved background normalisation extrapolates the observed sideband yield to the full mass range using the selected PDF integrals. The RooMultiPdf retains the candidate shapes for discrete profiling in the final fit.

## Outputs and checks

Results are written under `outdir_tth_th_analysis/`:

- `CMS-HGG_multipdf_<category>.root`: background workspace for each category.
- `bkgfTest-Data/`: fit, envelope, and goodness-of-fit plots.
- `fTestParallel/jobs/`: generated category job scripts.

The logging wrapper writes timestamped `ftest_log_*.log`, `clean_ftest_log_*.log`, `pvalues_*.txt`, and `summary_*.txt` in `Background/`. Use the full log to check failures and warnings; the summary alone is insufficient.

The current wrapper uses strict shell error handling, so a failed command or a grep with no matches can stop summary generation. Also, the Python submission helper uses `os.system` without propagating category job failures. Confirm that every expected ROOT file and diagnostic plot was produced, and inspect the full log even if the runner exits successfully.

Pass the per-category background workspaces to the datacard/final-fit workflow using the paths expected by that workflow. Preserve existing outputs until their downstream use is complete.

## Files to maintain and commit

Maintain the analysis config, `rkumarag_fTest_v2.sh`, this document, the active `test/fTest.cpp`, and the shared runner, submission tools, model sources, headers, and build files.

The older `rkumarag_fTest.sh` wrapper and reference copies `test/fTest_original.cpp` and `test/fTest_Florian.cpp` are redundant for this workflow and have been removed. The unused example configs `config_test.py` and `config_tutorial.py` were already deleted. Their contents remain available in Git history; examples in the original README are historical.

Generated ROOT files, plots, logs, job directories, compiled libraries, object files, and editor swap files are ignored by Git. They are not source changes to commit. Other package utilities remain available for legacy workflows.
