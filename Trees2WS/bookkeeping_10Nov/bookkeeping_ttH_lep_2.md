# Category bookkeeping: ttH_lep_2

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 3 | 0.000001195213 | 118.562100 | 0.003779323 |
| GluGluH | Inclusive workspace | 3 | 0.000001195213 | 118.562100 | 0.003779323 |
| GluGluH | In workspace | 1 | 0.000000385704 | 118.562100 | 0.001219617 |
| GluGluH | Out workspace | 2 | 0.000000809508 | 118.562100 | 0.002559706 |
| VBFH | Input ROOT tree | 0 | 0.000000000000 | 9.257060 | 0.000000000 |
| VBFH | Inclusive workspace | 0 | 0.000000000000 | 9.257060 | 0.000000000 |
| VBFH | In workspace | 0 | 0.000000000000 | 9.257060 | 0.000000000 |
| VBFH | Out workspace | 0 | 0.000000000000 | 9.257060 | 0.000000000 |
| VH | Input ROOT tree | 742 | 0.000490178066 | 5.450043 | 0.078867582 |
| VH | Inclusive workspace | 742 | 0.000490178066 | 5.450043 | 0.078867582 |
| VH | In workspace | 262 | 0.000137161370 | 5.450043 | 0.022429359 |
| VH | Out workspace | 480 | 0.000353016696 | 5.450043 | 0.056438222 |
| ttH | Input ROOT tree | 282,696 | 0.138947148192 | 1.293900 | 6.202787381 |
| ttH | Inclusive workspace | 282,696 | 0.138947148192 | 1.293900 | 6.202787381 |
| ttH | In workspace | 261,066 | 0.128291019397 | 1.293900 | 5.846148082 |
| ttH | Out workspace | 21,630 | 0.010656128795 | 1.293900 | 0.356639299 |
| tHqLep | Input ROOT tree | 25,382 | 0.014719525260 | 0.061576 | 0.030345546 |
| tHqLep | Inclusive workspace | 25,382 | 0.014719525260 | 0.061576 | 0.030345546 |
| tHqLep | In workspace | 24,009 | 0.014093293607 | 0.061576 | 0.029278692 |
| tHqLep | Out workspace | 1,373 | 0.000626231653 | 0.061576 | 0.001066854 |
| tHqHad | Input ROOT tree | 854 | 0.000490532660 | 0.127424 | 0.002329858 |
| tHqHad | Inclusive workspace | 854 | 0.000490532660 | 0.127424 | 0.002329858 |
| tHqHad | In workspace | 815 | 0.000473854139 | 0.127424 | 0.002295674 |
| tHqHad | Out workspace | 39 | 0.000016678521 | 0.127424 | 0.000034183 |
| tHW | Input ROOT tree | 177,254 | 0.118613199255 | 0.039044 | 0.153448827 |
| tHW | Inclusive workspace | 177,254 | 0.118613199255 | 0.039044 | 0.153448827 |
| tHW | In workspace | 164,170 | 0.108980001834 | 0.039044 | 0.144226708 |
| tHW | Out workspace | 13,084 | 0.009633197420 | 0.039044 | 0.009222119 |
| bbH | Input ROOT tree | 9 | 0.000023361933 | 1.196063 | 0.000473525 |
| bbH | Inclusive workspace | 9 | 0.000023361933 | 1.196063 | 0.000473525 |
| bbH | In workspace | 9 | 0.000023361933 | 1.196063 | 0.000473525 |
| bbH | Out workspace | 0 | 0.000000000000 | 1.196063 | 0.000000000 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 486,940 | 0.273285140578 | 6.472032042 |
| Inclusive workspace | 486,940 | 0.273285140578 | 6.472032042 |
| In workspace | 450,332 | 0.251999077985 | 6.046071657 |
| Out workspace | 36,608 | 0.021286062594 | 0.425960385 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 0 | 0.000000000000 | 7.98 | 118.562100 | 0.000000000 |
| 2022preEE | GluGluH | Inclusive workspace | 0 | 0.000000000000 | 7.98 | 118.562100 | 0.000000000 |
| 2022preEE | GluGluH | In workspace | 0 | 0.000000000000 | 7.98 | 118.562100 | 0.000000000 |
| 2022preEE | GluGluH | Out workspace | 0 | 0.000000000000 | 7.98 | 118.562100 | 0.000000000 |
| 2022preEE | VBFH | Input ROOT tree | 0 | 0.000000000000 | 7.98 | 9.257060 | 0.000000000 |
| 2022preEE | VBFH | Inclusive workspace | 0 | 0.000000000000 | 7.98 | 9.257060 | 0.000000000 |
| 2022preEE | VBFH | In workspace | 0 | 0.000000000000 | 7.98 | 9.257060 | 0.000000000 |
| 2022preEE | VBFH | Out workspace | 0 | 0.000000000000 | 7.98 | 9.257060 | 0.000000000 |
| 2022preEE | VH | Input ROOT tree | 37 | 0.000063946641 | 7.98 | 5.450043 | 0.002781125 |
| 2022preEE | VH | Inclusive workspace | 37 | 0.000063946641 | 7.98 | 5.450043 | 0.002781125 |
| 2022preEE | VH | In workspace | 9 | 0.000032489013 | 7.98 | 5.450043 | 0.001412991 |
| 2022preEE | VH | Out workspace | 28 | 0.000031457628 | 7.98 | 5.450043 | 0.001368134 |
| 2022preEE | ttH | Input ROOT tree | 64,415 | 0.028763580044 | 7.98 | 1.293900 | 0.296993226 |
| 2022preEE | ttH | Inclusive workspace | 64,415 | 0.028763580044 | 7.98 | 1.293900 | 0.296993226 |
| 2022preEE | ttH | In workspace | 59,036 | 0.026471269093 | 7.98 | 1.293900 | 0.273324377 |
| 2022preEE | ttH | Out workspace | 5,379 | 0.002292310951 | 7.98 | 1.293900 | 0.023668849 |
| 2022preEE | tHqLep | Input ROOT tree | 3,159 | 0.002988047821 | 7.98 | 0.061576 | 0.001468263 |
| 2022preEE | tHqLep | Inclusive workspace | 3,159 | 0.002988047821 | 7.98 | 0.061576 | 0.001468263 |
| 2022preEE | tHqLep | In workspace | 2,954 | 0.002844649057 | 7.98 | 0.061576 | 0.001397800 |
| 2022preEE | tHqLep | Out workspace | 205 | 0.000143398764 | 7.98 | 0.061576 | 0.000070463 |
| 2022preEE | tHqHad | Input ROOT tree | 76 | 0.000068111220 | 7.98 | 0.127424 | 0.000069258 |
| 2022preEE | tHqHad | Inclusive workspace | 76 | 0.000068111220 | 7.98 | 0.127424 | 0.000069258 |
| 2022preEE | tHqHad | In workspace | 72 | 0.000071376214 | 7.98 | 0.127424 | 0.000072578 |
| 2022preEE | tHqHad | Out workspace | 4 | -0.000003264994 | 7.98 | 0.127424 | -0.000003320 |
| 2022preEE | tHW | Input ROOT tree | 52,901 | 0.024841142439 | 7.98 | 0.039044 | 0.007739783 |
| 2022preEE | tHW | Inclusive workspace | 52,901 | 0.024841142439 | 7.98 | 0.039044 | 0.007739783 |
| 2022preEE | tHW | In workspace | 48,266 | 0.022663123521 | 7.98 | 0.039044 | 0.007061175 |
| 2022preEE | tHW | Out workspace | 4,635 | 0.002178018918 | 7.98 | 0.039044 | 0.000678608 |
| 2022preEE | bbH | Input ROOT tree | 1 | 0.000009516912 | 7.98 | 1.196063 | 0.000090835 |
| 2022preEE | bbH | Inclusive workspace | 1 | 0.000009516912 | 7.98 | 1.196063 | 0.000090835 |
| 2022preEE | bbH | In workspace | 1 | 0.000009516912 | 7.98 | 1.196063 | 0.000090835 |
| 2022preEE | bbH | Out workspace | 0 | 0.000000000000 | 7.98 | 1.196063 | 0.000000000 |
| 2022postEE | GluGluH | Input ROOT tree | 3 | 0.000001195213 | 26.67 | 118.562100 | 0.003779323 |
| 2022postEE | GluGluH | Inclusive workspace | 3 | 0.000001195213 | 26.67 | 118.562100 | 0.003779323 |
| 2022postEE | GluGluH | In workspace | 1 | 0.000000385704 | 26.67 | 118.562100 | 0.001219617 |
| 2022postEE | GluGluH | Out workspace | 2 | 0.000000809508 | 26.67 | 118.562100 | 0.002559706 |
| 2022postEE | VBFH | Input ROOT tree | 0 | 0.000000000000 | 26.67 | 9.257060 | 0.000000000 |
| 2022postEE | VBFH | Inclusive workspace | 0 | 0.000000000000 | 26.67 | 9.257060 | 0.000000000 |
| 2022postEE | VBFH | In workspace | 0 | 0.000000000000 | 26.67 | 9.257060 | 0.000000000 |
| 2022postEE | VBFH | Out workspace | 0 | 0.000000000000 | 26.67 | 9.257060 | 0.000000000 |
| 2022postEE | VH | Input ROOT tree | 121 | 0.000120614629 | 26.67 | 5.450043 | 0.017531656 |
| 2022postEE | VH | Inclusive workspace | 121 | 0.000120614629 | 26.67 | 5.450043 | 0.017531656 |
| 2022postEE | VH | In workspace | 31 | 0.000052487879 | 26.67 | 5.450043 | 0.007629252 |
| 2022postEE | VH | Out workspace | 90 | 0.000068126750 | 26.67 | 5.450043 | 0.009902403 |
| 2022postEE | ttH | Input ROOT tree | 64,016 | 0.026467335429 | 26.67 | 1.293900 | 0.913343095 |
| 2022postEE | ttH | Inclusive workspace | 64,016 | 0.026467335429 | 26.67 | 1.293900 | 0.913343095 |
| 2022postEE | ttH | In workspace | 58,666 | 0.024169561995 | 26.67 | 1.293900 | 0.834050810 |
| 2022postEE | ttH | Out workspace | 5,350 | 0.002297773434 | 26.67 | 1.293900 | 0.079292285 |
| 2022postEE | tHqLep | Input ROOT tree | 6,178 | 0.002763912071 | 26.67 | 0.061576 | 0.004539004 |
| 2022postEE | tHqLep | Inclusive workspace | 6,178 | 0.002763912071 | 26.67 | 0.061576 | 0.004539004 |
| 2022postEE | tHqLep | In workspace | 5,753 | 0.002562152471 | 26.67 | 0.061576 | 0.004207667 |
| 2022postEE | tHqLep | Out workspace | 425 | 0.000201759600 | 26.67 | 0.061576 | 0.000331337 |
| 2022postEE | tHqHad | Input ROOT tree | 194 | 0.000082365670 | 26.67 | 0.127424 | 0.000279911 |
| 2022postEE | tHqHad | Inclusive workspace | 194 | 0.000082365670 | 26.67 | 0.127424 | 0.000279911 |
| 2022postEE | tHqHad | In workspace | 188 | 0.000075500530 | 26.67 | 0.127424 | 0.000256581 |
| 2022postEE | tHqHad | Out workspace | 6 | 0.000006865140 | 26.67 | 0.127424 | 0.000023330 |
| 2022postEE | tHW | Input ROOT tree | 52,747 | 0.023474196175 | 26.67 | 0.039044 | 0.024443762 |
| 2022postEE | tHW | Inclusive workspace | 52,747 | 0.023474196175 | 26.67 | 0.039044 | 0.024443762 |
| 2022postEE | tHW | In workspace | 48,158 | 0.021329285559 | 26.67 | 0.039044 | 0.022210259 |
| 2022postEE | tHW | Out workspace | 4,589 | 0.002144910616 | 26.67 | 0.039044 | 0.002233503 |
| 2022postEE | bbH | Input ROOT tree | 3 | 0.000006554037 | 26.67 | 1.196063 | 0.000209067 |
| 2022postEE | bbH | Inclusive workspace | 3 | 0.000006554037 | 26.67 | 1.196063 | 0.000209067 |
| 2022postEE | bbH | In workspace | 3 | 0.000006554037 | 26.67 | 1.196063 | 0.000209067 |
| 2022postEE | bbH | Out workspace | 0 | 0.000000000000 | 26.67 | 1.196063 | 0.000000000 |
| 2023preBPix | GluGluH | Input ROOT tree | 0 | 0.000000000000 | 18.06 | 118.562100 | 0.000000000 |
| 2023preBPix | GluGluH | Inclusive workspace | 0 | 0.000000000000 | 18.06 | 118.562100 | 0.000000000 |
| 2023preBPix | GluGluH | In workspace | 0 | 0.000000000000 | 18.06 | 118.562100 | 0.000000000 |
| 2023preBPix | GluGluH | Out workspace | 0 | 0.000000000000 | 18.06 | 118.562100 | 0.000000000 |
| 2023preBPix | VBFH | Input ROOT tree | 0 | 0.000000000000 | 18.06 | 9.257060 | 0.000000000 |
| 2023preBPix | VBFH | Inclusive workspace | 0 | 0.000000000000 | 18.06 | 9.257060 | 0.000000000 |
| 2023preBPix | VBFH | In workspace | 0 | 0.000000000000 | 18.06 | 9.257060 | 0.000000000 |
| 2023preBPix | VBFH | Out workspace | 0 | 0.000000000000 | 18.06 | 9.257060 | 0.000000000 |
| 2023preBPix | VH | Input ROOT tree | 50 | 0.000074560669 | 18.06 | 5.450043 | 0.007340060 |
| 2023preBPix | VH | Inclusive workspace | 50 | 0.000074560669 | 18.06 | 5.450043 | 0.007340060 |
| 2023preBPix | VH | In workspace | 14 | 0.000000036838 | 18.06 | 5.450043 | 0.000003627 |
| 2023preBPix | VH | Out workspace | 36 | 0.000074523831 | 18.06 | 5.450043 | 0.007336433 |
| 2023preBPix | ttH | Input ROOT tree | 50,600 | 0.027665401810 | 18.06 | 1.293900 | 0.646587906 |
| 2023preBPix | ttH | Inclusive workspace | 50,600 | 0.027665401810 | 18.06 | 1.293900 | 0.646587906 |
| 2023preBPix | ttH | In workspace | 46,410 | 0.025127401690 | 18.06 | 1.293900 | 0.587270489 |
| 2023preBPix | ttH | Out workspace | 4,190 | 0.002538000120 | 18.06 | 1.293900 | 0.059317417 |
| 2023preBPix | tHqLep | Input ROOT tree | 718 | 0.002702536573 | 18.06 | 0.061576 | 0.003005902 |
| 2023preBPix | tHqLep | Inclusive workspace | 718 | 0.002702536573 | 18.06 | 0.061576 | 0.003005902 |
| 2023preBPix | tHqLep | In workspace | 682 | 0.002665778492 | 18.06 | 0.061576 | 0.002965018 |
| 2023preBPix | tHqLep | Out workspace | 36 | 0.000036758081 | 18.06 | 0.061576 | 0.000040884 |
| 2023preBPix | tHqHad | Input ROOT tree | 174 | 0.000100685497 | 18.06 | 0.127424 | 0.000231744 |
| 2023preBPix | tHqHad | Inclusive workspace | 174 | 0.000100685497 | 18.06 | 0.127424 | 0.000231744 |
| 2023preBPix | tHqHad | In workspace | 166 | 0.000091863520 | 18.06 | 0.127424 | 0.000211438 |
| 2023preBPix | tHqHad | Out workspace | 8 | 0.000008821977 | 18.06 | 0.127424 | 0.000020305 |
| 2023preBPix | tHW | Input ROOT tree | 14,754 | 0.024225658919 | 18.06 | 0.039044 | 0.017085189 |
| 2023preBPix | tHW | Inclusive workspace | 14,754 | 0.024225658919 | 18.06 | 0.039044 | 0.017085189 |
| 2023preBPix | tHW | In workspace | 13,431 | 0.021959734250 | 18.06 | 0.039044 | 0.015487141 |
| 2023preBPix | tHW | Out workspace | 1,323 | 0.002265924669 | 18.06 | 0.039044 | 0.001598047 |
| 2023preBPix | bbH | Input ROOT tree | 2 | 0.000000727841 | 18.06 | 1.196063 | 0.000015725 |
| 2023preBPix | bbH | Inclusive workspace | 2 | 0.000000727841 | 18.06 | 1.196063 | 0.000015725 |
| 2023preBPix | bbH | In workspace | 2 | 0.000000727841 | 18.06 | 1.196063 | 0.000015725 |
| 2023preBPix | bbH | Out workspace | 0 | 0.000000000000 | 18.06 | 1.196063 | 0.000000000 |
| 2023postBPix | GluGluH | Input ROOT tree | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | GluGluH | Inclusive workspace | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | GluGluH | In workspace | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | GluGluH | Out workspace | 0 | 0.000000000000 | 9.69 | 118.562100 | 0.000000000 |
| 2023postBPix | VBFH | Input ROOT tree | 0 | 0.000000000000 | 9.69 | 9.257060 | 0.000000000 |
| 2023postBPix | VBFH | Inclusive workspace | 0 | 0.000000000000 | 9.69 | 9.257060 | 0.000000000 |
| 2023postBPix | VBFH | In workspace | 0 | 0.000000000000 | 9.69 | 9.257060 | 0.000000000 |
| 2023postBPix | VBFH | Out workspace | 0 | 0.000000000000 | 9.69 | 9.257060 | 0.000000000 |
| 2023postBPix | VH | Input ROOT tree | 42 | 0.000159664613 | 9.69 | 5.450043 | 0.008434645 |
| 2023postBPix | VH | Inclusive workspace | 42 | 0.000159664613 | 9.69 | 5.450043 | 0.008434645 |
| 2023postBPix | VH | In workspace | 9 | 0.000032695633 | 9.69 | 5.450043 | 0.001727221 |
| 2023postBPix | VH | Out workspace | 33 | 0.000126968979 | 9.69 | 5.450043 | 0.006707424 |
| 2023postBPix | ttH | Input ROOT tree | 60,612 | 0.027968690445 | 9.69 | 1.293900 | 0.350776958 |
| 2023postBPix | ttH | Inclusive workspace | 60,612 | 0.027968690445 | 9.69 | 1.293900 | 0.350776958 |
| 2023postBPix | ttH | In workspace | 55,586 | 0.025597830003 | 9.69 | 1.293900 | 0.321042166 |
| 2023postBPix | ttH | Out workspace | 5,026 | 0.002370860442 | 9.69 | 1.293900 | 0.029734793 |
| 2023postBPix | tHqLep | Input ROOT tree | 4,386 | 0.003415238943 | 9.69 | 0.061576 | 0.002038415 |
| 2023postBPix | tHqLep | Inclusive workspace | 4,386 | 0.003415238943 | 9.69 | 0.061576 | 0.002038415 |
| 2023postBPix | tHqLep | In workspace | 4,078 | 0.003248408316 | 9.69 | 0.061576 | 0.001938841 |
| 2023postBPix | tHqLep | Out workspace | 308 | 0.000166830626 | 9.69 | 0.061576 | 0.000099574 |
| 2023postBPix | tHqHad | Input ROOT tree | 105 | 0.000125610799 | 9.69 | 0.127424 | 0.000155144 |
| 2023postBPix | tHqHad | Inclusive workspace | 105 | 0.000125610799 | 9.69 | 0.127424 | 0.000155144 |
| 2023postBPix | tHqHad | In workspace | 98 | 0.000120462867 | 9.69 | 0.127424 | 0.000148786 |
| 2023postBPix | tHqHad | Out workspace | 7 | 0.000005147933 | 9.69 | 0.127424 | 0.000006358 |
| 2023postBPix | tHW | Input ROOT tree | 7,348 | 0.023912190596 | 9.69 | 0.039044 | 0.009049652 |
| 2023postBPix | tHW | Inclusive workspace | 7,348 | 0.023912190596 | 9.69 | 0.039044 | 0.009049652 |
| 2023postBPix | tHW | In workspace | 6,707 | 0.021777255628 | 9.69 | 0.039044 | 0.008241678 |
| 2023postBPix | tHW | Out workspace | 641 | 0.002134934968 | 9.69 | 0.039044 | 0.000807974 |
| 2023postBPix | bbH | Input ROOT tree | 1 | 0.000005880911 | 9.69 | 1.196063 | 0.000068180 |
| 2023postBPix | bbH | Inclusive workspace | 1 | 0.000005880911 | 9.69 | 1.196063 | 0.000068180 |
| 2023postBPix | bbH | In workspace | 1 | 0.000005880911 | 9.69 | 1.196063 | 0.000068180 |
| 2023postBPix | bbH | Out workspace | 0 | 0.000000000000 | 9.69 | 1.196063 | 0.000000000 |
| 2024 | GluGluH | Input ROOT tree | 0 | 0.000000000000 | 109.95 | 118.562100 | 0.000000000 |
| 2024 | GluGluH | Inclusive workspace | 0 | 0.000000000000 | 109.95 | 118.562100 | 0.000000000 |
| 2024 | GluGluH | In workspace | 0 | 0.000000000000 | 109.95 | 118.562100 | 0.000000000 |
| 2024 | GluGluH | Out workspace | 0 | 0.000000000000 | 109.95 | 118.562100 | 0.000000000 |
| 2024 | VBFH | Input ROOT tree | 0 | 0.000000000000 | 109.95 | 9.257060 | 0.000000000 |
| 2024 | VBFH | Inclusive workspace | 0 | 0.000000000000 | 109.95 | 9.257060 | 0.000000000 |
| 2024 | VBFH | In workspace | 0 | 0.000000000000 | 109.95 | 9.257060 | 0.000000000 |
| 2024 | VBFH | Out workspace | 0 | 0.000000000000 | 109.95 | 9.257060 | 0.000000000 |
| 2024 | VH | Input ROOT tree | 492 | 0.000071391514 | 109.95 | 5.450043 | 0.042780096 |
| 2024 | VH | Inclusive workspace | 492 | 0.000071391514 | 109.95 | 5.450043 | 0.042780096 |
| 2024 | VH | In workspace | 199 | 0.000019452006 | 109.95 | 5.450043 | 0.011656269 |
| 2024 | VH | Out workspace | 293 | 0.000051939507 | 109.95 | 5.450043 | 0.031123827 |
| 2024 | ttH | Input ROOT tree | 43,053 | 0.028082140465 | 109.95 | 1.293900 | 3.995086196 |
| 2024 | ttH | Inclusive workspace | 43,053 | 0.028082140465 | 109.95 | 1.293900 | 3.995086196 |
| 2024 | ttH | In workspace | 41,368 | 0.026924956616 | 109.95 | 1.293900 | 3.830460240 |
| 2024 | ttH | Out workspace | 1,685 | 0.001157183848 | 109.95 | 1.293900 | 0.164625956 |
| 2024 | tHqLep | Input ROOT tree | 10,941 | 0.002849789852 | 109.95 | 0.061576 | 0.019293962 |
| 2024 | tHqLep | Inclusive workspace | 10,941 | 0.002849789852 | 109.95 | 0.061576 | 0.019293962 |
| 2024 | tHqLep | In workspace | 10,542 | 0.002772305270 | 109.95 | 0.061576 | 0.018769367 |
| 2024 | tHqLep | Out workspace | 399 | 0.000077484582 | 109.95 | 0.061576 | 0.000524595 |
| 2024 | tHqHad | Input ROOT tree | 305 | 0.000113759474 | 109.95 | 0.127424 | 0.001593800 |
| 2024 | tHqHad | Inclusive workspace | 305 | 0.000113759474 | 109.95 | 0.127424 | 0.001593800 |
| 2024 | tHqHad | In workspace | 291 | 0.000114651009 | 109.95 | 0.127424 | 0.001606291 |
| 2024 | tHqHad | Out workspace | 14 | -0.000000891535 | 109.95 | 0.127424 | -0.000012491 |
| 2024 | tHW | Input ROOT tree | 49,504 | 0.022160011126 | 109.95 | 0.039044 | 0.095130441 |
| 2024 | tHW | Inclusive workspace | 49,504 | 0.022160011126 | 109.95 | 0.039044 | 0.095130441 |
| 2024 | tHW | In workspace | 47,608 | 0.021250602876 | 109.95 | 0.039044 | 0.091226454 |
| 2024 | tHW | Out workspace | 1,896 | 0.000909408250 | 109.95 | 0.039044 | 0.003903988 |
| 2024 | bbH | Input ROOT tree | 2 | 0.000000682233 | 109.95 | 1.196063 | 0.000089718 |
| 2024 | bbH | Inclusive workspace | 2 | 0.000000682233 | 109.95 | 1.196063 | 0.000089718 |
| 2024 | bbH | In workspace | 2 | 0.000000682233 | 109.95 | 1.196063 | 0.000089718 |
| 2024 | bbH | Out workspace | 0 | 0.000000000000 | 109.95 | 1.196063 | 0.000000000 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 44 | 44.000000 | 0 |
| Data workspace | 44 | 44.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 12 | 12.000000 | 12 | 12.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 9 | 9.000000 | 9 | 9.000000 |
| Upper sideband | 130 < m ≤ 180 | 23 | 23.000000 | 23 | 23.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 35 | 35.000000 | 35 | 35.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 44 | 44.000000 | 44 | 44.000000 |
| Total | All entries | 44 | 44.000000 | 44 | 44.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_lep_2 |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_lep_2 |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_lep_2 |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_lep_2 |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_lep_2 |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_lep_2 |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_lep_2 |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_lep_2 |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_lep_2 |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_lep_2 |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_lep_2 |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_lep_2 |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_lep_2 |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_lep_2 |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_lep_2 |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_lep_2 |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_lep_2 |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_lep_2 |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_lep_2 |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_lep_2 |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_lep_2 |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_lep_2 |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_lep_2 |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_lep_2 |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_lep_2 |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_lep_2 |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_lep_2 |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_lep_2 |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_lep_2 |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_lep_2 |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_lep_2 |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_lep_2 |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_lep_2 |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_lep_2 |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_lep_2 |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_lep_2 |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_lep_2 |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_lep_2 |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_lep_2 |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_lep_2 |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_lep_2 |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_lep_2 |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_lep_2 |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_lep_2 |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_lep_2 |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_lep_2 |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_lep_2 |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_lep_2 |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_lep_2 |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_lep_2 |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_lep_2 |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_lep_2 |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_lep_2 |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_lep_2 |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_lep_2 |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_lep_2 |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_lep_2 |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_lep_2 |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_lep_2 |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_lep_2 |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_lep_2 |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_lep_2 |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_lep_2 |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_lep_2 |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_lep_2 |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_lep_2 |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_lep_2 |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_lep_2 |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_lep_2 |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_lep_2 |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_lep_2 |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_lep_2 |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_lep_2 |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_lep_2 |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_lep_2 |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_lep_2 |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_lep_2 |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_lep_2 |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_lep_2 |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_lep_2 |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_lep_2 |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_lep_2 |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_lep_2 |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_lep_2 |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_lep_2 |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_lep_2 |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_lep_2 |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_lep_2 |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_lep_2 |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_lep_2 |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_lep_2 |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_lep_2 |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_lep_2 |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_lep_2 |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_lep_2 |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_lep_2 |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_lep_2 |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_lep_2 |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_lep_2 |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_lep_2 |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_lep_2 |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_lep_2 |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_lep_2 |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_lep_2 |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_lep_2 |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_lep_2 |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_lep_2 |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_lep_2 |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_lep_2 |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_lep_2 |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_lep_2 |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_lep_2 |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_lep_2 |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_lep_2 |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_lep_2 |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_lep_2 |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_lep_2 |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_lep_2 |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_lep_2 |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_lep_2 |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_lep_2 |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_lep_2 |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_lep_2 |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_lep_2 |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_lep_2 |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_lep_2 |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_lep_2 |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_lep_2 |
| GluGluH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_ttH_lep_2 |
| GluGluH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_ttH_lep_2 |
| GluGluH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_ttH_lep_2 |
| GluGluH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_ttH_lep_2 |
| VBFH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_ttH_lep_2 |
| VBFH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_ttH_lep_2 |
| VBFH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_ttH_lep_2 |
| VBFH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_ttH_lep_2 |
| VH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_ttH_lep_2 |
| VH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_ttH_lep_2 |
| VH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_ttH_lep_2 |
| VH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_ttH_lep_2 |
| ttH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_ttH_lep_2 |
| ttH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_ttH_lep_2 |
| ttH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_ttH_lep_2 |
| ttH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_ttH_lep_2 |
| tHqLep / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_ttH_lep_2 |
| tHqLep / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_ttH_lep_2 |
| tHqLep / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_ttH_lep_2 |
| tHqLep / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_ttH_lep_2 |
| tHqHad / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_ttH_lep_2 |
| tHqHad / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_ttH_lep_2 |
| tHqHad / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_ttH_lep_2 |
| tHqHad / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_ttH_lep_2 |
| tHW / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_ttH_lep_2 |
| tHW / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_ttH_lep_2 |
| tHW / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_ttH_lep_2 |
| tHW / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_ttH_lep_2 |
| bbH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_ttH_lep_2 |
| bbH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_ttH_lep_2 |
| bbH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_ttH_lep_2 |
| bbH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_ttH_lep_2 |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/allData.root | Data_13TeV_ttH_lep_2 |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/ws/allData.root | Data_13TeV_ttH_lep_2 |
