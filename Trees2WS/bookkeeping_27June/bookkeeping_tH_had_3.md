# Category bookkeeping: tH_had_3

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 964 | 0.000309892459 | 118.562100 | 0.608586894 |
| GluGluH | Inclusive workspace | 964 | 0.000309892459 | 118.562100 | 0.608586894 |
| GluGluH | In workspace | 554 | 0.000176711402 | 118.562100 | 0.347180818 |
| GluGluH | Out workspace | 410 | 0.000133181058 | 118.562100 | 0.261406076 |
| VBFH | Input ROOT tree | 1,376 | 0.001913528577 | 9.257060 | 0.285535956 |
| VBFH | Inclusive workspace | 1,376 | 0.001913528577 | 9.257060 | 0.285535956 |
| VBFH | In workspace | 542 | 0.000635438386 | 9.257060 | 0.095038518 |
| VBFH | Out workspace | 834 | 0.001278090191 | 9.257060 | 0.190497438 |
| VH | Input ROOT tree | 1,236 | 0.002368613790 | 5.450043 | 0.202372348 |
| VH | Inclusive workspace | 1,236 | 0.002368613790 | 5.450043 | 0.202372348 |
| VH | In workspace | 859 | 0.001512013529 | 5.450043 | 0.129683402 |
| VH | Out workspace | 377 | 0.000856600261 | 5.450043 | 0.072688946 |
| ttH | Input ROOT tree | 71,929 | 0.025953376938 | 1.293900 | 0.521799821 |
| ttH | Inclusive workspace | 71,929 | 0.025953376938 | 1.293900 | 0.521799821 |
| ttH | In workspace | 64,640 | 0.023400308687 | 1.293900 | 0.470420267 |
| ttH | Out workspace | 7,289 | 0.002553068251 | 1.293900 | 0.051379554 |
| tHqLep | Input ROOT tree | 49,575 | 0.041892140095 | 0.061576 | 0.039952074 |
| tHqLep | Inclusive workspace | 49,575 | 0.041892140095 | 0.061576 | 0.039952074 |
| tHqLep | In workspace | 46,591 | 0.039307934937 | 0.061576 | 0.037422717 |
| tHqLep | Out workspace | 2,984 | 0.002584205158 | 0.061576 | 0.002529356 |
| tHqHad | Input ROOT tree | 128,170 | 0.104235315657 | 0.127424 | 0.207281941 |
| tHqHad | Inclusive workspace | 128,170 | 0.104235315657 | 0.127424 | 0.207281941 |
| tHqHad | In workspace | 123,024 | 0.099813881087 | 0.127424 | 0.198749298 |
| tHqHad | Out workspace | 5,146 | 0.004421434570 | 0.127424 | 0.008532643 |
| tHW | Input ROOT tree | 76,914 | 0.033435040990 | 0.039044 | 0.020207704 |
| tHW | Inclusive workspace | 76,914 | 0.033435040990 | 0.039044 | 0.020207704 |
| tHW | In workspace | 70,714 | 0.030654571602 | 0.039044 | 0.018522302 |
| tHW | Out workspace | 6,200 | 0.002780469388 | 0.039044 | 0.001685402 |
| bbH | Input ROOT tree | 734 | 0.002399676387 | 1.196063 | 0.046232761 |
| bbH | Inclusive workspace | 734 | 0.002399676387 | 1.196063 | 0.046232761 |
| bbH | In workspace | 723 | 0.002347472431 | 1.196063 | 0.045127791 |
| bbH | Out workspace | 11 | 0.000052203956 | 1.196063 | 0.001104970 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 330,898 | 0.212507584894 | 1.931969499 |
| Inclusive workspace | 330,898 | 0.212507584894 | 1.931969499 |
| In workspace | 307,647 | 0.197848332062 | 1.342145113 |
| Out workspace | 23,251 | 0.014659252833 | 0.589824386 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 114 | 0.000065179038 | 7.98 | 118.562100 | 0.061667553 |
| 2022preEE | GluGluH | Inclusive workspace | 114 | 0.000065179038 | 7.98 | 118.562100 | 0.061667553 |
| 2022preEE | GluGluH | In workspace | 69 | 0.000043484536 | 7.98 | 118.562100 | 0.041141831 |
| 2022preEE | GluGluH | Out workspace | 45 | 0.000021694501 | 7.98 | 118.562100 | 0.020525722 |
| 2022preEE | VBFH | Input ROOT tree | 169 | 0.000365329803 | 7.98 | 9.257060 | 0.026987402 |
| 2022preEE | VBFH | Inclusive workspace | 169 | 0.000365329803 | 7.98 | 9.257060 | 0.026987402 |
| 2022preEE | VBFH | In workspace | 73 | 0.000171133199 | 7.98 | 9.257060 | 0.012641839 |
| 2022preEE | VBFH | Out workspace | 96 | 0.000194196604 | 7.98 | 9.257060 | 0.014345563 |
| 2022preEE | VH | Input ROOT tree | 176 | 0.000544350013 | 7.98 | 5.450043 | 0.023674513 |
| 2022preEE | VH | Inclusive workspace | 176 | 0.000544350013 | 7.98 | 5.450043 | 0.023674513 |
| 2022preEE | VH | In workspace | 119 | 0.000336977980 | 7.98 | 5.450043 | 0.014655625 |
| 2022preEE | VH | Out workspace | 57 | 0.000207372033 | 7.98 | 5.450043 | 0.009018888 |
| 2022preEE | ttH | Input ROOT tree | 12,282 | 0.006590364064 | 7.98 | 1.293900 | 0.068047631 |
| 2022preEE | ttH | Inclusive workspace | 12,282 | 0.006590364064 | 7.98 | 1.293900 | 0.068047631 |
| 2022preEE | ttH | In workspace | 11,016 | 0.006029622889 | 7.98 | 1.293900 | 0.062257798 |
| 2022preEE | ttH | Out workspace | 1,266 | 0.000560741175 | 7.98 | 1.293900 | 0.005789833 |
| 2022preEE | tHqLep | Input ROOT tree | 6,951 | 0.011075294071 | 7.98 | 0.061576 | 0.005442162 |
| 2022preEE | tHqLep | Inclusive workspace | 6,951 | 0.011075294071 | 7.98 | 0.061576 | 0.005442162 |
| 2022preEE | tHqLep | In workspace | 6,526 | 0.010562622700 | 7.98 | 0.061576 | 0.005190247 |
| 2022preEE | tHqLep | Out workspace | 425 | 0.000512671371 | 7.98 | 0.061576 | 0.000251916 |
| 2022preEE | tHqHad | Input ROOT tree | 16,485 | 0.025814870132 | 7.98 | 0.127424 | 0.026249670 |
| 2022preEE | tHqHad | Inclusive workspace | 16,485 | 0.025814870132 | 7.98 | 0.127424 | 0.026249670 |
| 2022preEE | tHqHad | In workspace | 15,786 | 0.024693019836 | 7.98 | 0.127424 | 0.025108924 |
| 2022preEE | tHqHad | Out workspace | 699 | 0.001121850296 | 7.98 | 0.127424 | 0.001140746 |
| 2022preEE | tHW | Input ROOT tree | 18,893 | 0.008732528218 | 7.98 | 0.039044 | 0.002720804 |
| 2022preEE | tHW | Inclusive workspace | 18,893 | 0.008732528218 | 7.98 | 0.039044 | 0.002720804 |
| 2022preEE | tHW | In workspace | 17,380 | 0.008026988583 | 7.98 | 0.039044 | 0.002500978 |
| 2022preEE | tHW | Out workspace | 1,513 | 0.000705539635 | 7.98 | 0.039044 | 0.000219826 |
| 2022preEE | bbH | Input ROOT tree | 81 | 0.000547746482 | 7.98 | 1.196063 | 0.005228012 |
| 2022preEE | bbH | Inclusive workspace | 81 | 0.000547746482 | 7.98 | 1.196063 | 0.005228012 |
| 2022preEE | bbH | In workspace | 80 | 0.000533528691 | 7.98 | 1.196063 | 0.005092309 |
| 2022preEE | bbH | Out workspace | 1 | 0.000014217791 | 7.98 | 1.196063 | 0.000135703 |
| 2022postEE | GluGluH | Input ROOT tree | 459 | 0.000092439562 | 26.68 | 118.562100 | 0.292408226 |
| 2022postEE | GluGluH | Inclusive workspace | 459 | 0.000092439562 | 26.68 | 118.562100 | 0.292408226 |
| 2022postEE | GluGluH | In workspace | 268 | 0.000054091798 | 26.68 | 118.562100 | 0.171105166 |
| 2022postEE | GluGluH | Out workspace | 191 | 0.000038347764 | 26.68 | 118.562100 | 0.121303060 |
| 2022postEE | VBFH | Input ROOT tree | 469 | 0.000587020072 | 26.68 | 9.257060 | 0.144981255 |
| 2022postEE | VBFH | Inclusive workspace | 469 | 0.000587020072 | 26.68 | 9.257060 | 0.144981255 |
| 2022postEE | VBFH | In workspace | 188 | 0.000182488263 | 26.68 | 9.257060 | 0.045070652 |
| 2022postEE | VBFH | Out workspace | 281 | 0.000404531809 | 26.68 | 9.257060 | 0.099910603 |
| 2022postEE | VH | Input ROOT tree | 536 | 0.000617367816 | 26.68 | 5.450043 | 0.089769693 |
| 2022postEE | VH | Inclusive workspace | 536 | 0.000617367816 | 26.68 | 5.450043 | 0.089769693 |
| 2022postEE | VH | In workspace | 372 | 0.000382874733 | 26.68 | 5.450043 | 0.055672723 |
| 2022postEE | VH | Out workspace | 164 | 0.000234493082 | 26.68 | 5.450043 | 0.034096970 |
| 2022postEE | ttH | Input ROOT tree | 34,581 | 0.006404601605 | 26.68 | 1.293900 | 0.221094866 |
| 2022postEE | ttH | Inclusive workspace | 34,581 | 0.006404601605 | 26.68 | 1.293900 | 0.221094866 |
| 2022postEE | ttH | In workspace | 31,076 | 0.005801061130 | 26.68 | 1.293900 | 0.200259893 |
| 2022postEE | ttH | Out workspace | 3,505 | 0.000603540475 | 26.68 | 1.293900 | 0.020834973 |
| 2022postEE | tHqLep | Input ROOT tree | 15,548 | 0.010111590234 | 26.68 | 0.061576 | 0.016611874 |
| 2022postEE | tHqLep | Inclusive workspace | 15,548 | 0.010111590234 | 26.68 | 0.061576 | 0.016611874 |
| 2022postEE | tHqLep | In workspace | 14,613 | 0.009448101956 | 26.68 | 0.061576 | 0.015521859 |
| 2022postEE | tHqLep | Out workspace | 935 | 0.000663488278 | 26.68 | 0.061576 | 0.001090015 |
| 2022postEE | tHqHad | Input ROOT tree | 40,957 | 0.026263693331 | 26.68 | 0.127424 | 0.089287906 |
| 2022postEE | tHqHad | Inclusive workspace | 40,957 | 0.026263693331 | 26.68 | 0.127424 | 0.089287906 |
| 2022postEE | tHqHad | In workspace | 39,364 | 0.025327442103 | 26.68 | 0.127424 | 0.086104960 |
| 2022postEE | tHqHad | Out workspace | 1,593 | 0.000936251228 | 26.68 | 0.127424 | 0.003182946 |
| 2022postEE | tHW | Input ROOT tree | 50,041 | 0.008153427135 | 26.68 | 0.039044 | 0.008493375 |
| 2022postEE | tHW | Inclusive workspace | 50,041 | 0.008153427135 | 26.68 | 0.039044 | 0.008493375 |
| 2022postEE | tHW | In workspace | 46,011 | 0.007467444126 | 26.68 | 0.039044 | 0.007778791 |
| 2022postEE | tHW | Out workspace | 4,030 | 0.000685983009 | 26.68 | 0.039044 | 0.000714584 |
| 2022postEE | bbH | Input ROOT tree | 286 | 0.000661102456 | 26.68 | 1.196063 | 0.021096415 |
| 2022postEE | bbH | Inclusive workspace | 286 | 0.000661102456 | 26.68 | 1.196063 | 0.021096415 |
| 2022postEE | bbH | In workspace | 280 | 0.000646406361 | 26.68 | 1.196063 | 0.020627448 |
| 2022postEE | bbH | Out workspace | 6 | 0.000014696095 | 26.68 | 1.196063 | 0.000468967 |
| 2023preBPix | GluGluH | Input ROOT tree | 263 | 0.000081236377 | 17.96 | 118.562100 | 0.172982736 |
| 2023preBPix | GluGluH | Inclusive workspace | 263 | 0.000081236377 | 17.96 | 118.562100 | 0.172982736 |
| 2023preBPix | GluGluH | In workspace | 147 | 0.000044934561 | 17.96 | 118.562100 | 0.095682544 |
| 2023preBPix | GluGluH | Out workspace | 116 | 0.000036301817 | 17.96 | 118.562100 | 0.077300192 |
| 2023preBPix | VBFH | Input ROOT tree | 483 | 0.000357967687 | 17.96 | 9.257060 | 0.059514561 |
| 2023preBPix | VBFH | Inclusive workspace | 483 | 0.000357967687 | 17.96 | 9.257060 | 0.059514561 |
| 2023preBPix | VBFH | In workspace | 189 | 0.000157509765 | 17.96 | 9.257060 | 0.026187069 |
| 2023preBPix | VBFH | Out workspace | 294 | 0.000200457922 | 17.96 | 9.257060 | 0.033327492 |
| 2023preBPix | VH | Input ROOT tree | 342 | 0.000559687031 | 17.96 | 5.450043 | 0.054783718 |
| 2023preBPix | VH | Inclusive workspace | 342 | 0.000559687031 | 17.96 | 5.450043 | 0.054783718 |
| 2023preBPix | VH | In workspace | 236 | 0.000389206882 | 17.96 | 5.450043 | 0.038096649 |
| 2023preBPix | VH | Out workspace | 106 | 0.000170480149 | 17.96 | 5.450043 | 0.016687070 |
| 2023preBPix | ttH | Input ROOT tree | 16,000 | 0.006566845308 | 17.96 | 1.293900 | 0.152603267 |
| 2023preBPix | ttH | Inclusive workspace | 16,000 | 0.006566845308 | 17.96 | 1.293900 | 0.152603267 |
| 2023preBPix | ttH | In workspace | 14,377 | 0.005879836593 | 17.96 | 1.293900 | 0.136638253 |
| 2023preBPix | ttH | Out workspace | 1,623 | 0.000687008715 | 17.96 | 1.293900 | 0.015965014 |
| 2023preBPix | tHqLep | Input ROOT tree | 19,845 | 0.010898269403 | 17.96 | 0.061576 | 0.012052502 |
| 2023preBPix | tHqLep | Inclusive workspace | 19,845 | 0.010898269403 | 17.96 | 0.061576 | 0.012052502 |
| 2023preBPix | tHqLep | In workspace | 18,667 | 0.010215426426 | 17.96 | 0.061576 | 0.011297339 |
| 2023preBPix | tHqLep | Out workspace | 1,178 | 0.000682842977 | 17.96 | 0.061576 | 0.000755163 |
| 2023preBPix | tHqHad | Input ROOT tree | 47,161 | 0.025980172296 | 17.96 | 0.127424 | 0.059456504 |
| 2023preBPix | tHqHad | Inclusive workspace | 47,161 | 0.025980172296 | 17.96 | 0.127424 | 0.059456504 |
| 2023preBPix | tHqHad | In workspace | 45,266 | 0.024753840401 | 17.96 | 0.127424 | 0.056650002 |
| 2023preBPix | tHqHad | Out workspace | 1,895 | 0.001226331895 | 17.96 | 0.127424 | 0.002806502 |
| 2023preBPix | tHW | Input ROOT tree | 5,354 | 0.008472003269 | 17.96 | 0.039044 | 0.005940825 |
| 2023preBPix | tHW | Inclusive workspace | 5,354 | 0.008472003269 | 17.96 | 0.039044 | 0.005940825 |
| 2023preBPix | tHW | In workspace | 4,914 | 0.007772787213 | 17.96 | 0.039044 | 0.005450513 |
| 2023preBPix | tHW | Out workspace | 440 | 0.000699216055 | 17.96 | 0.039044 | 0.000490311 |
| 2023preBPix | bbH | Input ROOT tree | 233 | 0.000618077143 | 17.96 | 1.196063 | 0.013277095 |
| 2023preBPix | bbH | Inclusive workspace | 233 | 0.000618077143 | 17.96 | 1.196063 | 0.013277095 |
| 2023preBPix | bbH | In workspace | 229 | 0.000594787072 | 17.96 | 1.196063 | 0.012776794 |
| 2023preBPix | bbH | Out workspace | 4 | 0.000023290070 | 17.96 | 1.196063 | 0.000500301 |
| 2023postBPix | GluGluH | Input ROOT tree | 128 | 0.000071037483 | 9.68 | 118.562100 | 0.081528379 |
| 2023postBPix | GluGluH | Inclusive workspace | 128 | 0.000071037483 | 9.68 | 118.562100 | 0.081528379 |
| 2023postBPix | GluGluH | In workspace | 70 | 0.000034200507 | 9.68 | 118.562100 | 0.039251276 |
| 2023postBPix | GluGluH | Out workspace | 58 | 0.000036836976 | 9.68 | 118.562100 | 0.042277102 |
| 2023postBPix | VBFH | Input ROOT tree | 255 | 0.000603211015 | 9.68 | 9.257060 | 0.054052738 |
| 2023postBPix | VBFH | Inclusive workspace | 255 | 0.000603211015 | 9.68 | 9.257060 | 0.054052738 |
| 2023postBPix | VBFH | In workspace | 92 | 0.000124307159 | 9.68 | 9.257060 | 0.011138958 |
| 2023postBPix | VBFH | Out workspace | 163 | 0.000478903856 | 9.68 | 9.257060 | 0.042913780 |
| 2023postBPix | VH | Input ROOT tree | 182 | 0.000647208931 | 9.68 | 5.450043 | 0.034144424 |
| 2023postBPix | VH | Inclusive workspace | 182 | 0.000647208931 | 9.68 | 5.450043 | 0.034144424 |
| 2023postBPix | VH | In workspace | 132 | 0.000402953934 | 9.68 | 5.450043 | 0.021258405 |
| 2023postBPix | VH | Out workspace | 50 | 0.000244254997 | 9.68 | 5.450043 | 0.012886018 |
| 2023postBPix | ttH | Input ROOT tree | 9,066 | 0.006391565961 | 9.68 | 1.293900 | 0.080054057 |
| 2023postBPix | ttH | Inclusive workspace | 9,066 | 0.006391565961 | 9.68 | 1.293900 | 0.080054057 |
| 2023postBPix | ttH | In workspace | 8,171 | 0.005689788075 | 9.68 | 1.293900 | 0.071264323 |
| 2023postBPix | ttH | Out workspace | 895 | 0.000701777885 | 9.68 | 1.293900 | 0.008789734 |
| 2023postBPix | tHqLep | Input ROOT tree | 7,231 | 0.009806986388 | 9.68 | 0.061576 | 0.005845535 |
| 2023postBPix | tHqLep | Inclusive workspace | 7,231 | 0.009806986388 | 9.68 | 0.061576 | 0.005845535 |
| 2023postBPix | tHqLep | In workspace | 6,785 | 0.009081783856 | 9.68 | 0.061576 | 0.005413272 |
| 2023postBPix | tHqLep | Out workspace | 446 | 0.000725202532 | 9.68 | 0.061576 | 0.000432263 |
| 2023postBPix | tHqHad | Input ROOT tree | 23,567 | 0.026176579897 | 9.68 | 0.127424 | 0.032287861 |
| 2023postBPix | tHqHad | Inclusive workspace | 23,567 | 0.026176579897 | 9.68 | 0.127424 | 0.032287861 |
| 2023postBPix | tHqHad | In workspace | 22,608 | 0.025039578747 | 9.68 | 0.127424 | 0.030885411 |
| 2023postBPix | tHqHad | Out workspace | 959 | 0.001137001150 | 9.68 | 0.127424 | 0.001402450 |
| 2023postBPix | tHW | Input ROOT tree | 2,626 | 0.008077082367 | 9.68 | 0.039044 | 0.003052700 |
| 2023postBPix | tHW | Inclusive workspace | 2,626 | 0.008077082367 | 9.68 | 0.039044 | 0.003052700 |
| 2023postBPix | tHW | In workspace | 2,409 | 0.007387351679 | 9.68 | 0.039044 | 0.002792019 |
| 2023postBPix | tHW | Out workspace | 217 | 0.000689730688 | 9.68 | 0.039044 | 0.000260681 |
| 2023postBPix | bbH | Input ROOT tree | 134 | 0.000572750307 | 9.68 | 1.196063 | 0.006631240 |
| 2023postBPix | bbH | Inclusive workspace | 134 | 0.000572750307 | 9.68 | 1.196063 | 0.006631240 |
| 2023postBPix | bbH | In workspace | 134 | 0.000572750307 | 9.68 | 1.196063 | 0.006631240 |
| 2023postBPix | bbH | Out workspace | 0 | 0.000000000000 | 9.68 | 1.196063 | 0.000000000 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 190 | 190.000000 | 0 |
| Data workspace | 190 | 190.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 88 | 88.000000 | 88 | 88.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 29 | 29.000000 | 29 | 29.000000 |
| Upper sideband | 130 < m ≤ 180 | 73 | 73.000000 | 73 | 73.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 161 | 161.000000 | 161 | 161.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 190 | 190.000000 | 190 | 190.000000 |
| Total | All entries | 190 | 190.000000 | 190 | 190.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_had_3 |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_had_3 |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_had_3 |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_had_3 |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_had_3 |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_had_3 |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_had_3 |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_had_3 |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_had_3 |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_had_3 |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_had_3 |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_had_3 |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_had_3 |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_had_3 |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_had_3 |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_had_3 |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_had_3 |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_had_3 |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_had_3 |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_had_3 |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_had_3 |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_had_3 |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_had_3 |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_had_3 |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_had_3 |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_had_3 |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_had_3 |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_had_3 |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_had_3 |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_had_3 |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_had_3 |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_had_3 |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_had_3 |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_had_3 |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_had_3 |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_had_3 |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_had_3 |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_had_3 |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_had_3 |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_had_3 |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_had_3 |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_had_3 |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_had_3 |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_had_3 |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_had_3 |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_had_3 |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_had_3 |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_had_3 |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_had_3 |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_had_3 |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_had_3 |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_had_3 |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_had_3 |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_had_3 |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_had_3 |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_had_3 |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_had_3 |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_had_3 |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_had_3 |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_had_3 |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_had_3 |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_had_3 |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_had_3 |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_had_3 |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_had_3 |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_had_3 |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_had_3 |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_had_3 |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_had_3 |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_had_3 |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_had_3 |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_had_3 |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_had_3 |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_had_3 |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_had_3 |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_had_3 |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_had_3 |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_had_3 |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_had_3 |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_had_3 |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_had_3 |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_had_3 |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_had_3 |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_had_3 |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_had_3 |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_had_3 |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_had_3 |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_had_3 |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_had_3 |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_had_3 |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_had_3 |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_had_3 |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_had_3 |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_had_3 |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_had_3 |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_had_3 |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_had_3 |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_had_3 |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_had_3 |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_had_3 |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_had_3 |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_had_3 |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_had_3 |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_had_3 |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_had_3 |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_had_3 |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_had_3 |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_had_3 |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_had_3 |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_had_3 |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_had_3 |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_had_3 |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_had_3 |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_had_3 |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_had_3 |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_had_3 |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_had_3 |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_had_3 |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_had_3 |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_had_3 |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_had_3 |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_had_3 |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_had_3 |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_had_3 |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_had_3 |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_had_3 |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_had_3 |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_had_3 |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/allData.root | Data_13TeV_tH_had_3 |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/ws/allData.root | Data_13TeV_tH_had_3 |
