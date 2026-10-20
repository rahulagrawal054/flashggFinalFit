# All-era category packages and aggregate shape comparison

DCB/ and SoG/ each contain 16 category ROOT files. Each wsig_13TeV contains 64 distinct process/year PDFs, normalization functions and individual datasets (16 processes × 4 eras). These models are collected in one file, not refitted or replaced by one summed PDF. Years remain identified by object names. Correlated nuisance names are shared through the existing packager's RecycleConflictNodes behavior. MH and IntLumi remain shared variables; set their intended downstream treatment in the datacard/Combine workflow. No production source workspace or fitting configuration changed.

Packaging used the existing scripts/packageSignal.py --mergeYears implementation with links to the completed run outputs. The summed unweighted-by-cross-section category dataset is retained except bkg_had, where the existing code skips it to avoid ROOT buffer limits. It is not itself the luminosity-weighted physics sum used in the diagnostic plots.

All 32 files were reopened and all 2,048 process/year PDFs, normalization functions and datasets verified against the previous per-era package validation: entries, signed sums, central norms and single-point PDF values agree. See manifest.json and source_match_validation.csv. This does not validate full nuisance ranges or fit convergence.

## Aggregate plots and chi-square

For each category, comparison/ contains PNG and PDF overlays of all process/year models against the same luminosity-weighted signed MC sum. We use MH=125.09, m in 110–140, 80 bins over the observable range, photon nuisances zero. Luminosities (pb^-1): 2022preEE 7980, 2022postEE 26670, 2023preBPix 18063, 2023postBPix 9693, matching the local lumiMap. Curve = sum(norm_process,era × luminosity_era × PDF_process,era). MC weights are multiplied by production cross section × BR × luminosity. Input MC masses remain 125: the plotted PDF translates to 125.09, but the histogram is the original 125 MC, not shifted/regenerated. This 0.09 GeV hypothesis difference contributes to these residuals; compare equal mass hypotheses for a clean family-choice test.

Negative and zero rates are retained explicitly without clipping or omission. These curves are signed expected-spectrum diagnostics, not a validation that every component is a physical nonnegative probability PDF. Negative process rates must be resolved before final statistical use. Some total spectra can look acceptable while bad low-yield component shapes are hidden by the sum.

The aggregate chi-square uses nonzero bin contents in 110–140 and weighted gamma-interval errors, taking the larger error side, as in the central objective prescription. It is freshly calculated for the sum; it is not the sum of original chi-squares and no chi2/ndof or p-value is assigned. Aggregation hides process/era-specific discrepancies and parameter-count/model-selection differences; the number of independent fitted coefficients and effective degrees of freedom are not inferred from this plot. Diagnostic values do not identify a universal model winner and are not a substitute for the matched individual-shape review. Original fit failures, bounds, Gaussian-count-selection issues and negative-rate treatment remain unresolved.

| Category | DCB aggregate chi2 | SoG aggregate chi2 | Bins used | Negative components | Plot |
|---|---:|---:|---:|---:|---|
| bkg_had | 219.23 | 131.72 | 30 | 0 | [PNG](comparison/bkg_had.png) |
| bkg_lep | 38.97 | 24.70 | 30 | 1 | [PNG](comparison/bkg_lep.png) |
| tH_had_1 | 33.93 | 39.68 | 30 | 2 | [PNG](comparison/tH_had_1.png) |
| tH_had_2 | 24.78 | 18.19 | 30 | 2 | [PNG](comparison/tH_had_2.png) |
| tH_had_3 | 142.40 | 32.60 | 30 | 0 | [PNG](comparison/tH_had_3.png) |
| tH_had_4 | 196.30 | 91.23 | 30 | 0 | [PNG](comparison/tH_had_4.png) |
| tH_lep_1 | 30.03 | 34.97 | 30 | 8 | [PNG](comparison/tH_lep_1.png) |
| tH_lep_2 | 34.63 | 65.31 | 30 | 7 | [PNG](comparison/tH_lep_2.png) |
| ttH_had_1 | 76.47 | 77.59 | 30 | 7 | [PNG](comparison/ttH_had_1.png) |
| ttH_had_2 | 58.94 | 60.77 | 30 | 5 | [PNG](comparison/ttH_had_2.png) |
| ttH_had_3 | 36.22 | 43.85 | 30 | 6 | [PNG](comparison/ttH_had_3.png) |
| ttH_had_4 | 33.43 | 37.03 | 30 | 3 | [PNG](comparison/ttH_had_4.png) |
| ttH_lep_1 | 132.36 | 113.49 | 30 | 2 | [PNG](comparison/ttH_lep_1.png) |
| ttH_lep_2 | 56.25 | 118.67 | 30 | 4 | [PNG](comparison/ttH_lep_2.png) |
| ttH_lep_3 | 32.93 | 26.01 | 30 | 2 | [PNG](comparison/ttH_lep_3.png) |
| ttH_lep_4 | 40.95 | 33.41 | 30 | 5 | [PNG](comparison/ttH_lep_4.png) |

## Matched-mass comparison for model review

Use [README_MH125.md](README_MH125.md) and [comparison_MH125/](comparison_MH125/) for DCB-versus-SoG comparisons at MH=125, matching the MC generation mass. The original comparison/ plots evaluate MH=125.09 against unshifted 125 MC and therefore include the hypothesis shift. Both sets are preserved. Packaging did not change either model family.
