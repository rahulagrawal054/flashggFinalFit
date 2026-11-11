# Category bookkeeping: bkg_lep

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 414 | 0.000219824798 | 118.562100 | 1.181582022 |
| GluGluH | Inclusive workspace | 414 | 0.000219824798 | 118.562100 | 1.181582022 |
| GluGluH | In workspace | 148 | 0.000054501737 | 118.562100 | 0.341135059 |
| GluGluH | Out workspace | 266 | 0.000165323061 | 118.562100 | 0.840446962 |
| VBFH | Input ROOT tree | 452 | 0.000325880225 | 9.257060 | 0.115240855 |
| VBFH | Inclusive workspace | 452 | 0.000325880225 | 9.257060 | 0.115240855 |
| VBFH | In workspace | 101 | 0.000083476868 | 9.257060 | -0.000635028 |
| VBFH | Out workspace | 351 | 0.000242403357 | 9.257060 | 0.115875883 |
| VH | Input ROOT tree | 43,875 | 0.022853211763 | 5.450043 | 4.954372449 |
| VH | Inclusive workspace | 43,875 | 0.022853211763 | 5.450043 | 4.954372449 |
| VH | In workspace | 2,693 | 0.000966100667 | 5.450043 | 0.227311977 |
| VH | Out workspace | 41,182 | 0.021887111097 | 5.450043 | 4.727060472 |
| ttH | Input ROOT tree | 167,773 | 0.093986132757 | 1.293900 | 4.148290000 |
| ttH | Inclusive workspace | 167,773 | 0.093986132757 | 1.293900 | 4.148290000 |
| ttH | In workspace | 139,012 | 0.078184671657 | 1.293900 | 3.552659881 |
| ttH | Out workspace | 28,761 | 0.015801461100 | 1.293900 | 0.595630119 |
| tHqLep | Input ROOT tree | 194,347 | 0.163586177477 | 0.061576 | 0.356230647 |
| tHqLep | Inclusive workspace | 194,347 | 0.163586177477 | 0.061576 | 0.356230647 |
| tHqLep | In workspace | 170,549 | 0.141950848509 | 0.061576 | 0.310145442 |
| tHqLep | Out workspace | 23,798 | 0.021635328968 | 0.061576 | 0.046085205 |
| tHqHad | Input ROOT tree | 7,248 | 0.004767180805 | 0.127424 | 0.021716120 |
| tHqHad | Inclusive workspace | 7,248 | 0.004767180805 | 0.127424 | 0.021716120 |
| tHqHad | In workspace | 6,577 | 0.004388239131 | 0.127424 | 0.019511220 |
| tHqHad | Out workspace | 671 | 0.000378941674 | 0.127424 | 0.002204899 |
| tHW | Input ROOT tree | 187,788 | 0.131100223502 | 0.039044 | 0.195391998 |
| tHW | Inclusive workspace | 187,788 | 0.131100223502 | 0.039044 | 0.195391998 |
| tHW | In workspace | 153,134 | 0.105538898787 | 0.039044 | 0.160714088 |
| tHW | Out workspace | 34,654 | 0.025561324715 | 0.039044 | 0.034677910 |
| bbH | Input ROOT tree | 1,088 | 0.001872354309 | 1.196063 | 0.088537449 |
| bbH | Inclusive workspace | 1,088 | 0.001872354309 | 1.196063 | 0.088537449 |
| bbH | In workspace | 936 | 0.001573762200 | 1.196063 | 0.072531843 |
| bbH | Out workspace | 152 | 0.000298592109 | 1.196063 | 0.016005606 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 602,985 | 0.418710985636 | 11.061361539 |
| Inclusive workspace | 602,985 | 0.418710985636 | 11.061361539 |
| In workspace | 473,150 | 0.332740499556 | 4.683374483 |
| Out workspace | 129,835 | 0.085970486080 | 6.377987056 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 35 | 0.000026643727 | 7.98 | 118.562100 | 0.025208311 |
| 2022preEE | GluGluH | Inclusive workspace | 35 | 0.000026643727 | 7.98 | 118.562100 | 0.025208311 |
| 2022preEE | GluGluH | In workspace | 20 | 0.000021486684 | 7.98 | 118.562100 | 0.020329101 |
| 2022preEE | GluGluH | Out workspace | 15 | 0.000005157043 | 7.98 | 118.562100 | 0.004879210 |
| 2022preEE | VBFH | Input ROOT tree | 23 | 0.000031491907 | 7.98 | 9.257060 | 0.002326349 |
| 2022preEE | VBFH | Inclusive workspace | 23 | 0.000031491907 | 7.98 | 9.257060 | 0.002326349 |
| 2022preEE | VBFH | In workspace | 6 | 0.000012716004 | 7.98 | 9.257060 | 0.000939348 |
| 2022preEE | VBFH | Out workspace | 17 | 0.000018775903 | 7.98 | 9.257060 | 0.001387001 |
| 2022preEE | VH | Input ROOT tree | 900 | 0.003835224676 | 7.98 | 5.450043 | 0.166799072 |
| 2022preEE | VH | Inclusive workspace | 900 | 0.003835224676 | 7.98 | 5.450043 | 0.166799072 |
| 2022preEE | VH | In workspace | 56 | 0.000185880997 | 7.98 | 5.450043 | 0.008084214 |
| 2022preEE | VH | Out workspace | 844 | 0.003649343679 | 7.98 | 5.450043 | 0.158714858 |
| 2022preEE | ttH | Input ROOT tree | 35,939 | 0.017904412279 | 7.98 | 1.293900 | 0.184868822 |
| 2022preEE | ttH | Inclusive workspace | 35,939 | 0.017904412279 | 7.98 | 1.293900 | 0.184868822 |
| 2022preEE | ttH | In workspace | 29,436 | 0.014725851105 | 7.98 | 1.293900 | 0.152049154 |
| 2022preEE | ttH | Out workspace | 6,503 | 0.003178561174 | 7.98 | 1.293900 | 0.032819668 |
| 2022preEE | tHqLep | Input ROOT tree | 21,762 | 0.030791359089 | 7.98 | 0.061576 | 0.015130215 |
| 2022preEE | tHqLep | Inclusive workspace | 21,762 | 0.030791359089 | 7.98 | 0.061576 | 0.015130215 |
| 2022preEE | tHqLep | In workspace | 18,961 | 0.026584443902 | 7.98 | 0.061576 | 0.013063027 |
| 2022preEE | tHqLep | Out workspace | 2,801 | 0.004206915186 | 7.98 | 0.061576 | 0.002067188 |
| 2022preEE | tHqHad | Input ROOT tree | 571 | 0.000873574280 | 7.98 | 0.127424 | 0.000888288 |
| 2022preEE | tHqHad | Inclusive workspace | 571 | 0.000873574280 | 7.98 | 0.127424 | 0.000888288 |
| 2022preEE | tHqHad | In workspace | 527 | 0.000827864571 | 7.98 | 0.127424 | 0.000841808 |
| 2022preEE | tHqHad | Out workspace | 44 | 0.000045709709 | 7.98 | 0.127424 | 0.000046480 |
| 2022preEE | tHW | Input ROOT tree | 49,859 | 0.023435187027 | 7.98 | 0.039044 | 0.007301727 |
| 2022preEE | tHW | Inclusive workspace | 49,859 | 0.023435187027 | 7.98 | 0.039044 | 0.007301727 |
| 2022preEE | tHW | In workspace | 39,944 | 0.018728059643 | 7.98 | 0.039044 | 0.005835123 |
| 2022preEE | tHW | Out workspace | 9,915 | 0.004707127384 | 7.98 | 0.039044 | 0.001466605 |
| 2022preEE | bbH | Input ROOT tree | 39 | 0.000314341897 | 7.98 | 1.196063 | 0.003000262 |
| 2022preEE | bbH | Inclusive workspace | 39 | 0.000314341897 | 7.98 | 1.196063 | 0.003000262 |
| 2022preEE | bbH | In workspace | 31 | 0.000232601637 | 7.98 | 1.196063 | 0.002220086 |
| 2022preEE | bbH | Out workspace | 8 | 0.000081740260 | 7.98 | 1.196063 | 0.000780177 |
| 2022postEE | GluGluH | Input ROOT tree | 55 | 0.000038494111 | 26.67 | 118.562100 | 0.121720351 |
| 2022postEE | GluGluH | Inclusive workspace | 55 | 0.000038494111 | 26.67 | 118.562100 | 0.121720351 |
| 2022postEE | GluGluH | In workspace | 21 | 0.000002833488 | 26.67 | 118.562100 | 0.008959634 |
| 2022postEE | GluGluH | Out workspace | 34 | 0.000035660623 | 26.67 | 118.562100 | 0.112760717 |
| 2022postEE | VBFH | Input ROOT tree | 92 | 0.000042084240 | 26.67 | 9.257060 | 0.010390001 |
| 2022postEE | VBFH | Inclusive workspace | 92 | 0.000042084240 | 26.67 | 9.257060 | 0.010390001 |
| 2022postEE | VBFH | In workspace | 18 | 0.000009752687 | 26.67 | 9.257060 | 0.002407800 |
| 2022postEE | VBFH | Out workspace | 74 | 0.000032331553 | 26.67 | 9.257060 | 0.007982201 |
| 2022postEE | VH | Input ROOT tree | 3,000 | 0.003827705321 | 26.67 | 5.450043 | 0.556367100 |
| 2022postEE | VH | Inclusive workspace | 3,000 | 0.003827705321 | 26.67 | 5.450043 | 0.556367100 |
| 2022postEE | VH | In workspace | 166 | 0.000142941536 | 26.67 | 5.450043 | 0.020776931 |
| 2022postEE | VH | Out workspace | 2,834 | 0.003684763785 | 26.67 | 5.450043 | 0.535590169 |
| 2022postEE | ttH | Input ROOT tree | 35,451 | 0.017258034016 | 26.67 | 1.293900 | 0.595545640 |
| 2022postEE | ttH | Inclusive workspace | 35,451 | 0.017258034016 | 26.67 | 1.293900 | 0.595545640 |
| 2022postEE | ttH | In workspace | 29,100 | 0.014079291973 | 26.67 | 1.293900 | 0.485852614 |
| 2022postEE | ttH | Out workspace | 6,351 | 0.003178742043 | 26.67 | 1.293900 | 0.109693025 |
| 2022postEE | tHqLep | Input ROOT tree | 42,408 | 0.029165222106 | 26.67 | 0.061576 | 0.047896265 |
| 2022postEE | tHqLep | Inclusive workspace | 42,408 | 0.029165222106 | 26.67 | 0.061576 | 0.047896265 |
| 2022postEE | tHqLep | In workspace | 37,340 | 0.025786358951 | 26.67 | 0.061576 | 0.042347364 |
| 2022postEE | tHqLep | Out workspace | 5,068 | 0.003378863155 | 26.67 | 0.061576 | 0.005548901 |
| 2022postEE | tHqHad | Input ROOT tree | 1,759 | 0.000902822417 | 26.67 | 0.127424 | 0.003068148 |
| 2022postEE | tHqHad | Inclusive workspace | 1,759 | 0.000902822417 | 26.67 | 0.127424 | 0.003068148 |
| 2022postEE | tHqHad | In workspace | 1,584 | 0.000836670395 | 26.67 | 0.127424 | 0.002843338 |
| 2022postEE | tHqHad | Out workspace | 175 | 0.000066152022 | 26.67 | 0.127424 | 0.000224811 |
| 2022postEE | tHW | Input ROOT tree | 49,476 | 0.022751157149 | 26.67 | 0.039044 | 0.023690859 |
| 2022postEE | tHW | Inclusive workspace | 49,476 | 0.022751157149 | 26.67 | 0.039044 | 0.023690859 |
| 2022postEE | tHW | In workspace | 39,519 | 0.018027300707 | 26.67 | 0.039044 | 0.018771891 |
| 2022postEE | tHW | Out workspace | 9,957 | 0.004723856441 | 26.67 | 0.039044 | 0.004918968 |
| 2022postEE | bbH | Input ROOT tree | 133 | 0.000367808911 | 26.67 | 1.196063 | 0.011732737 |
| 2022postEE | bbH | Inclusive workspace | 133 | 0.000367808911 | 26.67 | 1.196063 | 0.011732737 |
| 2022postEE | bbH | In workspace | 120 | 0.000324121924 | 26.67 | 1.196063 | 0.010339165 |
| 2022postEE | bbH | Out workspace | 13 | 0.000043686988 | 26.67 | 1.196063 | 0.001393571 |
| 2023preBPix | GluGluH | Input ROOT tree | 101 | 0.000056957877 | 18.06 | 118.562100 | 0.121980260 |
| 2023preBPix | GluGluH | Inclusive workspace | 101 | 0.000056957877 | 18.06 | 118.562100 | 0.121980260 |
| 2023preBPix | GluGluH | In workspace | 31 | 0.000012301316 | 18.06 | 118.562100 | 0.026344340 |
| 2023preBPix | GluGluH | Out workspace | 70 | 0.000044656561 | 18.06 | 118.562100 | 0.095635920 |
| 2023preBPix | VBFH | Input ROOT tree | 94 | 0.000071649427 | 18.06 | 9.257060 | 0.011980520 |
| 2023preBPix | VBFH | Inclusive workspace | 94 | 0.000071649427 | 18.06 | 9.257060 | 0.011980520 |
| 2023preBPix | VBFH | In workspace | 22 | 0.000028652064 | 18.06 | 9.257060 | 0.004790920 |
| 2023preBPix | VBFH | Out workspace | 72 | 0.000042997363 | 18.06 | 9.257060 | 0.007189601 |
| 2023preBPix | VH | Input ROOT tree | 2,271 | 0.004744893577 | 18.06 | 5.450043 | 0.467106904 |
| 2023preBPix | VH | Inclusive workspace | 2,271 | 0.004744893577 | 18.06 | 5.450043 | 0.467106904 |
| 2023preBPix | VH | In workspace | 113 | 0.000215022974 | 18.06 | 5.450043 | 0.021167749 |
| 2023preBPix | VH | Out workspace | 2,158 | 0.004529870603 | 18.06 | 5.450043 | 0.445939156 |
| 2023preBPix | ttH | Input ROOT tree | 32,542 | 0.019880779451 | 18.06 | 1.293900 | 0.464647925 |
| 2023preBPix | ttH | Inclusive workspace | 32,542 | 0.019880779451 | 18.06 | 1.293900 | 0.464647925 |
| 2023preBPix | ttH | In workspace | 26,626 | 0.016188321798 | 18.06 | 1.293900 | 0.378348855 |
| 2023preBPix | ttH | Out workspace | 5,916 | 0.003692457654 | 18.06 | 1.293900 | 0.086299071 |
| 2023preBPix | tHqLep | Input ROOT tree | 5,537 | 0.035845812983 | 18.06 | 0.061576 | 0.039869580 |
| 2023preBPix | tHqLep | Inclusive workspace | 5,537 | 0.035845812983 | 18.06 | 0.061576 | 0.039869580 |
| 2023preBPix | tHqLep | In workspace | 4,769 | 0.030602667960 | 18.06 | 0.061576 | 0.034037881 |
| 2023preBPix | tHqLep | Out workspace | 768 | 0.005243145023 | 18.06 | 0.061576 | 0.005831699 |
| 2023preBPix | tHqHad | Input ROOT tree | 1,639 | 0.000968854117 | 18.06 | 0.127424 | 0.002229971 |
| 2023preBPix | tHqHad | Inclusive workspace | 1,639 | 0.000968854117 | 18.06 | 0.127424 | 0.002229971 |
| 2023preBPix | tHqHad | In workspace | 1,503 | 0.000902346059 | 18.06 | 0.127424 | 0.002076893 |
| 2023preBPix | tHqHad | Out workspace | 136 | 0.000066508058 | 18.06 | 0.127424 | 0.000153079 |
| 2023preBPix | tHW | Input ROOT tree | 16,402 | 0.026685490917 | 18.06 | 0.039044 | 0.018819990 |
| 2023preBPix | tHW | Inclusive workspace | 16,402 | 0.026685490917 | 18.06 | 0.039044 | 0.018819990 |
| 2023preBPix | tHW | In workspace | 13,168 | 0.021225530112 | 18.06 | 0.039044 | 0.014969343 |
| 2023preBPix | tHW | Out workspace | 3,234 | 0.005459960805 | 18.06 | 0.039044 | 0.003850647 |
| 2023preBPix | bbH | Input ROOT tree | 152 | 0.000406142959 | 18.06 | 1.196063 | 0.008774510 |
| 2023preBPix | bbH | Inclusive workspace | 152 | 0.000406142959 | 18.06 | 1.196063 | 0.008774510 |
| 2023preBPix | bbH | In workspace | 135 | 0.000346306503 | 18.06 | 1.196063 | 0.007481774 |
| 2023preBPix | bbH | Out workspace | 17 | 0.000059836456 | 18.06 | 1.196063 | 0.001292736 |
| 2023postBPix | GluGluH | Input ROOT tree | 53 | 0.000030396522 | 9.69 | 118.562100 | 0.034932365 |
| 2023postBPix | GluGluH | Inclusive workspace | 53 | 0.000030396522 | 9.69 | 118.562100 | 0.034932365 |
| 2023postBPix | GluGluH | In workspace | 16 | -0.000004409707 | 9.69 | 118.562100 | -0.005067734 |
| 2023postBPix | GluGluH | Out workspace | 37 | 0.000034806229 | 9.69 | 118.562100 | 0.040000099 |
| 2023postBPix | VBFH | Input ROOT tree | 46 | 0.000100560613 | 9.69 | 9.257060 | 0.009023171 |
| 2023postBPix | VBFH | Inclusive workspace | 46 | 0.000100560613 | 9.69 | 9.257060 | 0.009023171 |
| 2023postBPix | VBFH | In workspace | 8 | 0.000044937252 | 9.69 | 9.257060 | 0.004032160 |
| 2023postBPix | VBFH | Out workspace | 38 | 0.000055623361 | 9.69 | 9.257060 | 0.004991011 |
| 2023postBPix | VH | Input ROOT tree | 1,043 | 0.004566418758 | 9.69 | 5.450043 | 0.241231422 |
| 2023postBPix | VH | Inclusive workspace | 1,043 | 0.004566418758 | 9.69 | 5.450043 | 0.241231422 |
| 2023postBPix | VH | In workspace | 59 | 0.000138625786 | 9.69 | 5.450043 | 0.007323221 |
| 2023postBPix | VH | Out workspace | 984 | 0.004427792972 | 9.69 | 5.450043 | 0.233908201 |
| 2023postBPix | ttH | Input ROOT tree | 39,476 | 0.020327678935 | 9.69 | 1.293900 | 0.254945129 |
| 2023postBPix | ttH | Inclusive workspace | 39,476 | 0.020327678935 | 9.69 | 1.293900 | 0.254945129 |
| 2023postBPix | ttH | In workspace | 32,525 | 0.016847610574 | 9.69 | 1.293900 | 0.211298902 |
| 2023postBPix | ttH | Out workspace | 6,951 | 0.003480068361 | 9.69 | 1.293900 | 0.043646226 |
| 2023postBPix | tHqLep | Input ROOT tree | 33,962 | 0.033301089121 | 9.69 | 0.061576 | 0.019876046 |
| 2023postBPix | tHqLep | Inclusive workspace | 33,962 | 0.033301089121 | 9.69 | 0.061576 | 0.019876046 |
| 2023postBPix | tHqLep | In workspace | 29,638 | 0.028930004079 | 9.69 | 0.061576 | 0.017267126 |
| 2023postBPix | tHqLep | Out workspace | 4,324 | 0.004371085042 | 9.69 | 0.061576 | 0.002608920 |
| 2023postBPix | tHqHad | Input ROOT tree | 934 | 0.001001793685 | 9.69 | 0.127424 | 0.001237336 |
| 2023postBPix | tHqHad | Inclusive workspace | 934 | 0.001001793685 | 9.69 | 0.127424 | 0.001237336 |
| 2023postBPix | tHqHad | In workspace | 850 | 0.000921204800 | 9.69 | 0.127424 | 0.001137799 |
| 2023postBPix | tHqHad | Out workspace | 84 | 0.000080588885 | 9.69 | 0.127424 | 0.000099537 |
| 2023postBPix | tHW | Input ROOT tree | 8,174 | 0.026667586688 | 9.69 | 0.039044 | 0.010092441 |
| 2023postBPix | tHW | Inclusive workspace | 8,174 | 0.026667586688 | 9.69 | 0.039044 | 0.010092441 |
| 2023postBPix | tHW | In workspace | 6,535 | 0.021209568229 | 9.69 | 0.039044 | 0.008026835 |
| 2023postBPix | tHW | Out workspace | 1,639 | 0.005458018459 | 9.69 | 0.039044 | 0.002065606 |
| 2023postBPix | bbH | Input ROOT tree | 62 | 0.000317558483 | 9.69 | 1.196063 | 0.003681595 |
| 2023postBPix | bbH | Inclusive workspace | 62 | 0.000317558483 | 9.69 | 1.196063 | 0.003681595 |
| 2023postBPix | bbH | In workspace | 58 | 0.000297841211 | 9.69 | 1.196063 | 0.003453004 |
| 2023postBPix | bbH | Out workspace | 4 | 0.000019717272 | 9.69 | 1.196063 | 0.000228591 |
| 2024 | GluGluH | Input ROOT tree | 170 | 0.000067332562 | 109.95 | 118.562100 | 0.877740734 |
| 2024 | GluGluH | Inclusive workspace | 170 | 0.000067332562 | 109.95 | 118.562100 | 0.877740734 |
| 2024 | GluGluH | In workspace | 60 | 0.000022289957 | 109.95 | 118.562100 | 0.290569719 |
| 2024 | GluGluH | Out workspace | 110 | 0.000045042604 | 109.95 | 118.562100 | 0.587171015 |
| 2024 | VBFH | Input ROOT tree | 197 | 0.000080094038 | 109.95 | 9.257060 | 0.081520813 |
| 2024 | VBFH | Inclusive workspace | 197 | 0.000080094038 | 109.95 | 9.257060 | 0.081520813 |
| 2024 | VBFH | In workspace | 47 | -0.000012581139 | 109.95 | 9.257060 | -0.012805257 |
| 2024 | VBFH | Out workspace | 150 | 0.000092675177 | 109.95 | 9.257060 | 0.094326069 |
| 2024 | VH | Input ROOT tree | 36,661 | 0.005878969432 | 109.95 | 5.450043 | 3.522867950 |
| 2024 | VH | Inclusive workspace | 36,661 | 0.005878969432 | 109.95 | 5.450043 | 3.522867950 |
| 2024 | VH | In workspace | 2,299 | 0.000283629375 | 109.95 | 5.450043 | 0.169959862 |
| 2024 | VH | Out workspace | 34,362 | 0.005595340057 | 109.95 | 5.450043 | 3.352908088 |
| 2024 | ttH | Input ROOT tree | 24,365 | 0.018615228076 | 109.95 | 1.293900 | 2.648282485 |
| 2024 | ttH | Inclusive workspace | 24,365 | 0.018615228076 | 109.95 | 1.293900 | 2.648282485 |
| 2024 | ttH | In workspace | 21,325 | 0.016343596208 | 109.95 | 1.293900 | 2.325110356 |
| 2024 | ttH | Out workspace | 3,040 | 0.002271631868 | 109.95 | 1.293900 | 0.323172129 |
| 2024 | tHqLep | Input ROOT tree | 90,678 | 0.034482694179 | 109.95 | 0.061576 | 0.233458541 |
| 2024 | tHqLep | Inclusive workspace | 90,678 | 0.034482694179 | 109.95 | 0.061576 | 0.233458541 |
| 2024 | tHqLep | In workspace | 79,841 | 0.030047373617 | 109.95 | 0.061576 | 0.203430045 |
| 2024 | tHqLep | Out workspace | 10,837 | 0.004435320562 | 109.95 | 0.061576 | 0.030028497 |
| 2024 | tHqHad | Input ROOT tree | 2,345 | 0.001020136305 | 109.95 | 0.127424 | 0.014292377 |
| 2024 | tHqHad | Inclusive workspace | 2,345 | 0.001020136305 | 109.95 | 0.127424 | 0.014292377 |
| 2024 | tHqHad | In workspace | 2,113 | 0.000900153305 | 109.95 | 0.127424 | 0.012611383 |
| 2024 | tHqHad | Out workspace | 232 | 0.000119983000 | 109.95 | 0.127424 | 0.001680993 |
| 2024 | tHW | Input ROOT tree | 63,877 | 0.031560801720 | 109.95 | 0.039044 | 0.135486981 |
| 2024 | tHW | Inclusive workspace | 63,877 | 0.031560801720 | 109.95 | 0.039044 | 0.135486981 |
| 2024 | tHW | In workspace | 53,968 | 0.026348440096 | 109.95 | 0.039044 | 0.113110897 |
| 2024 | tHW | Out workspace | 9,909 | 0.005212361625 | 109.95 | 0.039044 | 0.022376084 |
| 2024 | bbH | Input ROOT tree | 702 | 0.000466502059 | 109.95 | 1.196063 | 0.061348345 |
| 2024 | bbH | Inclusive workspace | 702 | 0.000466502059 | 109.95 | 1.196063 | 0.061348345 |
| 2024 | bbH | In workspace | 592 | 0.000372890925 | 109.95 | 1.196063 | 0.049037814 |
| 2024 | bbH | Out workspace | 110 | 0.000093611134 | 109.95 | 1.196063 | 0.012310531 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 2,409 | 2409.000000 | 0 |
| Data workspace | 2,409 | 2409.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 1,250 | 1250.000000 | 1,250 | 1250.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 363 | 363.000000 | 363 | 363.000000 |
| Upper sideband | 130 < m ≤ 180 | 796 | 796.000000 | 796 | 796.000000 |
| Above range | m > 180 | 0 | 0.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 2,046 | 2046.000000 | 2,046 | 2046.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 2,409 | 2409.000000 | 2,409 | 2409.000000 |
| Total | All entries | 2,409 | 2409.000000 | 2,409 | 2409.000000 |

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
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| GluGluH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_bkg_lep |
| GluGluH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_bkg_lep |
| GluGluH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_bkg_lep |
| GluGluH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/GluGluH_2024/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_bkg_lep |
| VBFH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_bkg_lep |
| VBFH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_bkg_lep |
| VBFH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_bkg_lep |
| VBFH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VBFH_2024/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_bkg_lep |
| VH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_bkg_lep |
| VH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_bkg_lep |
| VH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_bkg_lep |
| VH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/VH_2024/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_bkg_lep |
| ttH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_bkg_lep |
| ttH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_bkg_lep |
| ttH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_bkg_lep |
| ttH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/ttH_2024/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_bkg_lep |
| tHqLep / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_bkg_lep |
| tHqLep / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_bkg_lep |
| tHqLep / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_bkg_lep |
| tHqLep / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqLep_2024/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_bkg_lep |
| tHqHad / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_bkg_lep |
| tHqHad / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_bkg_lep |
| tHqHad / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_bkg_lep |
| tHqHad / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHqHad_2024/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_bkg_lep |
| tHW / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_bkg_lep |
| tHW / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_bkg_lep |
| tHW / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_bkg_lep |
| tHW / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/tHW_2024/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_bkg_lep |
| bbH / 2024 / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_bkg_lep |
| bbH / 2024 / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_bkg_lep |
| bbH / 2024 / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_bkg_lep |
| bbH / 2024 / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/bbH_2024/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_bkg_lep |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/allData.root | Data_13TeV_bkg_lep |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_10Nov/Data/ws/allData.root | Data_13TeV_bkg_lep |
