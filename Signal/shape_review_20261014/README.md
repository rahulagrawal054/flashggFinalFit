# Matched DCB versus SoG shape review

Read-only review of 1,024 recipient pairs from the completed 12 October runs. No fitting settings, selections or workspaces changed. All central comparisons use MH=125 and photon nuisance values zero. all_pairs.csv gives log diagnostics for every pair. selected_shapes.json contains evaluated PDF metrics and the selected plots.

## All-pair convergence

| Era | Same donor | Both converged | DCB only converged | SoG only converged | Neither converged |
|---|---:|---:|---:|---:|---:|
| 2022postEE | 256 | 159 | 36 | 35 | 26 |
| 2022preEE | 256 | 142 | 57 | 55 | 2 |
| 2023postBPix | 256 | 151 | 68 | 34 | 3 |
| 2023preBPix | 256 | 209 | 18 | 25 | 4 |

## Representative shapes

Cases include the same ttH reference in each era, the largest reduced-chi-square differences among pairs where both converge, and the largest reduced chi-square overall. These selected examples emphasize differences; they are not an unbiased estimate of overall model quality. MC comes from the corresponding donor own-model saved nominal dataset, after beamspot reweighting. Its normalized histogram was checked to agree between DCB and SoG. Plot points/chi-square describe donor MC when borrowed, not recipient MC.

| Pair | DCB reduced chi2 | SoG reduced chi2 | DCB success | SoG success | PDF total variation | Plot |
|---|---:|---:|---|---|---:|---|
| 2022postEE / tth_in / ttH_had_1 | 0.548 | 0.787 | False | True | 0.0059 | [PNG](2022postEE_tth_in_ttH_had_1.png) |
| 2022postEE / tHW_out / bkg_had | 12.613 | 4.335 | True | True | 0.0155 | [PNG](2022postEE_tHW_out_bkg_had.png) |
| 2022postEE / tHW_in / ttH_had_3 | 1.08 | 2.356 | True | True | 0.0056 | [PNG](2022postEE_tHW_in_ttH_had_3.png) |
| 2022postEE / tHW_in / bkg_had | 22.492 | 4.694 | False | True | 0.0136 | [PNG](2022postEE_tHW_in_bkg_had.png) |
| 2022preEE / tth_in / ttH_had_1 | 0.607 | 0.683 | True | False | 0.0151 | [PNG](2022preEE_tth_in_ttH_had_1.png) |
| 2022preEE / tHW_out / bkg_had | 5.517 | 1.644 | True | True | 0.0147 | [PNG](2022preEE_tHW_out_bkg_had.png) |
| 2022preEE / tHqLep_in / tH_had_3 | 0.705 | 0.909 | True | True | 0.0285 | [PNG](2022preEE_tHqLep_in_tH_had_3.png) |
| 2022preEE / bbh_in / tH_lep_2 | 1.05 | 14.317 | True | False | 0.1688 | [PNG](2022preEE_bbh_in_tH_lep_2.png) |
| 2023postBPix / tth_in / ttH_had_1 | 0.462 | 0.426 | True | False | 0.0098 | [PNG](2023postBPix_tth_in_ttH_had_1.png) |
| 2023postBPix / tHW_in / ttH_lep_1 | 2.379 | 0.655 | True | True | 0.0339 | [PNG](2023postBPix_tHW_in_ttH_lep_1.png) |
| 2023postBPix / tHW_in / ttH_lep_2 | 0.676 | 2.02 | True | True | 0.0217 | [PNG](2023postBPix_tHW_in_ttH_lep_2.png) |
| 2023postBPix / bbh_in / ttH_lep_2 | 0.427 | 9.654 | True | False | 0.1199 | [PNG](2023postBPix_bbh_in_ttH_lep_2.png) |
| 2023preBPix / tth_in / ttH_had_1 | 0.415 | 0.326 | True | True | 0.0062 | [PNG](2023preBPix_tth_in_ttH_had_1.png) |
| 2023preBPix / bbh_out / bkg_lep | 1.68 | 0.531 | True | True | 0.0313 | [PNG](2023preBPix_bbh_out_bkg_lep.png) |
| 2023preBPix / tHW_in / tH_had_4 | 0.717 | 1.023 | True | True | 0.0220 | [PNG](2023preBPix_tHW_in_tH_had_4.png) |
| 2023preBPix / tHW_in / ttH_lep_4 | 1.739 | 1.093 | False | False | 0.0402 | [PNG](2023preBPix_tHW_in_ttH_lep_4.png) |

Total variation is half the absolute PDF difference integrated numerically over the observable range; it measures model differences, not goodness of fit. Pulls use the weighted gamma-interval error prescription of the objective and are shown only for nonzero bins inside 110–140 GeV. PDF curves are sampled; reported chi-square values come from logs. Tail fractions below 120 and above 130 and half the 16–84% quantile width are finite-range metrics, not fitted core sigma. Reduced chi-square alone does not account for model selection and is not a calibrated p-value. The SoG candidate-selection convergence issue remains unresolved. Log convergence is necessary evidence but does not prove global optimality, closure or physical rates. ROOT files were opened READ; analysis artifacts are new outputs only.

## Interpretation from direct plot inspection

- **Near-equivalent adequate central shapes:** `tth_in / ttH_had_1`, especially 2023preBPix. The peak/width nearly coincide and residuals are small. There is no compelling shape-quality reason in that example to prefer the more complex family. Reference shapes in other eras are also close, but optimizer failures in some of them still require stability checks.
- **A visibly poor returned SoG solution:** 2022preEE `bbh_in / tH_lep_2` borrows `tth_in / tH_lep_2`. Its SoG peak is shifted relative to MC and leaves structured, roughly 5–7 error-unit residuals; DCB follows the MC much better. Reduced chi-square is 14.317 versus 1.050. 2023postBPix `bbh_in / ttH_lep_2` has a similar SoG discrepancy (9.654 versus DCB 0.427). Both SoG optimizers failed. These are failure examples, not proof that a properly converged SoG family cannot fit the data.
- **A real SoG advantage:** 2023postBPix `tHW_in / ttH_lep_1` has both optimizers converged. SoG follows the peak and residuals better: reduced chi-square 0.655 versus DCB 2.379. DCB reaches two parameter bounds. This is a candidate exception to a blanket DCB prescription, subject to stability and calibrated goodness-of-fit checks.
- **A difficult case for both:** 2022postEE `tHW_out / bkg_had` has both optimizers converged, but DCB underestimates the high-mass tail and leaves structured residuals. SoG improves it, yet its reduced chi-square is still 4.335 versus DCB 12.613. Neither should be accepted merely because an optimizer converged or SoG has the smaller value.
- **Very similar curves can have different fit-quality diagnostics:** 2022postEE `tHW_in / ttH_had_3` has a small integrated shape difference but reduced chi-square 1.080 versus 2.356. Small differences matter where MC uncertainty is small, and different parameter counts affect the denominator.

The current outputs do not justify choosing one family universally. A provisional preference for DCB is defensible where both families have validated, adequate agreement and similar shapes because the DCB family avoids Gaussian-count selection. First resolve conspicuously incorrect returned fits; then revisit DCB-specific residuals/limits and SoG candidate-selection reliability. Do not mix families automatically by whichever reduced chi-square is smallest; define and validate a consistent analysis prescription. No production choice has been changed by this review.
