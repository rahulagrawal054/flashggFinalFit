# Category bookkeeping: ttH_had_3

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 352 | 0.000081998671 | 118.562100 | 0.390252345 |
| GluGluH | Inclusive workspace | 352 | 0.000081998671 | 118.562100 | 0.390252345 |
| GluGluH | In workspace | 208 | 0.000040914241 | 118.562100 | 0.252521584 |
| GluGluH | Out workspace | 144 | 0.000041084430 | 118.562100 | 0.137730762 |
| VBFH | Input ROOT tree | 89 | 0.000034203124 | 9.257060 | 0.019918199 |
| VBFH | Inclusive workspace | 89 | 0.000034203124 | 9.257060 | 0.019918199 |
| VBFH | In workspace | 45 | 0.000016187805 | 9.257060 | 0.001904401 |
| VBFH | Out workspace | 44 | 0.000018015318 | 9.257060 | 0.018013798 |
| VH | Input ROOT tree | 3,248 | 0.001694004148 | 5.450043 | 0.301723118 |
| VH | Inclusive workspace | 3,248 | 0.001694004148 | 5.450043 | 0.301723118 |
| VH | In workspace | 1,878 | 0.000650274003 | 5.450043 | 0.138063349 |
| VH | Out workspace | 1,370 | 0.001043730145 | 5.450043 | 0.163659769 |
| ttH | Input ROOT tree | 348,158 | 0.170421709326 | 1.293900 | 7.595527916 |
| ttH | Inclusive workspace | 348,158 | 0.170421709326 | 1.293900 | 7.595527916 |
| ttH | In workspace | 322,979 | 0.158883643265 | 1.293900 | 7.141011425 |
| ttH | Out workspace | 25,179 | 0.011538066061 | 1.293900 | 0.454516491 |
| tHqLep | Input ROOT tree | 19,911 | 0.013947783761 | 0.061576 | 0.028814214 |
| tHqLep | Inclusive workspace | 19,911 | 0.013947783761 | 0.061576 | 0.028814214 |
| tHqLep | In workspace | 18,764 | 0.013270948103 | 0.061576 | 0.027441766 |
| tHqLep | Out workspace | 1,147 | 0.000676835658 | 0.061576 | 0.001372448 |
| tHqHad | Input ROOT tree | 79,460 | 0.040158999329 | 0.127424 | 0.176508015 |
| tHqHad | Inclusive workspace | 79,460 | 0.040158999329 | 0.127424 | 0.176508015 |
| tHqHad | In workspace | 76,987 | 0.038859547434 | 0.127424 | 0.170214295 |
| tHqHad | Out workspace | 2,473 | 0.001299451895 | 0.127424 | 0.006293719 |
| tHW | Input ROOT tree | 196,420 | 0.135889448275 | 0.039044 | 0.178565318 |
| tHW | Inclusive workspace | 196,420 | 0.135889448275 | 0.039044 | 0.178565318 |
| tHW | In workspace | 183,747 | 0.126684692083 | 0.039044 | 0.168017773 |
| tHW | Out workspace | 12,673 | 0.009204756192 | 0.039044 | 0.010547545 |
| bbH | Input ROOT tree | 468 | 0.000855809760 | 1.196063 | 0.032923939 |
| bbH | Inclusive workspace | 468 | 0.000855809760 | 1.196063 | 0.032923939 |
| bbH | In workspace | 453 | 0.000830405760 | 1.196063 | 0.031552574 |
| bbH | Out workspace | 15 | 0.000025404000 | 1.196063 | 0.001371366 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 648,106 | 0.363083956394 | 8.724233064 |
| Inclusive workspace | 648,106 | 0.363083956394 | 8.724233064 |
| In workspace | 605,061 | 0.339236612695 | 7.930727167 |
| Out workspace | 43,045 | 0.023847343699 | 0.793505897 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 70 | 0.000020533896 | 7.98 | 118.562100 | 0.019427644 |
| 2022preEE | GluGluH | Inclusive workspace | 70 | 0.000020533896 | 7.98 | 118.562100 | 0.019427644 |
| 2022preEE | GluGluH | In workspace | 35 | 0.000006245274 | 7.98 | 118.562100 | 0.005908814 |
| 2022preEE | GluGluH | Out workspace | 35 | 0.000014288622 | 7.98 | 118.562100 | 0.013518830 |
| 2022preEE | VBFH | Input ROOT tree | 5 | -0.000039964268 | 7.98 | 9.257060 | -0.002952214 |
| 2022preEE | VBFH | Inclusive workspace | 5 | -0.000039964268 | 7.98 | 9.257060 | -0.002952214 |
| 2022preEE | VBFH | In workspace | 2 | -0.000017054136 | 7.98 | 9.257060 | -0.001259812 |
| 2022preEE | VBFH | Out workspace | 3 | -0.000022910132 | 7.98 | 9.257060 | -0.001692402 |
| 2022preEE | VH | Input ROOT tree | 102 | 0.000219138273 | 7.98 | 5.450043 | 0.009530618 |
| 2022preEE | VH | Inclusive workspace | 102 | 0.000219138273 | 7.98 | 5.450043 | 0.009530618 |
| 2022preEE | VH | In workspace | 41 | 0.000027578994 | 7.98 | 5.450043 | 0.001199447 |
| 2022preEE | VH | Out workspace | 61 | 0.000191559279 | 7.98 | 5.450043 | 0.008331170 |
| 2022preEE | ttH | Input ROOT tree | 77,718 | 0.034129549139 | 7.98 | 1.293900 | 0.352398585 |
| 2022preEE | ttH | Inclusive workspace | 77,718 | 0.034129549139 | 7.98 | 1.293900 | 0.352398585 |
| 2022preEE | ttH | In workspace | 71,854 | 0.031668723905 | 7.98 | 1.293900 | 0.326989772 |
| 2022preEE | ttH | Out workspace | 5,864 | 0.002460825234 | 7.98 | 1.293900 | 0.025408813 |
| 2022preEE | tHqLep | Input ROOT tree | 2,384 | 0.002252885106 | 7.98 | 0.061576 | 0.001107020 |
| 2022preEE | tHqLep | Inclusive workspace | 2,384 | 0.002252885106 | 7.98 | 0.061576 | 0.001107020 |
| 2022preEE | tHqLep | In workspace | 2,191 | 0.002191286246 | 7.98 | 0.061576 | 0.001076751 |
| 2022preEE | tHqLep | Out workspace | 193 | 0.000061598860 | 7.98 | 0.061576 | 0.000030268 |
| 2022preEE | tHqHad | Input ROOT tree | 6,448 | 0.008225738103 | 7.98 | 0.127424 | 0.008364284 |
| 2022preEE | tHqHad | Inclusive workspace | 6,448 | 0.008225738103 | 7.98 | 0.127424 | 0.008364284 |
| 2022preEE | tHqHad | In workspace | 6,231 | 0.007837116175 | 7.98 | 0.127424 | 0.007969117 |
| 2022preEE | tHqHad | Out workspace | 217 | 0.000388621927 | 7.98 | 0.127424 | 0.000395167 |
| 2022preEE | tHW | Input ROOT tree | 57,955 | 0.027670474505 | 7.98 | 0.039044 | 0.008621321 |
| 2022preEE | tHW | Inclusive workspace | 57,955 | 0.027670474505 | 7.98 | 0.039044 | 0.008621321 |
| 2022preEE | tHW | In workspace | 53,862 | 0.025701968487 | 7.98 | 0.039044 | 0.008007991 |
| 2022preEE | tHW | Out workspace | 4,093 | 0.001968506018 | 7.98 | 0.039044 | 0.000613330 |
| 2022preEE | bbH | Input ROOT tree | 23 | 0.000193247147 | 7.98 | 1.196063 | 0.001844463 |
| 2022preEE | bbH | Inclusive workspace | 23 | 0.000193247147 | 7.98 | 1.196063 | 0.001844463 |
| 2022preEE | bbH | In workspace | 23 | 0.000193247147 | 7.98 | 1.196063 | 0.001844463 |
| 2022preEE | bbH | Out workspace | 0 | 0.000000000000 | 7.98 | 1.196063 | 0.000000000 |
| 2022postEE | GluGluH | Input ROOT tree | 68 | 0.000011457593 | 26.67 | 118.562100 | 0.036229495 |
| 2022postEE | GluGluH | Inclusive workspace | 68 | 0.000011457593 | 26.67 | 118.562100 | 0.036229495 |
| 2022postEE | GluGluH | In workspace | 36 | 0.000000628522 | 26.67 | 118.562100 | 0.001987418 |
| 2022postEE | GluGluH | Out workspace | 32 | 0.000010829071 | 26.67 | 118.562100 | 0.034242077 |
| 2022postEE | VBFH | Input ROOT tree | 29 | 0.000021114836 | 26.67 | 9.257060 | 0.005212953 |
| 2022postEE | VBFH | Inclusive workspace | 29 | 0.000021114836 | 26.67 | 9.257060 | 0.005212953 |
| 2022postEE | VBFH | In workspace | 15 | 0.000006564406 | 26.67 | 9.257060 | 0.001620659 |
| 2022postEE | VBFH | Out workspace | 14 | 0.000014550430 | 26.67 | 9.257060 | 0.003592294 |
| 2022postEE | VH | Input ROOT tree | 378 | 0.000411496810 | 26.67 | 5.450043 | 0.059812151 |
| 2022postEE | VH | Inclusive workspace | 378 | 0.000411496810 | 26.67 | 5.450043 | 0.059812151 |
| 2022postEE | VH | In workspace | 177 | 0.000141543864 | 26.67 | 5.450043 | 0.020573775 |
| 2022postEE | VH | Out workspace | 201 | 0.000269952947 | 26.67 | 5.450043 | 0.039238375 |
| 2022postEE | ttH | Input ROOT tree | 77,146 | 0.033523875665 | 26.67 | 1.293900 | 1.156852394 |
| 2022postEE | ttH | Inclusive workspace | 77,146 | 0.033523875665 | 26.67 | 1.293900 | 1.156852394 |
| 2022postEE | ttH | In workspace | 71,279 | 0.030949717212 | 26.67 | 1.293900 | 1.068022529 |
| 2022postEE | ttH | Out workspace | 5,867 | 0.002574158453 | 26.67 | 1.293900 | 0.088829866 |
| 2022postEE | tHqLep | Input ROOT tree | 4,654 | 0.002766031517 | 26.67 | 0.061576 | 0.004542485 |
| 2022postEE | tHqLep | Inclusive workspace | 4,654 | 0.002766031517 | 26.67 | 0.061576 | 0.004542485 |
| 2022postEE | tHqLep | In workspace | 4,339 | 0.002671549004 | 26.67 | 0.061576 | 0.004387322 |
| 2022postEE | tHqLep | Out workspace | 315 | 0.000094482513 | 26.67 | 0.061576 | 0.000155163 |
| 2022postEE | tHqHad | Input ROOT tree | 21,310 | 0.007833581197 | 26.67 | 0.127424 | 0.026621614 |
| 2022postEE | tHqHad | Inclusive workspace | 21,310 | 0.007833581197 | 26.67 | 0.127424 | 0.026621614 |
| 2022postEE | tHqHad | In workspace | 20,642 | 0.007589768046 | 26.67 | 0.127424 | 0.025793040 |
| 2022postEE | tHqHad | Out workspace | 668 | 0.000243813151 | 26.67 | 0.127424 | 0.000828574 |
| 2022postEE | tHW | Input ROOT tree | 57,635 | 0.027139384738 | 26.67 | 0.039044 | 0.028260336 |
| 2022postEE | tHW | Inclusive workspace | 57,635 | 0.027139384738 | 26.67 | 0.039044 | 0.028260336 |
| 2022postEE | tHW | In workspace | 53,575 | 0.025106722036 | 26.67 | 0.039044 | 0.026143717 |
| 2022postEE | tHW | Out workspace | 4,060 | 0.002032662703 | 26.67 | 0.039044 | 0.002116619 |
| 2022postEE | bbH | Input ROOT tree | 81 | 0.000192409902 | 26.67 | 1.196063 | 0.006137684 |
| 2022postEE | bbH | Inclusive workspace | 81 | 0.000192409902 | 26.67 | 1.196063 | 0.006137684 |
| 2022postEE | bbH | In workspace | 77 | 0.000180549428 | 26.67 | 1.196063 | 0.005759346 |
| 2022postEE | bbH | Out workspace | 4 | 0.000011860475 | 26.67 | 1.196063 | 0.000378337 |
| 2023preBPix | GluGluH | Input ROOT tree | 92 | 0.000017610503 | 18.06 | 118.562100 | 0.037714428 |
| 2023preBPix | GluGluH | Inclusive workspace | 92 | 0.000017610503 | 18.06 | 118.562100 | 0.037714428 |
| 2023preBPix | GluGluH | In workspace | 54 | 0.000005238984 | 18.06 | 118.562100 | 0.011219741 |
| 2023preBPix | GluGluH | Out workspace | 38 | 0.000012371519 | 18.06 | 118.562100 | 0.026494686 |
| 2023preBPix | VBFH | Input ROOT tree | 15 | 0.000008375862 | 18.06 | 9.257060 | 0.001400530 |
| 2023preBPix | VBFH | Inclusive workspace | 15 | 0.000008375862 | 18.06 | 9.257060 | 0.001400530 |
| 2023preBPix | VBFH | In workspace | 6 | 0.000006648180 | 18.06 | 9.257060 | 0.001111644 |
| 2023preBPix | VBFH | Out workspace | 9 | 0.000001727682 | 18.06 | 9.257060 | 0.000288886 |
| 2023preBPix | VH | Input ROOT tree | 234 | 0.000377389522 | 18.06 | 5.450043 | 0.037151782 |
| 2023preBPix | VH | Inclusive workspace | 234 | 0.000377389522 | 18.06 | 5.450043 | 0.037151782 |
| 2023preBPix | VH | In workspace | 107 | 0.000156423916 | 18.06 | 5.450043 | 0.015399016 |
| 2023preBPix | VH | Out workspace | 127 | 0.000220965606 | 18.06 | 5.450043 | 0.021752766 |
| 2023preBPix | ttH | Input ROOT tree | 64,200 | 0.034928940055 | 18.06 | 1.293900 | 0.816349257 |
| 2023preBPix | ttH | Inclusive workspace | 64,200 | 0.034928940055 | 18.06 | 1.293900 | 0.816349257 |
| 2023preBPix | ttH | In workspace | 59,406 | 0.032574487748 | 18.06 | 1.293900 | 0.761321667 |
| 2023preBPix | ttH | Out workspace | 4,794 | 0.002354452307 | 18.06 | 1.293900 | 0.055027590 |
| 2023preBPix | tHqLep | Input ROOT tree | 570 | 0.003679508500 | 18.06 | 0.061576 | 0.004092541 |
| 2023preBPix | tHqLep | Inclusive workspace | 570 | 0.003679508500 | 18.06 | 0.061576 | 0.004092541 |
| 2023preBPix | tHqLep | In workspace | 538 | 0.003360673314 | 18.06 | 0.061576 | 0.003737916 |
| 2023preBPix | tHqLep | Out workspace | 32 | 0.000318835186 | 18.06 | 0.061576 | 0.000354625 |
| 2023preBPix | tHqHad | Input ROOT tree | 17,806 | 0.007996354518 | 18.06 | 0.127424 | 0.018404878 |
| 2023preBPix | tHqHad | Inclusive workspace | 17,806 | 0.007996354518 | 18.06 | 0.127424 | 0.018404878 |
| 2023preBPix | tHqHad | In workspace | 17,261 | 0.007843456858 | 18.06 | 0.127424 | 0.018052959 |
| 2023preBPix | tHqHad | Out workspace | 545 | 0.000152897659 | 18.06 | 0.127424 | 0.000351918 |
| 2023preBPix | tHW | Input ROOT tree | 16,843 | 0.027579069688 | 18.06 | 0.039044 | 0.019450188 |
| 2023preBPix | tHW | Inclusive workspace | 16,843 | 0.027579069688 | 18.06 | 0.039044 | 0.019450188 |
| 2023preBPix | tHW | In workspace | 15,629 | 0.025634981543 | 18.06 | 0.039044 | 0.018079116 |
| 2023preBPix | tHW | Out workspace | 1,214 | 0.001944088145 | 18.06 | 0.039044 | 0.001371072 |
| 2023preBPix | bbH | Input ROOT tree | 77 | 0.000199254090 | 18.06 | 1.196063 | 0.004304782 |
| 2023preBPix | bbH | Inclusive workspace | 77 | 0.000199254090 | 18.06 | 1.196063 | 0.004304782 |
| 2023preBPix | bbH | In workspace | 75 | 0.000192083728 | 18.06 | 1.196063 | 0.004149870 |
| 2023preBPix | bbH | Out workspace | 2 | 0.000007170361 | 18.06 | 1.196063 | 0.000154912 |
| 2023postBPix | GluGluH | Input ROOT tree | 40 | 0.000010552920 | 9.69 | 118.562100 | 0.012127652 |
| 2023postBPix | GluGluH | Inclusive workspace | 40 | 0.000010552920 | 9.69 | 118.562100 | 0.012127652 |
| 2023postBPix | GluGluH | In workspace | 24 | 0.000011950135 | 9.69 | 118.562100 | 0.013733364 |
| 2023postBPix | GluGluH | Out workspace | 16 | -0.000001397215 | 9.69 | 118.562100 | -0.001605711 |
| 2023postBPix | VBFH | Input ROOT tree | 10 | 0.000031479467 | 9.69 | 9.257060 | 0.002824611 |
| 2023postBPix | VBFH | Inclusive workspace | 10 | 0.000031479467 | 9.69 | 9.257060 | 0.002824611 |
| 2023postBPix | VBFH | In workspace | 6 | 0.000021500447 | 9.69 | 9.257060 | 0.001929207 |
| 2023postBPix | VBFH | Out workspace | 4 | 0.000009979020 | 9.69 | 9.257060 | 0.000895404 |
| 2023postBPix | VH | Input ROOT tree | 105 | 0.000395004617 | 9.69 | 5.450043 | 0.020867014 |
| 2023postBPix | VH | Inclusive workspace | 105 | 0.000395004617 | 9.69 | 5.450043 | 0.020867014 |
| 2023postBPix | VH | In workspace | 50 | 0.000171477050 | 9.69 | 5.450043 | 0.009058664 |
| 2023postBPix | VH | Out workspace | 55 | 0.000223527567 | 9.69 | 5.450043 | 0.011808350 |
| 2023postBPix | ttH | Input ROOT tree | 77,638 | 0.033773542919 | 9.69 | 1.293900 | 0.423580099 |
| 2023postBPix | ttH | Inclusive workspace | 77,638 | 0.033773542919 | 9.69 | 1.293900 | 0.423580099 |
| 2023postBPix | ttH | In workspace | 71,829 | 0.031422742749 | 9.69 | 1.293900 | 0.394096897 |
| 2023postBPix | ttH | Out workspace | 5,809 | 0.002350800170 | 9.69 | 1.293900 | 0.029483201 |
| 2023postBPix | tHqLep | Input ROOT tree | 3,482 | 0.002667489674 | 9.69 | 0.061576 | 0.001592115 |
| 2023postBPix | tHqLep | Inclusive workspace | 3,482 | 0.002667489674 | 9.69 | 0.061576 | 0.001592115 |
| 2023postBPix | tHqLep | In workspace | 3,234 | 0.002580882846 | 9.69 | 0.061576 | 0.001540422 |
| 2023postBPix | tHqLep | Out workspace | 248 | 0.000086606828 | 9.69 | 0.061576 | 0.000051692 |
| 2023postBPix | tHqHad | Input ROOT tree | 9,301 | 0.008022969051 | 9.69 | 0.127424 | 0.009909331 |
| 2023postBPix | tHqHad | Inclusive workspace | 9,301 | 0.008022969051 | 9.69 | 0.127424 | 0.009909331 |
| 2023postBPix | tHqHad | In workspace | 9,032 | 0.007828459737 | 9.69 | 0.127424 | 0.009669089 |
| 2023postBPix | tHqHad | Out workspace | 269 | 0.000194509315 | 9.69 | 0.127424 | 0.000240242 |
| 2023postBPix | tHW | Input ROOT tree | 8,422 | 0.027446687014 | 9.69 | 0.039044 | 0.010387295 |
| 2023postBPix | tHW | Inclusive workspace | 8,422 | 0.027446687014 | 9.69 | 0.039044 | 0.010387295 |
| 2023postBPix | tHW | In workspace | 7,818 | 0.025518914174 | 9.69 | 0.039044 | 0.009657722 |
| 2023postBPix | tHW | Out workspace | 604 | 0.001927772839 | 9.69 | 0.039044 | 0.000729572 |
| 2023postBPix | bbH | Input ROOT tree | 30 | 0.000124990643 | 9.69 | 1.196063 | 0.001449071 |
| 2023postBPix | bbH | Inclusive workspace | 30 | 0.000124990643 | 9.69 | 1.196063 | 0.001449071 |
| 2023postBPix | bbH | In workspace | 30 | 0.000124990643 | 9.69 | 1.196063 | 0.001449071 |
| 2023postBPix | bbH | Out workspace | 0 | 0.000000000000 | 9.69 | 1.196063 | 0.000000000 |
| 2024 | GluGluH | Input ROOT tree | 82 | 0.000021843759 | 109.95 | 118.562100 | 0.284753126 |
| 2024 | GluGluH | Inclusive workspace | 82 | 0.000021843759 | 109.95 | 118.562100 | 0.284753126 |
| 2024 | GluGluH | In workspace | 59 | 0.000016851326 | 109.95 | 118.562100 | 0.219672247 |
| 2024 | GluGluH | Out workspace | 23 | 0.000004992434 | 109.95 | 118.562100 | 0.065080879 |
| 2024 | VBFH | Input ROOT tree | 30 | 0.000013197227 | 109.95 | 9.257060 | 0.013432319 |
| 2024 | VBFH | Inclusive workspace | 30 | 0.000013197227 | 109.95 | 9.257060 | 0.013432319 |
| 2024 | VBFH | In workspace | 16 | -0.000001471091 | 109.95 | 9.257060 | -0.001497296 |
| 2024 | VBFH | Out workspace | 14 | 0.000014668317 | 109.95 | 9.257060 | 0.014929615 |
| 2024 | VH | Input ROOT tree | 2,429 | 0.000290974926 | 109.95 | 5.450043 | 0.174361553 |
| 2024 | VH | Inclusive workspace | 2,429 | 0.000290974926 | 109.95 | 5.450043 | 0.174361553 |
| 2024 | VH | In workspace | 1,503 | 0.000153250180 | 109.95 | 5.450043 | 0.091832447 |
| 2024 | VH | Out workspace | 926 | 0.000137724746 | 109.95 | 5.450043 | 0.082529106 |
| 2024 | ttH | Input ROOT tree | 51,456 | 0.034065801548 | 109.95 | 1.293900 | 4.846347581 |
| 2024 | ttH | Inclusive workspace | 51,456 | 0.034065801548 | 109.95 | 1.293900 | 4.846347581 |
| 2024 | ttH | In workspace | 48,611 | 0.032267971651 | 109.95 | 1.293900 | 4.590580561 |
| 2024 | ttH | Out workspace | 2,845 | 0.001797829897 | 109.95 | 1.293900 | 0.255767021 |
| 2024 | tHqLep | Input ROOT tree | 8,821 | 0.002581868963 | 109.95 | 0.061576 | 0.017480054 |
| 2024 | tHqLep | Inclusive workspace | 8,821 | 0.002581868963 | 109.95 | 0.061576 | 0.017480054 |
| 2024 | tHqLep | In workspace | 8,462 | 0.002466556693 | 109.95 | 0.061576 | 0.016699354 |
| 2024 | tHqLep | Out workspace | 359 | 0.000115312270 | 109.95 | 0.061576 | 0.000780700 |
| 2024 | tHqHad | Input ROOT tree | 24,595 | 0.008080356461 | 109.95 | 0.127424 | 0.113207908 |
| 2024 | tHqHad | Inclusive workspace | 24,595 | 0.008080356461 | 109.95 | 0.127424 | 0.113207908 |
| 2024 | tHqHad | In workspace | 23,821 | 0.007760746618 | 109.95 | 0.127424 | 0.108730091 |
| 2024 | tHqHad | Out workspace | 774 | 0.000319609842 | 109.95 | 0.127424 | 0.004477818 |
| 2024 | tHW | Input ROOT tree | 55,565 | 0.026053832330 | 109.95 | 0.039044 | 0.111846179 |
| 2024 | tHW | Inclusive workspace | 55,565 | 0.026053832330 | 109.95 | 0.039044 | 0.111846179 |
| 2024 | tHW | In workspace | 52,863 | 0.024722105843 | 109.95 | 0.039044 | 0.106129227 |
| 2024 | tHW | Out workspace | 2,702 | 0.001331726487 | 109.95 | 0.039044 | 0.005716952 |
| 2024 | bbH | Input ROOT tree | 257 | 0.000145907978 | 109.95 | 1.196063 | 0.019187939 |
| 2024 | bbH | Inclusive workspace | 257 | 0.000145907978 | 109.95 | 1.196063 | 0.019187939 |
| 2024 | bbH | In workspace | 248 | 0.000139534814 | 109.95 | 1.196063 | 0.018349822 |
| 2024 | bbH | Out workspace | 9 | 0.000006373164 | 109.95 | 1.196063 | 0.000838116 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 351 | 351.000000 | 0 |
| Data workspace | 351 | 351.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 152 | 152.000000 | 152 | 152.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 57 | 57.000000 | 57 | 57.000000 |
| Upper sideband | 130 < m ≤ 180 | 142 | 142.000000 | 142 | 142.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 294 | 294.000000 | 294 | 294.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 351 | 351.000000 | 351 | 351.000000 |
| Total | All entries | 351 | 351.000000 | 351 | 351.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| GluGluH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_had_3 |
| GluGluH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_had_3 |
| GluGluH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_had_3 |
| GluGluH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_had_3 |
| VBFH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_had_3 |
| VBFH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_had_3 |
| VBFH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_had_3 |
| VBFH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_had_3 |
| VH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_had_3 |
| VH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_had_3 |
| VH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_had_3 |
| VH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_had_3 |
| ttH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_had_3 |
| ttH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_had_3 |
| ttH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_had_3 |
| ttH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_had_3 |
| tHqLep / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_had_3 |
| tHqLep / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_had_3 |
| tHqLep / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_had_3 |
| tHqLep / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_had_3 |
| tHqHad / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_had_3 |
| tHqHad / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_had_3 |
| tHqHad / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_had_3 |
| tHqHad / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_had_3 |
| tHW / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_had_3 |
| tHW / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_had_3 |
| tHW / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_had_3 |
| tHW / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_had_3 |
| bbH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_had_3 |
| bbH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_had_3 |
| bbH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_had_3 |
| bbH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_had_3 |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/allData.root | Data_13TeV_ttH_had_3 |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/ws/allData.root | Data_13TeV_ttH_had_3 |
