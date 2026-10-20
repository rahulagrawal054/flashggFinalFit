# Smearing response of current DCB and SoG signal PDFs

This is a read-only scan of the latest packaged tth_in / ttH_had_1 model in each era, not a new fit or a profile-likelihood impact calculation. All photon nuisance values start at zero. MH is fixed to 125.09. Only CMS_hgg_nuisance_Smearing is assigned -2,-1,0,+1,+2 in memory; figures show -1,0,+1. A constant RooRealVar can still be assigned values with setVal; it need not be floated for this conditional evaluation. Its interpretation as ±1 standard deviation requires the downstream unit-Gaussian constraint prescription.

Normalized PDFs use RooFit's observable normalization set over the full mass range. The peak view is 118–132 and log-tail view 110–140. Ratio panels show 100*(PDF(theta)/PDF(0)-1), masking nominal density below 1e-5 of the peak to avoid ratios of numerically tiny tails. Means and widths are checked, along with total normalization and full-range integral; ±2 scans are stored in curves.csv and scan_results.json. Left/right window probabilities use [MH-5,MH-2] and [MH+2,MH+5]. No plotting pruning or summed-process weights are involved: this is one process/category PDF per era, matched between families.

The current source constructs photon responses in tools/finalModel.py:327–395. Widths are multiplied by max(0.01, 1+c_sigma*theta); mean and rate can also respond if the corresponding stored coefficients pass their inclusion thresholds. Inspect the measured parameter shifts below rather than assuming a pure width effect. DCB tail parameters and fractions and SoG component fractions are not directly changed by this nuisance. The six DCB parameters are not refitted for each theta.

A left/right asymmetric shape is different from an up/down nonlinear response. Even a single Gaussian changes nonlinearly with width, so the ±1 density changes need not be equal and opposite. A SoG with distinct means need not be symmetric about a common center. These PDFs therefore cannot establish a general rule that SoG impacts must be symmetric and DCB impacts asymmetric. Signal-strength impacts additionally depend on the background likelihood, normalization, constraints and profiling. Once datacards exist, the actual impact question requires the corresponding Combine fits. Full-range PDF integrals, measured responses and original fit success flags are recorded; some nominal production fits did not converge and their scans do not resolve that issue.

| Era | Peak scan | Tail scan | DCB nominal fit success | SoG nominal fit success |
|---|---|---|---|---|
| 2022preEE | [PNG](2022preEE_peak.png) | [PNG](2022preEE_tails.png) | True | False |
| 2022postEE | [PNG](2022postEE_peak.png) | [PNG](2022postEE_tails.png) | False | True |
| 2023preBPix | [PNG](2023preBPix_peak.png) | [PNG](2023preBPix_tails.png) | True | True |
| 2023postBPix | [PNG](2023postBPix_peak.png) | [PNG](2023postBPix_tails.png) | True | False |

## Measured ±1 responses

- 2022preEE DCB: width ratios +1=[1.0836239749201628, 1.0836239749201628], -1=[0.9163760250798373, 0.9163760250798371]; maximum absolute mean shift=0 GeV; relative rate shifts +1=0, -1=0.
- 2022preEE SoG: width ratios +1=[1.0836239749201628, 1.0836239749201628, 1.0836239749201628, 1.0836239749201628], -1=[0.9163760250798372, 0.9163760250798373, 0.9163760250798372, 0.9163760250798372]; maximum absolute mean shift=0 GeV; relative rate shifts +1=0, -1=0.
- 2022postEE DCB: width ratios +1=[1.0495211356087264, 1.0495211356087264], -1=[0.9504788643912734, 0.9504788643912734]; maximum absolute mean shift=0 GeV; relative rate shifts +1=0, -1=0.
- 2022postEE SoG: width ratios +1=[1.0495211356087264, 1.0495211356087264, 1.0495211356087264], -1=[0.9504788643912735, 0.9504788643912734, 0.9504788643912735]; maximum absolute mean shift=0 GeV; relative rate shifts +1=0, -1=0.
- 2023preBPix DCB: width ratios +1=[1.0435625187273523, 1.0435625187273523], -1=[0.9564374812726477, 0.9564374812726476]; maximum absolute mean shift=0.0369758 GeV; relative rate shifts +1=0, -1=0.
- 2023preBPix SoG: width ratios +1=[1.0435625187273523, 1.0435625187273523, 1.0435625187273523, 1.0435625187273523], -1=[0.9564374812726478, 0.9564374812726478, 0.9564374812726477, 0.9564374812726477]; maximum absolute mean shift=0.0371964 GeV; relative rate shifts +1=0, -1=0.
- 2023postBPix DCB: width ratios +1=[1.0425472092203165, 1.0425472092203165], -1=[0.9574527907796834, 0.9574527907796834]; maximum absolute mean shift=0.0176913 GeV; relative rate shifts +1=0, -1=0.
- 2023postBPix SoG: width ratios +1=[1.0425472092203165, 1.0425472092203165, 1.0425472092203165], -1=[0.9574527907796834, 0.9574527907796834, 0.9574527907796835]; maximum absolute mean shift=0.0177126 GeV; relative rate shifts +1=0, -1=0.

Inputs were opened READ; no workspace, nuisance constants, fit settings, datacard or source script was changed. All generated plots and scan tables are in this directory.

## Main observations

For this reference process/category, the width scales agree between DCB and SoG in each era: ±8.3624% in 2022preEE, ±4.9521% in 2022postEE, ±4.3563% in 2023preBPix, and ±4.2547% in 2023postBPix at theta=±1. The two 2022 eras have unchanged mean functions over this scan. The 2023 eras also have a nonzero stored mean response to Smearing: maximum component mean shifts are about 0.037 GeV (preBPix) and 0.018 GeV (postBPix) at ±1. Thus the 2023 changes are not exclusively width changes. Central normalization is unchanged at ±1 in all these cases. The observed PDF changes are not exactly equal-and-opposite and need not have left/right symmetry in either family. This scan does not demonstrate or predict a symmetric versus asymmetric signal-strength impact without a profiled full-likelihood calculation.

The 2023preBPix example has both nominal optimizers converged and is the cleanest of these four production examples for studying the conditional shape response. The other era figures explicitly identify nominal fits with optimizer warnings/failures and should not be treated as validated model-choice evidence.
