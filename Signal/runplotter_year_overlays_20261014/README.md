# RunPlotter combined-year and individual-year overlays

Produced with the existing RunPlotter.py and plotSignalModel implementation, without changing either script or any fitting configuration/workspace. DCB/Plots and SoG/Plots each contain 16 category PNG/PDF pairs plus effSigma JSON files. manifest.json records the exact command, outputs, logs and five effective widths per category.

The actual enabling flag is --plot-years-separate; the parser help text is misleading, but the drawing code displays per-year dashed coloured curves when this flag is true. The combined parametric model is solid blue and the combined MC points are black. Individual curves are luminosity-weighted contributions, not each independently normalized to the same peak: 2022preEE light blue, 2022postEE green, 2023preBPix yellow/olive, 2023postBPix gray-blue. The gray fill marks the implementation's combined effective-width band. The code uses the local year luminosities, mass=125 for MC and MH=125 for PDFs. Default data/PDF bins are 160/3200; --doFWHM was not requested.

Default threshold=0.001 prunes contributions below 0.1% of the signed category norm; in these packages that omits negative and zero-rate components too. This changes the plotted selection only, not the underlying workspaces, and does not resolve their physical negative-rate issue. These plots are therefore not identical to the earlier signed-weight aggregate diagnostics that retained every contribution. The existing code's displayed sigma_eff is a histogram-based effective width, not the DCB Gaussian-core sigma. Plots do not resolve optimizer failures, boundaries, selection validation or closure.

| Category | DCB plot | SoG plot | Combined sigma_eff DCB [GeV] | Combined sigma_eff SoG [GeV] |
|---|---|---|---:|---:|
| bkg_had | [PNG](DCB/Plots/smodel_bkg_had.png) | [PNG](SoG/Plots/smodel_bkg_had.png) | 2.188 | 2.197 |
| bkg_lep | [PNG](DCB/Plots/smodel_bkg_lep.png) | [PNG](SoG/Plots/smodel_bkg_lep.png) | 2.174 | 2.162 |
| tH_had_1 | [PNG](DCB/Plots/smodel_tH_had_1.png) | [PNG](SoG/Plots/smodel_tH_had_1.png) | 1.825 | 1.824 |
| tH_had_2 | [PNG](DCB/Plots/smodel_tH_had_2.png) | [PNG](SoG/Plots/smodel_tH_had_2.png) | 1.928 | 1.936 |
| tH_had_3 | [PNG](DCB/Plots/smodel_tH_had_3.png) | [PNG](SoG/Plots/smodel_tH_had_3.png) | 1.872 | 1.844 |
| tH_had_4 | [PNG](DCB/Plots/smodel_tH_had_4.png) | [PNG](SoG/Plots/smodel_tH_had_4.png) | 2.022 | 2.076 |
| tH_lep_1 | [PNG](DCB/Plots/smodel_tH_lep_1.png) | [PNG](SoG/Plots/smodel_tH_lep_1.png) | 1.880 | 1.881 |
| tH_lep_2 | [PNG](DCB/Plots/smodel_tH_lep_2.png) | [PNG](SoG/Plots/smodel_tH_lep_2.png) | 1.951 | 1.951 |
| ttH_had_1 | [PNG](DCB/Plots/smodel_ttH_had_1.png) | [PNG](SoG/Plots/smodel_ttH_had_1.png) | 1.555 | 1.553 |
| ttH_had_2 | [PNG](DCB/Plots/smodel_ttH_had_2.png) | [PNG](SoG/Plots/smodel_ttH_had_2.png) | 1.693 | 1.693 |
| ttH_had_3 | [PNG](DCB/Plots/smodel_ttH_had_3.png) | [PNG](SoG/Plots/smodel_ttH_had_3.png) | 1.866 | 1.873 |
| ttH_had_4 | [PNG](DCB/Plots/smodel_ttH_had_4.png) | [PNG](SoG/Plots/smodel_ttH_had_4.png) | 1.951 | 1.961 |
| ttH_lep_1 | [PNG](DCB/Plots/smodel_ttH_lep_1.png) | [PNG](SoG/Plots/smodel_ttH_lep_1.png) | 1.628 | 1.630 |
| ttH_lep_2 | [PNG](DCB/Plots/smodel_ttH_lep_2.png) | [PNG](SoG/Plots/smodel_ttH_lep_2.png) | 1.796 | 1.757 |
| ttH_lep_3 | [PNG](DCB/Plots/smodel_ttH_lep_3.png) | [PNG](SoG/Plots/smodel_ttH_lep_3.png) | 2.086 | 2.089 |
| ttH_lep_4 | [PNG](DCB/Plots/smodel_ttH_lep_4.png) | [PNG](SoG/Plots/smodel_ttH_lep_4.png) | 2.009 | 1.997 |
