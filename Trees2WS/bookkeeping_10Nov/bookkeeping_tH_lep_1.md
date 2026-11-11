# Category bookkeeping: tH_lep_1

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 17 | 0.000001302894 | 118.562100 | -0.002865704 |
| GluGluH | Inclusive workspace | 17 | 0.000001302894 | 118.562100 | -0.002865704 |
| GluGluH | In workspace | 10 | 0.000004338358 | 118.562100 | 0.013970974 |
| GluGluH | Out workspace | 7 | -0.000003035463 | 118.562100 | -0.016836678 |
| VBFH | Input ROOT tree | 64 | 0.000032863390 | 9.257060 | 0.014171238 |
| VBFH | Inclusive workspace | 64 | 0.000032863390 | 9.257060 | 0.014171238 |
| VBFH | In workspace | 35 | -0.000005527297 | 9.257060 | 0.004706472 |
| VBFH | Out workspace | 29 | 0.000038390687 | 9.257060 | 0.009464766 |
| VH | Input ROOT tree | 2,218 | 0.001660437354 | 5.450043 | 0.232993461 |
| VH | Inclusive workspace | 2,218 | 0.001660437354 | 5.450043 | 0.232993461 |
| VH | In workspace | 682 | 0.000169497659 | 5.450043 | 0.041756176 |
| VH | Out workspace | 1,536 | 0.001490939695 | 5.450043 | 0.191237285 |
| ttH | Input ROOT tree | 85,204 | 0.045061646604 | 1.293900 | 2.072655606 |
| ttH | Inclusive workspace | 85,204 | 0.045061646604 | 1.293900 | 2.072655606 |
| ttH | In workspace | 78,239 | 0.041362052592 | 1.293900 | 1.942997466 |
| ttH | Out workspace | 6,965 | 0.003699594012 | 1.293900 | 0.129658140 |
| tHqLep | Input ROOT tree | 396,133 | 0.361570013862 | 0.061576 | 0.754287623 |
| tHqLep | Inclusive workspace | 396,133 | 0.361570013862 | 0.061576 | 0.754287623 |
| tHqLep | In workspace | 378,284 | 0.344354403396 | 0.061576 | 0.719447191 |
| tHqLep | Out workspace | 17,849 | 0.017215610466 | 0.061576 | 0.034840432 |
| tHqHad | Input ROOT tree | 3,348 | 0.002344848827 | 0.127424 | 0.009629027 |
| tHqHad | Inclusive workspace | 3,348 | 0.002344848827 | 0.127424 | 0.009629027 |
| tHqHad | In workspace | 3,251 | 0.002244519571 | 0.127424 | 0.009076146 |
| tHqHad | Out workspace | 97 | 0.000100329256 | 0.127424 | 0.000552881 |
| tHW | Input ROOT tree | 91,836 | 0.059796044872 | 0.039044 | 0.083161520 |
| tHW | Inclusive workspace | 91,836 | 0.059796044872 | 0.039044 | 0.083161520 |
| tHW | In workspace | 85,006 | 0.054953630510 | 0.039044 | 0.077996621 |
| tHW | Out workspace | 6,830 | 0.004842414362 | 0.039044 | 0.005164899 |
| bbH | Input ROOT tree | 48 | -0.000000869104 | 1.196063 | 0.001330579 |
| bbH | Inclusive workspace | 48 | -0.000000869104 | 1.196063 | 0.001330579 |
| bbH | In workspace | 47 | -0.000001024153 | 1.196063 | 0.001310189 |
| bbH | Out workspace | 1 | 0.000000155049 | 1.196063 | 0.000020390 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 578,868 | 0.470466288700 | 3.165363350 |
| Inclusive workspace | 578,868 | 0.470466288700 | 3.165363350 |
| In workspace | 545,554 | 0.443081890636 | 2.811261235 |
| Out workspace | 33,314 | 0.027384398064 | 0.354102115 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 1 | -0.000000413144 | 7.98 | 118.562100 | -0.000390886 |
| 2022preEE | GluGluH | Inclusive workspace | 1 | -0.000000413144 | 7.98 | 118.562100 | -0.000390886 |
| 2022preEE | GluGluH | In workspace | 0 | 0.000000000000 | 7.98 | 118.562100 | 0.000000000 |
| 2022preEE | GluGluH | Out workspace | 1 | -0.000000413144 | 7.98 | 118.562100 | -0.000390886 |
| 2022preEE | VBFH | Input ROOT tree | 5 | -0.000008878263 | 7.98 | 9.257060 | -0.000655849 |
| 2022preEE | VBFH | Inclusive workspace | 5 | -0.000008878263 | 7.98 | 9.257060 | -0.000655849 |
| 2022preEE | VBFH | In workspace | 3 | -0.000017612166 | 7.98 | 9.257060 | -0.001301034 |
| 2022preEE | VBFH | Out workspace | 2 | 0.000008733903 | 7.98 | 9.257060 | 0.000645185 |
| 2022preEE | VH | Input ROOT tree | 82 | 0.000491859436 | 7.98 | 5.450043 | 0.021391628 |
| 2022preEE | VH | Inclusive workspace | 82 | 0.000491859436 | 7.98 | 5.450043 | 0.021391628 |
| 2022preEE | VH | In workspace | 18 | 0.000044292001 | 7.98 | 5.450043 | 0.001926319 |
| 2022preEE | VH | Out workspace | 64 | 0.000447567435 | 7.98 | 5.450043 | 0.019465309 |
| 2022preEE | ttH | Input ROOT tree | 19,477 | 0.009404117618 | 7.98 | 1.293900 | 0.097100543 |
| 2022preEE | ttH | Inclusive workspace | 19,477 | 0.009404117618 | 7.98 | 1.293900 | 0.097100543 |
| 2022preEE | ttH | In workspace | 17,786 | 0.008569541506 | 7.98 | 1.293900 | 0.088483275 |
| 2022preEE | ttH | Out workspace | 1,691 | 0.000834576112 | 7.98 | 1.293900 | 0.008617267 |
| 2022preEE | tHqLep | Input ROOT tree | 46,975 | 0.075587118364 | 7.98 | 0.061576 | 0.037141892 |
| 2022preEE | tHqLep | Inclusive workspace | 46,975 | 0.075587118364 | 7.98 | 0.061576 | 0.037141892 |
| 2022preEE | tHqLep | In workspace | 44,686 | 0.072205426781 | 7.98 | 0.061576 | 0.035480201 |
| 2022preEE | tHqLep | Out workspace | 2,289 | 0.003381691583 | 7.98 | 0.061576 | 0.001661691 |
| 2022preEE | tHqHad | Input ROOT tree | 290 | 0.000578240289 | 7.98 | 0.127424 | 0.000587980 |
| 2022preEE | tHqHad | Inclusive workspace | 290 | 0.000578240289 | 7.98 | 0.127424 | 0.000587980 |
| 2022preEE | tHqHad | In workspace | 282 | 0.000546701394 | 7.98 | 0.127424 | 0.000555909 |
| 2022preEE | tHqHad | Out workspace | 8 | 0.000031538895 | 7.98 | 0.127424 | 0.000032070 |
| 2022preEE | tHW | Input ROOT tree | 26,026 | 0.012153683645 | 7.98 | 0.039044 | 0.003786737 |
| 2022preEE | tHW | Inclusive workspace | 26,026 | 0.012153683645 | 7.98 | 0.039044 | 0.003786737 |
| 2022preEE | tHW | In workspace | 23,727 | 0.011072463089 | 7.98 | 0.039044 | 0.003449860 |
| 2022preEE | tHW | Out workspace | 2,299 | 0.001081220556 | 7.98 | 0.039044 | 0.000336877 |
| 2022preEE | bbH | Input ROOT tree | 2 | -0.000027960182 | 7.98 | 1.196063 | -0.000266868 |
| 2022preEE | bbH | Inclusive workspace | 2 | -0.000027960182 | 7.98 | 1.196063 | -0.000266868 |
| 2022preEE | bbH | In workspace | 2 | -0.000027960182 | 7.98 | 1.196063 | -0.000266868 |
| 2022preEE | bbH | Out workspace | 0 | 0.000000000000 | 7.98 | 1.196063 | 0.000000000 |
| 2022postEE | GluGluH | Input ROOT tree | 4 | 0.000003091308 | 26.67 | 118.562100 | 0.009774874 |
| 2022postEE | GluGluH | Inclusive workspace | 4 | 0.000003091308 | 26.67 | 118.562100 | 0.009774874 |
| 2022postEE | GluGluH | In workspace | 4 | 0.000003091308 | 26.67 | 118.562100 | 0.009774874 |
| 2022postEE | GluGluH | Out workspace | 0 | 0.000000000000 | 26.67 | 118.562100 | 0.000000000 |
| 2022postEE | VBFH | Input ROOT tree | 16 | 0.000012012032 | 26.67 | 9.257060 | 0.002965600 |
| 2022postEE | VBFH | Inclusive workspace | 16 | 0.000012012032 | 26.67 | 9.257060 | 0.002965600 |
| 2022postEE | VBFH | In workspace | 12 | 0.000008589817 | 26.67 | 9.257060 | 0.002120704 |
| 2022postEE | VBFH | Out workspace | 4 | 0.000003422215 | 26.67 | 9.257060 | 0.000844896 |
| 2022postEE | VH | Input ROOT tree | 210 | 0.000259217559 | 26.67 | 5.450043 | 0.037677958 |
| 2022postEE | VH | Inclusive workspace | 210 | 0.000259217559 | 26.67 | 5.450043 | 0.037677958 |
| 2022postEE | VH | In workspace | 43 | 0.000029964122 | 26.67 | 5.450043 | 0.004355364 |
| 2022postEE | VH | Out workspace | 167 | 0.000229253437 | 26.67 | 5.450043 | 0.033322594 |
| 2022postEE | ttH | Input ROOT tree | 19,485 | 0.008627908850 | 26.67 | 1.293900 | 0.297734579 |
| 2022postEE | ttH | Inclusive workspace | 19,485 | 0.008627908850 | 26.67 | 1.293900 | 0.297734579 |
| 2022postEE | ttH | In workspace | 17,748 | 0.007859301617 | 26.67 | 1.293900 | 0.271211240 |
| 2022postEE | ttH | Out workspace | 1,737 | 0.000768607233 | 26.67 | 1.293900 | 0.026523339 |
| 2022postEE | tHqLep | Input ROOT tree | 93,762 | 0.068279374341 | 26.67 | 0.061576 | 0.112131051 |
| 2022postEE | tHqLep | Inclusive workspace | 93,762 | 0.068279374341 | 26.67 | 0.061576 | 0.112131051 |
| 2022postEE | tHqLep | In workspace | 89,198 | 0.065189722273 | 26.67 | 0.061576 | 0.107057104 |
| 2022postEE | tHqLep | Out workspace | 4,564 | 0.003089652068 | 26.67 | 0.061576 | 0.005073947 |
| 2022postEE | tHqHad | Input ROOT tree | 896 | 0.000558018955 | 26.67 | 0.127424 | 0.001896370 |
| 2022postEE | tHqHad | Inclusive workspace | 896 | 0.000558018955 | 26.67 | 0.127424 | 0.001896370 |
| 2022postEE | tHqHad | In workspace | 872 | 0.000536618218 | 26.67 | 0.127424 | 0.001823641 |
| 2022postEE | tHqHad | Out workspace | 24 | 0.000021400737 | 26.67 | 0.127424 | 0.000072728 |
| 2022postEE | tHW | Input ROOT tree | 26,007 | 0.011386492783 | 26.67 | 0.039044 | 0.011856795 |
| 2022postEE | tHW | Inclusive workspace | 26,007 | 0.011386492783 | 26.67 | 0.039044 | 0.011856795 |
| 2022postEE | tHW | In workspace | 23,707 | 0.010345870866 | 26.67 | 0.039044 | 0.010773191 |
| 2022postEE | tHW | Out workspace | 2,300 | 0.001040621918 | 26.67 | 0.039044 | 0.001083603 |
| 2022postEE | bbH | Input ROOT tree | 7 | 0.000010383486 | 26.67 | 1.196063 | 0.000331223 |
| 2022postEE | bbH | Inclusive workspace | 7 | 0.000010383486 | 26.67 | 1.196063 | 0.000331223 |
| 2022postEE | bbH | In workspace | 7 | 0.000010383486 | 26.67 | 1.196063 | 0.000331223 |
| 2022postEE | bbH | Out workspace | 0 | 0.000000000000 | 26.67 | 1.196063 | 0.000000000 |
| 2023preBPix | GluGluH | Input ROOT tree | 4 | -0.000000521207 | 18.06 | 118.562100 | -0.001116210 |
| 2023preBPix | GluGluH | Inclusive workspace | 4 | -0.000000521207 | 18.06 | 118.562100 | -0.001116210 |
| 2023preBPix | GluGluH | In workspace | 2 | 0.000001107029 | 18.06 | 118.562100 | 0.002370799 |
| 2023preBPix | GluGluH | Out workspace | 2 | -0.000001628236 | 18.06 | 118.562100 | -0.003487009 |
| 2023preBPix | VBFH | Input ROOT tree | 16 | 0.000015183713 | 18.06 | 9.257060 | 0.002538873 |
| 2023preBPix | VBFH | Inclusive workspace | 16 | 0.000015183713 | 18.06 | 9.257060 | 0.002538873 |
| 2023preBPix | VBFH | In workspace | 9 | -0.000000387361 | 18.06 | 9.257060 | -0.000064771 |
| 2023preBPix | VBFH | Out workspace | 7 | 0.000015571074 | 18.06 | 9.257060 | 0.002603644 |
| 2023preBPix | VH | Input ROOT tree | 155 | 0.000303553928 | 18.06 | 5.450043 | 0.029883101 |
| 2023preBPix | VH | Inclusive workspace | 155 | 0.000303553928 | 18.06 | 5.450043 | 0.029883101 |
| 2023preBPix | VH | In workspace | 31 | 0.000037929928 | 18.06 | 5.450043 | 0.003733979 |
| 2023preBPix | VH | Out workspace | 124 | 0.000265624000 | 18.06 | 5.450043 | 0.026149123 |
| 2023preBPix | ttH | Input ROOT tree | 14,870 | 0.008849289531 | 18.06 | 1.293900 | 0.206823079 |
| 2023preBPix | ttH | Inclusive workspace | 14,870 | 0.008849289531 | 18.06 | 1.293900 | 0.206823079 |
| 2023preBPix | ttH | In workspace | 13,539 | 0.007961116415 | 18.06 | 1.293900 | 0.186064950 |
| 2023preBPix | ttH | Out workspace | 1,331 | 0.000888173115 | 18.06 | 1.293900 | 0.020758130 |
| 2023preBPix | tHqLep | Input ROOT tree | 10,427 | 0.073087740426 | 18.06 | 0.061576 | 0.081291991 |
| 2023preBPix | tHqLep | Inclusive workspace | 10,427 | 0.073087740426 | 18.06 | 0.061576 | 0.081291991 |
| 2023preBPix | tHqLep | In workspace | 9,911 | 0.069017385977 | 18.06 | 0.061576 | 0.076764731 |
| 2023preBPix | tHqLep | Out workspace | 516 | 0.004070354449 | 18.06 | 0.061576 | 0.004527260 |
| 2023preBPix | tHqHad | Input ROOT tree | 745 | 0.000506200781 | 18.06 | 0.127424 | 0.001165101 |
| 2023preBPix | tHqHad | Inclusive workspace | 745 | 0.000506200781 | 18.06 | 0.127424 | 0.001165101 |
| 2023preBPix | tHqHad | In workspace | 734 | 0.000491483632 | 18.06 | 0.127424 | 0.001131227 |
| 2023preBPix | tHqHad | Out workspace | 11 | 0.000014717149 | 18.06 | 0.127424 | 0.000033874 |
| 2023preBPix | tHW | Input ROOT tree | 7,231 | 0.012028415213 | 18.06 | 0.039044 | 0.008483061 |
| 2023preBPix | tHW | Inclusive workspace | 7,231 | 0.012028415213 | 18.06 | 0.039044 | 0.008483061 |
| 2023preBPix | tHW | In workspace | 6,579 | 0.010945471228 | 18.06 | 0.039044 | 0.007719313 |
| 2023preBPix | tHW | Out workspace | 652 | 0.001082943985 | 18.06 | 0.039044 | 0.000763748 |
| 2023preBPix | bbH | Input ROOT tree | 9 | -0.000001521611 | 18.06 | 1.196063 | -0.000032874 |
| 2023preBPix | bbH | Inclusive workspace | 9 | -0.000001521611 | 18.06 | 1.196063 | -0.000032874 |
| 2023preBPix | bbH | In workspace | 9 | -0.000001521611 | 18.06 | 1.196063 | -0.000032874 |
| 2023preBPix | bbH | Out workspace | 0 | 0.000000000000 | 18.06 | 1.196063 | 0.000000000 |
| 2023postBPix | GluGluH | Input ROOT tree | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | GluGluH | Inclusive workspace | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | GluGluH | In workspace | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | GluGluH | Out workspace | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | VBFH | Input ROOT tree | 5 | 0.000005907229 | 9.69 | 9.257060 | 0.000530048 |
| 2023postBPix | VBFH | Inclusive workspace | 5 | 0.000005907229 | 9.69 | 9.257060 | 0.000530048 |
| 2023postBPix | VBFH | In workspace | 0 | 0.000000000000 | 9.69 | 9.257060 | 0.000000000 |
| 2023postBPix | VBFH | Out workspace | 5 | 0.000005907229 | 9.69 | 9.257060 | 0.000530048 |
| 2023postBPix | VH | Input ROOT tree | 75 | 0.000400761303 | 9.69 | 5.450043 | 0.021171124 |
| 2023postBPix | VH | Inclusive workspace | 75 | 0.000400761303 | 9.69 | 5.450043 | 0.021171124 |
| 2023postBPix | VH | In workspace | 10 | 0.000004762857 | 9.69 | 5.450043 | 0.000251609 |
| 2023postBPix | VH | Out workspace | 65 | 0.000395998446 | 9.69 | 5.450043 | 0.020919516 |
| 2023postBPix | ttH | Input ROOT tree | 18,137 | 0.008598465304 | 9.69 | 1.293900 | 0.107839997 |
| 2023postBPix | ttH | Inclusive workspace | 18,137 | 0.008598465304 | 9.69 | 1.293900 | 0.107839997 |
| 2023postBPix | ttH | In workspace | 16,494 | 0.007842007118 | 9.69 | 1.293900 | 0.098352671 |
| 2023postBPix | ttH | Out workspace | 1,643 | 0.000756458186 | 9.69 | 1.293900 | 0.009487327 |
| 2023postBPix | tHqLep | Input ROOT tree | 62,704 | 0.073762792206 | 9.69 | 0.061576 | 0.044025967 |
| 2023postBPix | tHqLep | Inclusive workspace | 62,704 | 0.073762792206 | 9.69 | 0.061576 | 0.044025967 |
| 2023postBPix | tHqLep | In workspace | 59,536 | 0.070262817534 | 9.69 | 0.061576 | 0.041936977 |
| 2023postBPix | tHqLep | Out workspace | 3,168 | 0.003499974672 | 9.69 | 0.061576 | 0.002088990 |
| 2023postBPix | tHqHad | Input ROOT tree | 384 | 0.000302233412 | 9.69 | 0.127424 | 0.000373295 |
| 2023postBPix | tHqHad | Inclusive workspace | 384 | 0.000302233412 | 9.69 | 0.127424 | 0.000373295 |
| 2023postBPix | tHqHad | In workspace | 370 | 0.000298825135 | 9.69 | 0.127424 | 0.000369085 |
| 2023postBPix | tHqHad | Out workspace | 14 | 0.000003408278 | 9.69 | 0.127424 | 0.000004210 |
| 2023postBPix | tHW | Input ROOT tree | 3,528 | 0.011488457061 | 9.69 | 0.039044 | 0.004347847 |
| 2023postBPix | tHW | Inclusive workspace | 3,528 | 0.011488457061 | 9.69 | 0.039044 | 0.004347847 |
| 2023postBPix | tHW | In workspace | 3,208 | 0.010453957145 | 9.69 | 0.039044 | 0.003956337 |
| 2023postBPix | tHW | Out workspace | 320 | 0.001034499916 | 9.69 | 0.039044 | 0.000391510 |
| 2023postBPix | bbH | Input ROOT tree | 1 | 0.000009158022 | 9.69 | 1.196063 | 0.000106173 |
| 2023postBPix | bbH | Inclusive workspace | 1 | 0.000009158022 | 9.69 | 1.196063 | 0.000106173 |
| 2023postBPix | bbH | In workspace | 1 | 0.000009158022 | 9.69 | 1.196063 | 0.000106173 |
| 2023postBPix | bbH | Out workspace | 0 | 0.000000000000 | 9.69 | 1.196063 | 0.000000000 |
| 2024 | GluGluH | Input ROOT tree | 8 | -0.000000854063 | 109.95 | 118.562100 | -0.011133482 |
| 2024 | GluGluH | Inclusive workspace | 8 | -0.000000854063 | 109.95 | 118.562100 | -0.011133482 |
| 2024 | GluGluH | In workspace | 4 | 0.000000140021 | 109.95 | 118.562100 | 0.001825301 |
| 2024 | GluGluH | Out workspace | 4 | -0.000000994084 | 109.95 | 118.562100 | -0.012958783 |
| 2024 | VBFH | Input ROOT tree | 22 | 0.000008638680 | 109.95 | 9.257060 | 0.008792567 |
| 2024 | VBFH | Inclusive workspace | 22 | 0.000008638680 | 109.95 | 9.257060 | 0.008792567 |
| 2024 | VBFH | In workspace | 11 | 0.000003882413 | 109.95 | 9.257060 | 0.003951573 |
| 2024 | VBFH | Out workspace | 11 | 0.000004756267 | 109.95 | 9.257060 | 0.004840994 |
| 2024 | VH | Input ROOT tree | 1,696 | 0.000205045129 | 109.95 | 5.450043 | 0.122869649 |
| 2024 | VH | Inclusive workspace | 1,696 | 0.000205045129 | 109.95 | 5.450043 | 0.122869649 |
| 2024 | VH | In workspace | 580 | 0.000052548752 | 109.95 | 5.450043 | 0.031488906 |
| 2024 | VH | Out workspace | 1,116 | 0.000152496377 | 109.95 | 5.450043 | 0.091380744 |
| 2024 | ttH | Input ROOT tree | 13,235 | 0.009581865301 | 109.95 | 1.293900 | 1.363157408 |
| 2024 | ttH | Inclusive workspace | 13,235 | 0.009581865301 | 109.95 | 1.293900 | 1.363157408 |
| 2024 | ttH | In workspace | 12,672 | 0.009130085934 | 109.95 | 1.293900 | 1.298885330 |
| 2024 | ttH | Out workspace | 563 | 0.000451779366 | 109.95 | 1.293900 | 0.064272078 |
| 2024 | tHqLep | Input ROOT tree | 182,265 | 0.070852988524 | 109.95 | 0.061576 | 0.479696722 |
| 2024 | tHqLep | Inclusive workspace | 182,265 | 0.070852988524 | 109.95 | 0.061576 | 0.479696722 |
| 2024 | tHqLep | In workspace | 174,953 | 0.067679050831 | 109.95 | 0.061576 | 0.458208179 |
| 2024 | tHqLep | Out workspace | 7,312 | 0.003173937694 | 109.95 | 0.061576 | 0.021488543 |
| 2024 | tHqHad | Input ROOT tree | 1,033 | 0.000400155390 | 109.95 | 0.127424 | 0.005606282 |
| 2024 | tHqHad | Inclusive workspace | 1,033 | 0.000400155390 | 109.95 | 0.127424 | 0.005606282 |
| 2024 | tHqHad | In workspace | 993 | 0.000370891193 | 109.95 | 0.127424 | 0.005196283 |
| 2024 | tHqHad | Out workspace | 40 | 0.000029264197 | 109.95 | 0.127424 | 0.000409999 |
| 2024 | tHW | Input ROOT tree | 29,044 | 0.012738996170 | 109.95 | 0.039044 | 0.054687081 |
| 2024 | tHW | Inclusive workspace | 29,044 | 0.012738996170 | 109.95 | 0.039044 | 0.054687081 |
| 2024 | tHW | In workspace | 27,785 | 0.012135868183 | 109.95 | 0.039044 | 0.052097920 |
| 2024 | tHW | Out workspace | 1,259 | 0.000603127987 | 109.95 | 0.039044 | 0.002589161 |
| 2024 | bbH | Input ROOT tree | 29 | 0.000009071182 | 109.95 | 1.196063 | 0.001192925 |
| 2024 | bbH | Inclusive workspace | 29 | 0.000009071182 | 109.95 | 1.196063 | 0.001192925 |
| 2024 | bbH | In workspace | 28 | 0.000008916133 | 109.95 | 1.196063 | 0.001172535 |
| 2024 | bbH | Out workspace | 1 | 0.000000155049 | 109.95 | 1.196063 | 0.000020390 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 58 | 58.000000 | 0 |
| Data workspace | 58 | 58.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 23 | 23.000000 | 23 | 23.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 19 | 19.000000 | 19 | 19.000000 |
| Upper sideband | 130 < m ≤ 180 | 16 | 16.000000 | 16 | 16.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 39 | 39.000000 | 39 | 39.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 58 | 58.000000 | 58 | 58.000000 |
| Total | All entries | 58 | 58.000000 | 58 | 58.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_1 |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_1 |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_1 |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_1 |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_1 |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_1 |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_1 |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_1 |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_1 |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_1 |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_1 |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_1 |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_1 |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_1 |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_1 |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_1 |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_1 |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_1 |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_1 |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_1 |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_1 |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_1 |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_1 |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_1 |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_1 |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_1 |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_1 |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_1 |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_1 |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_1 |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_1 |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_1 |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_1 |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_1 |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_1 |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_1 |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_1 |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_1 |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_1 |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_1 |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_1 |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_1 |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_1 |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_1 |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_1 |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_1 |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_1 |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_1 |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_1 |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_1 |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_1 |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_1 |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_1 |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_1 |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_1 |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_1 |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_1 |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_1 |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_1 |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_1 |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_1 |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_1 |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_1 |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_1 |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_1 |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_1 |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_1 |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_1 |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_1 |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_1 |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_1 |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_1 |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_1 |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_1 |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_1 |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_1 |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_1 |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_1 |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_1 |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_1 |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_1 |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_1 |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_1 |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_1 |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_1 |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_1 |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_1 |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_1 |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_1 |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_1 |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_1 |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_1 |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_1 |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_1 |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_1 |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_1 |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_1 |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_1 |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_1 |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_1 |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_1 |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_1 |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_1 |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_1 |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_1 |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_1 |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_1 |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_1 |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_1 |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_1 |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_1 |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_1 |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_1 |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_1 |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_1 |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_1 |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_1 |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_1 |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_1 |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_1 |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_1 |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_1 |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_1 |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_1 |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_1 |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_1 |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_1 |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_1 |
| GluGluH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_1 |
| GluGluH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_1 |
| GluGluH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_1 |
| GluGluH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_1 |
| VBFH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_1 |
| VBFH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_1 |
| VBFH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_1 |
| VBFH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_1 |
| VH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_1 |
| VH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_1 |
| VH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_1 |
| VH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_1 |
| ttH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_1 |
| ttH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_1 |
| ttH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_1 |
| ttH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_1 |
| tHqLep / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_1 |
| tHqLep / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_1 |
| tHqLep / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_1 |
| tHqLep / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_1 |
| tHqHad / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_1 |
| tHqHad / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_1 |
| tHqHad / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_1 |
| tHqHad / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_1 |
| tHW / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_1 |
| tHW / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_1 |
| tHW / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_1 |
| tHW / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_1 |
| bbH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_1 |
| bbH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_1 |
| bbH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_1 |
| bbH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_1 |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/allData.root | Data_13TeV_tH_lep_1 |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/ws/allData.root | Data_13TeV_tH_lep_1 |
