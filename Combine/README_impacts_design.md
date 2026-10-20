# DCB impact workflow: design and source review

Status: prepared and initial commands **dry-run only**. No impact initial fit, nuisance fit, collection or plot has run. Current runner: `run_DCB_impacts.sh`; prepared directory: `logs_DCB/impacts_DCB_20261016_064053_3911845`. Input inspection found 91 constrained nuisances and five photon nuisances. Two initial MultiDimFit commands were generated successfully with `--dry-run`, and no fit ROOT files were created. The general DCB/SoG datacard/workspace pipeline and custom plotting implementation remain deferred, as requested.

## Compared implementations

- Analyst: `15OCT26/run_impacts_fiducial_ttH.sh` and `run_impacts_fiducial_tHq.sh`. Their initialization, nuisance-fit and JSON-collection blocks are currently commented out; their enabled sections plot and postprocess existing JSON. The commented commands describe an intended fit workflow, not proof of what previously ran.
- Florian cached remote: `florian-repo/higgsdnafinalfit`, commit `d9031abb4e8c4e10c312e73912fece53fbd974bb`, `Combine/runImpacts_tth_th.sh`. Initial/per-nuisance fit blocks at lines 179–188; optional missing-result exclusion at 191–223; per-POI plots at 249–256. This is a locally available pinned comparison, not a fresh remote fetch.
- Installed tool: `../../CombineHarvester/CombineTools/python/combine/Impacts.py`; fitter: `../../HiggsAnalysis/CombinedLimit/src/{MultiDimFit,FitterAlgoBase}.cc`.

| Feature | Analyst's archived design | Florian dedicated runner | New current-DCB design |
|---|---|---|---|
| Input | Old fiducial workspace/mass 125.08; generated Asimov options | Datacard-root argument, optional t2w, usually -t -1 and set strengths=1 | Same first-command DCB workspace/snapshot and exact saved SM Asimov via --toysFile; mass 125.09. No new data generation or t2w. |
| POIs | Separate one-target workflows, other strength not frozen | Both workspace POIs by default | Explicit identical list `r_ttH,r_tHq` at all stages. Both are POIs, so neither is accidentally treated as a nuisance row. |
| Initial fit | One per target | Standard doInitialFit | --splitInitial creates two --algo singles jobs, each profiling the other POI. |
| Impact parameters | Tool default, followed by removing background rows | Tool default, optional row correction/removal | --named list from the actual ModelConfig constrained nuisances (91 here). Backgrounds stay free in every fit; only their separate rows are omitted. |
| Profile intervals | --robustFit 1 | --robustFit 1 | Same profile-likelihood method, retaining independent nuisance-down/up responses. |
| Hessian | Not explicitly requested | --robustHesse 1 in EXTRA_OPTS | No --approx, --saveFitResult or --robustHesse. These are profile impacts, not covariance approximations; no need to add an independent Hessian to every nuisance fit. This avoids extra cost without claiming Hesse warnings have been solved. |
| Minimizer | Strategy 0; four standard runtime flags | Same plus approximate prefit, step/crossing options | Strategy 0 and same four flags; default/robust-profile tolerance 0.01; stepSize 0.05, crossing tolerance 0.00005. The latter two match Florian's values. These are planned numerical settings, not validated impact results. |
| Approximate prefit | Not specified | cminApproxPreFitTolerance 0.01 | Not enabled; use the validated starting snapshot and direct profile minimization. No code evidence that an additional approximate prefit is required. |
| POI bounds | ttH [-0.5,3], tHq [-20,25] | Workspace/user settings | Original workspace bounds: ttH [-1,3], tHq [-25,25]. Grid-study ranges and positive-only limit bounds are not imposed on impacts. |
| Frozen parameters | MH | MH by default | Only MH. Nuisances and background indices/shapes/normalizations are profiled except the single nuisance intentionally fixed at each impact endpoint. |
| Pilot | Not present | Not present in dedicated stage runner | Five photon rows first, including Smearing, before the full 91-nuisance run. |
| Local execution | parallel 4 | Default Condor; parallel default 24 (effective locally only in interactive mode) | Explicit interactive mode, maximum four simultaneous nuisance jobs, adjustable with IMPACT_PARALLEL. Per-nuisance stdout/stderr and exit logs. |
| Missing fits | Collection/plot assumptions | May exclude bad parameter outputs | Do not silently drop failures. Require every named nuisance's complete ROOT triples before collection. Preserve failures for review. |
| JSON | correctImpacts.py + manual quote replacements + remove other-POI row | Optional same correction helper | Preserve standard tool JSON unchanged; verify exactly 91 expected rows and two POIs. No fitted-centre recentering or signed-response sorting. |
| Plotting | All/corrected and with/without other strength | Per-POI plotImpacts.py | Standard plotImpacts.py for each POI in plots/combine; plots/custom reserved for later independent plots using the same raw JSON. |

## Actual impact definition

The installed `Impacts.py:115` creates initial singles fits; `:201` creates one `--algo impact` command per named nuisance, with both strengths in the redefined POI list and `--floatOtherPOIs 1`. In `MultiDimFit.cc:506`, the nuisance's fitted interval defines its lower/upper fixed values, and the rest of the model is refitted at each endpoint. This yields the effect on both strengths in one nuisance job.

For nuisance theta_i, the signed effects are conceptually

    Delta r_i^- = r_hat(theta_i = theta_i,low) - r_hat
    Delta r_i^+ = r_hat(theta_i = theta_i,high) - r_hat

The endpoints are the nuisance's postfit likelihood crossings, not blindly theta=±1 in every parameterization. ScaleEB/EE have prefit sigma=2 in this model; the other three photon nuisances have sigma=1. Keep both signed responses; do not impose opposite signs, equal magnitudes or a midpoint centre. Correlations and nonlinear responses mean impact bars are not an exact quadrature decomposition of total uncertainty.

Both strengths are estimated simultaneously. Initial intervals and per-nuisance central fits should agree with the successful scans to their numerical and confidence-level precision. The base fitter's default 68% crossing definition should be checked when comparing exact singles endpoints to the earlier q=1 (approximately 68.27%) scan intervals (`FitterAlgoBase.cc:236`). A small shift from injected 1 is not repaired by rewriting the impact centres; investigate actual minimization and model/profile choices if inconsistent.

`--robustFit 1` explicitly requests manual likelihood crossing searches instead of MINOS (`FitterAlgoBase.cc:74`, `:329–380`). It is different from `--robustHesse 1` and from the tool's covariance-based `--approx robust`. With `--saveFitResult` absent, MultiDimFit does not request the additional standard HESSE call (`MultiDimFit.cc:201–204`). Robust profile fits can still fail and still need validation.

## Why not use correctImpacts.py now?

`../Plots/correctImpacts.py:24–43` derives replacement POI centres from a user-selected frozen-parameter row. At `:64–73` it can replace nuisance-response centres with midpoints, and at `:117` it writes Python list representations for groups, which can be invalid JSON for nonempty string groups. The old shell scripts work around some quote cases afterward. MH is frozen and deliberately absent from the 91-nuisance list, so an MH impact row is not available for this procedure. Introducing such a row merely to supply a replacement centre is not part of the new design.

No correction to existing scripts is made in this task. Keep all original scripts for comparison, and preserve the raw new JSON. If a later display copy filters rows, it must not alter fitted values or overwrite the raw result.

Florian's `${PLOT_BLIND:+--blind}` uses a nonempty-string test: a value of "0" still expands to --blind. That is not copied into this Asimov-only plotting stage. No observed-data option is supplied; data provenance is the saved Asimov, not whether a plotting blind label is present.

## Stages and next command

Preparation and dry-run preview have been completed. To start the **initial impact fits only**, from Combine:

```bash
run_dir=logs_DCB/impacts_DCB_20261016_064053_3911845
bash run_DCB_impacts.sh initial "$run_dir"
```

After reviewing both initial intervals and logs, run the pilot:

```bash
bash run_DCB_impacts.sh pilot "$run_dir"
```

The five pilot nuisances are Smearing, ScaleEB, ScaleEE, Material and FNUF. Review their fitted nuisance intervals and both signed POI responses; in particular retain any smearing asymmetry rather than forcing symmetry. This is the global-fit check previously discussed, not a repetition of the single-process shape variation plot.

Later stages, run separately after the pilot review:

```bash
IMPACT_PARALLEL=4 bash run_DCB_impacts.sh fit "$run_dir"
bash run_DCB_impacts.sh check "$run_dir"
bash run_DCB_impacts.sh collect "$run_dir"
bash run_DCB_impacts.sh plot "$run_dir"
```

The installed tool supports joint POIs but needs the identical list/order at every stage (`Impacts.py:25–33`). With --splitInitial, files are named

- higgsCombine_initialFit_DCB_Impacts_POI_r_ttH.MultiDimFit.mH125.09.root
- higgsCombine_initialFit_DCB_Impacts_POI_r_tHq.MultiDimFit.mH125.09.root
- higgsCombine_paramFit_DCB_Impacts_NUISANCE.MultiDimFit.mH125.09.root

Do not add --saveToys to these generated commands: it adds a seed suffix in this release, whereas the collector expects the filenames above. The input --toysFile still reuses the exact saved data. No new impact-specific snapshot or regenerated Asimov is needed before initial fits.

## Files and validation limits

`manifest.json` stores the original input SHA256, both POIs, numerical mass/ranges, the 91-nuisance list, pilot list, background indices and saved-data dimensions. Each stage verifies that input hash. `nuisances.txt`, `pilot.txt` and `indices.txt` are the command inputs. Logs have separate timestamps and each nuisance has its own stdout/stderr and exit-status file. Existing result ROOT files are structurally checked and retained rather than silently overwritten; a malformed existing file stops the stage for review. Initial results and final JSON/plots are protected from overwrite.

The embedded checks require three finite ROOT entries (best fit plus two endpoints), both POI branches, and nuisance/POI endpoints that bracket their own best value. Collection requires the full named set and checks JSON fields and finite impacts. These are **structural checks**, not proof of fit convergence. `validation/*.json` retains available minimizer-status counts; inspect boundaries, incomplete likelihood crossings, trial failures, initial-interval consistency, per-nuisance central fits and starting-seed/tolerance stability before accepting a plot. Some Combine paths accept status 1 or do not propagate a failed minimizer; shell exit 0 alone is insufficient.

Unconstrained background parameters are still profiled, so background statistical freedom contributes to the POI uncertainty even though there are no separate background rows. There is no other-signal-strength nuisance row because both strengths are POIs; their correlation can be studied separately. The first-command runner, model/configuration files and old plotting scripts remain unchanged.

The ttH expected-limit reference-Asimov nonclosure at r_ttH=0.028112 and its internal failed trials remain an independent unresolved item. This new impact design does not mark that limit validated, or choose DCB over SoG. A generic workspace/datacard input pipeline, SoG application and the user's independent plotting implementation will follow only after this impact workflow has been tested.
