# Category bookkeeping: tH_lep_2

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 32 | 0.000012198516 | 118.562100 | 0.055216837 |
| GluGluH | Inclusive workspace | 32 | 0.000012198516 | 118.562100 | 0.055216837 |
| GluGluH | In workspace | 20 | 0.000001299724 | 118.562100 | 0.013966050 |
| GluGluH | Out workspace | 12 | 0.000010898792 | 118.562100 | 0.041250786 |
| VBFH | Input ROOT tree | 74 | 0.000087050549 | 9.257060 | 0.033809832 |
| VBFH | Inclusive workspace | 74 | 0.000087050549 | 9.257060 | 0.033809832 |
| VBFH | In workspace | 24 | 0.000046608554 | 9.257060 | 0.006131391 |
| VBFH | Out workspace | 50 | 0.000040441995 | 9.257060 | 0.027678441 |
| VH | Input ROOT tree | 5,485 | 0.003008606964 | 5.450043 | 0.591388063 |
| VH | Inclusive workspace | 5,485 | 0.003008606964 | 5.450043 | 0.591388063 |
| VH | In workspace | 595 | 0.000224538323 | 5.450043 | 0.058444737 |
| VH | Out workspace | 4,890 | 0.002784068642 | 5.450043 | 0.532943325 |
| ttH | Input ROOT tree | 25,889 | 0.014913680616 | 1.293900 | 0.754608514 |
| ttH | Inclusive workspace | 25,889 | 0.014913680616 | 1.293900 | 0.754608514 |
| ttH | In workspace | 22,223 | 0.012848666052 | 1.293900 | 0.668420532 |
| ttH | Out workspace | 3,666 | 0.002065014564 | 1.293900 | 0.086187982 |
| tHqLep | Input ROOT tree | 110,072 | 0.093293591014 | 0.061576 | 0.215131704 |
| tHqLep | Inclusive workspace | 110,072 | 0.093293591014 | 0.061576 | 0.215131704 |
| tHqLep | In workspace | 100,145 | 0.083933004514 | 0.061576 | 0.193702608 |
| tHqLep | Out workspace | 9,927 | 0.009360586500 | 0.061576 | 0.021429096 |
| tHqHad | Input ROOT tree | 1,998 | 0.001347400295 | 0.127424 | 0.005793872 |
| tHqHad | Inclusive workspace | 1,998 | 0.001347400295 | 0.127424 | 0.005793872 |
| tHqHad | In workspace | 1,884 | 0.001271368362 | 0.127424 | 0.005615496 |
| tHqHad | Out workspace | 114 | 0.000076031933 | 0.127424 | 0.000178376 |
| tHW | Input ROOT tree | 33,977 | 0.022942097516 | 0.039044 | 0.035831664 |
| tHW | Inclusive workspace | 33,977 | 0.022942097516 | 0.039044 | 0.035831664 |
| tHW | In workspace | 28,874 | 0.019250519355 | 0.039044 | 0.030832082 |
| tHW | Out workspace | 5,103 | 0.003691578161 | 0.039044 | 0.004999583 |
| bbH | Input ROOT tree | 96 | 0.000128442872 | 1.196063 | 0.007532767 |
| bbH | Inclusive workspace | 96 | 0.000128442872 | 1.196063 | 0.007532767 |
| bbH | In workspace | 93 | 0.000127559336 | 1.196063 | 0.007504332 |
| bbH | Out workspace | 3 | 0.000000883535 | 1.196063 | 0.000028435 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 177,623 | 0.135733068342 | 1.699313252 |
| Inclusive workspace | 177,623 | 0.135733068342 | 1.699313252 |
| In workspace | 153,858 | 0.117703564220 | 0.984617228 |
| Out workspace | 23,765 | 0.018029504122 | 0.714696024 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 3 | -0.000000601736 | 7.98 | 118.562100 | -0.000569318 |
| 2022preEE | GluGluH | Inclusive workspace | 3 | -0.000000601736 | 7.98 | 118.562100 | -0.000569318 |
| 2022preEE | GluGluH | In workspace | 3 | -0.000000601736 | 7.98 | 118.562100 | -0.000569318 |
| 2022preEE | GluGluH | Out workspace | 0 | 0.000000000000 | 7.98 | 118.562100 | 0.000000000 |
| 2022preEE | VBFH | Input ROOT tree | 1 | 0.000014887625 | 7.98 | 9.257060 | 0.001099769 |
| 2022preEE | VBFH | Inclusive workspace | 1 | 0.000014887625 | 7.98 | 9.257060 | 0.001099769 |
| 2022preEE | VBFH | In workspace | 1 | 0.000014887625 | 7.98 | 9.257060 | 0.001099769 |
| 2022preEE | VBFH | Out workspace | 0 | 0.000000000000 | 7.98 | 9.257060 | 0.000000000 |
| 2022preEE | VH | Input ROOT tree | 152 | 0.000579460777 | 7.98 | 5.450043 | 0.025201527 |
| 2022preEE | VH | Inclusive workspace | 152 | 0.000579460777 | 7.98 | 5.450043 | 0.025201527 |
| 2022preEE | VH | In workspace | 12 | 0.000029486310 | 7.98 | 5.450043 | 0.001282399 |
| 2022preEE | VH | Out workspace | 140 | 0.000549974467 | 7.98 | 5.450043 | 0.023919128 |
| 2022preEE | ttH | Input ROOT tree | 5,515 | 0.002936942656 | 7.98 | 1.293900 | 0.030324879 |
| 2022preEE | ttH | Inclusive workspace | 5,515 | 0.002936942656 | 7.98 | 1.293900 | 0.030324879 |
| 2022preEE | ttH | In workspace | 4,707 | 0.002490615320 | 7.98 | 1.293900 | 0.025716405 |
| 2022preEE | ttH | Out workspace | 808 | 0.000446327336 | 7.98 | 1.293900 | 0.004608473 |
| 2022preEE | tHqLep | Input ROOT tree | 11,524 | 0.017099030446 | 7.98 | 0.061576 | 0.008402098 |
| 2022preEE | tHqLep | Inclusive workspace | 11,524 | 0.017099030446 | 7.98 | 0.061576 | 0.008402098 |
| 2022preEE | tHqLep | In workspace | 10,420 | 0.015225116457 | 7.98 | 0.061576 | 0.007481296 |
| 2022preEE | tHqLep | Out workspace | 1,104 | 0.001873913989 | 7.98 | 0.061576 | 0.000920801 |
| 2022preEE | tHqHad | Input ROOT tree | 164 | 0.000263821401 | 7.98 | 0.127424 | 0.000268265 |
| 2022preEE | tHqHad | Inclusive workspace | 164 | 0.000263821401 | 7.98 | 0.127424 | 0.000268265 |
| 2022preEE | tHqHad | In workspace | 152 | 0.000224347421 | 7.98 | 0.127424 | 0.000228126 |
| 2022preEE | tHqHad | Out workspace | 12 | 0.000039473980 | 7.98 | 0.127424 | 0.000040139 |
| 2022preEE | tHW | Input ROOT tree | 8,712 | 0.004101320506 | 7.98 | 0.039044 | 0.001277853 |
| 2022preEE | tHW | Inclusive workspace | 8,712 | 0.004101320506 | 7.98 | 0.039044 | 0.001277853 |
| 2022preEE | tHW | In workspace | 7,198 | 0.003367066041 | 7.98 | 0.039044 | 0.001049081 |
| 2022preEE | tHW | Out workspace | 1,514 | 0.000734254464 | 7.98 | 0.039044 | 0.000228772 |
| 2022preEE | bbH | Input ROOT tree | 1 | 0.000005975200 | 7.98 | 1.196063 | 0.000057031 |
| 2022preEE | bbH | Inclusive workspace | 1 | 0.000005975200 | 7.98 | 1.196063 | 0.000057031 |
| 2022preEE | bbH | In workspace | 1 | 0.000005975200 | 7.98 | 1.196063 | 0.000057031 |
| 2022preEE | bbH | Out workspace | 0 | 0.000000000000 | 7.98 | 1.196063 | 0.000000000 |
| 2022postEE | GluGluH | Input ROOT tree | 4 | 0.000004311197 | 26.67 | 118.562100 | 0.013632227 |
| 2022postEE | GluGluH | Inclusive workspace | 4 | 0.000004311197 | 26.67 | 118.562100 | 0.013632227 |
| 2022postEE | GluGluH | In workspace | 2 | 0.000001626850 | 26.67 | 118.562100 | 0.005144182 |
| 2022postEE | GluGluH | Out workspace | 2 | 0.000002684348 | 26.67 | 118.562100 | 0.008488044 |
| 2022postEE | VBFH | Input ROOT tree | 30 | 0.000041945686 | 26.67 | 9.257060 | 0.010355794 |
| 2022postEE | VBFH | Inclusive workspace | 30 | 0.000041945686 | 26.67 | 9.257060 | 0.010355794 |
| 2022postEE | VBFH | In workspace | 9 | 0.000012241578 | 26.67 | 9.257060 | 0.003022272 |
| 2022postEE | VBFH | Out workspace | 21 | 0.000029704109 | 26.67 | 9.257060 | 0.007333522 |
| 2022postEE | VH | Input ROOT tree | 449 | 0.000677178493 | 26.67 | 5.450043 | 0.098429686 |
| 2022postEE | VH | Inclusive workspace | 449 | 0.000677178493 | 26.67 | 5.450043 | 0.098429686 |
| 2022postEE | VH | In workspace | 39 | 0.000060448743 | 26.67 | 5.450043 | 0.008786385 |
| 2022postEE | VH | Out workspace | 410 | 0.000616729749 | 26.67 | 5.450043 | 0.089643301 |
| 2022postEE | ttH | Input ROOT tree | 5,559 | 0.002655582840 | 26.67 | 1.293900 | 0.091639684 |
| 2022postEE | ttH | Inclusive workspace | 5,559 | 0.002655582840 | 26.67 | 1.293900 | 0.091639684 |
| 2022postEE | ttH | In workspace | 4,674 | 0.002235299569 | 26.67 | 1.293900 | 0.077136417 |
| 2022postEE | ttH | Out workspace | 885 | 0.000420283271 | 26.67 | 1.293900 | 0.014503267 |
| 2022postEE | tHqLep | Input ROOT tree | 22,730 | 0.015788197055 | 26.67 | 0.061576 | 0.025927993 |
| 2022postEE | tHqLep | Inclusive workspace | 22,730 | 0.015788197055 | 26.67 | 0.061576 | 0.025927993 |
| 2022postEE | tHqLep | In workspace | 20,600 | 0.014070216968 | 26.67 | 0.061576 | 0.023106659 |
| 2022postEE | tHqLep | Out workspace | 2,130 | 0.001717980087 | 26.67 | 0.061576 | 0.002821334 |
| 2022postEE | tHqHad | Input ROOT tree | 497 | 0.000231642852 | 26.67 | 0.127424 | 0.000787214 |
| 2022postEE | tHqHad | Inclusive workspace | 497 | 0.000231642852 | 26.67 | 0.127424 | 0.000787214 |
| 2022postEE | tHqHad | In workspace | 467 | 0.000227734797 | 26.67 | 0.127424 | 0.000773933 |
| 2022postEE | tHqHad | Out workspace | 30 | 0.000003908055 | 26.67 | 0.127424 | 0.000013281 |
| 2022postEE | tHW | Input ROOT tree | 8,792 | 0.003966237495 | 26.67 | 0.039044 | 0.004130057 |
| 2022postEE | tHW | Inclusive workspace | 8,792 | 0.003966237495 | 26.67 | 0.039044 | 0.004130057 |
| 2022postEE | tHW | In workspace | 7,326 | 0.003290893790 | 26.67 | 0.039044 | 0.003426819 |
| 2022postEE | tHW | Out workspace | 1,466 | 0.000675343705 | 26.67 | 0.039044 | 0.000703238 |
| 2022postEE | bbH | Input ROOT tree | 11 | 0.000025804331 | 26.67 | 1.196063 | 0.000823132 |
| 2022postEE | bbH | Inclusive workspace | 11 | 0.000025804331 | 26.67 | 1.196063 | 0.000823132 |
| 2022postEE | bbH | In workspace | 10 | 0.000024923318 | 26.67 | 1.196063 | 0.000795029 |
| 2022postEE | bbH | Out workspace | 1 | 0.000000881014 | 26.67 | 1.196063 | 0.000028103 |
| 2023preBPix | GluGluH | Input ROOT tree | 11 | 0.000003422067 | 18.06 | 118.562100 | 0.007328654 |
| 2023preBPix | GluGluH | Inclusive workspace | 11 | 0.000003422067 | 18.06 | 118.562100 | 0.007328654 |
| 2023preBPix | GluGluH | In workspace | 6 | 0.000001434051 | 18.06 | 118.562100 | 0.003071144 |
| 2023preBPix | GluGluH | Out workspace | 5 | 0.000001988016 | 18.06 | 118.562100 | 0.004257510 |
| 2023preBPix | VBFH | Input ROOT tree | 13 | 0.000003846730 | 18.06 | 9.257060 | 0.000643213 |
| 2023preBPix | VBFH | Inclusive workspace | 13 | 0.000003846730 | 18.06 | 9.257060 | 0.000643213 |
| 2023preBPix | VBFH | In workspace | 4 | 0.000003837256 | 18.06 | 9.257060 | 0.000641629 |
| 2023preBPix | VBFH | Out workspace | 9 | 0.000000009474 | 18.06 | 9.257060 | 0.000001584 |
| 2023preBPix | VH | Input ROOT tree | 315 | 0.000653484869 | 18.06 | 5.450043 | 0.064331747 |
| 2023preBPix | VH | Inclusive workspace | 315 | 0.000653484869 | 18.06 | 5.450043 | 0.064331747 |
| 2023preBPix | VH | In workspace | 24 | 0.000046082835 | 18.06 | 5.450043 | 0.004536584 |
| 2023preBPix | VH | Out workspace | 291 | 0.000607402034 | 18.06 | 5.450043 | 0.059795163 |
| 2023preBPix | ttH | Input ROOT tree | 4,654 | 0.002789093659 | 18.06 | 1.293900 | 0.065185904 |
| 2023preBPix | ttH | Inclusive workspace | 4,654 | 0.002789093659 | 18.06 | 1.293900 | 0.065185904 |
| 2023preBPix | ttH | In workspace | 3,954 | 0.002388094328 | 18.06 | 1.293900 | 0.055813862 |
| 2023preBPix | ttH | Out workspace | 700 | 0.000400999331 | 18.06 | 1.293900 | 0.009372042 |
| 2023preBPix | tHqLep | Input ROOT tree | 2,858 | 0.020188144659 | 18.06 | 0.061576 | 0.022454306 |
| 2023preBPix | tHqLep | Inclusive workspace | 2,858 | 0.020188144659 | 18.06 | 0.061576 | 0.022454306 |
| 2023preBPix | tHqLep | In workspace | 2,549 | 0.018443393893 | 18.06 | 0.061576 | 0.020513703 |
| 2023preBPix | tHqLep | Out workspace | 309 | 0.001744750766 | 18.06 | 0.061576 | 0.001940603 |
| 2023preBPix | tHqHad | Input ROOT tree | 415 | 0.000333920055 | 18.06 | 0.127424 | 0.000768570 |
| 2023preBPix | tHqHad | Inclusive workspace | 415 | 0.000333920055 | 18.06 | 0.127424 | 0.000768570 |
| 2023preBPix | tHqHad | In workspace | 404 | 0.000331904731 | 18.06 | 0.127424 | 0.000763931 |
| 2023preBPix | tHqHad | Out workspace | 11 | 0.000002015324 | 18.06 | 0.127424 | 0.000004639 |
| 2023preBPix | tHW | Input ROOT tree | 2,676 | 0.004543407251 | 18.06 | 0.039044 | 0.003204246 |
| 2023preBPix | tHW | Inclusive workspace | 2,676 | 0.004543407251 | 18.06 | 0.039044 | 0.003204246 |
| 2023preBPix | tHW | In workspace | 2,230 | 0.003753491437 | 18.06 | 0.039044 | 0.002647156 |
| 2023preBPix | tHW | Out workspace | 446 | 0.000789915814 | 18.06 | 0.039044 | 0.000557090 |
| 2023preBPix | bbH | Input ROOT tree | 16 | 0.000041929590 | 18.06 | 1.196063 | 0.000905867 |
| 2023preBPix | bbH | Inclusive workspace | 16 | 0.000041929590 | 18.06 | 1.196063 | 0.000905867 |
| 2023preBPix | bbH | In workspace | 16 | 0.000041929590 | 18.06 | 1.196063 | 0.000905867 |
| 2023preBPix | bbH | Out workspace | 0 | 0.000000000000 | 18.06 | 1.196063 | 0.000000000 |
| 2023postBPix | GluGluH | Input ROOT tree | 3 | 0.000002627099 | 9.69 | 118.562100 | 0.003019122 |
| 2023postBPix | GluGluH | Inclusive workspace | 3 | 0.000002627099 | 9.69 | 118.562100 | 0.003019122 |
| 2023postBPix | GluGluH | In workspace | 1 | -0.000001803228 | 9.69 | 118.562100 | -0.002072310 |
| 2023postBPix | GluGluH | Out workspace | 2 | 0.000004430328 | 9.69 | 118.562100 | 0.005091432 |
| 2023postBPix | VBFH | Input ROOT tree | 7 | 0.000005526659 | 9.69 | 9.257060 | 0.000495900 |
| 2023postBPix | VBFH | Inclusive workspace | 7 | 0.000005526659 | 9.69 | 9.257060 | 0.000495900 |
| 2023postBPix | VBFH | In workspace | 3 | 0.000015680695 | 9.69 | 9.257060 | 0.001407008 |
| 2023postBPix | VBFH | Out workspace | 4 | -0.000010154036 | 9.69 | 9.257060 | -0.000911108 |
| 2023postBPix | VH | Input ROOT tree | 165 | 0.000466359619 | 9.69 | 5.450043 | 0.024636504 |
| 2023postBPix | VH | Inclusive workspace | 165 | 0.000466359619 | 9.69 | 5.450043 | 0.024636504 |
| 2023postBPix | VH | In workspace | 10 | 0.000016846348 | 9.69 | 5.450043 | 0.000889947 |
| 2023postBPix | VH | Out workspace | 155 | 0.000449513270 | 9.69 | 5.450043 | 0.023746557 |
| 2023postBPix | ttH | Input ROOT tree | 5,752 | 0.002789192675 | 9.69 | 1.293900 | 0.034981421 |
| 2023postBPix | ttH | Inclusive workspace | 5,752 | 0.002789192675 | 9.69 | 1.293900 | 0.034981421 |
| 2023postBPix | ttH | In workspace | 4,916 | 0.002359521633 | 9.69 | 1.293900 | 0.029592584 |
| 2023postBPix | ttH | Out workspace | 836 | 0.000429671042 | 9.69 | 1.293900 | 0.005388837 |
| 2023postBPix | tHqLep | Input ROOT tree | 17,704 | 0.018456857362 | 9.69 | 0.061576 | 0.011016137 |
| 2023postBPix | tHqLep | Inclusive workspace | 17,704 | 0.018456857362 | 9.69 | 0.061576 | 0.011016137 |
| 2023postBPix | tHqLep | In workspace | 16,022 | 0.016594531914 | 9.69 | 0.061576 | 0.009904591 |
| 2023postBPix | tHqLep | Out workspace | 1,682 | 0.001862325449 | 9.69 | 0.061576 | 0.001111545 |
| 2023postBPix | tHqHad | Input ROOT tree | 243 | 0.000257352679 | 9.69 | 0.127424 | 0.000317861 |
| 2023postBPix | tHqHad | Inclusive workspace | 243 | 0.000257352679 | 9.69 | 0.127424 | 0.000317861 |
| 2023postBPix | tHqHad | In workspace | 232 | 0.000233174386 | 9.69 | 0.127424 | 0.000287998 |
| 2023postBPix | tHqHad | Out workspace | 11 | 0.000024178294 | 9.69 | 0.127424 | 0.000029863 |
| 2023postBPix | tHW | Input ROOT tree | 1,335 | 0.004376336850 | 9.69 | 0.039044 | 0.001656240 |
| 2023postBPix | tHW | Inclusive workspace | 1,335 | 0.004376336850 | 9.69 | 0.039044 | 0.001656240 |
| 2023postBPix | tHW | In workspace | 1,101 | 0.003636822351 | 9.69 | 0.039044 | 0.001376368 |
| 2023postBPix | tHW | Out workspace | 234 | 0.000739514499 | 9.69 | 0.039044 | 0.000279872 |
| 2023postBPix | bbH | Input ROOT tree | 4 | 0.000012101551 | 9.69 | 1.196063 | 0.000140299 |
| 2023postBPix | bbH | Inclusive workspace | 4 | 0.000012101551 | 9.69 | 1.196063 | 0.000140299 |
| 2023postBPix | bbH | In workspace | 4 | 0.000012101551 | 9.69 | 1.196063 | 0.000140299 |
| 2023postBPix | bbH | Out workspace | 0 | 0.000000000000 | 9.69 | 1.196063 | 0.000000000 |
| 2024 | GluGluH | Input ROOT tree | 11 | 0.000002439889 | 109.95 | 118.562100 | 0.031806152 |
| 2024 | GluGluH | Inclusive workspace | 11 | 0.000002439889 | 109.95 | 118.562100 | 0.031806152 |
| 2024 | GluGluH | In workspace | 8 | 0.000000643788 | 109.95 | 118.562100 | 0.008392352 |
| 2024 | GluGluH | Out workspace | 3 | 0.000001796101 | 109.95 | 118.562100 | 0.023413800 |
| 2024 | VBFH | Input ROOT tree | 23 | 0.000020843850 | 109.95 | 9.257060 | 0.021215157 |
| 2024 | VBFH | Inclusive workspace | 23 | 0.000020843850 | 109.95 | 9.257060 | 0.021215157 |
| 2024 | VBFH | In workspace | 7 | -0.000000038599 | 109.95 | 9.257060 | -0.000039286 |
| 2024 | VBFH | Out workspace | 16 | 0.000020882449 | 109.95 | 9.257060 | 0.021254443 |
| 2024 | VH | Input ROOT tree | 4,404 | 0.000632123207 | 109.95 | 5.450043 | 0.378788598 |
| 2024 | VH | Inclusive workspace | 4,404 | 0.000632123207 | 109.95 | 5.450043 | 0.378788598 |
| 2024 | VH | In workspace | 510 | 0.000071674086 | 109.95 | 5.450043 | 0.042949422 |
| 2024 | VH | Out workspace | 3,894 | 0.000560449121 | 109.95 | 5.450043 | 0.335839175 |
| 2024 | ttH | Input ROOT tree | 4,409 | 0.003742868785 | 109.95 | 1.293900 | 0.532476626 |
| 2024 | ttH | Inclusive workspace | 4,409 | 0.003742868785 | 109.95 | 1.293900 | 0.532476626 |
| 2024 | ttH | In workspace | 3,972 | 0.003375135202 | 109.95 | 1.293900 | 0.480161264 |
| 2024 | ttH | Out workspace | 437 | 0.000367733583 | 109.95 | 1.293900 | 0.052315363 |
| 2024 | tHqLep | Input ROOT tree | 55,256 | 0.021761361491 | 109.95 | 0.061576 | 0.147331171 |
| 2024 | tHqLep | Inclusive workspace | 55,256 | 0.021761361491 | 109.95 | 0.061576 | 0.147331171 |
| 2024 | tHqLep | In workspace | 50,554 | 0.019599745282 | 109.95 | 0.061576 | 0.132696358 |
| 2024 | tHqLep | Out workspace | 4,702 | 0.002161616208 | 109.95 | 0.061576 | 0.014634813 |
| 2024 | tHqHad | Input ROOT tree | 679 | 0.000260663307 | 109.95 | 0.127424 | 0.003651961 |
| 2024 | tHqHad | Inclusive workspace | 679 | 0.000260663307 | 109.95 | 0.127424 | 0.003651961 |
| 2024 | tHqHad | In workspace | 629 | 0.000254207027 | 109.95 | 0.127424 | 0.003561507 |
| 2024 | tHqHad | Out workspace | 50 | 0.000006456280 | 109.95 | 0.127424 | 0.000090454 |
| 2024 | tHW | Input ROOT tree | 12,462 | 0.005954795415 | 109.95 | 0.039044 | 0.025563269 |
| 2024 | tHW | Inclusive workspace | 12,462 | 0.005954795415 | 109.95 | 0.039044 | 0.025563269 |
| 2024 | tHW | In workspace | 11,019 | 0.005202245737 | 109.95 | 0.039044 | 0.022332657 |
| 2024 | tHW | Out workspace | 1,443 | 0.000752549679 | 109.95 | 0.039044 | 0.003230611 |
| 2024 | bbH | Input ROOT tree | 64 | 0.000042632199 | 109.95 | 1.196063 | 0.005606438 |
| 2024 | bbH | Inclusive workspace | 64 | 0.000042632199 | 109.95 | 1.196063 | 0.005606438 |
| 2024 | bbH | In workspace | 62 | 0.000042629678 | 109.95 | 1.196063 | 0.005606106 |
| 2024 | bbH | Out workspace | 2 | 0.000000002522 | 109.95 | 1.196063 | 0.000000332 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 101 | 101.000000 | 0 |
| Data workspace | 101 | 101.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 45 | 45.000000 | 45 | 45.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 15 | 15.000000 | 15 | 15.000000 |
| Upper sideband | 130 < m ≤ 180 | 41 | 41.000000 | 41 | 41.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 86 | 86.000000 | 86 | 86.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 101 | 101.000000 | 101 | 101.000000 |
| Total | All entries | 101 | 101.000000 | 101 | 101.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| GluGluH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/allData.root | Data_13TeV_tH_lep_2 |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/ws/allData.root | Data_13TeV_tH_lep_2 |
