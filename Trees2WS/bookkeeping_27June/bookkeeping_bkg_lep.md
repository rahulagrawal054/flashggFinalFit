# Category bookkeeping: bkg_lep

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 308 | 0.000166120707 | 118.562100 | 0.316711635 |
| GluGluH | Inclusive workspace | 308 | 0.000166120707 | 118.562100 | 0.316711635 |
| GluGluH | In workspace | 101 | 0.000036068846 | 118.562100 | 0.065857780 |
| GluGluH | Out workspace | 207 | 0.000130051861 | 118.562100 | 0.250853855 |
| VBFH | Input ROOT tree | 245 | 0.000211440225 | 9.257060 | 0.027310045 |
| VBFH | Inclusive workspace | 245 | 0.000211440225 | 9.257060 | 0.027310045 |
| VBFH | In workspace | 50 | 0.000086509530 | 9.257060 | 0.011171130 |
| VBFH | Out workspace | 195 | 0.000124930695 | 9.257060 | 0.016138915 |
| VH | Input ROOT tree | 8,693 | 0.021654131883 | 5.450043 | 1.808968564 |
| VH | Inclusive workspace | 8,693 | 0.021654131883 | 5.450043 | 1.808968564 |
| VH | In workspace | 483 | 0.000892985664 | 5.450043 | 0.079026436 |
| VH | Out workspace | 8,210 | 0.020761146219 | 5.450043 | 1.729942128 |
| ttH | Input ROOT tree | 237,801 | 0.089721785880 | 1.293900 | 1.778092432 |
| ttH | Inclusive workspace | 237,801 | 0.089721785880 | 1.293900 | 1.778092432 |
| ttH | In workspace | 194,967 | 0.073619242554 | 1.293900 | 1.458429223 |
| ttH | Out workspace | 42,834 | 0.016102543325 | 1.293900 | 0.319663210 |
| tHqLep | Input ROOT tree | 174,333 | 0.141449338596 | 0.061576 | 0.133191291 |
| tHqLep | Inclusive workspace | 174,333 | 0.141449338596 | 0.061576 | 0.133191291 |
| tHqLep | In workspace | 147,781 | 0.119352929931 | 0.061576 | 0.112460326 |
| tHqLep | Out workspace | 26,552 | 0.022096408665 | 0.061576 | 0.020730965 |
| tHqHad | Input ROOT tree | 4,709 | 0.003706226851 | 0.127424 | 0.007330032 |
| tHqHad | Inclusive workspace | 4,709 | 0.003706226851 | 0.127424 | 0.007330032 |
| tHqHad | In workspace | 4,269 | 0.003397172729 | 0.127424 | 0.006818044 |
| tHqHad | Out workspace | 440 | 0.000309054122 | 0.127424 | 0.000511989 |
| tHW | Input ROOT tree | 263,851 | 0.128602699605 | 0.039044 | 0.077084615 |
| tHW | Inclusive workspace | 263,851 | 0.128602699605 | 0.039044 | 0.077084615 |
| tHW | In workspace | 208,637 | 0.100997371566 | 0.039044 | 0.060495361 |
| tHW | Out workspace | 55,214 | 0.027605328039 | 0.039044 | 0.016589254 |
| bbH | Input ROOT tree | 403 | 0.001500023621 | 1.196063 | 0.028968662 |
| bbH | Inclusive workspace | 403 | 0.001500023621 | 1.196063 | 0.028968662 |
| bbH | In workspace | 359 | 0.001271183009 | 1.196063 | 0.024923504 |
| bbH | Out workspace | 44 | 0.000228840611 | 1.196063 | 0.004045158 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 690,343 | 0.387011767368 | 4.177657277 |
| Inclusive workspace | 690,343 | 0.387011767368 | 4.177657277 |
| In workspace | 556,647 | 0.299653463830 | 1.819181804 |
| Out workspace | 133,696 | 0.087358303538 | 2.358475473 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 32 | 0.000026270822 | 7.98 | 118.562100 | 0.024855496 |
| 2022preEE | GluGluH | Inclusive workspace | 32 | 0.000026270822 | 7.98 | 118.562100 | 0.024855496 |
| 2022preEE | GluGluH | In workspace | 16 | 0.000019905450 | 7.98 | 118.562100 | 0.018833055 |
| 2022preEE | GluGluH | Out workspace | 16 | 0.000006365372 | 7.98 | 118.562100 | 0.006022441 |
| 2022preEE | VBFH | Input ROOT tree | 21 | 0.000031286677 | 7.98 | 9.257060 | 0.002311189 |
| 2022preEE | VBFH | Inclusive workspace | 21 | 0.000031286677 | 7.98 | 9.257060 | 0.002311189 |
| 2022preEE | VBFH | In workspace | 3 | 0.000008070245 | 7.98 | 9.257060 | 0.000596160 |
| 2022preEE | VBFH | Out workspace | 18 | 0.000023216431 | 7.98 | 9.257060 | 0.001715029 |
| 2022preEE | VH | Input ROOT tree | 1,113 | 0.004833818868 | 7.98 | 5.450043 | 0.210229275 |
| 2022preEE | VH | Inclusive workspace | 1,113 | 0.004833818868 | 7.98 | 5.450043 | 0.210229275 |
| 2022preEE | VH | In workspace | 69 | 0.000237067074 | 7.98 | 5.450043 | 0.010310365 |
| 2022preEE | VH | Out workspace | 1,044 | 0.004596751794 | 7.98 | 5.450043 | 0.199918910 |
| 2022preEE | ttH | Input ROOT tree | 39,740 | 0.021354407333 | 7.98 | 1.293900 | 0.220491132 |
| 2022preEE | ttH | Inclusive workspace | 39,740 | 0.021354407333 | 7.98 | 1.293900 | 0.220491132 |
| 2022preEE | ttH | In workspace | 32,529 | 0.017553643315 | 7.98 | 1.293900 | 0.181247020 |
| 2022preEE | ttH | Out workspace | 7,211 | 0.003800764018 | 7.98 | 1.293900 | 0.039244112 |
| 2022preEE | tHqLep | Input ROOT tree | 22,853 | 0.033864920919 | 7.98 | 0.061576 | 0.016640497 |
| 2022preEE | tHqLep | Inclusive workspace | 22,853 | 0.033864920919 | 7.98 | 0.061576 | 0.016640497 |
| 2022preEE | tHqLep | In workspace | 19,293 | 0.028725055816 | 7.98 | 0.061576 | 0.014114878 |
| 2022preEE | tHqLep | Out workspace | 3,560 | 0.005139865104 | 7.98 | 0.061576 | 0.002525620 |
| 2022preEE | tHqHad | Input ROOT tree | 597 | 0.000797271385 | 7.98 | 0.127424 | 0.000810700 |
| 2022preEE | tHqHad | Inclusive workspace | 597 | 0.000797271385 | 7.98 | 0.127424 | 0.000810700 |
| 2022preEE | tHqHad | In workspace | 540 | 0.000711565246 | 7.98 | 0.127424 | 0.000723550 |
| 2022preEE | tHqHad | Out workspace | 57 | 0.000085706139 | 7.98 | 0.127424 | 0.000087150 |
| 2022preEE | tHW | Input ROOT tree | 63,722 | 0.030060242148 | 7.98 | 0.039044 | 0.009365903 |
| 2022preEE | tHW | Inclusive workspace | 63,722 | 0.030060242148 | 7.98 | 0.039044 | 0.009365903 |
| 2022preEE | tHW | In workspace | 50,366 | 0.023745973116 | 7.98 | 0.039044 | 0.007398559 |
| 2022preEE | tHW | Out workspace | 13,356 | 0.006314269032 | 7.98 | 0.039044 | 0.001967344 |
| 2022preEE | bbH | Input ROOT tree | 40 | 0.000321653049 | 7.98 | 1.196063 | 0.003070044 |
| 2022preEE | bbH | Inclusive workspace | 40 | 0.000321653049 | 7.98 | 1.196063 | 0.003070044 |
| 2022preEE | bbH | In workspace | 32 | 0.000237233130 | 7.98 | 1.196063 | 0.002264291 |
| 2022preEE | bbH | Out workspace | 8 | 0.000084419919 | 7.98 | 1.196063 | 0.000805753 |
| 2022postEE | GluGluH | Input ROOT tree | 119 | 0.000034429914 | 26.68 | 118.562100 | 0.108909971 |
| 2022postEE | GluGluH | Inclusive workspace | 119 | 0.000034429914 | 26.68 | 118.562100 | 0.108909971 |
| 2022postEE | GluGluH | In workspace | 39 | 0.000007477300 | 26.68 | 118.562100 | 0.023652471 |
| 2022postEE | GluGluH | Out workspace | 80 | 0.000026952614 | 26.68 | 118.562100 | 0.085257500 |
| 2022postEE | VBFH | Input ROOT tree | 68 | 0.000019896319 | 26.68 | 9.257060 | 0.004913960 |
| 2022postEE | VBFH | Inclusive workspace | 68 | 0.000019896319 | 26.68 | 9.257060 | 0.004913960 |
| 2022postEE | VBFH | In workspace | 17 | 0.000007002463 | 26.68 | 9.257060 | 0.001729457 |
| 2022postEE | VBFH | Out workspace | 51 | 0.000012893856 | 26.68 | 9.257060 | 0.003184503 |
| 2022postEE | VH | Input ROOT tree | 3,622 | 0.004836073281 | 26.68 | 5.450043 | 0.703199620 |
| 2022postEE | VH | Inclusive workspace | 3,622 | 0.004836073281 | 26.68 | 5.450043 | 0.703199620 |
| 2022postEE | VH | In workspace | 211 | 0.000264029788 | 26.68 | 5.450043 | 0.038391818 |
| 2022postEE | VH | Out workspace | 3,411 | 0.004572043492 | 26.68 | 5.450043 | 0.664807801 |
| 2022postEE | ttH | Input ROOT tree | 107,128 | 0.020391158628 | 26.68 | 1.293900 | 0.703928326 |
| 2022postEE | ttH | Inclusive workspace | 107,128 | 0.020391158628 | 26.68 | 1.293900 | 0.703928326 |
| 2022postEE | ttH | In workspace | 87,734 | 0.016742517896 | 26.68 | 1.293900 | 0.577972679 |
| 2022postEE | ttH | Out workspace | 19,394 | 0.003648640731 | 26.68 | 1.293900 | 0.125955646 |
| 2022postEE | tHqLep | Input ROOT tree | 50,370 | 0.031928413017 | 26.68 | 0.061576 | 0.052453745 |
| 2022postEE | tHqLep | Inclusive workspace | 50,370 | 0.031928413017 | 26.68 | 0.061576 | 0.052453745 |
| 2022postEE | tHqLep | In workspace | 42,970 | 0.027187222509 | 26.68 | 0.061576 | 0.044664658 |
| 2022postEE | tHqLep | Out workspace | 7,400 | 0.004741190508 | 26.68 | 0.061576 | 0.007789087 |
| 2022postEE | tHqHad | Input ROOT tree | 1,347 | 0.000857806037 | 26.68 | 0.127424 | 0.002916258 |
| 2022postEE | tHqHad | Inclusive workspace | 1,347 | 0.000857806037 | 26.68 | 0.127424 | 0.002916258 |
| 2022postEE | tHqHad | In workspace | 1,202 | 0.000822740064 | 26.68 | 0.127424 | 0.002797045 |
| 2022postEE | tHqHad | Out workspace | 145 | 0.000035065973 | 26.68 | 0.127424 | 0.000119213 |
| 2022postEE | tHW | Input ROOT tree | 168,952 | 0.029250202395 | 26.68 | 0.039044 | 0.030469758 |
| 2022postEE | tHW | Inclusive workspace | 168,952 | 0.029250202395 | 26.68 | 0.039044 | 0.030469758 |
| 2022postEE | tHW | In workspace | 133,612 | 0.022977132286 | 26.68 | 0.039044 | 0.023935139 |
| 2022postEE | tHW | Out workspace | 35,340 | 0.006273070109 | 26.68 | 0.039044 | 0.006534619 |
| 2022postEE | bbH | Input ROOT tree | 145 | 0.000396138794 | 26.68 | 1.196063 | 0.012641170 |
| 2022postEE | bbH | Inclusive workspace | 145 | 0.000396138794 | 26.68 | 1.196063 | 0.012641170 |
| 2022postEE | bbH | In workspace | 131 | 0.000350942379 | 26.68 | 1.196063 | 0.011198908 |
| 2022postEE | bbH | Out workspace | 14 | 0.000045196416 | 26.68 | 1.196063 | 0.001442261 |
| 2023preBPix | GluGluH | Input ROOT tree | 101 | 0.000063112991 | 17.96 | 118.562100 | 0.134391245 |
| 2023preBPix | GluGluH | Inclusive workspace | 101 | 0.000063112991 | 17.96 | 118.562100 | 0.134391245 |
| 2023preBPix | GluGluH | In workspace | 29 | 0.000013653321 | 17.96 | 118.562100 | 0.029073044 |
| 2023preBPix | GluGluH | Out workspace | 72 | 0.000049459670 | 17.96 | 118.562100 | 0.105318201 |
| 2023preBPix | VBFH | Input ROOT tree | 106 | 0.000074685278 | 17.96 | 9.257060 | 0.012416935 |
| 2023preBPix | VBFH | Inclusive workspace | 106 | 0.000074685278 | 17.96 | 9.257060 | 0.012416935 |
| 2023preBPix | VBFH | In workspace | 23 | 0.000031888160 | 17.96 | 9.257060 | 0.005301623 |
| 2023preBPix | VBFH | Out workspace | 83 | 0.000042797118 | 17.96 | 9.257060 | 0.007115312 |
| 2023preBPix | VH | Input ROOT tree | 2,689 | 0.005834597629 | 17.96 | 5.450043 | 0.571106591 |
| 2023preBPix | VH | Inclusive workspace | 2,689 | 0.005834597629 | 17.96 | 5.450043 | 0.571106591 |
| 2023preBPix | VH | In workspace | 136 | 0.000213835211 | 17.96 | 5.450043 | 0.020930783 |
| 2023preBPix | VH | Out workspace | 2,553 | 0.005620762418 | 17.96 | 5.450043 | 0.550175808 |
| 2023preBPix | ttH | Input ROOT tree | 57,680 | 0.023593906021 | 17.96 | 1.293900 | 0.548285664 |
| 2023preBPix | ttH | Inclusive workspace | 57,680 | 0.023593906021 | 17.96 | 1.293900 | 0.548285664 |
| 2023preBPix | ttH | In workspace | 47,226 | 0.019292478807 | 17.96 | 1.293900 | 0.448327188 |
| 2023preBPix | ttH | Out workspace | 10,454 | 0.004301427214 | 17.96 | 1.293900 | 0.099958475 |
| 2023preBPix | tHqLep | Input ROOT tree | 73,639 | 0.037269016426 | 17.96 | 0.061576 | 0.041216168 |
| 2023preBPix | tHqLep | Inclusive workspace | 73,639 | 0.037269016426 | 17.96 | 0.061576 | 0.041216168 |
| 2023preBPix | tHqLep | In workspace | 62,210 | 0.031119782192 | 17.96 | 0.061576 | 0.034415670 |
| 2023preBPix | tHqLep | Out workspace | 11,429 | 0.006149234235 | 17.96 | 0.061576 | 0.006800498 |
| 2023preBPix | tHqHad | Input ROOT tree | 1,826 | 0.001017047166 | 17.96 | 0.127424 | 0.002327547 |
| 2023preBPix | tHqHad | Inclusive workspace | 1,826 | 0.001017047166 | 17.96 | 0.127424 | 0.002327547 |
| 2023preBPix | tHqHad | In workspace | 1,675 | 0.000947490565 | 17.96 | 0.127424 | 0.002168364 |
| 2023preBPix | tHqHad | Out workspace | 151 | 0.000069556601 | 17.96 | 0.127424 | 0.000159183 |
| 2023preBPix | tHW | Input ROOT tree | 20,775 | 0.034212078055 | 17.96 | 0.039044 | 0.023990544 |
| 2023preBPix | tHW | Inclusive workspace | 20,775 | 0.034212078055 | 17.96 | 0.039044 | 0.023990544 |
| 2023preBPix | tHW | In workspace | 16,451 | 0.026753307617 | 17.96 | 0.039044 | 0.018760228 |
| 2023preBPix | tHW | Out workspace | 4,324 | 0.007458770438 | 17.96 | 0.039044 | 0.005230315 |
| 2023preBPix | bbH | Input ROOT tree | 153 | 0.000424183079 | 17.96 | 1.196063 | 0.009112000 |
| 2023preBPix | bbH | Inclusive workspace | 153 | 0.000424183079 | 17.96 | 1.196063 | 0.009112000 |
| 2023preBPix | bbH | In workspace | 136 | 0.000358717061 | 17.96 | 1.196063 | 0.007705706 |
| 2023preBPix | bbH | Out workspace | 17 | 0.000065466018 | 17.96 | 1.196063 | 0.001406295 |
| 2023postBPix | GluGluH | Input ROOT tree | 56 | 0.000042306980 | 9.68 | 118.562100 | 0.048554922 |
| 2023postBPix | GluGluH | Inclusive workspace | 56 | 0.000042306980 | 9.68 | 118.562100 | 0.048554922 |
| 2023postBPix | GluGluH | In workspace | 17 | -0.000004967225 | 9.68 | 118.562100 | -0.005700791 |
| 2023postBPix | GluGluH | Out workspace | 39 | 0.000047274205 | 9.68 | 118.562100 | 0.054255713 |
| 2023postBPix | VBFH | Input ROOT tree | 50 | 0.000085571952 | 9.68 | 9.257060 | 0.007667961 |
| 2023postBPix | VBFH | Inclusive workspace | 50 | 0.000085571952 | 9.68 | 9.257060 | 0.007667961 |
| 2023postBPix | VBFH | In workspace | 7 | 0.000039548662 | 9.68 | 9.257060 | 0.003543890 |
| 2023postBPix | VBFH | Out workspace | 43 | 0.000046023290 | 9.68 | 9.257060 | 0.004124071 |
| 2023postBPix | VH | Input ROOT tree | 1,269 | 0.006149642105 | 9.68 | 5.450043 | 0.324433079 |
| 2023postBPix | VH | Inclusive workspace | 1,269 | 0.006149642105 | 9.68 | 5.450043 | 0.324433079 |
| 2023postBPix | VH | In workspace | 67 | 0.000178053591 | 9.68 | 5.450043 | 0.009393469 |
| 2023postBPix | VH | Out workspace | 1,202 | 0.005971588514 | 9.68 | 5.450043 | 0.315039609 |
| 2023postBPix | ttH | Input ROOT tree | 33,253 | 0.024382313898 | 9.68 | 1.293900 | 0.305387311 |
| 2023postBPix | ttH | Inclusive workspace | 33,253 | 0.024382313898 | 9.68 | 1.293900 | 0.305387311 |
| 2023postBPix | ttH | In workspace | 27,478 | 0.020030602536 | 9.68 | 1.293900 | 0.250882335 |
| 2023postBPix | ttH | Out workspace | 5,775 | 0.004351711362 | 9.68 | 1.293900 | 0.054504976 |
| 2023postBPix | tHqLep | Input ROOT tree | 27,471 | 0.038386988233 | 9.68 | 0.061576 | 0.022880881 |
| 2023postBPix | tHqLep | Inclusive workspace | 27,471 | 0.038386988233 | 9.68 | 0.061576 | 0.022880881 |
| 2023postBPix | tHqLep | In workspace | 23,308 | 0.032320869415 | 9.68 | 0.061576 | 0.019265121 |
| 2023postBPix | tHqLep | Out workspace | 4,163 | 0.006066118818 | 9.68 | 0.061576 | 0.003615760 |
| 2023postBPix | tHqHad | Input ROOT tree | 939 | 0.001034102263 | 9.68 | 0.127424 | 0.001275528 |
| 2023postBPix | tHqHad | Inclusive workspace | 939 | 0.001034102263 | 9.68 | 0.127424 | 0.001275528 |
| 2023postBPix | tHqHad | In workspace | 852 | 0.000915376854 | 9.68 | 0.127424 | 0.001129084 |
| 2023postBPix | tHqHad | Out workspace | 87 | 0.000118725408 | 9.68 | 0.127424 | 0.000146443 |
| 2023postBPix | tHW | Input ROOT tree | 10,402 | 0.035080177007 | 9.68 | 0.039044 | 0.013258410 |
| 2023postBPix | tHW | Inclusive workspace | 10,402 | 0.035080177007 | 9.68 | 0.039044 | 0.013258410 |
| 2023postBPix | tHW | In workspace | 8,208 | 0.027520958547 | 9.68 | 0.039044 | 0.010401434 |
| 2023postBPix | tHW | Out workspace | 2,194 | 0.007559218460 | 9.68 | 0.039044 | 0.002856976 |
| 2023postBPix | bbH | Input ROOT tree | 65 | 0.000358048698 | 9.68 | 1.196063 | 0.004145448 |
| 2023postBPix | bbH | Inclusive workspace | 65 | 0.000358048698 | 9.68 | 1.196063 | 0.004145448 |
| 2023postBPix | bbH | In workspace | 60 | 0.000324290440 | 9.68 | 1.196063 | 0.003754599 |
| 2023postBPix | bbH | Out workspace | 5 | 0.000033758258 | 9.68 | 1.196063 | 0.000390849 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 797 | 797.000000 | 0 |
| Data workspace | 797 | 797.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 423 | 423.000000 | 423 | 423.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 124 | 124.000000 | 124 | 124.000000 |
| Upper sideband | 130 < m ≤ 180 | 250 | 250.000000 | 250 | 250.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 673 | 673.000000 | 673 | 673.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 797 | 797.000000 | 797 | 797.000000 |
| Total | All entries | 797 | 797.000000 | 797 | 797.000000 |

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
| Data | Input = workspace | PASS |

Checks compare event counts and summed weights. Input versus inclusive differences may indicate conversion selections or a mismatch between input and workspace versions.

## Source ROOT files

| Sample/version | File | ROOT object |
| --- | --- | --- |
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/allData.root | Data_13TeV_bkg_lep |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/ws/allData.root | Data_13TeV_bkg_lep |
