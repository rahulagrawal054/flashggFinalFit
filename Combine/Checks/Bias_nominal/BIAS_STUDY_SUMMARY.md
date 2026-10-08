# Recovered nominal bias study history

Recovered from saved job lists, command sidecars, completion records, and results JSON on 8 October 2026.

## Runs and completion

| Run | Scope | Saved state |
|---|---|---|
| toys10_truth0_20261007_214445 | 10-toy truth-zero check | Completed |
| toys300_truth0_20261007_212855 / 212959 | 300-toy exploratory runs | No run-level completion marker; do not assume completion |
| toys1000_truth0_20261007_215318 | 1,000-toy truth-zero baseline | Completed |
| rangecheck10_20261007_222459 | 10-toy range check | Completed |
| injection_comparison_20261008_054641 | Injection comparison | Completed |
| boundary_comparison_20261008_062944 | Wider-range comparison | Incomplete: wider_ttH (0,0) completed; wider_both (0,0) stopped after one saved fit; other jobs have no fit outputs |
| wider_both_rerun_20261008_075124 | Wider-both fits for (0,0), (1,1), (1,0) | Completed at 09:08:50 Europe/Zurich, 8 October 2026 |

The exact reason for the original batch interruption is not recorded; no failed.log or completed.json was found.

## Matched (0,0) comparison

Ranges: baseline r_ttH=[-5,15], r_tHq=[-25,25]; wider_ttH=[-10,30]/[-25,25]; wider_both=[-10,30]/[-50,50]. Same saved toys, 1,000 per generating function, seed 12345.

| Function | Baseline bias | Wider ttH bias | Wider both bias | Usable pulls (baseline / wider ttH / wider both) | Boundary flags (baseline / wider ttH / wider both) |
|---|---:|---:|---:|---|---|
| bern1 | 0.131 ± 0.026 | 0.116 ± 0.027 | 0.098 ± 0.025 | 965 / 892 / 886 | 149 / 73 / 68 |
| exp1 | 0.118 ± 0.026 | 0.122 ± 0.027 | 0.056 ± 0.027 | 966 / 880 / 885 | 170 / 81 / 85 |
| pow1 | 0.072 ± 0.026 | 0.053 ± 0.030 | 0.063 ± 0.026 | 970 / 890 / 881 | 217 / 121 / 118 |
| lau1 | 0.052 ± 0.028 | 0.067 ± 0.028 | 0.050 ± 0.027 | 956 / 849 / 849 | 199 / 80 / 95 |

## All completed wider_both results

| Injection | Function | Bias ± Gaussian-fit error | Pull width | Usable / 1000 | Boundary flags |
|---|---|---:|---:|---:|---:|
| ttH0_tHq0 | bern1 | 0.098 ± 0.025 | 0.668 | 886/1000 | 68 |
| ttH0_tHq0 | exp1 | 0.056 ± 0.027 | 0.697 | 885/1000 | 85 |
| ttH0_tHq0 | pow1 | 0.063 ± 0.026 | 0.678 | 881/1000 | 118 |
| ttH0_tHq0 | lau1 | 0.050 ± 0.027 | 0.706 | 849/1000 | 95 |
| ttH1_tHq1 | bern1 | -0.039 ± 0.027 | 0.766 | 973/1000 | 22 |
| ttH1_tHq1 | exp1 | -0.047 ± 0.028 | 0.824 | 979/1000 | 26 |
| ttH1_tHq1 | pow1 | -0.080 ± 0.029 | 0.787 | 980/1000 | 14 |
| ttH1_tHq1 | lau1 | -0.091 ± 0.028 | 0.785 | 972/1000 | 26 |
| ttH1_tHq0 | bern1 | -0.045 ± 0.026 | 0.762 | 962/1000 | 18 |
| ttH1_tHq0 | exp1 | -0.017 ± 0.028 | 0.804 | 972/1000 | 24 |
| ttH1_tHq0 | pow1 | -0.093 ± 0.029 | 0.792 | 978/1000 | 12 |
| ttH1_tHq0 | lau1 | -0.062 ± 0.027 | 0.763 | 961/1000 | 28 |

## Interpretation

- All 12 wider_both central pull biases satisfy abs(bias) < 0.14; this alone is not a complete validation.
- For (0,0), wider ranges reduce flagged r_ttH boundary hits relative to baseline, but usable-pull counts fall.
- Widths remain below 1. Boundary flags here refer to the fitted POI, not every profiled parameter.
- The same toys make the comparisons correlated. Differences require paired analysis to establish significance.
- Wider_ttH (1,1) and (1,0) remain unperformed in this batch; no results are inferred for them.

## Source files and commands

- Original planned jobs: `runs/boundary_comparison_20261008_062944/jobs.json`.
- Original baseline and partial summary: corresponding `baseline.json` and `comparison.json`.
- Rerun arguments and completion: `runs/wider_both_rerun_20261008_075124/jobs.json` and `completed.json`.
- Per-case exact Combine arguments, return codes, and elapsed times: `BiasLogs/*.command.json`.
- Per-case diagnostics and Gaussian results: `BiasPlots/BiasResults_r_ttH_seed12345.json`.
- `nominal_bias_slides.md` contains generation, fitting, and plotting command examples.

No fit jobs were started or stopped during this recovery audit.
