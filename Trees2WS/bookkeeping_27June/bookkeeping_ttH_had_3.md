# Category bookkeeping: ttH_had_3

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 895 | 0.000179293403 | 118.562100 | 0.352428435 |
| GluGluH | Inclusive workspace | 895 | 0.000179293403 | 118.562100 | 0.352428435 |
| GluGluH | In workspace | 564 | 0.000092630133 | 118.562100 | 0.173191094 |
| GluGluH | Out workspace | 331 | 0.000086663270 | 118.562100 | 0.179237341 |
| VBFH | Input ROOT tree | 336 | 0.000152702718 | 9.257060 | 0.037943708 |
| VBFH | Inclusive workspace | 336 | 0.000152702718 | 9.257060 | 0.037943708 |
| VBFH | In workspace | 160 | -0.000022989411 | 9.257060 | -0.003883036 |
| VBFH | Out workspace | 176 | 0.000175692129 | 9.257060 | 0.041826743 |
| VH | Input ROOT tree | 1,635 | 0.002960916917 | 5.450043 | 0.266426768 |
| VH | Inclusive workspace | 1,635 | 0.002960916917 | 5.450043 | 0.266426768 |
| VH | In workspace | 978 | 0.001514142607 | 5.450043 | 0.143810506 |
| VH | Out workspace | 657 | 0.001446774310 | 5.450043 | 0.122616262 |
| ttH | Input ROOT tree | 384,604 | 0.136604231355 | 1.293900 | 2.747596504 |
| ttH | Inclusive workspace | 384,604 | 0.136604231355 | 1.293900 | 2.747596504 |
| ttH | In workspace | 353,153 | 0.125685625105 | 1.293900 | 2.527961360 |
| ttH | Out workspace | 31,451 | 0.010918606250 | 1.293900 | 0.219635145 |
| tHqLep | Input ROOT tree | 51,137 | 0.036810756744 | 0.061576 | 0.035365183 |
| tHqLep | Inclusive workspace | 51,137 | 0.036810756744 | 0.061576 | 0.035365183 |
| tHqLep | In workspace | 47,854 | 0.034526333317 | 0.061576 | 0.033259189 |
| tHqLep | Out workspace | 3,283 | 0.002284423428 | 0.061576 | 0.002105994 |
| tHqHad | Input ROOT tree | 118,050 | 0.083133252593 | 0.127424 | 0.164896179 |
| tHqHad | Inclusive workspace | 118,050 | 0.083133252593 | 0.127424 | 0.164896179 |
| tHqHad | In workspace | 114,287 | 0.080951917599 | 0.127424 | 0.160572409 |
| tHqHad | Out workspace | 3,763 | 0.002181334994 | 0.127424 | 0.004323770 |
| tHW | Input ROOT tree | 300,166 | 0.129921788809 | 0.039044 | 0.078949359 |
| tHW | Inclusive workspace | 300,166 | 0.129921788809 | 0.039044 | 0.078949359 |
| tHW | In workspace | 279,457 | 0.120767563499 | 0.039044 | 0.073374012 |
| tHW | Out workspace | 20,709 | 0.009154225310 | 0.039044 | 0.005575347 |
| bbH | Input ROOT tree | 541 | 0.001627525722 | 1.196063 | 0.028913078 |
| bbH | Inclusive workspace | 541 | 0.001627525722 | 1.196063 | 0.028913078 |
| bbH | In workspace | 532 | 0.001611286024 | 1.196063 | 0.028414201 |
| bbH | Out workspace | 9 | 0.000016239699 | 1.196063 | 0.000498877 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 857,364 | 0.391390468261 | 3.712519214 |
| Inclusive workspace | 857,364 | 0.391390468261 | 3.712519214 |
| In workspace | 796,985 | 0.365126508872 | 3.136699734 |
| Out workspace | 60,379 | 0.026263959389 | 0.575819480 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 120 | 0.000038006557 | 7.98 | 118.562100 | 0.035958975 |
| 2022preEE | GluGluH | Inclusive workspace | 120 | 0.000038006557 | 7.98 | 118.562100 | 0.035958975 |
| 2022preEE | GluGluH | In workspace | 76 | 0.000014861361 | 7.98 | 118.562100 | 0.014060713 |
| 2022preEE | GluGluH | Out workspace | 44 | 0.000023145196 | 7.98 | 118.562100 | 0.021898262 |
| 2022preEE | VBFH | Input ROOT tree | 30 | -0.000037807086 | 7.98 | 9.257060 | -0.002792860 |
| 2022preEE | VBFH | Inclusive workspace | 30 | -0.000037807086 | 7.98 | 9.257060 | -0.002792860 |
| 2022preEE | VBFH | In workspace | 11 | -0.000012122323 | 7.98 | 9.257060 | -0.000895492 |
| 2022preEE | VBFH | Out workspace | 19 | -0.000025684763 | 7.98 | 9.257060 | -0.001897368 |
| 2022preEE | VH | Input ROOT tree | 216 | 0.000586179141 | 7.98 | 5.450043 | 0.025493718 |
| 2022preEE | VH | Inclusive workspace | 216 | 0.000586179141 | 7.98 | 5.450043 | 0.025493718 |
| 2022preEE | VH | In workspace | 128 | 0.000267498999 | 7.98 | 5.450043 | 0.011633891 |
| 2022preEE | VH | Out workspace | 88 | 0.000318680142 | 7.98 | 5.450043 | 0.013859827 |
| 2022preEE | ttH | Input ROOT tree | 66,528 | 0.034831863446 | 7.98 | 1.293900 | 0.359650206 |
| 2022preEE | ttH | Inclusive workspace | 66,528 | 0.034831863446 | 7.98 | 1.293900 | 0.359650206 |
| 2022preEE | ttH | In workspace | 61,130 | 0.032077787694 | 7.98 | 1.293900 | 0.331213487 |
| 2022preEE | ttH | Out workspace | 5,398 | 0.002754075751 | 7.98 | 1.293900 | 0.028436719 |
| 2022preEE | tHqLep | Input ROOT tree | 7,342 | 0.009871371339 | 7.98 | 0.061576 | 0.004850581 |
| 2022preEE | tHqLep | Inclusive workspace | 7,342 | 0.009871371339 | 7.98 | 0.061576 | 0.004850581 |
| 2022preEE | tHqLep | In workspace | 6,881 | 0.009121296325 | 7.98 | 0.061576 | 0.004482010 |
| 2022preEE | tHqLep | Out workspace | 461 | 0.000750075014 | 7.98 | 0.061576 | 0.000368571 |
| 2022preEE | tHqHad | Input ROOT tree | 15,329 | 0.021342037982 | 7.98 | 0.127424 | 0.021701502 |
| 2022preEE | tHqHad | Inclusive workspace | 15,329 | 0.021342037982 | 7.98 | 0.127424 | 0.021701502 |
| 2022preEE | tHqHad | In workspace | 14,825 | 0.020759622392 | 7.98 | 0.127424 | 0.021109277 |
| 2022preEE | tHqHad | Out workspace | 504 | 0.000582415589 | 7.98 | 0.127424 | 0.000592225 |
| 2022preEE | tHW | Input ROOT tree | 72,817 | 0.033801997407 | 7.98 | 0.039044 | 0.010531726 |
| 2022preEE | tHW | Inclusive workspace | 72,817 | 0.033801997407 | 7.98 | 0.039044 | 0.010531726 |
| 2022preEE | tHW | In workspace | 67,744 | 0.031423848283 | 7.98 | 0.039044 | 0.009790764 |
| 2022preEE | tHW | Out workspace | 5,073 | 0.002378149124 | 7.98 | 0.039044 | 0.000740963 |
| 2022preEE | bbH | Input ROOT tree | 73 | 0.000466572518 | 7.98 | 1.196063 | 0.004453240 |
| 2022preEE | bbH | Inclusive workspace | 73 | 0.000466572518 | 7.98 | 1.196063 | 0.004453240 |
| 2022preEE | bbH | In workspace | 73 | 0.000466572518 | 7.98 | 1.196063 | 0.004453240 |
| 2022preEE | bbH | Out workspace | 0 | 0.000000000000 | 7.98 | 1.196063 | 0.000000000 |
| 2022postEE | GluGluH | Input ROOT tree | 432 | 0.000048787438 | 26.68 | 118.562100 | 0.154326220 |
| 2022postEE | GluGluH | Inclusive workspace | 432 | 0.000048787438 | 26.68 | 118.562100 | 0.154326220 |
| 2022postEE | GluGluH | In workspace | 278 | 0.000024243435 | 26.68 | 118.562100 | 0.076687727 |
| 2022postEE | GluGluH | Out workspace | 154 | 0.000024544002 | 26.68 | 118.562100 | 0.077638492 |
| 2022postEE | VBFH | Input ROOT tree | 115 | 0.000110890306 | 26.68 | 9.257060 | 0.027387506 |
| 2022postEE | VBFH | Inclusive workspace | 115 | 0.000110890306 | 26.68 | 9.257060 | 0.027387506 |
| 2022postEE | VBFH | In workspace | 55 | -0.000010161878 | 26.68 | 9.257060 | -0.002509764 |
| 2022postEE | VBFH | Out workspace | 60 | 0.000121052184 | 26.68 | 9.257060 | 0.029897270 |
| 2022postEE | VH | Input ROOT tree | 744 | 0.000820464550 | 26.68 | 5.450043 | 0.119301410 |
| 2022postEE | VH | Inclusive workspace | 744 | 0.000820464550 | 26.68 | 5.450043 | 0.119301410 |
| 2022postEE | VH | In workspace | 444 | 0.000450458848 | 26.68 | 5.450043 | 0.065499936 |
| 2022postEE | VH | Out workspace | 300 | 0.000370005701 | 26.68 | 5.450043 | 0.053801473 |
| 2022postEE | ttH | Input ROOT tree | 185,148 | 0.033920593599 | 26.68 | 1.293900 | 1.170981360 |
| 2022postEE | ttH | Inclusive workspace | 185,148 | 0.033920593599 | 26.68 | 1.293900 | 1.170981360 |
| 2022postEE | ttH | In workspace | 170,136 | 0.031279485290 | 26.68 | 1.293900 | 1.079806994 |
| 2022postEE | ttH | Out workspace | 15,012 | 0.002641108309 | 26.68 | 1.293900 | 0.091174366 |
| 2022postEE | tHqLep | Input ROOT tree | 16,119 | 0.009474633933 | 26.68 | 0.061576 | 0.015565447 |
| 2022postEE | tHqLep | Inclusive workspace | 16,119 | 0.009474633933 | 26.68 | 0.061576 | 0.015565447 |
| 2022postEE | tHqLep | In workspace | 15,085 | 0.008956142622 | 26.68 | 0.061576 | 0.014713641 |
| 2022postEE | tHqLep | Out workspace | 1,034 | 0.000518491311 | 26.68 | 0.061576 | 0.000851806 |
| 2022postEE | tHqHad | Input ROOT tree | 37,660 | 0.020817353023 | 26.68 | 0.127424 | 0.070772143 |
| 2022postEE | tHqHad | Inclusive workspace | 37,660 | 0.020817353023 | 26.68 | 0.127424 | 0.070772143 |
| 2022postEE | tHqHad | In workspace | 36,500 | 0.020215376730 | 26.68 | 0.127424 | 0.068725622 |
| 2022postEE | tHqHad | Out workspace | 1,160 | 0.000601976293 | 26.68 | 0.127424 | 0.002046521 |
| 2022postEE | tHW | Input ROOT tree | 196,642 | 0.032356035915 | 26.68 | 0.039044 | 0.033705086 |
| 2022postEE | tHW | Inclusive workspace | 196,642 | 0.032356035915 | 26.68 | 0.039044 | 0.033705086 |
| 2022postEE | tHW | In workspace | 183,149 | 0.030035591740 | 26.68 | 0.039044 | 0.031287893 |
| 2022postEE | tHW | Out workspace | 13,493 | 0.002320444175 | 26.68 | 0.039044 | 0.002417193 |
| 2022postEE | bbH | Input ROOT tree | 201 | 0.000366373968 | 26.68 | 1.196063 | 0.011691345 |
| 2022postEE | bbH | Inclusive workspace | 201 | 0.000366373968 | 26.68 | 1.196063 | 0.011691345 |
| 2022postEE | bbH | In workspace | 198 | 0.000356220128 | 26.68 | 1.196063 | 0.011367327 |
| 2022postEE | bbH | Out workspace | 3 | 0.000010153840 | 26.68 | 1.196063 | 0.000324019 |
| 2023preBPix | GluGluH | Input ROOT tree | 226 | 0.000057027347 | 17.96 | 118.562100 | 0.121432625 |
| 2023preBPix | GluGluH | Inclusive workspace | 226 | 0.000057027347 | 17.96 | 118.562100 | 0.121432625 |
| 2023preBPix | GluGluH | In workspace | 132 | 0.000021404460 | 17.96 | 118.562100 | 0.045578129 |
| 2023preBPix | GluGluH | Out workspace | 94 | 0.000035622887 | 17.96 | 118.562100 | 0.075854496 |
| 2023preBPix | VBFH | Input ROOT tree | 127 | 0.000081077831 | 17.96 | 9.257060 | 0.013479740 |
| 2023preBPix | VBFH | Inclusive workspace | 127 | 0.000081077831 | 17.96 | 9.257060 | 0.013479740 |
| 2023preBPix | VBFH | In workspace | 59 | -0.000005408938 | 17.96 | 9.257060 | -0.000899273 |
| 2023preBPix | VBFH | Out workspace | 68 | 0.000086486769 | 17.96 | 9.257060 | 0.014379013 |
| 2023preBPix | VH | Input ROOT tree | 450 | 0.000878283959 | 17.96 | 5.450043 | 0.085968869 |
| 2023preBPix | VH | Inclusive workspace | 450 | 0.000878283959 | 17.96 | 5.450043 | 0.085968869 |
| 2023preBPix | VH | In workspace | 283 | 0.000546749757 | 17.96 | 5.450043 | 0.053517382 |
| 2023preBPix | VH | Out workspace | 167 | 0.000331534202 | 17.96 | 5.450043 | 0.032451487 |
| 2023preBPix | ttH | Input ROOT tree | 84,651 | 0.034267512635 | 17.96 | 1.293900 | 0.796323673 |
| 2023preBPix | ttH | Inclusive workspace | 84,651 | 0.034267512635 | 17.96 | 1.293900 | 0.796323673 |
| 2023preBPix | ttH | In workspace | 77,621 | 0.031388576193 | 17.96 | 1.293900 | 0.729421670 |
| 2023preBPix | ttH | Out workspace | 7,030 | 0.002878936443 | 17.96 | 1.293900 | 0.066902003 |
| 2023preBPix | tHqLep | Input ROOT tree | 20,110 | 0.008902879407 | 17.96 | 0.061576 | 0.009845781 |
| 2023preBPix | tHqLep | Inclusive workspace | 20,110 | 0.008902879407 | 17.96 | 0.061576 | 0.009845781 |
| 2023preBPix | tHqLep | In workspace | 18,764 | 0.008353489231 | 17.96 | 0.061576 | 0.009238205 |
| 2023preBPix | tHqLep | Out workspace | 1,346 | 0.000549390176 | 17.96 | 0.061576 | 0.000607576 |
| 2023preBPix | tHqHad | Input ROOT tree | 43,182 | 0.020740576636 | 17.96 | 0.127424 | 0.047465512 |
| 2023preBPix | tHqHad | Inclusive workspace | 43,182 | 0.020740576636 | 17.96 | 0.127424 | 0.047465512 |
| 2023preBPix | tHqHad | In workspace | 41,778 | 0.020309012413 | 17.96 | 0.127424 | 0.046477863 |
| 2023preBPix | tHqHad | Out workspace | 1,404 | 0.000431564222 | 17.96 | 0.127424 | 0.000987649 |
| 2023preBPix | tHW | Input ROOT tree | 20,679 | 0.032829602319 | 17.96 | 0.039044 | 0.023021110 |
| 2023preBPix | tHW | Inclusive workspace | 20,679 | 0.032829602319 | 17.96 | 0.039044 | 0.023021110 |
| 2023preBPix | tHW | In workspace | 19,223 | 0.030561617826 | 17.96 | 0.039044 | 0.021430731 |
| 2023preBPix | tHW | Out workspace | 1,456 | 0.002267984493 | 17.96 | 0.039044 | 0.001590379 |
| 2023preBPix | bbH | Input ROOT tree | 169 | 0.000360375332 | 17.96 | 1.196063 | 0.007741328 |
| 2023preBPix | bbH | Inclusive workspace | 169 | 0.000360375332 | 17.96 | 1.196063 | 0.007741328 |
| 2023preBPix | bbH | In workspace | 166 | 0.000349833805 | 17.96 | 1.196063 | 0.007514882 |
| 2023preBPix | bbH | Out workspace | 3 | 0.000010541527 | 17.96 | 1.196063 | 0.000226446 |
| 2023postBPix | GluGluH | Input ROOT tree | 117 | 0.000035472062 | 9.68 | 118.562100 | 0.040710616 |
| 2023postBPix | GluGluH | Inclusive workspace | 117 | 0.000035472062 | 9.68 | 118.562100 | 0.040710616 |
| 2023postBPix | GluGluH | In workspace | 78 | 0.000032120878 | 9.68 | 118.562100 | 0.036864525 |
| 2023postBPix | GluGluH | Out workspace | 39 | 0.000003351184 | 9.68 | 118.562100 | 0.003846091 |
| 2023postBPix | VBFH | Input ROOT tree | 64 | -0.000001458333 | 9.68 | 9.257060 | -0.000130679 |
| 2023postBPix | VBFH | Inclusive workspace | 64 | -0.000001458333 | 9.68 | 9.257060 | -0.000130679 |
| 2023postBPix | VBFH | In workspace | 35 | 0.000004703728 | 9.68 | 9.257060 | 0.000421493 |
| 2023postBPix | VBFH | Out workspace | 29 | -0.000006162061 | 9.68 | 9.257060 | -0.000552172 |
| 2023postBPix | VH | Input ROOT tree | 225 | 0.000675989267 | 9.68 | 5.450043 | 0.035662771 |
| 2023postBPix | VH | Inclusive workspace | 225 | 0.000675989267 | 9.68 | 5.450043 | 0.035662771 |
| 2023postBPix | VH | In workspace | 123 | 0.000249435002 | 9.68 | 5.450043 | 0.013159297 |
| 2023postBPix | VH | Out workspace | 102 | 0.000426554264 | 9.68 | 5.450043 | 0.022503474 |
| 2023postBPix | ttH | Input ROOT tree | 48,277 | 0.033584261675 | 9.68 | 1.293900 | 0.420641265 |
| 2023postBPix | ttH | Inclusive workspace | 48,277 | 0.033584261675 | 9.68 | 1.293900 | 0.420641265 |
| 2023postBPix | ttH | In workspace | 44,266 | 0.030939775928 | 9.68 | 1.293900 | 0.387519208 |
| 2023postBPix | ttH | Out workspace | 4,011 | 0.002644485746 | 9.68 | 1.293900 | 0.033122057 |
| 2023postBPix | tHqLep | Input ROOT tree | 7,566 | 0.008561872065 | 9.68 | 0.061576 | 0.005103374 |
| 2023postBPix | tHqLep | Inclusive workspace | 7,566 | 0.008561872065 | 9.68 | 0.061576 | 0.005103374 |
| 2023postBPix | tHqLep | In workspace | 7,124 | 0.008095405139 | 9.68 | 0.061576 | 0.004825333 |
| 2023postBPix | tHqLep | Out workspace | 442 | 0.000466466927 | 9.68 | 0.061576 | 0.000278041 |
| 2023postBPix | tHqHad | Input ROOT tree | 21,879 | 0.020233284953 | 9.68 | 0.127424 | 0.024957022 |
| 2023postBPix | tHqHad | Inclusive workspace | 21,879 | 0.020233284953 | 9.68 | 0.127424 | 0.024957022 |
| 2023postBPix | tHqHad | In workspace | 21,184 | 0.019667906064 | 9.68 | 0.127424 | 0.024259648 |
| 2023postBPix | tHqHad | Out workspace | 695 | 0.000565378889 | 9.68 | 0.127424 | 0.000697374 |
| 2023postBPix | tHW | Input ROOT tree | 10,028 | 0.030934153168 | 9.68 | 0.039044 | 0.011691437 |
| 2023postBPix | tHW | Inclusive workspace | 10,028 | 0.030934153168 | 9.68 | 0.039044 | 0.011691437 |
| 2023postBPix | tHW | In workspace | 9,341 | 0.028746505650 | 9.68 | 0.039044 | 0.010864625 |
| 2023postBPix | tHW | Out workspace | 687 | 0.002187647518 | 9.68 | 0.039044 | 0.000826812 |
| 2023postBPix | bbH | Input ROOT tree | 98 | 0.000434203905 | 9.68 | 1.196063 | 0.005027165 |
| 2023postBPix | bbH | Inclusive workspace | 98 | 0.000434203905 | 9.68 | 1.196063 | 0.005027165 |
| 2023postBPix | bbH | In workspace | 95 | 0.000438659573 | 9.68 | 1.196063 | 0.005078752 |
| 2023postBPix | bbH | Out workspace | 3 | -0.000004455668 | 9.68 | 1.196063 | -0.000051587 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 227 | 227.000000 | 0 |
| Data workspace | 227 | 227.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 116 | 116.000000 | 116 | 116.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 36 | 36.000000 | 36 | 36.000000 |
| Upper sideband | 130 < m ≤ 180 | 75 | 75.000000 | 75 | 75.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 191 | 191.000000 | 191 | 191.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 227 | 227.000000 | 227 | 227.000000 |
| Total | All entries | 227 | 227.000000 | 227 | 227.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/allData.root | Data_13TeV_ttH_had_3 |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/ws/allData.root | Data_13TeV_ttH_had_3 |
