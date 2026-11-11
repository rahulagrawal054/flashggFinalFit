# Category bookkeeping: bkg_had

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 352,649 | 0.181185020347 | 118.562100 | 878.022593054 |
| GluGluH | Inclusive workspace | 352,649 | 0.181185020347 | 118.562100 | 878.022593054 |
| GluGluH | In workspace | 23,198 | 0.008994928599 | 118.562100 | 40.597767664 |
| GluGluH | Out workspace | 329,451 | 0.172190091748 | 118.562100 | 837.424825390 |
| VBFH | Input ROOT tree | 346,352 | 0.316280787153 | 9.257060 | 105.944233031 |
| VBFH | Inclusive workspace | 346,352 | 0.316280787153 | 9.257060 | 105.944233031 |
| VBFH | In workspace | 20,690 | 0.014220870608 | 9.257060 | 4.587255113 |
| VBFH | Out workspace | 325,662 | 0.302059916545 | 9.257060 | 101.356977918 |
| VH | Input ROOT tree | 530,330 | 0.365177067144 | 5.450043 | 69.346227238 |
| VH | Inclusive workspace | 530,330 | 0.365177067144 | 5.450043 | 69.346227238 |
| VH | In workspace | 71,985 | 0.043299128010 | 5.450043 | 8.719407396 |
| VH | Out workspace | 458,345 | 0.321877939135 | 5.450043 | 60.626819842 |
| ttH | Input ROOT tree | 349,013 | 0.196238870616 | 1.293900 | 8.206826611 |
| ttH | Inclusive workspace | 349,013 | 0.196238870616 | 1.293900 | 8.206826611 |
| ttH | In workspace | 277,991 | 0.157833062728 | 1.293900 | 6.672189996 |
| ttH | Out workspace | 71,022 | 0.038405807888 | 1.293900 | 1.534636616 |
| tHqLep | Input ROOT tree | 232,598 | 0.213310407578 | 0.061576 | 0.475254632 |
| tHqLep | Inclusive workspace | 232,598 | 0.213310407578 | 0.061576 | 0.475254632 |
| tHqLep | In workspace | 188,180 | 0.173823119969 | 0.061576 | 0.380357902 |
| tHqLep | Out workspace | 44,418 | 0.039487287609 | 0.061576 | 0.094896730 |
| tHqHad | Input ROOT tree | 605,349 | 0.396560865742 | 0.127424 | 1.741123115 |
| tHqHad | Inclusive workspace | 605,349 | 0.396560865742 | 0.127424 | 1.741123115 |
| tHqHad | In workspace | 466,676 | 0.303635434367 | 0.127424 | 1.325159002 |
| tHqHad | Out workspace | 138,673 | 0.092925431374 | 0.127424 | 0.415964114 |
| tHW | Input ROOT tree | 394,544 | 0.298899277726 | 0.039044 | 0.398629372 |
| tHW | Inclusive workspace | 394,544 | 0.298899277726 | 0.039044 | 0.398629372 |
| tHW | In workspace | 293,159 | 0.221105351976 | 0.039044 | 0.297154482 |
| tHW | Out workspace | 101,385 | 0.077793925750 | 0.039044 | 0.101474890 |
| bbH | Input ROOT tree | 135,531 | 0.253627492035 | 1.196063 | 11.766628914 |
| bbH | Inclusive workspace | 135,531 | 0.253627492035 | 1.196063 | 11.766628914 |
| bbH | In workspace | 96,307 | 0.169994763908 | 1.196063 | 7.499626269 |
| bbH | Out workspace | 39,224 | 0.083632728128 | 1.196063 | 4.267002644 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 2,946,366 | 2.221279788342 | 1075.901515967 |
| Inclusive workspace | 2,946,366 | 2.221279788342 | 1075.901515967 |
| In workspace | 1,438,186 | 1.092906660165 | 70.078917823 |
| Out workspace | 1,508,180 | 1.128373128177 | 1005.822598144 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 36,144 | 0.028935719988 | 7.98 | 118.562100 | 27.376824220 |
| 2022preEE | GluGluH | Inclusive workspace | 36,144 | 0.028935719988 | 7.98 | 118.562100 | 27.376824220 |
| 2022preEE | GluGluH | In workspace | 2,455 | 0.001746857444 | 7.98 | 118.562100 | 1.652746474 |
| 2022preEE | GluGluH | Out workspace | 33,689 | 0.027188862544 | 7.98 | 118.562100 | 25.724077746 |
| 2022preEE | VBFH | Input ROOT tree | 18,426 | 0.054291330337 | 7.98 | 9.257060 | 4.010573257 |
| 2022preEE | VBFH | Inclusive workspace | 18,426 | 0.054291330337 | 7.98 | 9.257060 | 4.010573257 |
| 2022preEE | VBFH | In workspace | 1,023 | 0.002571098854 | 7.98 | 9.257060 | 0.189930515 |
| 2022preEE | VBFH | Out workspace | 17,403 | 0.051720231483 | 7.98 | 9.257060 | 3.820642743 |
| 2022preEE | VH | Input ROOT tree | 14,037 | 0.068276362557 | 7.98 | 5.450043 | 2.969430712 |
| 2022preEE | VH | Inclusive workspace | 14,037 | 0.068276362557 | 7.98 | 5.450043 | 2.969430712 |
| 2022preEE | VH | In workspace | 1,735 | 0.008485078819 | 7.98 | 5.450043 | 0.369027474 |
| 2022preEE | VH | Out workspace | 12,302 | 0.059791283739 | 7.98 | 5.450043 | 2.600403238 |
| 2022preEE | ttH | Input ROOT tree | 76,465 | 0.038702072871 | 7.98 | 1.293900 | 0.399611364 |
| 2022preEE | ttH | Inclusive workspace | 76,465 | 0.038702072871 | 7.98 | 1.293900 | 0.399611364 |
| 2022preEE | ttH | In workspace | 60,586 | 0.031694553270 | 7.98 | 1.293900 | 0.327256468 |
| 2022preEE | ttH | Out workspace | 15,879 | 0.007007519601 | 7.98 | 1.293900 | 0.072354896 |
| 2022preEE | tHqLep | Input ROOT tree | 26,461 | 0.040660346527 | 7.98 | 0.061576 | 0.019979624 |
| 2022preEE | tHqLep | Inclusive workspace | 26,461 | 0.040660346527 | 7.98 | 0.061576 | 0.019979624 |
| 2022preEE | tHqLep | In workspace | 21,628 | 0.033562174083 | 7.98 | 0.061576 | 0.016491734 |
| 2022preEE | tHqLep | Out workspace | 4,833 | 0.007098172444 | 7.98 | 0.061576 | 0.003487890 |
| 2022preEE | tHqHad | Input ROOT tree | 48,116 | 0.077394459849 | 7.98 | 0.127424 | 0.078698015 |
| 2022preEE | tHqHad | Inclusive workspace | 48,116 | 0.077394459849 | 7.98 | 0.127424 | 0.078698015 |
| 2022preEE | tHqHad | In workspace | 37,080 | 0.059017258339 | 7.98 | 0.127424 | 0.060011286 |
| 2022preEE | tHqHad | Out workspace | 11,036 | 0.018377201510 | 7.98 | 0.127424 | 0.018686729 |
| 2022preEE | tHW | Input ROOT tree | 115,214 | 0.057692155916 | 7.98 | 0.039044 | 0.017975210 |
| 2022preEE | tHW | Inclusive workspace | 115,214 | 0.057692155916 | 7.98 | 0.039044 | 0.017975210 |
| 2022preEE | tHW | In workspace | 84,883 | 0.042706778162 | 7.98 | 0.039044 | 0.013306199 |
| 2022preEE | tHW | Out workspace | 30,331 | 0.014985377754 | 7.98 | 0.039044 | 0.004669011 |
| 2022preEE | bbH | Input ROOT tree | 5,457 | 0.044793747366 | 7.98 | 1.196063 | 0.427537628 |
| 2022preEE | bbH | Inclusive workspace | 5,457 | 0.044793747366 | 7.98 | 1.196063 | 0.427537628 |
| 2022preEE | bbH | In workspace | 4,023 | 0.031769477992 | 7.98 | 1.196063 | 0.303226411 |
| 2022preEE | bbH | Out workspace | 1,434 | 0.013024269374 | 7.98 | 1.196063 | 0.124311217 |
| 2022postEE | GluGluH | Input ROOT tree | 58,150 | 0.032073257397 | 26.67 | 118.562100 | 101.417282266 |
| 2022postEE | GluGluH | Inclusive workspace | 58,150 | 0.032073257397 | 26.67 | 118.562100 | 101.417282266 |
| 2022postEE | GluGluH | In workspace | 4,181 | 0.001513727499 | 26.67 | 118.562100 | 4.786483865 |
| 2022postEE | GluGluH | Out workspace | 53,969 | 0.030559529899 | 26.67 | 118.562100 | 96.630798401 |
| 2022postEE | VBFH | Input ROOT tree | 93,277 | 0.060541802775 | 26.67 | 9.257060 | 14.946910818 |
| 2022postEE | VBFH | Inclusive workspace | 93,277 | 0.060541802775 | 26.67 | 9.257060 | 14.946910818 |
| 2022postEE | VBFH | In workspace | 5,736 | 0.002806616208 | 26.67 | 9.257060 | 0.692913660 |
| 2022postEE | VBFH | Out workspace | 87,541 | 0.057735186567 | 26.67 | 9.257060 | 14.253997158 |
| 2022postEE | VH | Input ROOT tree | 45,036 | 0.069841936673 | 26.67 | 5.450043 | 10.151710354 |
| 2022postEE | VH | Inclusive workspace | 45,036 | 0.069841936673 | 26.67 | 5.450043 | 10.151710354 |
| 2022postEE | VH | In workspace | 5,532 | 0.008168206343 | 26.67 | 5.450043 | 1.187270412 |
| 2022postEE | VH | Out workspace | 39,504 | 0.061673730330 | 26.67 | 5.450043 | 8.964439942 |
| 2022postEE | ttH | Input ROOT tree | 74,875 | 0.038061727189 | 26.67 | 1.293900 | 1.313445995 |
| 2022postEE | ttH | Inclusive workspace | 74,875 | 0.038061727189 | 26.67 | 1.293900 | 1.313445995 |
| 2022postEE | ttH | In workspace | 59,383 | 0.030059118592 | 26.67 | 1.293900 | 1.037289473 |
| 2022postEE | ttH | Out workspace | 15,492 | 0.008002608597 | 26.67 | 1.293900 | 0.276156522 |
| 2022postEE | tHqLep | Input ROOT tree | 52,308 | 0.039351637812 | 26.67 | 0.061576 | 0.064624794 |
| 2022postEE | tHqLep | Inclusive workspace | 52,308 | 0.039351637812 | 26.67 | 0.061576 | 0.064624794 |
| 2022postEE | tHqLep | In workspace | 42,957 | 0.031939681469 | 26.67 | 0.061576 | 0.052452590 |
| 2022postEE | tHqLep | Out workspace | 9,351 | 0.007411956343 | 26.67 | 0.061576 | 0.012172204 |
| 2022postEE | tHqHad | Input ROOT tree | 158,172 | 0.074994029830 | 26.67 | 0.127424 | 0.254859437 |
| 2022postEE | tHqHad | Inclusive workspace | 158,172 | 0.074994029830 | 26.67 | 0.127424 | 0.254859437 |
| 2022postEE | tHqHad | In workspace | 123,065 | 0.057689415217 | 26.67 | 0.127424 | 0.196051498 |
| 2022postEE | tHqHad | Out workspace | 35,107 | 0.017304614613 | 26.67 | 0.127424 | 0.058807939 |
| 2022postEE | tHW | Input ROOT tree | 113,838 | 0.056634436753 | 26.67 | 0.039044 | 0.058973636 |
| 2022postEE | tHW | Inclusive workspace | 113,838 | 0.056634436753 | 26.67 | 0.039044 | 0.058973636 |
| 2022postEE | tHW | In workspace | 84,318 | 0.041573363395 | 26.67 | 0.039044 | 0.043290488 |
| 2022postEE | tHW | Out workspace | 29,520 | 0.015061073358 | 26.67 | 0.039044 | 0.015683148 |
| 2022postEE | bbH | Input ROOT tree | 17,555 | 0.045655817254 | 26.67 | 1.196063 | 1.456374924 |
| 2022postEE | bbH | Inclusive workspace | 17,555 | 0.045655817254 | 26.67 | 1.196063 | 1.456374924 |
| 2022postEE | bbH | In workspace | 13,366 | 0.031702539424 | 26.67 | 1.196063 | 1.011279312 |
| 2022postEE | bbH | Out workspace | 4,189 | 0.013953277831 | 26.67 | 1.196063 | 0.445095612 |
| 2023preBPix | GluGluH | Input ROOT tree | 78,115 | 0.036899316216 | 18.06 | 118.562100 | 79.023103750 |
| 2023preBPix | GluGluH | Inclusive workspace | 78,115 | 0.036899316216 | 18.06 | 118.562100 | 79.023103750 |
| 2023preBPix | GluGluH | In workspace | 4,851 | 0.001819349160 | 18.06 | 118.562100 | 3.896294896 |
| 2023preBPix | GluGluH | Out workspace | 73,264 | 0.035079967055 | 18.06 | 118.562100 | 75.126808854 |
| 2023preBPix | VBFH | Input ROOT tree | 63,748 | 0.068863627325 | 18.06 | 9.257060 | 11.514706047 |
| 2023preBPix | VBFH | Inclusive workspace | 63,748 | 0.068863627325 | 18.06 | 9.257060 | 11.514706047 |
| 2023preBPix | VBFH | In workspace | 3,412 | 0.002957624497 | 18.06 | 9.257060 | 0.494545205 |
| 2023preBPix | VBFH | Out workspace | 60,336 | 0.065906002828 | 18.06 | 9.257060 | 11.020160842 |
| 2023preBPix | VH | Input ROOT tree | 32,114 | 0.077330813383 | 18.06 | 5.450043 | 7.612764391 |
| 2023preBPix | VH | Inclusive workspace | 32,114 | 0.077330813383 | 18.06 | 5.450043 | 7.612764391 |
| 2023preBPix | VH | In workspace | 3,578 | 0.008542148154 | 18.06 | 5.450043 | 0.840924315 |
| 2023preBPix | VH | Out workspace | 28,536 | 0.068788665230 | 18.06 | 5.450043 | 6.771840076 |
| 2023preBPix | ttH | Input ROOT tree | 69,614 | 0.042062498773 | 18.06 | 1.293900 | 0.983072763 |
| 2023preBPix | ttH | Inclusive workspace | 69,614 | 0.042062498773 | 18.06 | 1.293900 | 0.983072763 |
| 2023preBPix | ttH | In workspace | 55,336 | 0.033323215888 | 18.06 | 1.293900 | 0.778820728 |
| 2023preBPix | ttH | Out workspace | 14,278 | 0.008739282885 | 18.06 | 1.293900 | 0.204252035 |
| 2023preBPix | tHqLep | Input ROOT tree | 6,803 | 0.041887599755 | 18.06 | 0.061576 | 0.046589570 |
| 2023preBPix | tHqLep | Inclusive workspace | 6,803 | 0.041887599755 | 18.06 | 0.061576 | 0.046589570 |
| 2023preBPix | tHqLep | In workspace | 5,558 | 0.035174389365 | 18.06 | 0.061576 | 0.039122788 |
| 2023preBPix | tHqLep | Out workspace | 1,245 | 0.006713210390 | 18.06 | 0.061576 | 0.007466782 |
| 2023preBPix | tHqHad | Input ROOT tree | 144,005 | 0.081717282364 | 18.06 | 0.127424 | 0.188085280 |
| 2023preBPix | tHqHad | Inclusive workspace | 144,005 | 0.081717282364 | 18.06 | 0.127424 | 0.188085280 |
| 2023preBPix | tHqHad | In workspace | 111,308 | 0.063211954873 | 18.06 | 0.127424 | 0.145492335 |
| 2023preBPix | tHqHad | Out workspace | 32,697 | 0.018505327491 | 18.06 | 0.127424 | 0.042592945 |
| 2023preBPix | tHW | Input ROOT tree | 37,424 | 0.062744171489 | 18.06 | 0.039044 | 0.044250438 |
| 2023preBPix | tHW | Inclusive workspace | 37,424 | 0.062744171489 | 18.06 | 0.039044 | 0.044250438 |
| 2023preBPix | tHW | In workspace | 27,674 | 0.046127086741 | 18.06 | 0.039044 | 0.032531210 |
| 2023preBPix | tHW | Out workspace | 9,750 | 0.016617084748 | 18.06 | 0.039044 | 0.011719228 |
| 2023preBPix | bbH | Input ROOT tree | 17,317 | 0.050442847878 | 18.06 | 1.196063 | 1.089791799 |
| 2023preBPix | bbH | Inclusive workspace | 17,317 | 0.050442847878 | 18.06 | 1.196063 | 1.089791799 |
| 2023preBPix | bbH | In workspace | 12,221 | 0.033931442175 | 18.06 | 1.196063 | 0.733071366 |
| 2023preBPix | bbH | Out workspace | 5,096 | 0.016511405704 | 18.06 | 1.196063 | 0.356720433 |
| 2023postBPix | GluGluH | Input ROOT tree | 38,097 | 0.034945159152 | 9.69 | 118.562100 | 40.159760903 |
| 2023postBPix | GluGluH | Inclusive workspace | 38,097 | 0.034945159152 | 9.69 | 118.562100 | 40.159760903 |
| 2023postBPix | GluGluH | In workspace | 2,289 | 0.001747606973 | 9.69 | 118.562100 | 2.008389141 |
| 2023postBPix | GluGluH | Out workspace | 35,808 | 0.033197552180 | 9.69 | 118.562100 | 38.151371762 |
| 2023postBPix | VBFH | Input ROOT tree | 31,979 | 0.064082274779 | 9.69 | 9.257060 | 5.750018093 |
| 2023postBPix | VBFH | Inclusive workspace | 31,979 | 0.064082274779 | 9.69 | 9.257060 | 5.750018093 |
| 2023postBPix | VBFH | In workspace | 1,711 | 0.002995963175 | 9.69 | 9.257060 | 0.268823829 |
| 2023postBPix | VBFH | Out workspace | 30,268 | 0.061086311604 | 9.69 | 9.257060 | 5.481194264 |
| 2023postBPix | VH | Input ROOT tree | 15,665 | 0.075236311737 | 9.69 | 5.450043 | 3.974528713 |
| 2023postBPix | VH | Inclusive workspace | 15,665 | 0.075236311737 | 9.69 | 5.450043 | 3.974528713 |
| 2023postBPix | VH | In workspace | 1,759 | 0.008283475502 | 9.69 | 5.450043 | 0.437593370 |
| 2023postBPix | VH | Out workspace | 13,906 | 0.066952836235 | 9.69 | 5.450043 | 3.536935343 |
| 2023postBPix | ttH | Input ROOT tree | 85,947 | 0.042416295277 | 9.69 | 1.293900 | 0.531975534 |
| 2023postBPix | ttH | Inclusive workspace | 85,947 | 0.042416295277 | 9.69 | 1.293900 | 0.531975534 |
| 2023postBPix | ttH | In workspace | 68,455 | 0.033911921181 | 9.69 | 1.293900 | 0.425315607 |
| 2023postBPix | ttH | Out workspace | 17,492 | 0.008504374096 | 9.69 | 1.293900 | 0.106659927 |
| 2023postBPix | tHqLep | Input ROOT tree | 41,671 | 0.044516263715 | 9.69 | 0.061576 | 0.026569921 |
| 2023postBPix | tHqLep | Inclusive workspace | 41,671 | 0.044516263715 | 9.69 | 0.061576 | 0.026569921 |
| 2023postBPix | tHqLep | In workspace | 33,881 | 0.036112092454 | 9.69 | 0.061576 | 0.021553818 |
| 2023postBPix | tHqLep | Out workspace | 7,790 | 0.008404171261 | 9.69 | 0.061576 | 0.005016103 |
| 2023postBPix | tHqHad | Input ROOT tree | 78,484 | 0.082704210248 | 9.69 | 0.127424 | 0.102149641 |
| 2023postBPix | tHqHad | Inclusive workspace | 78,484 | 0.082704210248 | 9.69 | 0.127424 | 0.102149641 |
| 2023postBPix | tHqHad | In workspace | 60,581 | 0.063380976364 | 9.69 | 0.127424 | 0.078283124 |
| 2023postBPix | tHqHad | Out workspace | 17,903 | 0.019323233885 | 9.69 | 0.127424 | 0.023866517 |
| 2023postBPix | tHW | Input ROOT tree | 18,677 | 0.062733471033 | 9.69 | 0.039044 | 0.023741701 |
| 2023postBPix | tHW | Inclusive workspace | 18,677 | 0.062733471033 | 9.69 | 0.039044 | 0.023741701 |
| 2023postBPix | tHW | In workspace | 13,833 | 0.046323496328 | 9.69 | 0.039044 | 0.017531289 |
| 2023postBPix | tHW | Out workspace | 4,844 | 0.016409974705 | 9.69 | 0.039044 | 0.006210412 |
| 2023postBPix | bbH | Input ROOT tree | 8,797 | 0.050307366354 | 9.69 | 1.196063 | 0.583235366 |
| 2023postBPix | bbH | Inclusive workspace | 8,797 | 0.050307366354 | 9.69 | 1.196063 | 0.583235366 |
| 2023postBPix | bbH | In workspace | 6,201 | 0.034143096981 | 9.69 | 1.196063 | 0.395835900 |
| 2023postBPix | bbH | Out workspace | 2,596 | 0.016164269373 | 9.69 | 1.196063 | 0.187399465 |
| 2024 | GluGluH | Input ROOT tree | 142,143 | 0.048331567594 | 109.95 | 118.562100 | 630.045621915 |
| 2024 | GluGluH | Inclusive workspace | 142,143 | 0.048331567594 | 109.95 | 118.562100 | 630.045621915 |
| 2024 | GluGluH | In workspace | 9,422 | 0.002167387523 | 109.95 | 118.562100 | 28.253853288 |
| 2024 | GluGluH | Out workspace | 132,721 | 0.046164180071 | 109.95 | 118.562100 | 601.791768627 |
| 2024 | VBFH | Input ROOT tree | 138,922 | 0.068501751937 | 109.95 | 9.257060 | 69.722024815 |
| 2024 | VBFH | Inclusive workspace | 138,922 | 0.068501751937 | 109.95 | 9.257060 | 69.722024815 |
| 2024 | VBFH | In workspace | 8,808 | 0.002889567874 | 109.95 | 9.257060 | 2.941041905 |
| 2024 | VBFH | Out workspace | 130,114 | 0.065612184064 | 109.95 | 9.257060 | 66.780982911 |
| 2024 | VH | Input ROOT tree | 423,478 | 0.074491642793 | 109.95 | 5.450043 | 44.637793067 |
| 2024 | VH | Inclusive workspace | 423,478 | 0.074491642793 | 109.95 | 5.450043 | 44.637793067 |
| 2024 | VH | In workspace | 59,381 | 0.009820219191 | 109.95 | 5.450043 | 5.884591824 |
| 2024 | VH | Out workspace | 364,097 | 0.064671423602 | 109.95 | 5.450043 | 38.753201243 |
| 2024 | ttH | Input ROOT tree | 42,112 | 0.034996276506 | 109.95 | 1.293900 | 4.978720955 |
| 2024 | ttH | Inclusive workspace | 42,112 | 0.034996276506 | 109.95 | 1.293900 | 4.978720955 |
| 2024 | ttH | In workspace | 34,231 | 0.028844253796 | 109.95 | 1.293900 | 4.103507720 |
| 2024 | ttH | Out workspace | 7,881 | 0.006152022709 | 109.95 | 1.293900 | 0.875213235 |
| 2024 | tHqLep | Input ROOT tree | 105,355 | 0.046894559768 | 109.95 | 0.061576 | 0.317490724 |
| 2024 | tHqLep | Inclusive workspace | 105,355 | 0.046894559768 | 109.95 | 0.061576 | 0.317490724 |
| 2024 | tHqLep | In workspace | 84,156 | 0.037034782597 | 109.95 | 0.061576 | 0.250736972 |
| 2024 | tHqLep | Out workspace | 21,199 | 0.009859777170 | 109.95 | 0.061576 | 0.066753751 |
| 2024 | tHqHad | Input ROOT tree | 176,572 | 0.079750883451 | 109.95 | 0.127424 | 1.117330743 |
| 2024 | tHqHad | Inclusive workspace | 176,572 | 0.079750883451 | 109.95 | 0.127424 | 1.117330743 |
| 2024 | tHqHad | In workspace | 134,642 | 0.060335829575 | 109.95 | 0.127424 | 0.845320758 |
| 2024 | tHqHad | Out workspace | 41,930 | 0.019415053876 | 109.95 | 0.127424 | 0.272009984 |
| 2024 | tHW | Input ROOT tree | 109,391 | 0.059095042535 | 109.95 | 0.039044 | 0.253688387 |
| 2024 | tHW | Inclusive workspace | 109,391 | 0.059095042535 | 109.95 | 0.039044 | 0.253688387 |
| 2024 | tHW | In workspace | 82,451 | 0.044374627350 | 109.95 | 0.039044 | 0.190495296 |
| 2024 | tHW | Out workspace | 26,940 | 0.014720415185 | 109.95 | 0.039044 | 0.063193091 |
| 2024 | bbH | Input ROOT tree | 86,405 | 0.062427713182 | 109.95 | 1.196063 | 8.209689196 |
| 2024 | bbH | Inclusive workspace | 86,405 | 0.062427713182 | 109.95 | 1.196063 | 8.209689196 |
| 2024 | bbH | In workspace | 60,496 | 0.038448207336 | 109.95 | 1.196063 | 5.056213279 |
| 2024 | bbH | Out workspace | 25,909 | 0.023979505846 | 109.95 | 1.196063 | 3.153475917 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 506,049 | 506049.000000 | 0 |
| Data workspace | 506,049 | 506049.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 286,882 | 286882.000000 | 286,882 | 286882.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 74,419 | 74419.000000 | 74,419 | 74419.000000 |
| Upper sideband | 130 < m ≤ 180 | 144,748 | 144748.000000 | 144,748 | 144748.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 431,630 | 431630.000000 | 431,630 | 431630.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 506,049 | 506049.000000 | 506,049 | 506049.000000 |
| Total | All entries | 506,049 | 506049.000000 | 506,049 | 506049.000000 |

## Consistency checks

| Sample | Check | Result |
| --- | --- | --- |
| GluGluH / 2022preEE | Input = inclusive | PASS |
| GluGluH / 2022preEE | Inclusive = in + out | PASS |
| VBFH / 2022preEE | Input = inclusive | PASS |
| VBFH / 2022preEE | Inclusive = in + out | PASS |
| VH / 2022preEE | Input = inclusive | PASS |
| VH / 2022preEE | Inclusive = in + out | PASS |
| ttH / 2022preEE | Input = inclusive | PASS |
| ttH / 2022preEE | Inclusive = in + out | PASS |
| tHqLep / 2022preEE | Input = inclusive | PASS |
| tHqLep / 2022preEE | Inclusive = in + out | PASS |
| tHqHad / 2022preEE | Input = inclusive | PASS |
| tHqHad / 2022preEE | Inclusive = in + out | PASS |
| tHW / 2022preEE | Input = inclusive | PASS |
| tHW / 2022preEE | Inclusive = in + out | PASS |
| bbH / 2022preEE | Input = inclusive | PASS |
| bbH / 2022preEE | Inclusive = in + out | PASS |
| GluGluH / 2022postEE | Input = inclusive | PASS |
| GluGluH / 2022postEE | Inclusive = in + out | PASS |
| VBFH / 2022postEE | Input = inclusive | PASS |
| VBFH / 2022postEE | Inclusive = in + out | PASS |
| VH / 2022postEE | Input = inclusive | PASS |
| VH / 2022postEE | Inclusive = in + out | PASS |
| ttH / 2022postEE | Input = inclusive | PASS |
| ttH / 2022postEE | Inclusive = in + out | PASS |
| tHqLep / 2022postEE | Input = inclusive | PASS |
| tHqLep / 2022postEE | Inclusive = in + out | PASS |
| tHqHad / 2022postEE | Input = inclusive | PASS |
| tHqHad / 2022postEE | Inclusive = in + out | PASS |
| tHW / 2022postEE | Input = inclusive | PASS |
| tHW / 2022postEE | Inclusive = in + out | PASS |
| bbH / 2022postEE | Input = inclusive | PASS |
| bbH / 2022postEE | Inclusive = in + out | PASS |
| GluGluH / 2023preBPix | Input = inclusive | PASS |
| GluGluH / 2023preBPix | Inclusive = in + out | PASS |
| VBFH / 2023preBPix | Input = inclusive | PASS |
| VBFH / 2023preBPix | Inclusive = in + out | PASS |
| VH / 2023preBPix | Input = inclusive | PASS |
| VH / 2023preBPix | Inclusive = in + out | PASS |
| ttH / 2023preBPix | Input = inclusive | PASS |
| ttH / 2023preBPix | Inclusive = in + out | PASS |
| tHqLep / 2023preBPix | Input = inclusive | PASS |
| tHqLep / 2023preBPix | Inclusive = in + out | PASS |
| tHqHad / 2023preBPix | Input = inclusive | PASS |
| tHqHad / 2023preBPix | Inclusive = in + out | PASS |
| tHW / 2023preBPix | Input = inclusive | PASS |
| tHW / 2023preBPix | Inclusive = in + out | PASS |
| bbH / 2023preBPix | Input = inclusive | PASS |
| bbH / 2023preBPix | Inclusive = in + out | PASS |
| GluGluH / 2023postBPix | Input = inclusive | PASS |
| GluGluH / 2023postBPix | Inclusive = in + out | PASS |
| VBFH / 2023postBPix | Input = inclusive | PASS |
| VBFH / 2023postBPix | Inclusive = in + out | PASS |
| VH / 2023postBPix | Input = inclusive | PASS |
| VH / 2023postBPix | Inclusive = in + out | PASS |
| ttH / 2023postBPix | Input = inclusive | PASS |
| ttH / 2023postBPix | Inclusive = in + out | PASS |
| tHqLep / 2023postBPix | Input = inclusive | PASS |
| tHqLep / 2023postBPix | Inclusive = in + out | PASS |
| tHqHad / 2023postBPix | Input = inclusive | PASS |
| tHqHad / 2023postBPix | Inclusive = in + out | PASS |
| tHW / 2023postBPix | Input = inclusive | PASS |
| tHW / 2023postBPix | Inclusive = in + out | PASS |
| bbH / 2023postBPix | Input = inclusive | PASS |
| bbH / 2023postBPix | Inclusive = in + out | PASS |
| GluGluH / 2024 | Input = inclusive | PASS |
| GluGluH / 2024 | Inclusive = in + out | PASS |
| VBFH / 2024 | Input = inclusive | PASS |
| VBFH / 2024 | Inclusive = in + out | PASS |
| VH / 2024 | Input = inclusive | PASS |
| VH / 2024 | Inclusive = in + out | PASS |
| ttH / 2024 | Input = inclusive | PASS |
| ttH / 2024 | Inclusive = in + out | PASS |
| tHqLep / 2024 | Input = inclusive | PASS |
| tHqLep / 2024 | Inclusive = in + out | PASS |
| tHqHad / 2024 | Input = inclusive | PASS |
| tHqHad / 2024 | Inclusive = in + out | PASS |
| tHW / 2024 | Input = inclusive | PASS |
| tHW / 2024 | Inclusive = in + out | PASS |
| bbH / 2024 | Input = inclusive | PASS |
| bbH / 2024 | Inclusive = in + out | PASS |
| Data | Input = workspace | PASS |

Checks compare event counts and summed weights. Input versus inclusive differences may indicate conversion selections or a mismatch between input and workspace versions.

## Source ROOT files

| Sample/version | File | ROOT object |
| --- | --- | --- |
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| GluGluH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/allData.root | Data_13TeV_bkg_had |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/ws/allData.root | Data_13TeV_bkg_had |
