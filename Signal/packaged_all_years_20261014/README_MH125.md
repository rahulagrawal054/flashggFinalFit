# All-era category packages and aggregate shape comparison

DCB/ and SoG/ each contain 16 category ROOT files. Each wsig_13TeV contains 64 distinct process/year PDFs, normalization functions and individual datasets (16 processes × 4 eras). These models are collected in one file, not refitted or replaced by one summed PDF. Years remain identified by object names. Correlated nuisance names are shared through the existing packager's RecycleConflictNodes behavior. MH and IntLumi remain shared variables; set their intended downstream treatment in the datacard/Combine workflow. No production source workspace or fitting configuration changed.

Packaging used the existing scripts/packageSignal.py --mergeYears implementation with links to the completed run outputs. The summed unweighted-by-cross-section category dataset is retained except bkg_had, where the existing code skips it to avoid ROOT buffer limits. It is not itself the luminosity-weighted physics sum used in the diagnostic plots.

All 32 files were reopened and all 2,048 process/year PDFs, normalization functions and datasets verified against the previous per-era package validation: entries, signed sums, central norms and single-point PDF values agree. See manifest.json and source_match_validation.csv. This does not validate full nuisance ranges or fit convergence.

## Aggregate plots and chi-square

For each category, comparison_MH125/ contains PNG and PDF overlays of all process/year models against the same luminosity-weighted signed MC sum. We use MH=125.0, matching the generated MC mass, m in 110–140, 80 bins over the observable range, photon nuisances zero. Luminosities (pb^-1): 2022preEE 7980, 2022postEE 26670, 2023preBPix 18063, 2023postBPix 9693, matching the local lumiMap. Curve = sum(norm_process,era × luminosity_era × PDF_process,era). MC weights are multiplied by production cross section × BR × luminosity. Both the input MC and the comparison PDFs use mass 125.0. Separate structural/numerical package checks above evaluated the functions at MH=125.09 without writing that setting into the output files.

Negative and zero rates are retained explicitly without clipping or omission. These curves are signed expected-spectrum diagnostics, not a validation that every component is a physical nonnegative probability PDF. Negative process rates must be resolved before final statistical use. Some total spectra can look acceptable while bad low-yield component shapes are hidden by the sum.

The aggregate chi-square uses nonzero bin contents in 110–140 and weighted gamma-interval errors, taking the larger error side, as in the central objective prescription. It is freshly calculated for the sum; it is not the sum of original chi-squares and no chi2/ndof or p-value is assigned. Aggregation hides process/era-specific discrepancies and parameter-count/model-selection differences; the number of independent fitted coefficients and effective degrees of freedom are not inferred from this plot. Diagnostic values do not identify a universal model winner and are not a substitute for the matched individual-shape review. Original fit failures, bounds, Gaussian-count-selection issues and negative-rate treatment remain unresolved.

| Category | DCB aggregate chi2 | SoG aggregate chi2 | Bins used | Negative components | Plot |
|---|---:|---:|---:|---:|---|
| bkg_had | 124.90 | 34.02 | 30 | 0 | [PNG ](comparison_MH125/bkg_had.png) |
| bkg_lep | 30.52 | 16.49 | 30 | 1 | [PNG ](comparison_MH125/bkg_lep.png) |
| tH_had_1 | 29.41 | 35.05 | 30 | 2 | [PNG ](comparison_MH125/tH_had_1.png) |
| tH_had_2 | 23.95 | 17.27 | 30 | 2 | [PNG ](comparison_MH125/tH_had_2.png) |
| tH_had_3 | 133.82 | 28.72 | 30 | 0 | [PNG ](comparison_MH125/tH_had_3.png) |
| tH_had_4 | 178.95 | 80.88 | 30 | 0 | [PNG ](comparison_MH125/tH_had_4.png) |
| tH_lep_1 | 21.30 | 26.02 | 30 | 8 | [PNG ](comparison_MH125/tH_lep_1.png) |
| tH_lep_2 | 19.27 | 39.25 | 30 | 7 | [PNG ](comparison_MH125/tH_lep_2.png) |
| ttH_had_1 | 10.77 | 13.13 | 30 | 7 | [PNG ](comparison_MH125/ttH_had_1.png) |
| ttH_had_2 | 16.17 | 14.93 | 30 | 5 | [PNG ](comparison_MH125/ttH_had_2.png) |
| ttH_had_3 | 26.62 | 34.95 | 30 | 6 | [PNG ](comparison_MH125/ttH_had_3.png) |
| ttH_had_4 | 23.64 | 28.76 | 30 | 3 | [PNG ](comparison_MH125/ttH_had_4.png) |
| ttH_lep_1 | 43.50 | 23.80 | 30 | 2 | [PNG ](comparison_MH125/ttH_lep_1.png) |
| ttH_lep_2 | 18.25 | 47.89 | 30 | 4 | [PNG ](comparison_MH125/ttH_lep_2.png) |
| ttH_lep_3 | 18.48 | 11.53 | 30 | 2 | [PNG ](comparison_MH125/ttH_lep_3.png) |
| ttH_lep_4 | 28.38 | 23.03 | 30 | 5 | [PNG ](comparison_MH125/ttH_lep_4.png) |

## Interpretation

The summed diagnostic chi-square is smaller for DCB in 7 categories and SoG in 9. This is a descriptive comparison, not a calibrated test selecting a family. `ttH_had_1` has almost coincident central shapes, with aggregate chi-square 10.77 (DCB) versus 13.13 (SoG). In `tH_had_4`, both peaks look reasonably close to MC, but high-mass-tail bins have large pulls: chi-square 178.95 (DCB) versus 80.88 (SoG). SoG reduces the discrepancy without eliminating it. Large tail pulls can dominate the statistic even when the peak overlay looks good. Negative component rates in other categories remain a separate physical-normalization issue; they were retained explicitly.

Packaging is complete for both model families. These aggregate comparisons do not justify adopting the lower-chi-square family automatically for each category. Keep the earlier individual process/era convergence and shape review, resolve negative-rate prescriptions, and validate final model/systematic behavior and closure before selecting the final analysis model.
