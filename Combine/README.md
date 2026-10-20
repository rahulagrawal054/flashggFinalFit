# Running the fits

## Current DCB workspace (15 October 2026)

The DCB workspace was built using the current corrected review datacard, current signal packages and current background output. `15OCT26` was inspected as a workflow reference only; no archived cards, ROOT models or fit results were used.

Input layout:

- `Datacard.txt`: working DCB card, based on `../Datacard/review_datacards_20261015/20261015_122949_2444123/DCB/Datacard_review_DCB.txt`. Only its shape-file paths were changed to use `Models_DCB/signal` and `Models_DCB/background`.
- `Datacard_DCB_source_20261015.txt`: exact unchanged source-card copy.
- `Models_DCB/signal`: 16 checksum-verified copies from `../Signal/packaged_all_years_20261014/DCB`.
- `Models_DCB/background`: 16 checksum-verified copies from `../Background/outdir_tth_th_analysis`.
- `DCB_inputs_manifest_20261015.json`: copy-time sources/checksums. The subsequent path-only working-card adjustment and POI mapping are recorded in the build log directory's `build_inputs.json`.

The selected `models.py` entry is `r_2D_fiducial`:

| Contributions | POI normalization scaling | Workspace initial value/range | Retained contributions |
|---|---|---|---:|
| `tth_in`, `tHW_in`, all supplied eras/categories | `r_ttH` | 1, [-1,3] | 122 |
| `tHqHad_in`, `tHqLep_in`, all supplied eras/categories | `r_tHq` | 1, [-25,25] | 80 |
| All remaining Higgs contributions, including all `_out` processes | 1 | No POI normalization scaling | 361 |

“Scaling 1” does not freeze the process's applicable uncertainty nuisances. In particular, `r_ttH` is the common ttH+tHW fiducial strength in this model, not an independent pure-ttH strength. The DCB/SoG mass-shape choice is already encoded in the input signal ROOT files; `r_2D_fiducial` specifies physics scaling rather than the mass-PDF family.

Executed from `Combine`, after CMSSW/project setup:

```bash
python3 -B -u RunText2Workspace.py \
  --mode r_2D_fiducial \
  --common_opts "-m 125.09" \
  --batch local
```

Reusable build runner: `bash run_text2workspace_DCB_20261015.sh`. It verifies current inputs/POI mappings, adjusts only local model paths, saves terminal output/errors, and invokes the existing Python runner. It refuses to overwrite an existing `Datacard_r_2D_fiducial.root`. No existing Python scripts or POI definitions were modified. The existing Python runner uses `os.system`, so output existence and ROOT-content checks are used in addition to process status.

**Built output:** `Datacard_r_2D_fiducial.root` (workspace `w`, PDF `model_s`, `ModelConfig`, observed dataset `data_obs`). Logs/provenance and ROOT validation are under `logs_DCB/text2workspace_20261015_143319_2648653`. ROOT validation can be repeated read-only with `bash validate_DCB_workspace_20261015.sh`.

Verified: exactly the two intended POIs; MH=125.09; 16 categories and background discrete indices; all 86 active lnN nuisance parameters and five photon parameters; 563 positive nominal expected Higgs contributions. In-memory POI changes from 1 to 2 doubled exactly the intended yields and left the other contributions unchanged. Photon prior widths are 2 for ScaleEB/ScaleEE and 1 for Smearing/Material/FNUF. Total nominal retained Higgs expectation is approximately 375.814 events across all categories. ROOT validation does not establish fit convergence, closure, or final physics validity.

**Mass handling:** in the installed `MultiSignalModel` implementation, `-m 125.09` sets the mass value, but imported `MH` remains nonconstant with an unbounded range. It is neither a POI nor a constrained nuisance. Every intended fixed-mass fit must explicitly use `--setParameters MH=125.09 --freezeParameters MH` (along with the chosen POI values). The archived fit scripts also froze MH. No workspace rewrite was made to change this behavior.

At workspace-construction completion, no fit had been run. A first DCB Asimov diagnostic has now been executed with strategy 2; it requires covariance review, as detailed below. No SoG workspace has been built in this fresh workflow. The unresolved heavy-flavor capped responses and the MC-statistics treatment remain analysis review items. This workspace keeps 0.1% true-yield pruning, the six-source external-theory entry-count exemption, disabled PDF migrations and disabled `--doMCStatUncertainty`, as documented in `../Datacard/README.md`.

### First nominal command: Asimov best fit and snapshot

**First command of the new nominal workflow:** `new_runner_codex.sh`. This follows the snapshot step of the analyst's actual earlier main runner, `15OCT26/run_2D_fiducial.sh`. It is separate from the earlier fixed-index closure diagnostics documented below. The analyst subsequently ran this command in `logs_DCB/codex_step1_20261015_151859_713741`. Saved fit-quality validation is **REVIEW_REQUIRED** (status 1, covariance quality 2); see the result below.

Run from Combine:

```bash
bash new_runner_codex.sh
```

The runner sets up CMSSW, uses the original validated `Datacard_r_2D_fiducial.root`, and executes only:

```bash
combine -M MultiDimFit "$workspace" \
  -m 125.09 -t -1 --algo none \
  --setParameters r_tHq=1,r_ttH=1,MH=125.09 \
  --freezeParameters MH \
  -P r_tHq -P r_ttH --floatOtherPOIs 1 \
  --cminDefaultMinimizerStrategy 2 \
  --cminDefaultMinimizerTolerance 0.1 \
  --X-rtd MINIMIZER_freezeDisassociatedParams \
  --X-rtd MINIMIZER_multiMin_hideConstants \
  --X-rtd MINIMIZER_multiMin_maskConstraints \
  --X-rtd MINIMIZER_multiMin_maskChannels=2 \
  --saveWorkspace --saveFitResult --saveToys \
  -n _Codex_DCB_AsimovPostfit \
  2>&1 | tee first_command.log
```

The runner defines `$workspace` as the absolute path to the validated DCB workspace. It creates a new timestamp/PID directory under `logs_DCB/codex_step1_*` for each execution, saves its executed script/input-workspace checksum, prints terminal output and errors through `tee`, and records the command exit status. It does not run scans, limits, significance or impacts.

**One Combine command performs the complete sequence:** generate the SM Asimov dataset at `r_ttH=r_tHq=1` and `MH=125.09` -> fit that dataset with both POIs floating -> save the fitted snapshot, dataset and fit result. An Asimov dataset contains model expectations without random Poisson fluctuations. A snapshot contains parameter values/state; it is not itself a dataset. `--saveWorkspace` alone should not be confused with explicitly saving the Asimov toy.

| Option | Role in this first command |
|---|---|
| `-M MultiDimFit --algo none` | Obtain the joint best-fit point; no likelihood grid scan. Saving the fit result can also invoke error calculations. |
| `-t -1` | Use an Asimov dataset instead of fitting observed data. |
| `--setParameters r_tHq=1,r_ttH=1,MH=125.09` | Explicitly set both generation strengths and the mass. Avoid relying on generic `--expectSignal 1` with this two-POI model. |
| `--freezeParameters MH` | Keep the mass fixed; this command does **not** freeze background PDF indices or manually freeze the 87 alternative-function parameters. |
| `-P r_tHq -P r_ttH --floatOtherPOIs 1` | Fit both POIs together. |
| Strategy 2, tolerance 0.1 | Initial validation settings; a faster strategy is a later comparison, not a substitute for checking fit quality. |
| `MINIMIZER_freezeDisassociatedParams` and other listed runtime options | The same background-envelope optimization family used by the archived main runner and Florian; inactive functions are handled dynamically while discrete choices are profiled. |
| `--saveWorkspace` | Save the post-fit workspace and `MultiDimFit` snapshot. |
| `--saveFitResult` | Save the RooFitResult used to inspect status, covariance, EDM and parameter estimates. |
| `--saveToys` | Explicitly save the generated Asimov dataset for consistent reuse. |

Expected files inside the new run directory, with the default seed 123456 in this installed release:

| File | Contents / use |
|---|---|
| `first_command.log` | Full terminal output/errors. |
| `higgsCombine_Codex_DCB_AsimovPostfit.MultiDimFit.mH125.09.123456.root` | Saved workspace `w`, snapshot `MultiDimFit`, toy `toys/toy_asimov`, and result tree. |
| `multidimfit_Codex_DCB_AsimovPostfit.root` | RooFitResult `fit_mdf`; authoritative fit-quality checks. |
| `executed_runner.sh`, `input_workspace.sha256`, `exit_status.txt` | Reproduction/provenance and process exit status. A zero process exit alone does not establish a valid fit. |

#### Relation to Florian and the old first command

Verified against Florian `FloMau/flashggFinalFit` commit `a7479b74425366d43f8b35e52ea7ad9ddb2cfbe0`, `Combine/RunFits.py` (`bestfit` block around lines 245–253; defaults around lines 13–24) and `Combine/README.md` (`bestfit`/snapshot guidance). His expected best-fit workflow likewise generates Asimov data and fits it in one command; adding `--saveWorkspace` saves the fitted snapshot. His default `--setPdfIndices` is False, so background choices are profiled unless explicitly fixed. His framework does not impose a universal second command: the input JSON selects the fit sequence, and loading an earlier snapshot requires `--snapshotWSFile` explicitly.

Our first command has the same purpose and sequencing, not identical flags. Florian's default strategy is 0 and default mass is 125.38, while our chosen settings are strategy 2 and mass 125.09. The new runner explicitly sets both POIs and saves toys/results. Your archived main runner also uses strategy 0 and mass 125.08; these defaults were deliberately adapted here. No claim of fit convergence follows from matching either workflow.

The previous fixed-index first diagnostic froze all 16 PDF choices; its controlled retry additionally froze 87 parameters belonging only to unused background functions. The new nominal first command freezes only MH and starts from the original validated workspace, so those diagnostic freezes are not carried forward. A profiled-background best fit need not reproduce precisely the same central values as the fixed-generation-function closure test: changing the selected background function can change the best-fit configuration.

#### What happens before the second command?

**Decision:** keep `new_runner_codex.sh` and its first command unchanged. The switches in `bkg_lep` and `ttH_had_2` are observed background-model selections, not an established cause of the covariance warning or of the POI shifts. A separate full-profile robust-Hessian validation is the next check; no category, nuisance or model is removed on this basis.

The first nominal run has now been inspected. It finished with process exit 0 in 7.47 min, but `fit_mdf` records status **1**, covariance quality **2**, EDM **0.181394**, MINIMIZE=1/HESSE=1. Its strengths are r_tHq=1.02025741 and r_ttH=1.04221487. Two background choices changed: bkg_lep bern3 -> pow1 and ttH_had_2 bern2 -> exp1, both with smaller complexity corrections. Such switching can affect the central strengths; it does not excuse the covariance warning or establish a unique cause for the shift. Do not quote the saved error estimates as validated uncertainties. Full report: `logs_DCB/codex_step1_20261015_151859_713741/README.md`; background changes and fit-quality fields are saved alongside it. No scans have been started.

Inspect the new `fit_mdf` status, covariance quality, EDM, POI values/errors, boundaries and selected background indices. Review any warnings; in particular, do not accept a fit merely because its POIs print near 1. The existing fixed-index retry has status 1/covariance quality 2 and is not an approved baseline for scans.

Once the new nominal fit is validated, the next planned stage is a full-systematics 1D profile scan, first for one POI with the other floating, then vice versa. Load the first command's saved workspace with `--snapshotName MultiDimFit` and reuse its actual Asimov dataset via `--toysFile` rather than regenerating expectations at a different post-fit configuration. Snapshot loading sets starting conditions; it does not itself freeze all nuisance parameters. Keep MH fixed and preserve the intended background profiling. Stat-only scans follow as a separately defined step. The diagnostic scan command below has now been added and started; no final intervals are approved yet.

### Covariance investigation: controlled tests (15 October 2026)

The nominal snapshot above remains **REVIEW_REQUIRED**. Two controlled tests reused its saved `toys/toy_asimov` and `MultiDimFit` starting snapshot, fixed its 16 selected background indices, and froze 90 parameters belonging only to unused background alternatives. There were 25 active background shape parameters (plus the mass observable in the PDF parameter inventory), 16 background normalizations, 91 constrained nuisances and both POIs; the resulting fit had 134 floating parameters. All constrained nuisances remained free. These tests omitted the four background-selection masking/hiding runtime options. They do **not** replace the nominal discrete-profile fit.

| Test | Result | Interpretation |
|---|---|---|
| Standard HESSE, strategy 2, tolerance 0.01 | Initial MIGRAD status 0; saved result status 3, HESSE=3, covariance quality 2, EDM 4.79757e-5; r_tHq=1.02027082, r_ttH=1.04221447 | Fixing background choices and tightening tolerance do not resolve standard HESSE. |
| Same controlled setup, `--robustHesse 1` | MIGRAD status 0, EDM 2.71185e-7; robust Hessian has all positive eigenvalues without excluding any of the 134 parameters; r_tHq=1.02025741, r_ttH=1.04221487 | The selected continuous model admits a positive curvature matrix. Standard HESSE is numerically unstable here; this is not evidence that the DCB signal fit itself failed. |

The robust covariance gives diagnostic standard errors 4.94115 (r_tHq) and 0.460477 (r_ttH), and photon FNUF/Smearing errors 0.99773/0.99343. These are **conditional on the fixed background choices**, not final discrete-profile uncertainties. The saved robust result reports **covQual=-1**, not 3: `RobustHesse::GetRooFitResult` constructs a replacement covariance and calls `setCovarianceMatrix` without assigning a Minuit quality code (`../../HiggsAnalysis/CombinedLimit/src/RobustHesse.cc:542` and `:575`). Its replacement parameter list also has zero MINOS asymmetric-error fields, which must not be interpreted as zero uncertainty. The robust matrix was checked directly: minimum correlation-matrix eigenvalue 0.00252561, no zero-error parameters, and the algorithm logged `All eigenvalues are positive` at iteration 0. No parameters were removed.

Code evidence: `FitterAlgoBase::doFit` runs a separate HESSE call when requested (`src/FitterAlgoBase.cc:263`); `CascadeMinimizer::hesse` remakes the minimizer and minimizes again before calling HESSE (`src/CascadeMinimizer.cc:280`). `MultiDimFit` suppresses that standard call when `--robustHesse 1` is selected (`src/MultiDimFit.cc:204`) and subsequently computes the robust Hessian (`:251`). Paths here are relative to `../../HiggsAnalysis/CombinedLimit/`. The same starting fit returns MIGRAD status 0 when that extra standard HESSE call is absent. This localizes the observed deterioration to the standard curvature calculation in the controlled test; it does not prove the cause of every warning in the original profiled run.

Artifacts: `logs_DCB/selected_background_diagnostic_20261015_154022/` and `logs_DCB/selected_background_robustHesse_20261015_154519/`. Each has exact `command.json`, `command.sh`, logs and fit validation. The original outputs, model, workspace, priors, parameter ranges and `new_runner_codex.sh` were preserved. The next check is the **full background-profile fit** with robust Hessian evaluation and explicit inspection of inactive-parameter handling. Do not start scans from either fixed-choice diagnostic.

#### Full background-profile robust-Hessian validation

A separate validation run completed in `logs_DCB/profiled_robustHesse_20261015_155815/` (6.95 min). It used the original workspace, the first command's exact saved Asimov dataset, the original strategy 2/tolerance 0.1 and four runtime options, with only MH frozen. Background indices were profiled. Added `--robustHesse 1` for independent curvature evaluation, verbose logging and a saved Hessian; `new_runner_codex.sh` remains unchanged.

Results: r_tHq=1.02023225, r_ttH=1.04221528; EDM=1.00428e-5, MINIMIZE status **1**. Both MINOS error calculations reported failures. The robust Hessian was positive at iteration 0, required no negative-eigenvalue parameter removals, and had a minimum correlation-matrix eigenvalue 0.00252558. Exactly 90 omitted parameters were verified to belong only to background alternatives inactive at the selected indices; all 134 active continuous parameters remained in the matrix. Those alternatives were available during background profiling: omission from the final local Hessian does not remove them from the likelihood search.

Robust local standard errors are 4.94653 (r_tHq) and 0.461334 (r_ttH), with saved covQual=-1 as explained above. A local Hessian is conditional on the selected background branch even when its minimum was found by discrete profiling; it is not the full envelope's profile interval. **REVIEW_REQUIRED_MINIMIZE_AND_MINOS** remains the status. The positive robust matrix does not validate the failed MINOS intervals. `provenance.json`, `command.sh`, `fit.log` and `fit_validation.json` preserve the evidence. The switches in `bkg_lep` and `ttH_had_2` remain observations, not a proved cause of these numerical warnings. The next step is explicit likelihood profiling for the two POIs, inspecting minimization quality at each point rather than quoting the failed MINOS errors.

### First Asimov closure attempt: status requires review

Kept `--cminDefaultMinimizerStrategy 2` and tolerance 0.1 for the first DCB diagnostic rather than switching to 0 for speed. The requested fixed-index attempt failed and produced no RooFitResult. Inspection found 87 floating parameters belonging only to unselected background functions. A targeted retry reused the exact saved Asimov dataset and explicitly fixed those 87 unused parameters, while keeping all 28 selected background-shape parameters, both POIs and detector/theory nuisances free. MH and the 16 background indices stayed fixed. This is a diagnostic-only configuration; model/source files were unchanged.

The retry ran about 3.74 minutes and returned r_ttH=0.99998090, r_tHq=1.00315756. However, saved RooFitResult status is **1**, covariance quality **2** (forced positive-definite), EDM=1.3063985e-05; MINIMIZE=1 and HESSE=1. Central agreement with injection is therefore not sufficient to accept this fit. See `logs_DCB/DCB_AsimovClosure_fixedInactive_20261015_145345_2680146/README.md`, `fit_validation.json` and `combine_logger.out`. `fit_validation.status.txt` is REVIEW_REQUIRED. No scans or impacts were started.

The immediate next investigation is the covariance warning. Retain strategy 2 until a clean fit is validated; a faster strategy can then be benchmarked against it. Do not carry frozen inactive parameters into a profiled-background run: when other functions become selectable those parameters must regain their intended freedom. Use the original validated input workspace for that separate step. The original requested run and its failure log were preserved. The actual `--saveToys` workspace output names include the `.123456` seed suffix in this release.

The remainder of this README describes the general framework; its generic defaults/examples do not supersede the current DCB settings above.

Now the signal and background models and the datacard has been produced, it is time to run the fits using [combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/). Please refer to the linked manual for the details on fitting and the options you can use.

### Diagnostic r_ttH likelihood scan

**First attempt stopped:** the strategy-2 initial reference fit returned status -1 (`MultiDimFit failed`), but Combine continued into the grid. The process was deliberately terminated and marked STOPPED_INVALID_GLOBAL_REFERENCE; partial output is not a valid scan. A strategy-0 reference test and scan retry subsequently completed; see the result below.

Runner: `run_DCB_scan_r_ttH_diagnostic.sh`; first execution: `logs_DCB/scan_r_ttH_diagnostic_20261015_161215_2866734/`. The first-command runner remains unchanged. This is a coarse full-systematics profile scan of r_ttH, with 21 edge-aligned points from -0.5 to 3.0 (spacing 0.175). r_tHq remains profiled over its existing workspace range [-25,25]; nuisance parameters and all 16 background choices are profiled, with only MH fixed at 125.09.

The input and `--toysFile` both point to the first command's saved file, and `--snapshotName MultiDimFit` supplies starting values. The actual saved SM Asimov is reused: no new expectation is generated at the post-fit strengths. A global reference is refitted before the grid; `--skipInitialFit` is not used. Strategy 2, tolerance 0.1 and the four original minimizer runtime options are retained. `--saveFitResult` and `--robustHesse` are not needed for a grid: omitting the former avoids requesting the extra standard HESSE and MINOS calculations (`MultiDimFit.cc:201`). Grid points profile the likelihood directly (`RandStartPt.cc:154`).

The runner prints terminal output through `tee`, saves `scan.log`, the executed runner and input hash, and records exit status. `--saveSpecifiedNuis all`, explicit `--saveSpecifiedIndex` names and `--saveInactivePOI 1` retain nuisance values, selected background indices and profiled r_tHq in the ROOT `limit` tree. A smooth plot alone is not proof of convergence. Check all 21 expected coordinates, finite likelihood values, missing/failed points, the global reference, and minimizer messages at each grid point. In this Combine version, status 1 can be accepted internally, so tree presence does not prove a clean fit. Positive/negative shifts between background branches can create genuine envelope kinks. This scan is diagnostic; refine and validate around crossings before quoting intervals. For a one-dimensional profile, q=2 deltaNLL and the usual asymptotic crossings are q=1 and 3.84, regardless of the tree's `quantileExpected` bookkeeping.

#### Completed first diagnostic scan: strategy 0

The first strategy-2 grid attempt was stopped after its global reference failed. A separate reference test (`logs_DCB/scan_reference_strategy0_20261015_161526/`) changed only numerical strategy to 0 and retained the snapshot/data, ranges, tolerance and profiling options. All 69 logged minimizations returned status 0; final EDM was 7.55558e-9, r_ttH=1.04221508 and r_tHq=1.02028982, with the same background choices as the original saved snapshot. Its NLL improvement relative to the loaded configuration was about 1.54e-8: the central solution was effectively unchanged. Strategy 0 is the upstream default. This is a numerical comparison, not a change of physics model or an acceptance of the earlier HESSE/MINOS errors.

The retry runner is `run_DCB_scan_r_ttH_diagnostic_strategy0.sh`. Its completed execution is `logs_DCB/scan_r_ttH_strategy0_20261015_161718_2876268/`, runtime 4.31 min. It keeps the first-command script unchanged. The strategy-2 scan runner and its failed output are retained separately. To repeat the completed diagnostic with a fresh timestamp directory:

```bash
bash run_DCB_scan_r_ttH_diagnostic_strategy0.sh
```

The ROOT tree contains the refitted reference plus all 21 requested grid coordinates. Reference r_ttH=1.04221511, profiled r_tHq=1.02028978. Nineteen grid coordinates have finite nonsentinel likelihoods, and their final minimization status is 0. The profile has one observed minimum and both threshold crossings inside the finite region. No sampled point improves on the global reference. The second panel of `scan_r_ttH_diagnostic.png` shows that r_tHq changes as r_ttH is scanned: it was profiled, not frozen.

| Check | Result / limitation |
|---|---|
| Initial reference | All logged minimizations status 0. |
| Invalid negative grid points | r_ttH=-0.5 and -0.325 have deltaNLL=9990. In `RandStartPt.cc:167`, this sentinel is written when the starting NLL reports evaluation errors, before attempting profiling. These are not physical exclusion measurements or proof that no valid profile exists there. Excluded from the plotted curve. |
| Valid points | 19 grid points, each ending with status 0, plus the reference point. |
| Internal alternative-fit failure | At r_ttH=2.475, a tH_had_4 background-alternative trial returned -1; later trials and the final minimization returned 0. It is above the sampled 95% crossing, but remains a review item before treating the entire tail as validated. |
| Boundary messages | Background-alternative boundary warnings remain in the log; they cannot all be attributed to the selected branch without checking the saved indices. |
| Approximate q=1 crossings | [0.62554, 1.52859], obtained by linear interpolation between coarse points. |
| Approximate q=3.84 crossings | [0.27356, 2.07655], same interpolation. |

These crossings are **diagnostic estimates, not final quoted uncertainties**. Grid spacing is 0.175. A denser scan and numerical stability checks near the crossings are needed before quoting intervals. The r_tHq profile with r_ttH floating was subsequently run; see the following section. No stat-only scans, limits, significance fits or impacts were run.

Artifacts in the completed directory: `scan.log` and `combine_logger.out`; output ROOT file; executed runner and input SHA256; `scan_points.csv`/`.json`; `point_minimization_summary.json`; `background_index_changes.json`; `scan_validation.json`; PNG/PDF likelihood plots. Status is `COARSE_DIAGNOSTIC_VALID_CROSSING_REGION_TAIL_ISSUES`. The nuisance branches are in the ROOT tree. All original model files and the first-command runner were preserved.

### Completed r_tHq diagnostic profile scan

Runner: `run_DCB_scan_r_tHq_diagnostic_strategy0.sh`. Main output: `logs_DCB/scan_r_tHq_strategy0_20261015_164035_2908966/`; runtime 2.89 min. It scans 21 edge-aligned points from -10 to 15 (spacing 1.25), profiles r_ttH, all nuisances and background choices, and freezes only MH=125.09. The original saved Asimov dataset and first-command snapshot are reused. Strategy 0/tolerance 0.1 and the same four minimizer runtime options as the completed r_ttH scan are used. r_ttH retains its original [-1,3] range. The first-command script, models and existing outputs are unchanged.

The main scan saved a reference at r_tHq=1.02028978, r_ttH=1.04221511. Its four far-negative coordinates (-10,-8.75,-7.5,-6.25) initially received deltaNLL=9990 before profiling because the starting NLL reported evaluation errors (`RandStartPt.cc:167`). This sentinel is not a physical exclusion. All 17 other original grid points ended with status 0; all logged reference minimizations returned 0.

Targeted retries preserve those results and use `--setParametersForGrid r_ttH=2` and then `r_ttH=2.9`, via separate bash runners. These set a starting value only: r_ttH is still free in every point fit. `MultiDimFit::doGrid` records nll0 before applying this option (`MultiDimFit.cc:592`), so the global reference is retained. All run input hashes and reference central values were checked consistent. The seed-2 retry recovered -6.25 with status 0. The seed-2.9 results and all remaining point statuses are recorded in `scan_validation.json`. No parameter range, nuisance prior or physics model was changed.

Final composite valid grid points: 19/21. Still-invalid coordinates: [-10.0, -8.75]. Overlapping valid-point deltaNLL differences: [{'r_tHq': -6.25, 'deltaNLL_spread': 2.0265579223632812e-06}]. The composite CSV/JSON retain the source run of each point and use the lowest valid likelihood at duplicate coordinates. Original ROOT files are not overwritten or silently merged.

Approximate linearly interpolated q=1 crossings: [-3.460692797369122, 6.5173177060335235]; q=3.84 crossings: [-6.635636650790623, 12.803158405193697]. These are coarse diagnostic estimates, not final quoted intervals. Status: **COARSE_DIAGNOSTIC_CROSSINGS_BRACKETED_TAIL_ISSUES**. Profiled r_ttH spans [0.79422,1.52736] at valid points; compare to its original [-1,3] range. If either crossing is unbracketed, it remains unresolved rather than being extrapolated. Background-alternative boundary warnings remain in the original logs. A denser scan and numerical stability checks around the crossings are still needed.

Artifacts: `scan_r_tHq_diagnostic.png`/`.pdf`; `scan_points_combined.csv`/`.json`; `scan_validation.json`; per-run raw `scan_points.json`, `point_minimization_summary.json`, ROOT output, executed runner, snapshot hash and terminal/error logs.

- scan_r_tHq_strategy0_20261015_164035_2908966: reference statuses [0]; point records in `point_minimization_summary.json`.
- scan_r_tHq_negative_seed2_20261015_164523_2923492: reference statuses [0]; point records in `point_minimization_summary.json`.
- scan_r_tHq_negative_seed2p9_20261015_171422_3015014: reference statuses [0]; point records in `point_minimization_summary.json`.

### Completed 100-point stat-only scans

Both POIs have now been scanned with `--freezeParameters MH,allConstrainedNuisances`, reusing the first-command snapshot and saved SM Asimov data. Runners:

```bash
bash run_DCB_scan_r_ttH_statOnly_100.sh
bash run_DCB_scan_r_tHq_statOnly_100.sh
```

Both jobs returned process exit 0 (r_ttH: 1.90 min; r_tHq: 1.48 min). Saved-workspace checks verify all 91 constrained nuisances constant at their exact loaded snapshot values, with MH fixed. The other POI, 16 background normalizations, 25 selected background-shape parameters and all 16 background choices remain floating. Thus this is stat-only with background profiling, not a fit fixing all background parameters. Values are frozen at the snapshot, not reset to zero. The first-command runner and physics model remain unchanged.

| POI | Scan range / grid | Best reference | Approximate q=1 crossings | Approximate q=3.84 crossings | Valid grid points |
|---|---|---|---|---|---|
| r_ttH | [-0.5,3], 100 points | 1.042215 | [0.61664,1.52947] | [0.26739,2.06253] | 92/100 |
| r_tHq | [-10,15], 100 points | 1.020247 | [-3.47146,6.46004] | [-6.57864,12.58524] | 94/100 |

The quoted crossings are interpolated scan estimates, not final analysis-approved intervals. Both scans have status-0 reference fits and status-0 final minimizations at every valid grid coordinate, with no negative-deltaNLL warning points. There are invalid far-negative starting configurations (r_ttH: 8 points; r_tHq: 6 points), all outside the bracketed crossing regions. Seven r_ttH upper-tail grid coordinates have failed internal background-alternative trials but successful final fits; no such internal failures appear in the r_tHq run. Detailed counts/coordinates, freeze checks and plots are in each run's report.

For r_tHq, `--setParametersForGrid r_ttH=2.9` changes only the floating r_ttH starting value to reduce the known negative-point evaluation failures; it does not freeze r_ttH or change a parameter range. The existing 21-point with-systematics tHq scan had separate seed retries. Numerical seeds and grids should be matched or explicitly checked when producing the refined comparison.

The matching 100-point full-systematics scans have now been completed; see the comparison below. Do not extract a systematic contribution by subtracting the present 100-point stat-only widths from the old 21-point full-systematics widths: interpolation alone can produce misleading differences. Overlay and validate matched profiles first; background-alternative trial failures and numerical stability still need review before final uncertainties are quoted.

- r_ttH report and plots: `logs_DCB/scan_r_ttH_statOnly100_20261015_172936_3076979/README.md`.
- r_tHq report and plots: `logs_DCB/scan_r_tHq_statOnly100_20261015_172937_3077109/README.md`.

### Matched 100-point with-systematics versus stat-only comparison

Completed runners:

```bash
bash run_DCB_scan_r_ttH_withSyst_100.sh
bash run_DCB_scan_r_tHq_withSyst_100.sh
```

The full-systematics scans now match the stat-only 100-point ranges/grids, input snapshot and actual saved SM Asimov data, minimizer strategy/tolerance and starting seeds. The only fit-option difference is `--freezeParameters MH` versus `MH,allConstrainedNuisances`; output names and nuisance-value logging also differ. `matched_command_audit.json` verifies this in each full-systematics directory. Saved workspace checks confirm all 91 constrained nuisances free in full-systematics and frozen at snapshot values in stat-only, with the other POI and background choices/parameters profiled in both. The first-command script and physics model were preserved.

| POI | With syst q=1 interval | Stat-only q=1 interval | With syst q=3.84 interval | Stat-only q=3.84 interval |
|---|---|---|---|---|
| r_ttH | [0.61503, 1.53460] | [0.61664, 1.52947] | [0.26588, 2.07877] | [0.26739, 2.06253] |
| r_tHq | [-3.50451, 6.53389] | [-3.47146, 6.46004] | [-6.67891, 12.80583] | [-6.57864, 12.58524] |

These are asymptotic crossing estimates obtained by linear interpolation, not final approved intervals. The comparison directory is `logs_DCB/matched100_comparison_20261015_180046/`: `comparison.json`, per-POI PNG/PDF overlays and this report. The upper panels show q=2 deltaNLL; the lower panels show q(stat-only)-q(full), not a percentage, ratio, impact, or separately fitted systematic likelihood. Positive differences indicate a lower full likelihood profile at that coordinate when nuisances can adjust. Each curve uses its own refitted reference; those references are checked in the reports.

- r_ttH: full valid points 92/100; invalid starts [-0.5, -0.46464645862579346, -0.4292929172515869, -0.39393940567970276, -0.3585858643054962, -0.3232323229312897, -0.28787878155708313, -0.2525252401828766]; reference statuses [0]; final minimization issues []; internal nonzero trial coordinates [-0.146465, -0.075758, 0.136364, 2.116162, 2.328283, 2.434343, 2.540404, 2.575758, 2.646465, 2.752525, 2.787879]. Core ordering violations >0.001: [].
- r_tHq: full valid points 94/100; invalid starts [-10.0, -9.747474670410156, -9.494949340820312, -9.242424011230469, -8.989898681640625, -8.737373352050781]; reference statuses [0]; final minimization issues []; internal nonzero trial coordinates [-3.686869]. Core ordering violations >0.001: [].

The matched profiles allow a comparison of total versus statistical expected precision under the current nuisance model. They do not select DCB over SoG by goodness of fit, and do not repair omitted nuisances or inherited heavy-flavor capping choices. Trial underflows and background-alternative failures remain explicitly recorded. Invalid starting points are omitted from curves; sentinel deltaNLL=9990 is not an exclusion measurement. Interval endpoints and any small systematic contribution still require numerical-stability checks before final quoting; do not interpret quadrature subtraction as an exact nuisance decomposition for asymmetric/non-Gaussian profiles. No significance, limit, impact or observed-data fit was run here.


#### Local tolerance check at the tHq lower 68% crossing

The two grid points bracketing the lower 68% tHq crossing were rerun with tolerance 0.01 rather than 0.1; all other data/model/grid/seed settings were preserved. Results: [{'r_tHq': -3.4343433380126953, 'original_deltaNLL': 0.48154520988464355, 'tighter_deltaNLL': 0.48151201009750366, 'difference_q': -6.639957427978516e-05, 'profiled_r_ttH': 1.1947064399719238}, {'r_tHq': -3.686868667602539, 'original_deltaNLL': 0.5479660630226135, 'tighter_deltaNLL': 0.5479438304901123, 'difference_q': -4.4465065002441406e-05, 'profiled_r_ttH': 1.2072572708129883}]. Per-point minimizer results: [{'coordinate': -3.434343, 'final_status': 0, 'internal_nonzero_statuses': [-1]}, {'coordinate': -3.686869, 'final_status': 0, 'internal_nonzero_statuses': [-1]}]. Interpolated crossing changed from -3.50450657 to -3.50462119 (change -0.00011462); maximum absolute change in q was 6.6399574e-05. Output: `logs_DCB/check_r_tHq_lower68_tol001_20261015_180222_3164134/`. This tests the neighborhood containing the internal failed alternative trial; it does not validate all tails, all nuisance assumptions or all possible starting minima. See `tHq_lower68_tolerance_check.json` in the comparison directory.


The matched 68% error widths increase by approximately 0.38%/1.05% (lower/upper) for r_ttH and 0.74%/1.36% for r_tHq when the currently included constrained nuisances are profiled. This indicates predominantly statistical expected precision under this nuisance model. It is not a statement about uncertainties omitted from the current datacard. The local lower-68% tHq tolerance check changes the endpoint by 0.000115 and q by at most 0.0000664; internal alternative-trial failures persist despite status-0 final fits, so this is local numerical evidence, not a claim that every model trial or tail is validated.

### Designed significance and limit commands: previous-run comparison

The runners below were initially prepared and syntax checked without execution. Significance and primary expected-limit calculations have since run, as reported below; the supplemental SM-injected-data limit runners have not run. No 300-point scan has been launched. The interrupted earlier preparation left none of these files; they were created after reviewing the archive. The first-command runner, original workspace, model files, old scripts and results are unchanged.

Baseline: `15OCT26/run_2D_fiducial.sh:132` (limit) and `:150` (significance), corroborated by the argument runner's corresponding blocks. The old main runner calculated r_tHq limits and r_ttH significance only. Its archived DCB limit tree contains quantiles 0.025, 0.16, 0.5, 0.84 and 0.975, with no -1 result: those are background-reference expected-limit bands, not a limit on the SM-injected data. Reading the archive was for comparison only; no archived card, model or dataset is used by the new commands.

| Feature | Previous main runner | New design / reason |
|---|---|---|
| Workspace/data | Postfit snapshot, `-t -1`; no explicit saved `--toysFile` | Same first-command r_2D_fiducial workspace snapshot AND its exact saved `toys/toy_asimov`, via `--toysFile` pointing to that file. Avoid regenerating a different Asimov from postfit parameter values. |
| Mass | 125.08 | 125.09, matching current workspace and all current fits. |
| Targets | Limit r_tHq; significance r_ttH | Separate commands for each method and each POI. |
| POI selection | `--redefineSignalPOI` abbreviated spelling | Use documented `--redefineSignalPOIs`. Do not claim the old abbreviation necessarily failed. |
| Other strength | Not explicitly frozen in main runner | Explicit `--floatParameters OTHER`; original other-POI limits retained. `--floatOtherPOIs` is a MultiDimFit option and is not used here. |
| Range selection | `--rMin/--rMax` | Named `--setParameterRanges TARGET=0,MAX`. In this version, generic rMin/rMax alter the original first POI before redefinition (`Combine.cc:448`, `:613`). The current saved POI order is r_tHq, r_ttH, so a generic range override can affect r_tHq even when targeting r_ttH. The archived workspace order was not verified; do not automatically assign that historical failure to it. |
| Significance bounds | Generic [0,5] | Target r_ttH [0,5], target r_tHq [0,25]; null target strength 0, other strength profiled. Bounds must be checked in results; they do not modify the saved workspace. |
| Limit bounds | Generic [0,25] | Target r_ttH [0,10], target r_tHq [0,50], deliberately broad starting search bounds, not yet validated. Check crossing/automatic expansion and other-POI boundaries after running. |
| Limit mode | `--run expected` | `--run observed` applied ONLY to the saved SM Asimov, per the user's instruction to use the same dataset. Label as **SM-injected Asimov 95% CLs upper limit**, never a real observed limit or background-only median expected limit. This is a deliberate statistical-definition change from the old limit command. |
| Other model parameters | Set both strengths=1 after loading snapshot; freeze MH | Retain loaded starting values; freeze only MH. Both strengths were 1 when the saved data were generated; this does not require resetting fit starting values to 1. |
| Minimizer | Strategy 0 + four runtime options | Same; explicit tolerance 0.1, matching validated scan settings. |
| Logging | Main script no per-stage tee; argument runner does tee | Separate timestamp directories, terminal/error log via tee, executed-runner copy, input hash and shell exit status. Limit uses `--picky` as an additional fit-failure guard, not a substitute for log validation. |

The input is `logs_DCB/codex_step1_20261015_151859_713741/higgsCombine_Codex_DCB_AsimovPostfit.MultiDimFit.mH125.09.123456.root`. Its physics model is the same r_2D_fiducial DCB workspace; the snapshot supplies starting values and `--toysFile` supplies the actual SM-injected data. No new workspace is built. Background PDF indices, background shape/normalization parameters and constrained nuisances remain profiled. Only the target is tested/fixed at each null or upper-limit hypothesis, with MH frozen.

For Significance, `Significance.cc:248` sets the null target to zero and the optimized likelihood-ratio implementation profiles free PDF parameters (`ProfiledLikelihoodRatioTestStatExt.cc:150`, `:398`). With a single redefined target and the other strength explicitly floating, this tests that process with the other process profiled. It uses the saved (r_ttH,r_tHq)=(1,1) Asimov. The default Significance path uses an optimized profile-likelihood statistic despite its internal useMinos name; it is not the same MINOS interval calculation that failed in MultiDimFit.

For CLs, using `--run observed` does not replace the supplied data: it selects `AsymptoticLimits::runLimit` on those data (`AsymptoticLimits.cc:113`). The algorithm necessarily constructs an **auxiliary target-zero reference Asimov** for its asymptotic CLs calibration (`:156`, `:733`). With no `--noFitAsimov`, it uses a conditional fit with target=0 (`AsimovUtils.cc:36`), profiling the other strength and free parameters. This internal calibration is distinct from replacing the user's input dataset. It is neither the median background-only expected limit nor the scan's two-sided q=3.84 upper endpoint. Combine may print `Observed Limit` and a quantileExpected=-1 entry: those labels describe the algorithm/output convention, not real observed data here. The old `--run expected` would instead request its auxiliary background-reference expected quantiles. The old no-asimov branch's `--run blind` likewise requests expected-only output, not a limit on observed data.

Original supplementary-design commands (the primary expected limits use the separate `run_DCB_expectedLimit_*.sh` runners reported below):

```bash
bash run_DCB_significance_r_ttH.sh
bash run_DCB_significance_r_tHq.sh
bash run_DCB_SMAsimovLimit_r_ttH.sh
bash run_DCB_SMAsimovLimit_r_tHq.sh
```

Validation after each future run: confirm the saved input-data fingerprint matches the first-command Asimov; inspect target/other-POI ranges and constant flags, nuisance and background freedom, minimization statuses and finite ROOT result entries; compare significance with direct q(0) from the profile; verify CLs target 0.05 is bracketed away from numerical bounds. Status-0 process exit or a finite reported result alone is insufficient: some installed code paths do not propagate every minimizer failure. This validation prescription was set before execution; run-specific results and qualifications are reported below.

### Clarification: expected precision, significance and upper-limit conventions

The earlier SM-Asimov limit design followed the request to evaluate the exact first-command (r_ttH,r_tHq)=(1,1) dataset. It is valid as an SM-injected-data limit, but **is not automatically the preferred convention for a fiducial measurement or reduced model dependence**. Both SM-injected and target-zero Asimov calculations are blinded. The statistical truth hypothesis and use of real blinded-window data are separate choices.

Checked the locally available Florian remote ref `florian-repo/higgsdnafinalfit`, commit `d9031abb4e8c4e10c312e73912fece53fbd974bb` (cached ref, not a fresh remote fetch). In `Combine/run_fits_tth_th_1D.sh:302`, `build_limit_mode_opts` returns `--run expected` for Asimov running. The tH limit command uses it at `:496`; the other POI is profiled by default (`FREEZE_OTHER_POI=0`, `:74`), with an optional freeze-other switch. Its significance block starts at `:558`, using SM-injected running options. The earlier `Combine/run_fits_tth_th.sh:95` also explicitly uses `--run expected` for tHq. These statements describe inspected script definitions, not proof of every command Florian actually ran for a result.

The generic `Combine/RunFits.py:61` supports `--toysFile ... -t -1` or otherwise `--expectSignal 1 -t -1`. Its AsymptoticLimit command (`:280`) passes user fit/common options and does not itself force `--run expected`. The installed Combine default `--run both` computes both background-reference expected quantiles and the limit on the supplied data. Thus 'expected' as a generic RunFits/Asimov label must not be confused with `AsymptoticLimits --run expected` selecting the expected-limit quantiles.

Recommended primary conventions:

| Purpose | Asimov truth / result |
|---|---|
| Expected fiducial-XS precision | Both strengths=1; profile the other POI, as in the completed scans. |
| Expected significance of each target process | Both strengths=1; test target=0, profiling the other strength. |
| Conventional expected 95% CLs upper limit | Target-zero reference distribution; the other Higgs process is not automatically removed. Keep it in the model and profile its strength according to the chosen procedure. `--run expected` reports median and expected bands, as Florian's dedicated runner does. With conditional calibration, free parameters including the other strength are fitted under target=0. |
| Supplemental limit on an SM-injected ideal dataset | Evaluate the saved (1,1) toy directly with `--run observed`, labelled SM-injected Asimov limit, not a background-only median expected limit. |

For the primary expected limit, the same workspace/saved input file can still be loaded, but Combine calculates the expected quantiles from its internal target-zero reference; this is not the same quantity as directly limiting the saved SM-injected data. Target-zero does not mean setting every Higgs process to zero. Neither choice uses real signal-window data here. The two limit conventions can be reported separately with explicit labels.

Reducing model dependence concerns fiducial definitions, detector-response/acceptance assumptions and the treatment of other processes (including profiling their strengths); it is not established by choosing SM-injected rather than target-zero Asimov truth. The already-prepared `run_DCB_SMAsimovLimit_*.sh` remain supplementary-design scripts and have not been run. No command or physics model was changed during this clarification. Primary expected-limit runners were subsequently created and executed; see the first-execution results below. The old statement that expected bands and supplied-data limits are different remains true; the correction is to the implied preference, not their mathematical definitions.

### Expected significance and conventional expected limits: first executions

These runs use the same saved r_2D_fiducial workspace and first-command SM Asimov input, mass 125.09, strategy 0/tolerance 0.1 and four minimizer runtime options. They redefine a single tested POI, explicitly float the other, and freeze only MH. No 300-point scans, real-data tests or SM-injected-data limits were run. The conventional expected-limit runners use `--run expected`, matching Florian's dedicated expected-limit convention. All original model files and the first-command runner remain unchanged.

The ROOT `toys/toy_asimov` observable rows/categories and weights were hashed entry by entry. All four saved outputs exactly match the first-command dataset. All 91 constrained nuisances, the other strength, all 16 background indices and all 16 background normalizations were verified free. `ModelConfig` has only the intended target POI. Expected limits use a separate internal target-zero auxiliary Asimov for CLs calibration, conditional on the provided data; this does not imply the other strength equals 1 in that auxiliary reference. It is fitted under the target-zero hypothesis.

| POI | Expected significance (SM injection) | Median expected 95% CLs limit | Expected -1σ/+1σ limits | Expected -2σ/+2σ limits |
|---|---|---|---|---|
| r_ttH | 2.82668 sigma | 0.83984 | [0.58354,1.24491] | [0.42976,1.77155] |
| r_tHq | 0.21115 sigma | 11.48438 | [7.85065,17.11497] | [5.74219,24.41876] |

Limits are on the dimensionless strengths as implemented in this workspace; no conversion to a cross section in fb was made. The ±1σ/±2σ columns are quantiles of the expected **upper-limit distribution**, not confidence intervals on the measured signal strength. No quantileExpected=-1 limit was requested; all five conventional expected quantiles were present and ordered, with values below the output target upper bounds.

Significance was first run at verbosity 2, then repeated with verbosity 3 solely to expose fit statuses. Values agreed; all logged minimizations in the verbose significance runs returned status 0. This method computes q0 directly; its name useMinos does not request the failed MultiDimFit MINOS intervals. Compare exact q0=Z² with the coarse linear interpolation near zero in `validation.json`; interpolation is only a cross-check.

The ttH expected-limit calculation warns that the target-zero reference Asimov refits to r_ttH=0.028112 rather than exactly 0, and has internal nonzero alternative-trial statuses despite successful reported quantiles. Its limit is **REVIEW_REQUIRED_REFERENCE_CLOSURE_AND_INTERNAL_TRIALS**, not a fully validated final result. The source of that displacement has not been established; do not automatically attribute it to bkg_lep or ttH_had_2. The tHq limit's independent status is recorded below. Read process exit 0 together with fit-status logs, not as acceptance by itself.

- significance r_ttH: `logs_DCB/significance_r_ttH_20261016_062423_3870560/`; validation **VALIDATED_ASIMOV_SIGNIFICANCE_LOGGED_FITS_STATUS0**; logged minimizer counts {'0': 274}; last logged status 0.
- significance r_tHq: `logs_DCB/significance_r_tHq_20261016_062422_3870359/`; validation **VALIDATED_ASIMOV_SIGNIFICANCE_LOGGED_FITS_STATUS0**; logged minimizer counts {'0': 138}; last logged status 0.
- expectedLimit r_ttH: `logs_DCB/expectedLimit_r_ttH_20261016_062156_3867899/`; validation **REVIEW_REQUIRED_REFERENCE_CLOSURE_AND_INTERNAL_TRIALS**; logged minimizer counts {'0': 3500, '-1': 5}; last logged status 0.
- expectedLimit r_tHq: `logs_DCB/expectedLimit_r_tHq_20261016_062158_3868168/`; validation **EXPECTED_QUANTILES_VALIDATED_CONDITIONAL_ASIMOV**; logged minimizer counts {'0': 2621}; last logged status 0.

Combined machine-readable results and dataset fingerprint: `logs_DCB/significance_expectedLimits_20261016_062836/results.json`, `results.csv` and `input_asimov_fingerprint.json`. The first significance attempts at `significance_r_ttH_20261016_062152_3867454` and `significance_r_tHq_20261016_062159_3868419` are preserved; the verbosity-3 attempts above supply status validation. No significance or limit is an observed-data result. Before final use, resolve the ttH reference closure and examine any other fit warnings; a finite upper limit alone is insufficient.

### Impact command review and staged DCB runner (prepared only)

Compared the analyst's archived ttH/tHq scripts, Florian's dedicated impact runner at cached commit `d9031abb4e8c4e10c312e73912fece53fbd974bb`, and the installed Impacts/MultiDimFit code. Full comparison, source references, fitting definition and cautions: [README_impacts_design.md](README_impacts_design.md).

New runner: `run_DCB_impacts.sh`. Preparation and initial-command dry-run succeeded in `logs_DCB/impacts_DCB_20261016_064053_3911845/`; exactly 91 constrained nuisances and five photon pilot nuisances were identified. **No impact fit or plot has run.** Both POIs are processed together, the other strength/backgrounds remain profiled, and only MH is frozen outside the intentional per-nuisance endpoint tests. Same saved SM Asimov/snapshot; no workspace rebuild or 300-point scans.

The next step is initial fits only:

```bash
run_dir=logs_DCB/impacts_DCB_20261016_064053_3911845
bash run_DCB_impacts.sh initial "$run_dir"
```

Review both initial intervals and minimizer logs before the five-photon pilot and full nuisance stage. The runner uses profile crossings (--robustFit 1), not covariance impacts or the old midpoint recentering helper; it keeps the full raw JSON and refuses to silently drop missing parameter fits. Per-nuisance logs, structural QC and standard per-POI plots are staged separately. Original first-command script and old plotting/physics code are unchanged. The generic DCB/SoG pipeline and custom plots are deferred; `plots/combine` and `plots/custom` remain separate destinations. The ttH-limit closure warning is still unresolved.

## Copy everything across

The very first step is to copy your signal and background models, and the `.txt` datacard to this directory. The signal and background models must match the specified paths in the `.txt` datacard (the default is `./Models/signal` and `./Models/background`, you can change this with the `--sigModelWSDir` and `--bkgModelWSDir` options in the `Datacard/RunYields.py` script) i.e.
```
mkdir Models
mkdir Models/signal
mkdir Models/background
cp /path-to-signal-models/CMS-HGG*.root ./Models/signal/
cp /path-to-background-models/CMS-HGG*.root ./Models/background/
cp /path-to-datacard/Datacard.txt .
```

## Building the workspace

Then you are ready to build the `RooWorkspace` from the `.txt` datacard i.e. define the likelihood function. At this step you need to specify the signal parametrization (physics model) you want to use in the fit. These parametrizations are defined in `models.py`:

 * `mu_inclusive`: common signal strength for all signal processes

 * `mu`: per-production mode signal strength. This uses the `multiSignalModel` in combine to define the mapping between the parameter of interest (poi) and each signal process. The mapping is of the format `--PO \"map={cat}/{proc}:poi[nominal,min,max]\"`, where you can use wildcards to scale all processes which match the input string by the same poi. See also STXS `stage0`, `stage1p2_maximal` and `stage1p2_minimal` for example. You will need to write your own entry in the `models.py` file for a specific mapping.

 * `kappas`: an example of using a pre-defined `PhysicsModel` in combine. You can find the full list [here](https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit/tree/102x/python). If needed, you will need to add an entry into the `models.py` file.

Once you have decided/defined your signal parametrization you can run: 
```
python3 RunText2Workspace.py --mode {model} --dryRun
```
where `{model}` matches the key in `models.py`. For the simplest case, where you scale all signal processes equally then use `--mode mu_inclusive`.

The `--dryRun` option means the script (produced in `t2w_jobs`) will not be submitted. You can then go and run this script locally (recommend for analyses with a small number of categories as this step should not take too long). For bigger analyses you will want to submit the job to your favourite batch system e.g.
```
python3 RunText2Workspace.py --mode {model} --batch condor --queue workday
```
The output will be a compiled `RooWorkspace` with the name `Datacard_{model}.root`.

## Running the fits

When you have built the workspace, you are finally ready to run the fits and extract the results! The options for the fit are steered using the input json files:
```
python3 RunFits.py --inputJson inputs.json --mode {model}
```
This script uses the functionalities of [combineHarvester](https://cms-analysis.github.io/CombineHarvester/) in `combineTools`. The nominal fit is an `expected` fit (i.e. using an asimov toy dataset). An example input json file specifying the options for the `mu` model:
```
{
    "mu":{
        "pois":"r_ggH,r_VBF,r_VH,r_top",
        "fits":"profile1D:syst:all+profile1D:statonly:all",
        "points":"20:1+20:1",
        "fit_opts":"--saveSpecifiedNuis all --saveInactivePOI 1+--saveSpecifiedNuis all --saveInactivePOI 1"
    }
}
```
 * `pois`: full list of parameters of interest

 * `fits`: mapping for fit details with options deliminated using `:`. The first string specifies the type of fit e.g. `profile1D` corresponds to a 1D likelihood scan, where the other parameters of interest are profiled. Other options for this include `bestfit`, `singles`, `fixed`, `AsymptoticLimit`, `scan1D`, `profile2D`, `scan2D` and `robustHesse` (see bottom of this page for details). The second string is the user specified name of the fit. If this string contains `statonly` then the option `--freezeParameters allConstrainedNuisances` will be added to the combine command. The last string specifies the pois (comma-separated list) to run the fit for. Use `all` to run over all parameters of interest. You can define multiple fits using the `+` deliminator. In the example above there are two types of fit defined, one named `syst` and one named `statonly`.

 *  `points`: number of points in the likelihood scan, followed by the number of points per job. In this example you have 20 points and one point per job. Again, if multiple fits are defined, specify the respective `points` using the `+` deliminator. 

 * `fit_opts`: this is where you specify the combine options you want to use. For example `--setParameters`, `--setParameterRanges`, `--freezeParameters` etc. Separate options for multiple fits using the `+` deliminator. 

For tips, please refer to `example_inputs` directory for a set of example input jsons. 

There's a bunch of additional options when using the `RunFits.py` script:

 * `--ext`: running over a datacard with an extension in the name e.g. for `Datacard_LEPTONIC_mu.root` you would use `--ext _LEPTONIC`.
 * `--setPdfIndices`: set the pdfindex parameters to values specified in `pdfindex.json` when throwing the asimov toy in the expected scan. This can help to obtain closure in the expected scans: the prefit (B-only) pdf indices can differ from the postfit (S+B) pdf indices, which means you can extract a different signal strength to that put in. First run a `bestfit` adding `--saveSpecifiedIndex pdfindex_cat0,pdfindex_cat1,...,pdfindex_catN` to the `fit_opts` of the json file (see `example_inputs/inputs_bestfit.json`). Then make a `pdfindex.json` file using the post-fit values of the pdf indices.
 * `--doObserved`: run the observed fit (unblinding)
 * `--snapshotWSFile`: path to post-fit workspace created using the `--saveWorkspace` option in `fit-opts`. The initial value of the fit parameters will be set to their post-fit values. Useful when running stat-only observed scans, to fix nuisance parameters to their post-fit values (and hence obtain the same central value).
 * `--commonOpts`: combine options to add to all commands
 * `--batch`: batch system e.g. condor
 * `--queue`: batch queue e.g. workday
 * `--dryRun`: do not submit jobs, only create submission scripts

All jobs and outputs will be stored in the `runFits_{model}` directory.

## Collecting the fit results

After the fits are completed, you can collect/hadd the outputs using:
```
python3 CollectFits.py --inputJson inputs.json --mode {model} (--doObserved)
```

The hadded output will be of the format: `runFits_mu/profile1D_syst_r_ggH.root` for e.g. using the model `mu`, a `profile1D` fit with name `syst` for poi `r_ggH`. This contains the `limit` tree with all of the fit results plus any nuisance parameters that you have specified to save. The tree can then be used to plot the results with whatever fancy plots you can make e.g. for `profile2D` scans you can use the `../Plots/make2DPlot.py` for a smooth 2D likelihood contour.

For the 1D likelihood scans (`profile1D`) and (`scan1D`) fit types, the `CollectFits.py` script will execute `plot1DScan.py` of `combineTools` and the output is stored in `runFits_mu/Plots` directory. You can also use this script to produce plots with overlapping likelihood scans e.g.:
```
plot1DScan.py runFits_mu/profile1D_syst_r_ggH.root --y-cut 20 --y-max 20 --output r_ggH_statsyst --POI r_ggH --translate ../Plots/pois_mu.json --main-label "Expected" --main-color 1 --others runFits_mu/profile1D_statonly_r_ggH.root:"Stat only":2 --logo-sub "Preliminary"
```
Will overlay the systematic and stat-only fit results for the `r_ggH` parameter. 

## Impacts

See [combine manual](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/#nuisance-parameter-impacts) for details. Method for calculating the impact of nuisance parameters on the parameters of interest. Using your compiled `RooWorkspace` as input (e.g. `Datacard_mu.root`). The first step is to run an initial fit for each POI (as below), where the options in brackets are added for the calculating the expected impacts, setting the POIs to their SM values:
```
combineTool.py -M Impacts -d Datacard_mu.root -m 125 --doInitialFit --robustFit 1 (-t -1 --setParameters r_ggH=1,r_VBF=1,r_VH=1,r_top=1)
```
Then you perform a similar scan for each nuisance parameter:
```
combineTool.py -M Impacts -d Datacard_mu.root -m 125 --robustFit 1 --doFits (-t -1 --setParameters r_ggH=1,r_VBF=1,r_VH=1,r_top=1)
```
This command will run approximately 60 scans, and to speed things up the option `--parallel X` can be given to run `X` combine jobs simultaneously. When all jobs are finished you can collect the output and write to a json file and then plot the standard impacts plots using:
```
combineTool.py -M Impacts -d Datacard_mu.root -m 125 -o impacts.json
plotImpacts.py -i impacts.json -o impacts
```

Be careful: if you are running the observed impacts, the unblinded value of the POI will be displayed in the top right of the plot!


## Supported types of fit

 * `profile1D`: 1D likelihood scan where other pois are profiled
 * `scan1D`: 1D likelihood scan where other pois are fixed
 * `robuseHesse`: make correlation matrix of fit parameters like [this](http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/HIG-19-015/CMS-PAS-HIG-19-015_Figure_019.pdf). Use `Plots/makeCorrMatrix.py` to plot.
 * `bestfit`: single best-fit point. Add `--saveWorkspace` option to `fit_opts` to save the postfit workspace. This can then be loaded when using `RunFits.py` with the `--snapshotWSFile` option
 * `fixed`: extract deltaNLL for a fixed point in the parameter space specified with e.g. `--setParameters r=1 --fixedPointPOIs r=1` for SM scenario.
 * `singles`: extract +-1sigma confidence interval, assuming gaussian interval. Better to use the full likelihood scan for non-gaussian scenario.
 * `AsymptoticLimits`: use for limits e.g. rare/BSM analyses
 * `profile2D`: 2D likelihood scan, where other pois are profiled. Separate the two pois in the `fits` option options of the input json using a comma.
 * `scan2D`: 2D likelihood scan, where other pois are fixed. Separate the two pois in the `fits` option options of the input json using a comma.

## Bias studies

Scripts/instructions for bias studies are in `Checks` folder.


## Reusable fiducial runner: first stage (16 October 2026)

`runner_r_2D_fiducial.sh` currently implements **only `--step snapshot`**. Later stages (scans, limits, significance, impacts, custom plots and www publication) are not implemented or run by this version. The existing `new_runner_codex.sh` is unchanged.

Preview without creating files or running a fit:

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/Datacard_r_2D_fiducial.root" \
  --outdir "$PWD/DCB" \
  --step snapshot --dry-run
```

Remove `--dry-run` to execute. Choose a new output folder; an existing snapshot directory is never overwritten. This new runner has been syntax checked and its default and custom dry-run commands inspected; no actual snapshot fit has yet been executed with it.

Optional settings are `--mass 125.09`, `--set-parameters r_tHq=1,r_ttH=1`, `--ranges r_ttH=-1,3:r_tHq=-25,25`, `--strategy 2`, `--tolerance 0.1` and `--seed 123456`. These are defaults except ranges: omitting `--ranges` retains the workspace limits. `--set-parameters` must include both POIs; set MH using `--mass`, not this list. Extra named initial values are checked against the workspace. Both POIs float in this stage; fixing the other POI is a later scan option.

The input is moved to `<outdir>/workspace.root`, with a SHA256 recorded before moving and checked afterward. The source path is removed. If the workspace already lives at that exact destination, it is reused. A different existing destination workspace is never overwritten. The runner and README remain directly in `Combine/`; the output folder name is supplied with `--outdir` (for example `CombineFit`, `DCB`, or `SoG`). All subsequent fit paths are absolute. `<outdir>/snapshot/` contains the executed runner, shell-quoted command, JSON manifest with input SHA256 and settings, combined stdout/stderr `fit.log`, exit status, Combine ROOT outputs and `validation.json`. `<outdir>/audit/` is reserved for later workflow records. A directory lock prevents two runners using the same output folder concurrently; after an interrupted process, inspect the folder before removing a stale lock.

The default physics command follows `new_runner_codex.sh`: `MultiDimFit --algo none -t -1`, both injected strengths 1, fixed MH 125.09, both POIs floating, strategy 2, tolerance 0.1, the same four discrete-profiling runtime options, and `--saveWorkspace --saveFitResult --saveToys`. The seed is now explicit and output names are model-independent. No background indices are frozen by the runner; existing workspace constant/free settings are retained.

Validation checks the saved `MultiDimFit` snapshot, `toys/toy_asimov`, `fit_mdf`, finite POI values and fixed MH. It records minimizer status, covariance quality, EDM, dataset size and weight sum. It always marks numerical/physics review required: successful execution and readable outputs do not establish covariance validity, boundary stability or Asimov closure. This first version never automatically proceeds to another stage.


Cleanup on 16 October: removed `example_inputs/` and `inputs_tutorial/` (12 files), after verifying every file was tracked and byte-identical to Git HEAD. Recovery: `git restore --source=HEAD -- Combine/example_inputs Combine/inputs_tutorial` from the repository root. File checksums are recorded in `codex_checker/cleanup_examples_20261016.json`. No results, `Checks/`, archives, component models, Python tools or their default configuration inputs were removed. The previously completed `DCB/inputs/` and `DCB/snapshot/` retain their original layout; no existing run was migrated. The updated move layout was syntax checked and dry-run checked; no new fit or workspace move was executed during cleanup.


### Minimal top-level Python and JSON files

The new direct-Combine workflow retains `RunText2Workspace.py` and its imported `models.py` for building the workspace, and `rename.json` for POI display labels. The snapshot runner itself does not need any top-level JSON file.

Removed from the top level on 16 October 2026: `RunFits.py` (generic legacy fit dispatcher), `CollectFits.py` (collector/plotter for that dispatcher's output layout), `custom_crab.py` (optional CRAB customization used by RunFits), `inputs.json` and `inputs_fixed_MH.json` (generic inclusive/STXS fit configurations for RunFits/CollectFits), `pdfindex.json` (background-index choices for older RECO/STXS categories), and `replaceDataWithPseudoToy.py` (random-toy replacement of data_obs, unused in the saved-Asimov workflow). These are not required by `runner_r_2D_fiducial.sh` or by `RunText2Workspace.py`. Their removal retires the generic RunFits/CollectFits entry points from this working tree; it does not change the saved workspaces or fitted results. Git-unchanged files were removed; any local modifications were archived. Checksums and recovery details are under `codex_checker/cleanup_unused_*/manifest.json`. Restore individual tracked files from the repository root with `git restore --source=HEAD -- Combine/FILENAME` if the older workflow is needed again.


### Self-contained DCB input folder (16 October 2026)

Current inputs have been moved into `DCB/`: `Datacard_DCB.txt`, `workspace.root` (formerly `Datacard_DCB_r_2D_fiducial.root`), `Models_DCB/`, `text2workspace_DCB.log`, and `t2w_jobs/`. Datacard contents and ROOT model contents are unchanged; relative `Models_DCB/...` shape paths remain valid because both moved together. Relocation SHA256 records and original build scripts are in `DCB/audit/`. The generated DCB build job now uses absolute input/output paths and the DCB working directory. The one-line top-level `run_text2workspace_DCB.sh` executes that job and appends to the build log; it refuses to overwrite `DCB/workspace.root`. It retains the original r_2D_fiducial model options generated from models.py. If the model definition is later changed, regenerate the build job with RunText2Workspace.py rather than assuming the saved job picks up those edits.

The runner and README remain in `Combine/`. Start the snapshot from `Combine/` with:

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" \
  --outdir "$PWD/DCB" \
  --step snapshot
```

The already-relocated workspace is reused in place. No snapshot fit was started during this reorganization. Older examples with the workspace in the parent directory describe the previous layout.


### General build and input-organization script

Use `run_text2workspace.sh` for either DCB or SoG. It replaces the top-level DCB-only wrapper (preserved in `codex_checker/run_text2workspace_DCB_retired_20261016.sh`). Supply the current datacard, its model folder, and a **new** output folder:

```bash
bash run_text2workspace.sh \
  --datacard "$PWD/Datacard_DCB.txt" \
  --models "$PWD/Models_DCB" \
  --outdir "$PWD/DCB" \
  --mass 125.09 \
  --mode r_2D_fiducial
```

Add `--dry-run` to validate inputs and print the plan without moving files or building anything. DCB is just an example folder name; use the corresponding SoG inputs and output name for SoG. No old inputs are selected automatically. Missing inputs fail before folder creation. The datacard and model folder must be siblings, with relative shape paths inside that model folder. Absolute paths, parent-relative paths, and external model symlinks are rejected rather than silently rewritten. Existing output folders are rejected.

The script checks the model entry in models.py and referenced shape files, records all input SHA256 values, creates the output/audit/t2w_jobs folders, moves the datacard and model directory into the output folder, verifies checksums, and executes an absolute-path text2workspace command derived directly from models.py. This bypasses the original Python dispatcher's os.system exit-code limitation. All build output goes to terminal and `<outdir>/text2workspace.log`; command, settings, input hashes, a copy of models.py and build runner, and exit status are in audit/. The generated job is `t2w_jobs/build_workspace.sh`; it inherits the initialized CMSSW environment and refuses workspace overwrite. The final file is always `<outdir>/workspace.root`. ROOT object checks establish structural validity only; no Asimov or observed-data fit is run by this script.

After building, run `runner_r_2D_fiducial.sh --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" --step snapshot` from Combine. If the DCB folder was deleted along with its inputs, first restore the intended current datacard and model folder from their source locations; this script cannot reconstruct deleted physics inputs.


### Configurable one-POI likelihood scans

The reusable runner now implements `--step scan` as well as snapshot. It does not yet implement automatic multi-stage execution, significance, limits, impacts, plotting or publication. The current DCB snapshot reproduced the earlier central values (`r_ttH=1.04221487`, `r_tHq=1.02025741`) and saved Asimov (5120 entries, weight sum 162707.42120589444), **including** fit status 1, covariance quality 2 and EDM 0.18139. This is not a clean covariance result. Scan commands refit their likelihood reference from the snapshot; they do not use skipInitialFit. Their convergence and interval coverage still require validation.

Run one total ttH scan, profiling tHq:

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" \
  --step scan --poi r_ttH --scenario total \
  --scan-range '-0.5,3' --points 300 --other-poi profile
```

Append `--dry-run` to preview without a fit. Use `--scenario statOnly` for its matched statistical scan. Use `--poi r_tHq --scan-range '-10,15'` for the other POI; these are previously inspected ranges, not hardcoded defaults. Both scan range and number of points are configurable. `--ranges` can optionally change the other POI range; it cannot override the scanned POI's explicit `--scan-range`. Omitting it retains that other parameter's saved workspace range. `--other-poi fixed --other-value 1` produces a conditional scan with the other strength frozen at 1, which is a different statistical question from profiling it. Fixed values have their own output directory. Do not compare conditional and profiled uncertainties as if they were identical measurements.

The default scan minimizer is strategy 0 and tolerance 0.01; both are configurable. `--grid-start r_ttH=2.9` reproduces the optional grid-only seed used for previous tHq diagnostics; it does not freeze ttH. It is not automatically applied. Explicit `--set-parameters` values affect the initial reference as well as subsequent starting state; otherwise saved POI values are retained. The snapshot stage still defaults to both injected strengths 1, strategy 2, tolerance 0.1. A scan must use the same MH as the saved snapshot.

Every scan uses the exact saved `toys/toy_asimov` through `--toysFile`, the saved MultiDimFit snapshot, and a SHA256-checked input workspace. Only MH is frozen for total/profile scans. Stat-only additionally freezes allConstrainedNuisances at snapshot values; background normalizations, continuous shape parameters and discrete indices remain profiled according to their saved free/constant settings. Fixed-other mode additionally freezes that POI. This is a statistical-only convention with background fitting retained, not a frozen-background test.

Output hierarchy: `<outdir>/scans/<poi>/<total|statOnly>/<profile_other|fixed_other_VALUE>/`. Each contains the exact command, runner copy, input provenance/manifest (including the original snapshot warnings), combined terminal/error log, exit status, ROOT output, points.csv, and validation.json. Existing scan directories are rejected. Validation checks entry count, nonfinite/extreme/negative likelihood values and records minimizer-status counts; it does not establish correct interval crossings or convergence at every point. Negative/nonphysical tail points can require range adjustment or fit review. Standard/custom scan plots and interval extraction will be added separately after checking this first run. Only syntax and dry runs were exercised when implementing this stage.


### Completed 300-point DCB scan plots

All four current profile-other scans were checked. Each ttH scan has 276 valid grid points and 24 invalid negative-tail points; each tHq scan has 284 valid points and 16 invalid negative-tail points. Every valid point's last logged minimization status is 0, although internal alternative-background failures and background boundary warnings remain. Total q is below stat-only q across shared valid grid coordinates. This does not resolve the original snapshot covariance warning.

Both standard and custom overlays are now in `DCB/plots/scans/`. `combine/` contains CombineHarvester plot1DScan PNG/PDF/ROOT outputs and logs. The upstream script uses a cubic spline and thresholds q=1 and q=4 (1σ/2σ); 2σ corresponds to about 95.45%, not exactly 95%. It requires local output basenames because it prepends './'; the runner changes into the absolute output directory before invoking it. `custom/` contains straight-line raw-point overlays in PNG/PDF, `summary.json`, and `intervals.csv`, with q=1 and q=3.841458820694124 for approximately 68% and 95%. No recentering or smoothing is used in custom plots. Invalid rows are omitted, listed in summary.json, and never joined across gaps. Standard plotting removes high-q rows with y-cut 20; y-max 6 changes only the display.

| POI | Scenario | Best fit | 68% interval (linear interpolation) | 95% interval (linear interpolation) |
|---|---|---:|---|---|
| r_ttH | Total | 1.042215 | [0.614590, 1.534877] | [0.265488, 2.079022] |
| r_ttH | Stat-only | 1.042215 | [0.616219, 1.529727] | [0.267020, 2.062874] |
| r_tHq | Total | 1.020290 | [-3.506599, 6.535043] | [-6.680856, 12.808921] |
| r_tHq | Stat-only | 1.020247 | [-3.472930, 6.460902] | [-6.581895, 12.588220] |

Reusable plotting command from Combine (regenerates plot artifacts, never reruns fits):

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" --step plot
```

Add --dry-run for a no-write preview. This runner plot stage currently supports profile-other overlays only. The standalone custom plotter is `../Plots/plot_fiducial_scans.py --run-dir /absolute/run/folder`; it reads existing points.csv and manifests, checks matched snapshot hashes/ranges/points/other-POI modes and valid-point final statuses, then writes the custom plots and interval reports. PDF/PNG outputs were generated for both POIs; the tHq custom overlay was visually inspected. No significance, limit, impact or www publication was run in this plotting step.


### Scan plot presentation matched to the earlier DCB plots

The custom overlays were restyled after inspecting `/eos/user/r/rkumarag/www/ttH-tH-CP-Analysis/old_16OCT/Combine/DCBplusGaussaian/CombinePlot_r_ttH.png` and `CombinePlot_r_tHq.png`: black total curve, red dotted statistical-only curve, CMS Internal, an upper-right fitted-value/uncertainty annotation, and a default y maximum of 20 (`--y-max` can override this in the standalone plotter). Current best-fit values are retained, not shifted toward 1 to resemble older fits. The tHq curve stops at the actual scanned endpoint 15; the older plot extending to 25 does not justify extrapolation.

The second annotation uses an **approximate** asymmetric quadrature subtraction: sigma_syst,down/up = sqrt(sigma_total,down/up^2 - sigma_stat,down/up^2), separately for each side of the 68% interval. This is a conventional error decomposition, not an independent systematic-only fit, and correlated individual impacts do not add in quadrature to it. Values and this qualification are stored in custom/summary.json. No scan points, fitted values or likelihood values were changed by restyling. Both PNG/PDF pairs were regenerated and inspected.


Standard Combine overlays were also regenerated to match the earlier DCB presentation: --y-max 20, --main-label 'Total Uncert.', red Stat-Only overlay, --breakdown Syst,Stat, and local POI translation labels. The installed plotter uses its own marker/line style and cubic-spline interval extraction; its q=4 line is 2σ. The displayed systematic component is the plotter's approximate quadrature subtraction, not a separate fitted uncertainty. Options and exact commands are saved in the main runner and combine/*.command.sh; PNG/PDF outputs and logs were verified and the ttH image inspected. Upstream CombineHarvester code was not modified. No fit was rerun.


### Stat-first display, future ranges and Asimov closure check

Both plot styles now show **Stat before Syst** in the decomposed annotation. The standard-style plotter is a local copy `../Plots/plot1DScan_fiducial.py` with an upstream SHA256 header and one display-only --stat-first option. It computes breakdown components in the original Syst,Stat order, then reorders their display. Simply passing --breakdown Stat,Syst to the upstream script would mislabel the subtraction and is not done. Upstream CombineHarvester is unchanged.

Recommendations for the next matched 300-point scans are ttH [0,2.5] and tHq [-8,20], recorded in DCB/audit/recommended_scan_ranges.json. Both cover current 95% crossings with margin and exclude known invalid tails; the added tHq region above 15 is not yet validated. There is no need to rerun the existing scans merely to restyle the plots. To preserve prior scans, --scan-tag refined writes to `profile_other__refined` instead of profile_other. Supply the same tag to --step plot to read those scans and write plots/scans/refined/. Fixed-other tagged scan output is supported; runner plotting remains profile-other only.

A dedicated check reused the exact saved SM Asimov and snapshot, profiled continuous nuisance/background parameters, and compared --algo fixed at (r_ttH,r_tHq)=(1,1) with the free-reference fit. Commands, logs, ROOT outputs, index comparison and results.json are in DCB/checks/asimov_closure_20261016_150317/.

| Discrete-background treatment | Free-reference r_ttH | Free-reference r_tHq | q at injected (1,1) relative to that reference |
|---|---:|---:|---:|
| Profiled | 1.042215 | 1.020290 | 0.00958997 |
| Fixed to generation input choices | 1.000129 | 0.998802 | -0.000001989 (numerical residual) |

The original and saved-fit indices differ in bkg_lep (1 to 3) and ttH_had_2 (1 to 2). Fixing all indices to their generation input choices restores practical closure, supporting discrete-background freedom as the origin of the offset in this check. This does not separately isolate either category, establish global optimizer robustness, or resolve the original snapshot covariance warning. The tiny negative fixed-index q is a minimization residual, not a physical negative test statistic. Production scans and their input dataset remain unchanged, with background choices profiled. No curves were artificially shifted to 1 and no refined scan was launched.

Custom scan plots now use the label **CMS Private work**, as requested; standard-style plots retain CMS Internal. This is a label-only change. In the closure diagnostic, fixed-to-generation choices means freezing discrete background PDF indices, not fixing the signal strengths in the free-reference fit. Continuous nuisance/background parameters were still fitted. Production scans retain discrete profiling.


### Verified explanation of old versus current Asimov closure

The old first snapshot was not exactly at unity: archived DCB ROOT outputs give r_ttH=1.02919135 and r_tHq=1.03424166 (fit status 0, covariance quality 3). The later old total scans give r_ttH=0.98866761 and r_tHq=1.00720537. Their commands load the postfit snapshot, reset strengths to 1 and use -t -1 without --toysFile, generating a NEW Asimov dataset from postfit background/nuisance settings. Current scans explicitly reuse the first saved dataset. Installed Combine.cc loads the snapshot around line 455, reads a supplied toys/toy_asimov around line 934, and otherwise generates new Asimov around line 985.

A controlled diagnostic on the current model reproduced this difference: reusing the first Asimov gives (1.04221487,1.02025735), while regenerating from the postfit state gives (1.00004649,1.00119436). Both datasets have 5120 entries, but different hashes and weight sums (162707.42120589444 versus 162706.33617070450). All 69 logged minimizations in the regeneration diagnostic report status 0. Evidence is in DCB/checks/legacy_asimov_regeneration_20261016_153219/ (commands, logs, ROOT and results.json).

This supports the change in dataset construction as the reason the old scan looked closer to 1, without needing a DCB shape modification. It does not isolate every historical difference or resolve the separate first-snapshot covariance warning. Production datasets and scans are unchanged. Both initial-workspace and postfit expected-data constructions can be deliberate conventions; changing datasets between stages must be explicit, and closeness to 1 alone does not validate a fit.


### Decision: keep the current saved Asimov and scans

The analyst agreed to retain the current first-generated SM Asimov dataset and existing total/stat-only scans. Do not regenerate or replace production data merely to force fitted strengths to 1. The near-unity result from generation-fixed background choices is a diagnostic; production background PDF choices remain profiled. Before treating the whole pipeline as validated, investigate the separate first-snapshot status 1 / covariance quality 2 / EDM warning. An isolated current-workspace comparison of minimum-only versus standard error calculations has been started under DCB/checks/covariance_pair_*/; the exact saved dataset and starting snapshot are shared, both POIs and background indices remain profiled, and the only command difference is saveFitResult. No production snapshot, scan, nuisance prior, model or dataset is changed.


### Current-workspace covariance pair: result and next step

The controlled pair in DCB/checks/covariance_pair_20261016_161348/ finished. Both start from the current saved MultiDimFit snapshot, use its exact saved Asimov, profile both POIs and background choices, and use strategy 2/tolerance 0.1. Neither modifies production results. The minimum-only command omits an explicit saveFitResult error pass, but Minuit strategy 2 can itself perform internal curvature calculations; it is not a promise of no Hessian work.

Both runs return r_ttH=1.04221287 and r_tHq=1.02027797, consistent with the production snapshot/scans. The minimum-only run logs one final status 1 (forced-positive-definite covariance). Adding saveFitResult triggers an additional minimization/HESSE/error sequence: the final saved RooFitResult reports MINIMIZE=0, HESSE=0, covQual=3, EDM=4.77383e-7. Nevertheless, **MINOS fails for both POIs**, explicitly recorded in fit.log. Saved RooFitResult status 0 alone therefore does not certify successful profile intervals.

This warm-start comparison demonstrates that a clean local covariance can be recovered at essentially the same minimum; it does not prove standard HESSE always fails, identify the exact original numerical instability, or validate MINOS. Keep the original snapshot and scans. Use their checked explicit grid-profile crossings for quoted expected intervals, retaining numerical/background-envelope caveats. Next workflow work is adding and validating significance and expected-limit stages with explicit hypotheses and dataset handling, not regenerating Asimov data to improve visual closure. Significance and limits from earlier archived checks are separate from newly implementing these stages in the reusable runner.


### Reusable significance stage

The main runner now supports --step significance, one POI per command. It reuses the exact saved SM-injected Asimov and MultiDimFit starting snapshot. The target strength tests zero against a nonnegative alternative; --ranges is required and the target lower bound must be zero. The other POI is explicitly floated/profiled; only MH is frozen, so all constrained nuisances and background choices retain their intended profiling. This first version supports total uncertainties and profile-other only, refusing unsupported scenarios/fixed-other modes rather than silently changing the hypothesis. No observed collision data are fitted.

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" \
  --step significance --poi r_ttH --ranges r_ttH=0,5 --other-poi profile
```

After validation, use --poi r_tHq --ranges r_tHq=0,25 for the second strength. Default strategy 0/tolerance 0.01 are configurable. Other-POI ranges remain those of the saved workspace unless explicitly included in --ranges. No grid-point option is needed for significance. Each result goes to significance/POI/total/profile_other/ (optional --scan-tag appends a suffix), with the runner copy, exact command, input snapshot SHA256, saved workspace/toys, full terminal/error log, exit status and results.json (Z, q0 and logged minimizer statuses). Existing outputs are rejected. Entry/finite-value checks do not replace convergence/boundary review. Both significance commands passed syntax and no-write dry-run checks; no significance fit was executed when adding this stage. Limits and impacts are not yet implemented in this reusable runner.


### Current significance results and reusable expected limits

Current saved-SM-Asimov significances: ttH Z=2.82667960 (273 logged status 0, one internal background-alternative status -1 followed by success; final status 0), tHq Z=0.21112518 (all 138 logged minimizations status 0). Both profile the other signal strength; these are expected local significances, not observed-data results.

The runner now implements --step limit with --poi and explicit --ranges. It invokes AsymptoticLimits --run expected --rule CLs --cl 0.95 --picky, starting from the saved snapshot and supplying the exact saved SM Asimov via --toysFile. Combine constructs the target-zero auxiliary expected reference, conditioning on the supplied data and profiling the other strength. This is not --run observed on the SM toy and not a new real-data fit. Non-target contributions and the other strength follow the defined physics model; target-zero does not mean removing all Higgs processes. Expected bands describe the distribution of limits, not measurement error bars. Results are dimensionless strength limits, not fb.

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" \
  --step limit --poi r_ttH --ranges r_ttH=0,10 --other-poi profile
```

After validation, use --poi r_tHq --ranges r_tHq=0,50. The target range starts at zero; other-POI ranges retain snapshot settings unless explicitly supplied. Default strategy 0/tolerance 0.01 can be overridden. Both nuisances and background choices are profiled with MH frozen. This version supports total/profile-other only. Outputs are limits/POI/total/profile_other/, with exact command, runner copy, snapshot SHA256, full log, saved workspace/toys, exit status and results.json containing all five expected bands. Checks require five ordered finite nonnegative expected quantiles; numerical convergence, auxiliary-Asimov closure warnings and range saturation still require review. The old ttH limit diagnostic had an auxiliary closure warning; do not assume the new settings resolve it until inspecting this run. No limit fit was run when adding this stage; dry-run and syntax checks passed.

Current ttH expected limit: median 0.83984375; expected bands [0.42812347,0.58412683,0.83984375,1.24490976,1.77155054]. Final minimization status 0, four internal -1 statuses, and an auxiliary-Asimov closure warning: its best fit is r_ttH=0.027983 rather than zero. This reproduces the earlier warning and remains REVIEW_REQUIRED, not final validation. The automated warning collector was corrected to recognize lowercase asimov in the log. The separate tHq expected limit can proceed, while this ttH diagnostic remains open.


### Current runner: checked significance and expected upper limits

| Target strength | Expected local significance on saved SM Asimov | Median expected 95% CLs upper limit | Expected limit 68% band | Expected limit 95% band |
|---|---:|---:|---|---|
| r_ttH (ttH+tHW) | 2.826680 sigma | 0.839844 | [0.584127, 1.244910] | [0.428123, 1.771551] |
| r_tHq | 0.211125 sigma | 11.445313 | [7.877122, 17.056757] | [5.700302, 24.474350] |

These are expected/blinded results with the other strength profiled, not real-data measurements. Significance tests target strength zero using the saved SM-injected data, giving q0=7.990118 and 0.044574. Expected CLs bands use the target-zero auxiliary expected reference; the saved SM data condition that fit, and the other strength is fitted rather than necessarily fixed at its injected value. Therefore r_ttH<0.840 does NOT claim the SM signal has been excluded by the SM Asimov dataset. The limit band is the expected distribution of upper limits, not uncertainty on the measured signal strength. Limits are dimensionless normalization factors for the defined fiducial model, not fb; conversion requires the corresponding reference cross section.

All four processes exit 0 and end with minimizer status 0. ttH significance contains one internal failed alternative fit followed by successful fits; tHq significance has all 138 statuses 0. ttH limit contains four internal failures and an auxiliary-Asimov closure warning (r_ttH=0.027983 instead of zero), so it remains provisional. tHq limit has all 3104 logged statuses 0 and no auxiliary closure warning. Both limit logs contain background-parameter near-boundary warnings (77 ttH messages, 42 tHq messages), which are retained for review; these counts are repeated log messages, not counts of failed final fits. All five expected limit quantiles are ordered and inside target ranges [0,10] and [0,50]. A zero final status does not by itself validate the statistical model or all alternative fits.

Combined result records and boundary-parameter names are in DCB/checks/statistical_results_summary.json. Existing heavy-flavor cap, unavailable PDF-migration and MC-stat modeling review items remain. The next diagnostic target is the ttH auxiliary-reference closure warning; do not label the entire chain physics-final merely because all commands finished.


### Expected-limit plots with 1sigma and 2sigma bands

The existing Plots/makeSummaryPlot.py primarily handles measurement summaries, so `../Plots/plot_fiducial_limits.py` was added for this two-strength expected-limit result. It reads the five checked Combine limit quantiles in each results.json, validates order/positivity, and makes combined and individual PNG/PDF summaries under `DCB/plots/limits/`. `expected_limits.png/pdf` shows both POIs on a common logarithmic strength axis; r_ttH.png/pdf and r_tHq.png/pdf show individual linear-axis summaries. No observed limit is drawn. The CMS Private work label is used.

Black dashed markers show the median expected **95% CLs upper limit**. Green bands span the 16th to 84th percentile of expected limits (approximately +/-1sigma); yellow bands span the 2.5th to 97.5th percentiles (approximately +/-2sigma). They are not uncertainty intervals on a measured strength, not significance errors, and do not change the 95% CLs threshold. The vertical reference at strength 1 is the SM normalization; this target-zero expected-limit plot does not claim an observed exclusion of the SM. The target-zero reference and other-strength profiling are explicit. The ttH auxiliary-Asimov closure warning is visibly marked provisional and retained in plot_inputs.json with source hashes. The background near-boundary warnings in both limit logs remain review items.

Regenerate without running any fits:

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" --step plot-limits
```

The standalone alternative is `python3 -B ../Plots/plot_fiducial_limits.py --run-dir "$PWD/DCB"` in an active CMSSW environment. The plotter generated all six PNG/PDF artifacts from the current quantiles; the combined image was visually inspected. Significance values have no corresponding five expected-limit bands, so none were invented for significance. Current fit/scan/limit results were not changed by plotting.

Limit-plot axis/layout correction: combined log axis now displays explicit numeric ticks (0.3, 0.5, 1, 2, 3, 5, 10, 20, 30 where in range), and states log scale. Individual panels use readable linear ticks and rounded endpoints (current ttH 0–2, tHq 0–30). Floating top/right ticks were removed, category-label margins enlarged, and legend/footer spacing and tight export bounds adjusted. All combined/individual PNG/PDF outputs were regenerated and visually inspected. Quantiles, bands and provisional warnings are unchanged.


### Main reporting choice: ttH measurement/significance, tHq upper limit

The analyst chose to retain ttH+tHW signal-strength scans/measurement and its current expected significance (2.82668 sigma), and to show only the tHq expected upper limit in the main limit plots. This is a reporting choice, not a rule that significance forbids reporting a limit. The ttH limit calculation and its unresolved auxiliary-reference warning remain diagnostics.

The default plot-limits stage now needs only the tHq limit result and writes the tHq-only main summary to plots/limits/expected_limits.png/pdf (also r_tHq.png/pdf), with green/yellow expected bands. Previously generated ttH and two-POI comparison plots plus their input record have been moved to plots/limits/diagnostics/. The raw ttH calculation remains under limits/r_ttH/, unchanged, and must not be mistaken for a validated main result. The standalone plotter can optionally regenerate these diagnostics with --include-tth-diagnostic; the main summary remains tHq-only. No warning was removed from diagnostic records, and no fitting or statistical prescriptions changed.


### Reusable impacts: first stage only

The main runner now accepts --step impacts --impact-stage initial. This runs two sequential MultiDimFit --algo singles robust profile-interval fits, one per POI, with the other strength profiled. It reads the current run's exact saved Asimov/snapshot, freezes only MH, profiles background choices, uses both POIs in a consistent order, and calls the compiled combine binary directly. It does not start nuisance impact fits or collect/plot impacts yet.

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" \
  --step impacts --impact-stage initial \
  --ranges 'r_ttH=-1,3:r_tHq=-25,25'
```

These explicit ranges match the original workspace impact bounds; they are not the nonnegative significance/limit bounds or the future grid-display ranges. Default minimizer/robust strategy 0, tolerance 0.01, stepSize 0.05 and crossingTolerance 0.00005 match the reviewed impact workflow. Output is impacts/, with manifest, exact commands, runner copy, per-POI logs/exit statuses, constrained-nuisance list for future stages, five-photon pilot list and validation/initial.json. No saveToys option is added here, preserving the no-seed filenames needed by split-initial impact collection. Existing impact folders are refused. Structural checks require three finite entries and bracketing endpoints; inspect the fits before proceeding. Syntax and dry-run checks passed; no initial impact fit was started while implementing the stage.


### Initial impact check and photon pilot

Current initial robust intervals: r_ttH best 1.042215, [0.616538,1.532038]; r_tHq best 1.020290, [-3.484469,6.502394]. Both initial minimizations report MINIMIZE=0 and final status 0. Verbose crossing logs contain 3/7 internal failed attempts respectively and background near-boundary warnings; these remain review caveats, not discarded failures. Intervals agree with the previous impact initialization and the grid scan within the threshold/interpolation differences.

Next command (only the five photon nuisances):

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" \
  --step impacts --impact-stage pilot
```

The pilot uses Smearing, ScaleEB, ScaleEE, Material and FNUF. It derives compiled-combine --algo impact commands from the initial manifest, retaining the exact snapshot/data hash, POI order, ranges, minimizer/crossing settings and nuisance constraints. Both strengths and backgrounds are profiled. Four independent fits run at a time, with start/finish progress on terminal and full per-nuisance stdout/stderr in impacts/logs/pilot_TIMESTAMP_NUISANCE.log. Exact commands and runner copy are in impacts/pilot_runs/TIMESTAMP/. Results are checked for three finite entries, bracketing nuisance endpoints and final statuses; all warnings remain in validation/pilot.json. It refuses to overwrite existing photon outputs or change initial settings. No parameters are recentered/removed. This stage passed syntax and no-fit dry-run checks; it was not executed during implementation. Run the pilot and inspect it before all-nuisance fits.

**Sequential execution preference:** at the analyst’s request, the photon pilot now runs strictly one nuisance at a time. The next Combine process starts only after the previous one exits; no thread/process pool is used. Earlier descriptions of four parallel pilot fits are superseded. Keep all future nuisance fits sequential as well. Compiled Combine calls are retained to avoid the previous Python-launcher import problem; sequential execution is a precaution, not proof that parallelism caused that issue.


### Full nuisance impacts: strictly sequential

The five current photon pilot fits completed with process exit 0, structurally complete triples and final minimizer status 0. No Python import errors occurred. Internal failed minimizations and background near-boundary warnings remain in validation/pilot.json; final success alone does not validate all candidate fits. Their responses match the earlier pilot. They are retained rather than rerun solely because they finished under the older parallel launcher.

Run remaining nuisances:

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" \
  --step impacts --impact-stage fit
```

This selects the 91 constrained nuisances, revalidates/reuses the five completed photon fits and runs the 86 missing fits strictly one at a time with compiled combine. It retains the initial manifest's dataset, ranges, parameter order, constraints and minimizer/crossing settings. Start/finish progress is printed; full per-fit output is saved in impacts/logs/fit_TIMESTAMP_NUISANCE.log. Exact pending commands/runner copy are in impacts/fit_runs/TIMESTAMP/. Validation/fit.json is saved after each completed or reused result. A nonzero process exit, incomplete/nonfinite/nonbracketing ROOT result, or nonzero final logged minimization status stops the run before the next nuisance. Internal candidate failures and boundaries are recorded for review rather than automatically discarded. Existing unvalidated results block overwrite; inspect/preserve them before a targeted retry. A later invocation reuses already accepted entries from the saved report. No nuisance is removed/recentered. This stage was syntax and dry-run checked (91 selected, 5 existing, 86 pending); no full fit run was launched during implementation. Collection and plotting will follow only after validating completeness and warnings.


### Sequential impacts stopped at ElectronSmearing: targeted recovery

The full stage stopped at CMS_hgg_ElectronSmearing as designed: process exit was 0 but the final minimization status was -1 and its ROOT result lacked the required three entries. The log reports line-search stagnation with EDM 0.000127662 above the acceptance threshold. Nine nuisance outputs are accepted at this point (five photons plus four earlier nuisances); this is a fit convergence failure, not a Python import/environment failure.

A targeted recovery stage is now available:

```bash
bash runner_r_2D_fiducial.sh \
  --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" \
  --step impacts --impact-stage retry \
  --nuisance CMS_hgg_ElectronSmearing --strategy 1
```

This changes the minimizer and robust-crossing strategy only for that nuisance, preserving the data, model, nuisance priors, ranges and tolerances. It archives the failed ROOT result and prior validation under impacts/retry_runs/TIMESTAMP/ before fitting. Original logs remain. It requires a recorded failed result and explicit strategy 1 or 2; accepted results cannot be silently overwritten. On success it updates that nuisance entry in validation/fit.json with the retry provenance. After reviewing the retry, resume the ordinary --impact-stage fit command, which revalidates/reuses the accepted results and starts only missing nuisances sequentially. A strategy change is a numerical recovery attempt, not a guarantee of success. The retry command was syntax/dry-run checked but not launched during implementation.


## Automatic sequential impact retries (17 October 2026)

`runner_r_2D_fiducial.sh --step impacts --impact-stage fit` now retains validated results and automatically escalates a failed nuisance from the initial strategy to strategies 1 and 2. Pilot fits use the same escalation. Explicit `retry --strategy 1` also tries strategy 2 if necessary. The saved workspace, Asimov dataset, mass, ranges, tolerances and physics model are unchanged; both minimizer and robust-fit strategy change together.

Each attempt has a separate log, exit status and exact command JSON. Failed ROOT outputs are archived under `impacts/<stage>_runs/<timestamp>/<nuisance>/` before another attempt replaces the canonical output. Validation reports keep attempt history and list `failed_nuisances` and `accepted_nuisances`. Acceptance requires process exit 0, three finite entries with nuisance endpoints bracketing the best fit, and final logged minimization status 0. Internal failures and boundary warnings remain available for review; automatic acceptance is not physics approval.

If strategy 2 also fails, the runner records that nuisance and continues sequentially. The final command returns nonzero if unresolved fits remain; do not collect/finalize impact plots until they are resolved. Resuming preserves accepted results, retries recorded failures, and runs missing nuisances. Unknown existing ROOT outputs still require inspection. Initial-fit failures are not automatically retried.

A process already launched before this update continues using its old embedded Python code. Do not launch another runner concurrently. When the current process ends or stops, use the same fit command again to activate this behavior:

```bash
bash runner_r_2D_fiducial.sh --workspace "$PWD/DCB/workspace.root" --outdir "$PWD/DCB" --step impacts --impact-stage fit
```

## DCB impacts collected (17 October 2026)

All 91 selected constrained nuisances completed with finite endpoint results, exit 0 and final logged minimization status 0. Official Combine collection and standard plotImpacts plots are saved under `DCB/impacts/collected_20261017/`: `impacts.json`, `impacts_r_ttH.pdf`, `impacts_r_tHq.pdf`, first-page PNG previews, exact commands, logs and `collection_validation.json`. Each PDF includes all 91 rows over four pages. No values were recentered and correctImpacts.py was not used. Background parameters/indices profile during fits but are not separate scanned impact rows.

The initial fitted intervals are r_ttH = 1.042215 -0.425678/+0.489823 and r_tHq = 1.020290 -4.504759/+5.482104, with the other POI profiled. Leading r_ttH impacts are ttH scale_0 shape, bTagSF_sys_lf, bTagSF_sys_cferr1 and photon Smearing (fourth). Leading r_tHq impact is Higgs_plus_b_syst_ggH. These are absolute strength impacts, not percentages.

Boundary warnings occur in 51 nuisance logs, mostly for background-function parameters. Higgs_plus_c_syst_ggH also has intermediate large-error warnings for photon nuisances/background normalizations; final technical acceptance does not establish numerical stability of every internal step. The collected results are for review, with the warning audit and original snapshot fit-quality caveat retained. No new fits were run during collection.

### ggH charm nuisance strategy-1 stability check

The separate `check_impact_ggH_charm.sh` run completed in 13.27 minutes on 17 October. All 2,277 logged minimization statuses are zero. Impacts change from 0.00334847 to 0.00357306 for r_ttH (+6.7%, absolute change 0.000225), and from 0.0870267 to 0.0847337 for r_tHq (-2.6%, absolute change 0.002293). These changes are small relative to the total POI uncertainties and support stability of this nuisance's impact. They do not establish exact convergence of every other nuisance. Photon/background-normalization warnings seen in the strategy-0 log do not appear in this check; a background Bernstein parameter still has within-one-error-of-bound warnings, which are not equivalent to its value being pinned to a boundary. Results/log/comparison.json are under `DCB/impacts/stability_Higgs_plus_c_syst_ggH_strategy1/`. The canonical strategy-0 fit and collected JSON/plots have not been replaced.
