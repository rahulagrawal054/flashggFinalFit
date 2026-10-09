# Category bookkeeping: bkg_had

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 278,601 | 0.144996645375 | 118.562100 | 267.504740041 |
| GluGluH | Inclusive workspace | 278,601 | 0.144996645375 | 118.562100 | 267.504740041 |
| GluGluH | In workspace | 22,697 | 0.008405271929 | 118.562100 | 15.095755343 |
| GluGluH | Out workspace | 255,904 | 0.136591373446 | 118.562100 | 252.408984698 |
| VBFH | Input ROOT tree | 181,837 | 0.267265940353 | 9.257060 | 38.477868712 |
| VBFH | Inclusive workspace | 181,837 | 0.267265940353 | 9.257060 | 38.477868712 |
| VBFH | In workspace | 12,888 | 0.016094386891 | 9.257060 | 2.269844848 |
| VBFH | Out workspace | 168,949 | 0.251171553462 | 9.257060 | 36.208023865 |
| VH | Input ROOT tree | 116,965 | 0.321159321471 | 5.450043 | 27.143337217 |
| VH | Inclusive workspace | 116,965 | 0.321159321471 | 5.450043 | 27.143337217 |
| VH | In workspace | 16,974 | 0.044338610662 | 5.450043 | 3.741335212 |
| VH | Out workspace | 99,991 | 0.276820710809 | 5.450043 | 23.402002006 |
| ttH | Input ROOT tree | 763,665 | 0.289877499227 | 1.293900 | 5.809665359 |
| ttH | Inclusive workspace | 763,665 | 0.289877499227 | 1.293900 | 5.809665359 |
| ttH | In workspace | 636,466 | 0.242872136978 | 1.293900 | 4.863937745 |
| ttH | Out workspace | 127,199 | 0.047005362249 | 1.293900 | 0.945727614 |
| tHqLep | Input ROOT tree | 325,789 | 0.272641068592 | 0.061576 | 0.259603995 |
| tHqLep | Inclusive workspace | 325,789 | 0.272641068592 | 0.061576 | 0.259603995 |
| tHqLep | In workspace | 278,023 | 0.231958971029 | 0.061576 | 0.220777660 |
| tHqLep | Out workspace | 47,766 | 0.040682097564 | 0.061576 | 0.038826336 |
| tHqHad | Input ROOT tree | 691,748 | 0.557259627082 | 0.127424 | 1.095705780 |
| tHqHad | Inclusive workspace | 691,748 | 0.557259627082 | 0.127424 | 1.095705780 |
| tHqHad | In workspace | 579,476 | 0.462795917533 | 0.127424 | 0.911232717 |
| tHqHad | Out workspace | 112,272 | 0.094463709549 | 0.127424 | 0.184473063 |
| tHW | Input ROOT tree | 829,337 | 0.398634659630 | 0.039044 | 0.241659844 |
| tHW | Inclusive workspace | 829,337 | 0.398634659630 | 0.039044 | 0.241659844 |
| tHW | In workspace | 659,756 | 0.314806123561 | 0.039044 | 0.190773573 |
| tHW | Out workspace | 169,581 | 0.083828536069 | 0.039044 | 0.050886271 |
| bbH | Input ROOT tree | 55,135 | 0.217283241772 | 1.196063 | 4.017783865 |
| bbH | Inclusive workspace | 55,135 | 0.217283241772 | 1.196063 | 4.017783865 |
| bbH | In workspace | 41,603 | 0.152396377672 | 1.196063 | 2.821252624 |
| bbH | Out workspace | 13,532 | 0.064886864100 | 1.196063 | 1.196531240 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 3,243,077 | 2.469118003504 | 344.550364813 |
| Inclusive workspace | 3,243,077 | 2.469118003504 | 344.550364813 |
| In workspace | 2,247,883 | 1.473667796255 | 30.114909720 |
| Out workspace | 995,194 | 0.995450207249 | 314.435455093 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 37,867 | 0.030409353050 | 7.98 | 118.562100 | 28.771066123 |
| 2022preEE | GluGluH | Inclusive workspace | 37,867 | 0.030409353050 | 7.98 | 118.562100 | 28.771066123 |
| 2022preEE | GluGluH | In workspace | 3,144 | 0.002203699714 | 7.98 | 118.562100 | 2.084976622 |
| 2022preEE | GluGluH | Out workspace | 34,723 | 0.028205653336 | 7.98 | 118.562100 | 26.686089501 |
| 2022preEE | VBFH | Input ROOT tree | 19,688 | 0.057843557911 | 7.98 | 9.257060 | 4.272981064 |
| 2022preEE | VBFH | Inclusive workspace | 19,688 | 0.057843557911 | 7.98 | 9.257060 | 4.272981064 |
| 2022preEE | VBFH | In workspace | 1,386 | 0.004112711890 | 7.98 | 9.257060 | 0.303811533 |
| 2022preEE | VBFH | Out workspace | 18,302 | 0.053730846021 | 7.98 | 9.257060 | 3.969169530 |
| 2022preEE | VH | Input ROOT tree | 15,489 | 0.074779235218 | 7.98 | 5.450043 | 3.252249379 |
| 2022preEE | VH | Inclusive workspace | 15,489 | 0.074779235218 | 7.98 | 5.450043 | 3.252249379 |
| 2022preEE | VH | In workspace | 2,360 | 0.011382133607 | 7.98 | 5.450043 | 0.495024278 |
| 2022preEE | VH | Out workspace | 13,129 | 0.063397101611 | 7.98 | 5.450043 | 2.757225100 |
| 2022preEE | ttH | Input ROOT tree | 128,364 | 0.071009959396 | 7.98 | 1.293900 | 0.733200696 |
| 2022preEE | ttH | Inclusive workspace | 128,364 | 0.071009959396 | 7.98 | 1.293900 | 0.733200696 |
| 2022preEE | ttH | In workspace | 106,634 | 0.060218924339 | 7.98 | 1.293900 | 0.621779784 |
| 2022preEE | ttH | Out workspace | 21,730 | 0.010791035058 | 7.98 | 1.293900 | 0.111420912 |
| 2022preEE | tHqLep | Input ROOT tree | 43,451 | 0.067119827002 | 7.98 | 0.061576 | 0.032981246 |
| 2022preEE | tHqLep | Inclusive workspace | 43,451 | 0.067119827002 | 7.98 | 0.061576 | 0.032981246 |
| 2022preEE | tHqLep | In workspace | 37,073 | 0.057578472505 | 7.98 | 0.061576 | 0.028292829 |
| 2022preEE | tHqLep | Out workspace | 6,378 | 0.009541354497 | 7.98 | 0.061576 | 0.004688417 |
| 2022preEE | tHqHad | Input ROOT tree | 85,932 | 0.139890153073 | 7.98 | 0.127424 | 0.142246323 |
| 2022preEE | tHqHad | Inclusive workspace | 85,932 | 0.139890153073 | 7.98 | 0.127424 | 0.142246323 |
| 2022preEE | tHqHad | In workspace | 71,898 | 0.116290045763 | 7.98 | 0.127424 | 0.118248719 |
| 2022preEE | tHqHad | Out workspace | 14,034 | 0.023600107310 | 7.98 | 0.127424 | 0.023997604 |
| 2022preEE | tHW | Input ROOT tree | 199,093 | 0.096114250442 | 7.98 | 0.039044 | 0.029946425 |
| 2022preEE | tHW | Inclusive workspace | 199,093 | 0.096114250442 | 7.98 | 0.039044 | 0.029946425 |
| 2022preEE | tHW | In workspace | 157,974 | 0.076320012669 | 7.98 | 0.039044 | 0.023779112 |
| 2022preEE | tHW | Out workspace | 41,119 | 0.019794237773 | 7.98 | 0.039044 | 0.006167313 |
| 2022preEE | bbH | Input ROOT tree | 6,167 | 0.050859706489 | 7.98 | 1.196063 | 0.485434677 |
| 2022preEE | bbH | Inclusive workspace | 6,167 | 0.050859706489 | 7.98 | 1.196063 | 0.485434677 |
| 2022preEE | bbH | In workspace | 4,701 | 0.037404947662 | 7.98 | 1.196063 | 0.357014618 |
| 2022preEE | bbH | Out workspace | 1,466 | 0.013454758827 | 7.98 | 1.196063 | 0.128420059 |
| 2022postEE | GluGluH | Input ROOT tree | 120,356 | 0.032993907691 | 26.68 | 118.562100 | 104.367543908 |
| 2022postEE | GluGluH | Inclusive workspace | 120,356 | 0.032993907691 | 26.68 | 118.562100 | 104.367543908 |
| 2022postEE | GluGluH | In workspace | 10,575 | 0.001859904634 | 26.68 | 118.562100 | 5.883318836 |
| 2022postEE | GluGluH | Out workspace | 109,781 | 0.031134003057 | 26.68 | 118.562100 | 98.484225072 |
| 2022postEE | VBFH | Input ROOT tree | 60,742 | 0.061616272882 | 26.68 | 9.257060 | 15.217886075 |
| 2022postEE | VBFH | Inclusive workspace | 60,742 | 0.061616272882 | 26.68 | 9.257060 | 15.217886075 |
| 2022postEE | VBFH | In workspace | 4,707 | 0.003670931950 | 26.68 | 9.257060 | 0.906640756 |
| 2022postEE | VBFH | Out workspace | 56,035 | 0.057945340932 | 26.68 | 9.257060 | 14.311245319 |
| 2022postEE | VH | Input ROOT tree | 49,398 | 0.075774974159 | 26.68 | 5.450043 | 11.018222825 |
| 2022postEE | VH | Inclusive workspace | 49,398 | 0.075774974159 | 26.68 | 5.450043 | 11.018222825 |
| 2022postEE | VH | In workspace | 7,460 | 0.010806560473 | 26.68 | 5.450043 | 1.571351130 |
| 2022postEE | VH | Out workspace | 41,938 | 0.064968413686 | 26.68 | 5.450043 | 9.446871695 |
| 2022postEE | ttH | Input ROOT tree | 356,569 | 0.070659185708 | 26.68 | 1.293900 | 2.439243556 |
| 2022postEE | ttH | Inclusive workspace | 356,569 | 0.070659185708 | 26.68 | 1.293900 | 2.439243556 |
| 2022postEE | ttH | In workspace | 297,337 | 0.059143438632 | 26.68 | 1.293900 | 2.041705549 |
| 2022postEE | ttH | Out workspace | 59,232 | 0.011515747076 | 26.68 | 1.293900 | 0.397538007 |
| 2022postEE | tHqLep | Input ROOT tree | 99,103 | 0.065564763457 | 26.68 | 0.061576 | 0.107713383 |
| 2022postEE | tHqLep | Inclusive workspace | 99,103 | 0.065564763457 | 26.68 | 0.061576 | 0.107713383 |
| 2022postEE | tHqLep | In workspace | 84,948 | 0.055795831683 | 26.68 | 0.061576 | 0.091664447 |
| 2022postEE | tHqLep | Out workspace | 14,155 | 0.009768931774 | 26.68 | 0.061576 | 0.016048936 |
| 2022postEE | tHqHad | Input ROOT tree | 212,768 | 0.134065694107 | 26.68 | 0.127424 | 0.455779196 |
| 2022postEE | tHqHad | Inclusive workspace | 212,768 | 0.134065694107 | 26.68 | 0.127424 | 0.455779196 |
| 2022postEE | tHqHad | In workspace | 179,488 | 0.111916603723 | 26.68 | 0.127424 | 0.380479585 |
| 2022postEE | tHqHad | Out workspace | 33,280 | 0.022149090384 | 26.68 | 0.127424 | 0.075299611 |
| 2022postEE | tHW | Input ROOT tree | 538,389 | 0.096796637263 | 26.68 | 0.039044 | 0.100832469 |
| 2022postEE | tHW | Inclusive workspace | 538,389 | 0.096796637263 | 26.68 | 0.039044 | 0.100832469 |
| 2022postEE | tHW | In workspace | 428,852 | 0.076568367930 | 26.68 | 0.039044 | 0.079760803 |
| 2022postEE | tHW | Out workspace | 109,537 | 0.020228269334 | 26.68 | 0.039044 | 0.021071665 |
| 2022postEE | bbH | Input ROOT tree | 19,966 | 0.051172952564 | 26.68 | 1.196063 | 1.632978085 |
| 2022postEE | bbH | Inclusive workspace | 19,966 | 0.051172952564 | 26.68 | 1.196063 | 1.632978085 |
| 2022postEE | bbH | In workspace | 15,695 | 0.036792217634 | 26.68 | 1.196063 | 1.174075016 |
| 2022postEE | bbH | Out workspace | 4,271 | 0.014380734930 | 26.68 | 1.196063 | 0.458903069 |
| 2023preBPix | GluGluH | Input ROOT tree | 80,926 | 0.041482309657 | 17.96 | 118.562100 | 88.331406235 |
| 2023preBPix | GluGluH | Inclusive workspace | 80,926 | 0.041482309657 | 17.96 | 118.562100 | 88.331406235 |
| 2023preBPix | GluGluH | In workspace | 6,102 | 0.002184600831 | 17.96 | 118.562100 | 4.651835085 |
| 2023preBPix | GluGluH | Out workspace | 74,824 | 0.039297708826 | 17.96 | 118.562100 | 83.679571150 |
| 2023preBPix | VBFH | Input ROOT tree | 67,533 | 0.074917898880 | 17.96 | 9.257060 | 12.455609951 |
| 2023preBPix | VBFH | Inclusive workspace | 67,533 | 0.074917898880 | 17.96 | 9.257060 | 12.455609951 |
| 2023preBPix | VBFH | In workspace | 4,532 | 0.004105505526 | 17.96 | 9.257060 | 0.682568201 |
| 2023preBPix | VBFH | Out workspace | 63,001 | 0.070812393354 | 17.96 | 9.257060 | 11.773041749 |
| 2023preBPix | VH | Input ROOT tree | 35,006 | 0.085811287401 | 17.96 | 5.450043 | 8.399446704 |
| 2023preBPix | VH | Inclusive workspace | 35,006 | 0.085811287401 | 17.96 | 5.450043 | 8.399446704 |
| 2023preBPix | VH | In workspace | 4,809 | 0.011222035832 | 17.96 | 5.450043 | 1.098443978 |
| 2023preBPix | VH | Out workspace | 30,197 | 0.074589251569 | 17.96 | 5.450043 | 7.301002726 |
| 2023preBPix | ttH | Input ROOT tree | 176,865 | 0.072891134444 | 17.96 | 1.293900 | 1.693876546 |
| 2023preBPix | ttH | Inclusive workspace | 176,865 | 0.072891134444 | 17.96 | 1.293900 | 1.693876546 |
| 2023preBPix | ttH | In workspace | 147,528 | 0.060997704609 | 17.96 | 1.293900 | 1.417491743 |
| 2023preBPix | ttH | Out workspace | 29,337 | 0.011893429835 | 17.96 | 1.293900 | 0.276384803 |
| 2023preBPix | tHqLep | Input ROOT tree | 133,560 | 0.069602922365 | 17.96 | 0.061576 | 0.076974549 |
| 2023preBPix | tHqLep | Inclusive workspace | 133,560 | 0.069602922365 | 17.96 | 0.061576 | 0.076974549 |
| 2023preBPix | tHqLep | In workspace | 113,710 | 0.059109399775 | 17.96 | 0.061576 | 0.065369660 |
| 2023preBPix | tHqLep | Out workspace | 19,850 | 0.010493522589 | 17.96 | 0.061576 | 0.011604889 |
| 2023preBPix | tHqHad | Input ROOT tree | 261,301 | 0.140498080479 | 17.96 | 0.127424 | 0.321534616 |
| 2023preBPix | tHqHad | Inclusive workspace | 261,301 | 0.140498080479 | 17.96 | 0.127424 | 0.321534616 |
| 2023preBPix | tHqHad | In workspace | 218,207 | 0.116719314623 | 17.96 | 0.127424 | 0.267116105 |
| 2023preBPix | tHqHad | Out workspace | 43,094 | 0.023778765856 | 17.96 | 0.127424 | 0.054418511 |
| 2023preBPix | tHW | Input ROOT tree | 61,468 | 0.102474782389 | 17.96 | 0.039044 | 0.071858416 |
| 2023preBPix | tHW | Inclusive workspace | 61,468 | 0.102474782389 | 17.96 | 0.039044 | 0.071858416 |
| 2023preBPix | tHW | In workspace | 48,839 | 0.080540582109 | 17.96 | 0.039044 | 0.056477492 |
| 2023preBPix | tHW | Out workspace | 12,629 | 0.021934200280 | 17.96 | 0.039044 | 0.015380925 |
| 2023preBPix | bbH | Input ROOT tree | 19,219 | 0.057052371738 | 17.96 | 1.196063 | 1.225558627 |
| 2023preBPix | bbH | Inclusive workspace | 19,219 | 0.057052371738 | 17.96 | 1.196063 | 1.225558627 |
| 2023preBPix | bbH | In workspace | 14,054 | 0.038853430159 | 17.96 | 1.196063 | 0.834621858 |
| 2023preBPix | bbH | Out workspace | 5,165 | 0.018198941579 | 17.96 | 1.196063 | 0.390936769 |
| 2023postBPix | GluGluH | Input ROOT tree | 39,452 | 0.040111074976 | 9.68 | 118.562100 | 46.034723774 |
| 2023postBPix | GluGluH | Inclusive workspace | 39,452 | 0.040111074976 | 9.68 | 118.562100 | 46.034723774 |
| 2023postBPix | GluGluH | In workspace | 2,876 | 0.002157066749 | 9.68 | 118.562100 | 2.475624800 |
| 2023postBPix | GluGluH | Out workspace | 36,576 | 0.037954008227 | 9.68 | 118.562100 | 43.559098975 |
| 2023postBPix | VBFH | Input ROOT tree | 33,874 | 0.072888210681 | 9.68 | 9.257060 | 6.531391623 |
| 2023postBPix | VBFH | Inclusive workspace | 33,874 | 0.072888210681 | 9.68 | 9.257060 | 6.531391623 |
| 2023postBPix | VBFH | In workspace | 2,263 | 0.004205237526 | 9.68 | 9.257060 | 0.376824357 |
| 2023postBPix | VBFH | Out workspace | 31,611 | 0.068682973155 | 9.68 | 9.257060 | 6.154567266 |
| 2023postBPix | VH | Input ROOT tree | 17,072 | 0.084793824693 | 9.68 | 5.450043 | 4.473418310 |
| 2023postBPix | VH | Inclusive workspace | 17,072 | 0.084793824693 | 9.68 | 5.450043 | 4.473418310 |
| 2023postBPix | VH | In workspace | 2,345 | 0.010927880751 | 9.68 | 5.450043 | 0.576515826 |
| 2023postBPix | VH | Out workspace | 14,727 | 0.073865943943 | 9.68 | 5.450043 | 3.896902485 |
| 2023postBPix | ttH | Input ROOT tree | 101,867 | 0.075317219680 | 9.68 | 1.293900 | 0.943344561 |
| 2023postBPix | ttH | Inclusive workspace | 101,867 | 0.075317219680 | 9.68 | 1.293900 | 0.943344561 |
| 2023postBPix | ttH | In workspace | 84,967 | 0.062512069399 | 9.68 | 1.293900 | 0.782960669 |
| 2023postBPix | ttH | Out workspace | 16,900 | 0.012805150280 | 9.68 | 1.293900 | 0.160383893 |
| 2023postBPix | tHqLep | Input ROOT tree | 49,675 | 0.070353555768 | 9.68 | 0.061576 | 0.041934817 |
| 2023postBPix | tHqLep | Inclusive workspace | 49,675 | 0.070353555768 | 9.68 | 0.061576 | 0.041934817 |
| 2023postBPix | tHqLep | In workspace | 42,292 | 0.059475267065 | 9.68 | 0.061576 | 0.035450723 |
| 2023postBPix | tHqLep | Out workspace | 7,383 | 0.010878288703 | 9.68 | 0.061576 | 0.006484094 |
| 2023postBPix | tHqHad | Input ROOT tree | 131,747 | 0.142805699424 | 9.68 | 0.127424 | 0.176145645 |
| 2023postBPix | tHqHad | Inclusive workspace | 131,747 | 0.142805699424 | 9.68 | 0.127424 | 0.176145645 |
| 2023postBPix | tHqHad | In workspace | 109,883 | 0.117869953424 | 9.68 | 0.127424 | 0.145388308 |
| 2023postBPix | tHqHad | Out workspace | 21,864 | 0.024935746000 | 9.68 | 0.127424 | 0.030757337 |
| 2023postBPix | tHW | Input ROOT tree | 30,387 | 0.103248989535 | 9.68 | 0.039044 | 0.039022534 |
| 2023postBPix | tHW | Inclusive workspace | 30,387 | 0.103248989535 | 9.68 | 0.039044 | 0.039022534 |
| 2023postBPix | tHW | In workspace | 24,091 | 0.081377160853 | 9.68 | 0.039044 | 0.030756166 |
| 2023postBPix | tHW | Out workspace | 6,296 | 0.021871828682 | 9.68 | 0.039044 | 0.008266368 |
| 2023postBPix | bbH | Input ROOT tree | 9,783 | 0.058198210981 | 9.68 | 1.196063 | 0.673812476 |
| 2023postBPix | bbH | Inclusive workspace | 9,783 | 0.058198210981 | 9.68 | 1.196063 | 0.673812476 |
| 2023postBPix | bbH | In workspace | 7,153 | 0.039345782218 | 9.68 | 1.196063 | 0.455541132 |
| 2023postBPix | bbH | Out workspace | 2,630 | 0.018852428764 | 9.68 | 1.196063 | 0.218271343 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 160,795 | 160795.000000 | 0 |
| Data workspace | 160,795 | 160795.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 90,148 | 90148.000000 | 90,148 | 90148.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 23,803 | 23803.000000 | 23,803 | 23803.000000 |
| Upper sideband | 130 < m ≤ 180 | 46,844 | 46844.000000 | 46,844 | 46844.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 136,992 | 136992.000000 | 136,992 | 136992.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 160,795 | 160795.000000 | 160,795 | 160795.000000 |
| Total | All entries | 160,795 | 160795.000000 | 160,795 | 160795.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_had |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_had |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_had |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_had |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_had |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_had |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_had |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_had |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_had |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_had |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_had |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_had |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_had |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_had |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_had |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_had |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_had |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_had |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_had |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_had |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_had |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_had |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_had |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_had |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/allData.root | Data_13TeV_bkg_had |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/ws/allData.root | Data_13TeV_bkg_had |
