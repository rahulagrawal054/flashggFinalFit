---
marp: true
theme: default
paginate: true
math: mathjax
style: |
  section { font-size: 23px; }
  pre { font-size: 16px; }
  section.small pre { font-size: 14px; }
  table { font-size: 21px; }
---

# Nominal bias study: ttH_had_1

Two-POI workspace: `r_ttH` and `r_tHq`

**Question:** how does widening the fit ranges affect the fitted pull bias, toy losses, and boundary hits?

Updated: 8 October 2026. Completed wider_both results for all three injection cases.

<!-- Commands below are drawn from saved command records; wrapper examples reproduce the same stages. -->

---

# Study setup

- One category, one `RooMultiPdf`, and one `pdfindex`.
- Four generating background functions: `bern1`, `exp1`, `pow1`, `lau1`.
- 1,000 toys **per function and injection case**, seed `12345`.
- Higgs mass: `125.08` GeV.
- Fit `r_ttH` while profiling `r_tHq`.
- Compare ranges using the **same saved toy ROOT files**.

The boundary-comparison jobs specify injection cases `(0,0)`, `(1,1)`, and `(1,0)`; wider_ttH completed only `(0,0)`; wider_both rerun results cover all three cases.

---

# Environment and input

Run inside an initialized CMSSW environment, in a dedicated case directory containing the script and `biasUtils.py`.

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src
eval "$(scram runtime -sh)"

WORKSPACE="/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/Checks/Datacard/Datacard_ttH_had_1_r_2D_fiducial.root"
```

For the completed comparison, the case directory is:
`runs/boundary_comparison_20261008_062944/wider_ttH/ttH0_tHq0/`

---

# 1. Generate pseudo-data toys

Equivalent stage command using the study script:

```bash
python3 RunBiasStudy_twoPOI.py -d "$WORKSPACE" \
  --gridTtH 0 --gridTHq 0 -n 1000 -s 12345 \
  --toys
```

- Set injected strengths `r_ttH=0`, `r_tHq=0`.
- Select and freeze **one background index** for each generating function.
- `GenerateOnly` creates statistical pseudo-data toys from that model.
- `--toysNoSystematics` disables systematic nuisance randomization during generation; it does not remove nuisance parameters from the later fit.
- Save each function's toys under `BiasToys/`.

---

# Exact recorded generation command: bern1

```bash
combine \
  -m 125.0800 \
  -d "$WORKSPACE" \
  -M GenerateOnly \
  -s 12345 \
  --saveToys \
  --toysNoSystematics \
  -t 1000 \
  -n _bern1_ttH0.0_tHq0.0_seed12345 \
  --setParameters pdfindex_ttH_had_1_13TeV=0,r_ttH=0,r_tHq=0 \
  --freezeParameters pdfindex_ttH_had_1_13TeV
```

Recorded index mapping: `0=bern1`, `1=exp1`, `2=pow1`, `3=lau1`.

The script runs the corresponding command for each function and moves the output to `BiasToys/biasStudy_<function>_ttH0.0_tHq0.0_seed12345_toys.root`.

---

# 2. Fit the saved toys

Equivalent fits-only command for `wider_ttH`:

```bash
python3 RunBiasStudy_twoPOI.py -d "$WORKSPACE" \
  --gridTtH 0 --gridTHq 0 -n 1000 -s 12345 \
  --fits --poi r_ttH \
  --rMinTtH -10 --rMaxTtH 30 \
  --rMinTHq -25 --rMaxTHq 25
```

- `MultiDimFit --algo singles` obtains the best fit and interval.
- `-P r_ttH --floatOtherPOIs 1`: fit ttH and profile tHq.
- The generating `pdfindex` is **not frozen in the fit**: fit with the background envelope.
- `MH` is frozen; the command does not freeze all constrained nuisances.
- Read toys from `BiasToys/`; write fits to `BiasFits/`.

---

# Exact recorded fit command: bern1

<!-- _class: small -->

```bash
combine \
  -m 125.0800 \
  -d "$WORKSPACE" \
  -M MultiDimFit \
  -P r_ttH \
  --algo singles \
  --floatOtherPOIs 1 \
  --setParameters r_ttH=0,r_tHq=0 \
  --setParameterRanges r_ttH=-10,30:r_tHq=-25,25 \
  --cminDefaultMinimizerStrategy 0 \
  --X-rtd MINIMIZER_freezeDisassociatedParams \
  --X-rtd MINIMIZER_multiMin_hideConstants \
  --X-rtd MINIMIZER_multiMin_maskConstraints \
  --X-rtd MINIMIZER_multiMin_maskChannels=2 \
  --freezeParameters MH \
  -t 1000 \
  -n _bern1_ttH0.0_tHq0.0_seed12345_r_ttH \
  --toysFile=BiasToys/biasStudy_bern1_ttH0.0_tHq0.0_seed12345_toys.root
```

The four recorded wider_ttH Combine commands returned exit code 0. Individual toy failures still occur and are reported separately.

---

# 3. Plot and summarize the fits

Equivalent plots-only command:

```bash
python3 RunBiasStudy_twoPOI.py -d "$WORKSPACE" \
  --gridTtH 0 --gridTHq 0 -n 1000 -s 12345 \
  --plots --gaussianFit --poi r_ttH \
  --rMinTtH -10 --rMaxTtH 30 \
  --rMinTHq -25 --rMaxTHq 25
```

Plotting is Python/ROOT processing, **not another Combine command**.

Outputs: pull PNG/PDF files and `BiasPlots/BiasResults_r_ttH_seed12345.json`.

The recorded job requested `--fits --plots --gaussianFit` together; the separate commands above explain the two stages.

---

# What the pull and bias mean

$$p = \frac{\hat r_{ttH}-r_{ttH}^{\mathrm{truth}}}{(r_{ttH}^{\mathrm{upper}}-r_{ttH}^{\mathrm{lower}})/2}$$

- Read best-fit, lower, upper entries with expected quantiles `-1`, `-0.32`, `+0.32`.
- Reject incomplete, invalid, nonfinite, or nonpositive-uncertainty results.
- Fill 80 pull bins over `[-4,4]`; retain underflow/overflow counts separately.
- Fit the histogram with a Gaussian; its fitted mean is the reported **bias** and its width is **sigma**.
- Flag best-fit/interval values touching the **fitted POI's range**; flagged toys are not automatically excluded.

Usable pulls are not a complete assessment of minimizer convergence; missing/invalid results, boundaries, and tails must also be reviewed.

---

# Fit-range comparison

| Configuration | r_ttH range | r_tHq range |
|---|---|---|
| baseline | [-5, 15] | [-25, 25] |
| wider_ttH | [-10, 30] | [-25, 25] |
| wider_both | [-10, 30] | [-50, 50] |

Each configuration fits the same saved toys for its injection case.

`wider_both` differs from `wider_ttH` only in the profiled tHq range. No regeneration is needed for this comparison.

---

# Completed wider_ttH result: injection (0,0)

| Function | Gaussian pull bias | Pull sigma | Usable pulls | Boundary flags |
|---|---:|---:|---:|---:|
| bern1 | 0.116 ± 0.027 | 0.715 | 892/1000 | 73 |
| exp1 | 0.122 ± 0.027 | 0.713 | 880/1000 | 81 |
| pow1 | 0.053 ± 0.030 | 0.731 | 890/1000 | 121 |
| lau1 | 0.067 ± 0.028 | 0.729 | 849/1000 | 80 |

All central bias magnitudes are below `0.14`; this is a comparison against that criterion, not a full validation statement.

108–151 of 1,000 toys lack usable pulls, and 73–121 boundary flags remain. Pull widths are around 0.71–0.73; the quoted bias errors are Gaussian-fit statistical errors.

---

# wider_both rerun completed

Completed **8 October 2026, 09:08:50 Europe/Zurich**.

Directory: `runs/wider_both_rerun_20261008_075124/`

- Same saved toys, 1,000 per generating function, seed `12345`.
- Fit ranges: `r_ttH=[-10,30]`, `r_tHq=[-50,50]`.
- All three cases completed: `(0,0)`, `(1,1)`, `(1,0)`.
- All 12 Combine commands returned 0; all 12 Gaussian fits have status 0.
- The original wider-range batch remains incomplete; its interruption reason was not recorded.

The original `wider_ttH` jobs for `(1,1)` and `(1,0)` have no results.


---

# Reproducibility records

- Generation source: `runs/toys1000_truth0_20261007_215318/BiasLogs/*.command.json`.
- wider_ttH fit commands: `runs/boundary_comparison_20261008_062944/wider_ttH/ttH0_tHq0/BiasLogs/*.command.json`.
- Exact driver arguments: `runs/boundary_comparison_20261008_062944/jobs.json`.
- Numerical results: corresponding `BiasPlots/BiasResults_r_ttH_seed12345.json`.
- Rerun jobs and host/PID: `runs/wider_both_rerun_20261008_075124/jobs.json` and `run_info.json`.

The full absolute workspace path is defined on the environment slide. Exact Combine examples replace only that recorded path with `$WORKSPACE`.


---

# Completed wider_both: ttH0_tHq0

| Function | Pull bias | Pull sigma | Usable pulls | Boundary flags |
|---|---:|---:|---:|---:|
| bern1 | 0.098 ± 0.025 | 0.668 | 886/1000 | 68 |
| exp1 | 0.056 ± 0.027 | 0.697 | 885/1000 | 85 |
| pow1 | 0.063 ± 0.026 | 0.678 | 881/1000 | 118 |
| lau1 | 0.050 ± 0.027 | 0.706 | 849/1000 | 95 |

All four Gaussian fits have status 0. Boundary flags are retained in the pull sample; missing/invalid toy fits still require review.

---

# Completed wider_both: ttH1_tHq1

| Function | Pull bias | Pull sigma | Usable pulls | Boundary flags |
|---|---:|---:|---:|---:|
| bern1 | -0.039 ± 0.027 | 0.766 | 973/1000 | 22 |
| exp1 | -0.047 ± 0.028 | 0.824 | 979/1000 | 26 |
| pow1 | -0.080 ± 0.029 | 0.787 | 980/1000 | 14 |
| lau1 | -0.091 ± 0.028 | 0.785 | 972/1000 | 26 |

All four Gaussian fits have status 0. Boundary flags are retained in the pull sample; missing/invalid toy fits still require review.

---

# Completed wider_both: ttH1_tHq0

| Function | Pull bias | Pull sigma | Usable pulls | Boundary flags |
|---|---:|---:|---:|---:|
| bern1 | -0.045 ± 0.026 | 0.762 | 962/1000 | 18 |
| exp1 | -0.017 ± 0.028 | 0.804 | 972/1000 | 24 |
| pow1 | -0.093 ± 0.029 | 0.792 | 978/1000 | 12 |
| lau1 | -0.062 ± 0.027 | 0.763 | 961/1000 | 28 |

All four Gaussian fits have status 0. Boundary flags are retained in the pull sample; missing/invalid toy fits still require review.

---

# What the range tests establish

- All 12 wider_both central pull biases are below 0.14 in magnitude.
- For (0,0), boundary flags are lower than baseline, but usable-pull counts are also lower.
- Pull widths remain below 1, so bias alone does not establish satisfactory coverage.
- Same-toy comparisons are correlated; individual fit errors do not establish the significance of differences.
- Wider_ttH results for (1,1) and (1,0) were never produced in the original batch.

Recovered run history and full numerical comparison: `BIAS_STUDY_SUMMARY.md`.
