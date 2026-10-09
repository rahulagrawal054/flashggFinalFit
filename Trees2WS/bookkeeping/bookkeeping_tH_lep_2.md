# Category bookkeeping: tH_lep_2

Input directory: `/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June`

MC uses nominal datasets only. Events are unweighted entry counts; Σ weight is the sum of event weights. Expected yield = Σ weight × Lumi × XS × BR.

Normalization values follow `Trees2WS/calc_yields.py`; the upstream normalization of `weight` must be verified separately. Mass regions are in GeV.

## MC: totals across selected eras

| Process | Version | Events | Σ weight | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- |
| GluGluH | Input ROOT tree | 28 | 0.000006125328 | 118.562100 | 0.015996467 |
| GluGluH | Inclusive workspace | 28 | 0.000006125328 | 118.562100 | 0.015996467 |
| GluGluH | In workspace | 22 | 0.000006609960 | 118.562100 | 0.016253002 |
| GluGluH | Out workspace | 6 | -0.000000484632 | 118.562100 | -0.000256535 |
| VBFH | Input ROOT tree | 15 | 0.000064299243 | 9.257060 | 0.007396721 |
| VBFH | Inclusive workspace | 15 | 0.000064299243 | 9.257060 | 0.007396721 |
| VBFH | In workspace | 8 | 0.000045974125 | 9.257060 | 0.005221926 |
| VBFH | Out workspace | 7 | 0.000018325118 | 9.257060 | 0.002174795 |
| VH | Input ROOT tree | 487 | 0.000942563242 | 5.450043 | 0.086781550 |
| VH | Inclusive workspace | 487 | 0.000942563242 | 5.450043 | 0.086781550 |
| VH | In workspace | 103 | 0.000059429754 | 5.450043 | 0.006410143 |
| VH | Out workspace | 384 | 0.000883133488 | 5.450043 | 0.080371407 |
| ttH | Input ROOT tree | 84,827 | 0.032326392064 | 1.293900 | 0.646215166 |
| ttH | Inclusive workspace | 84,827 | 0.032326392064 | 1.293900 | 0.646215166 |
| ttH | In workspace | 74,706 | 0.028708314422 | 1.293900 | 0.571540891 |
| ttH | Out workspace | 10,121 | 0.003618077642 | 1.293900 | 0.074674275 |
| tHqLep | Input ROOT tree | 126,807 | 0.098300127248 | 0.061576 | 0.092310852 |
| tHqLep | Inclusive workspace | 126,807 | 0.098300127248 | 0.061576 | 0.092310852 |
| tHqLep | In workspace | 119,439 | 0.092307274581 | 0.061576 | 0.086575151 |
| tHqLep | Out workspace | 7,368 | 0.005992852668 | 0.061576 | 0.005735701 |
| tHqHad | Input ROOT tree | 1,446 | 0.001194662508 | 0.127424 | 0.002309103 |
| tHqHad | Inclusive workspace | 1,446 | 0.001194662508 | 0.127424 | 0.002309103 |
| tHqHad | In workspace | 1,405 | 0.001192647555 | 0.127424 | 0.002296107 |
| tHqHad | Out workspace | 41 | 0.000002014953 | 0.127424 | 0.000012997 |
| tHW | Input ROOT tree | 102,487 | 0.044556251799 | 0.039044 | 0.026650230 |
| tHW | Inclusive workspace | 102,487 | 0.044556251799 | 0.039044 | 0.026650230 |
| tHW | In workspace | 91,469 | 0.039655901653 | 0.039044 | 0.023700484 |
| tHW | Out workspace | 11,018 | 0.004900350146 | 0.039044 | 0.002949745 |
| bbH | Input ROOT tree | 20 | 0.000055287922 | 1.196063 | 0.001370391 |
| bbH | Inclusive workspace | 20 | 0.000055287922 | 1.196063 | 0.001370391 |
| bbH | In workspace | 20 | 0.000055287922 | 1.196063 | 0.001370391 |
| bbH | Out workspace | 0 | 0.000000000000 | 1.196063 | 0.000000000 |

## MC: total category yield across processes and eras

| Version | Events | Σ weight | Yield |
| --- | --- | --- | --- |
| Input ROOT tree | 316,117 | 0.177445709355 | 0.879030479 |
| Inclusive workspace | 316,117 | 0.177445709355 | 0.879030479 |
| In workspace | 287,172 | 0.162031439972 | 0.713368095 |
| Out workspace | 28,945 | 0.015414269383 | 0.165662384 |

Yields are summed after each process and era receives its own normalization. The combined Σ weight is a bookkeeping sum, not a common-normalization yield.

## MC: per-era bookkeeping

| Era | Process | Version | Events | Σ weight | Lumi (fb⁻¹) | XS × BR (fb) | Yield |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2022preEE | GluGluH | Input ROOT tree | 3 | 0.000001558545 | 7.98 | 118.562100 | 0.001474579 |
| 2022preEE | GluGluH | Inclusive workspace | 3 | 0.000001558545 | 7.98 | 118.562100 | 0.001474579 |
| 2022preEE | GluGluH | In workspace | 3 | 0.000001558545 | 7.98 | 118.562100 | 0.001474579 |
| 2022preEE | GluGluH | Out workspace | 0 | 0.000000000000 | 7.98 | 118.562100 | 0.000000000 |
| 2022preEE | VBFH | Input ROOT tree | 1 | 0.000016042247 | 7.98 | 9.257060 | 0.001185062 |
| 2022preEE | VBFH | Inclusive workspace | 1 | 0.000016042247 | 7.98 | 9.257060 | 0.001185062 |
| 2022preEE | VBFH | In workspace | 1 | 0.000016042247 | 7.98 | 9.257060 | 0.001185062 |
| 2022preEE | VBFH | Out workspace | 0 | 0.000000000000 | 7.98 | 9.257060 | 0.000000000 |
| 2022preEE | VH | Input ROOT tree | 82 | 0.000168356909 | 7.98 | 5.450043 | 0.007322068 |
| 2022preEE | VH | Inclusive workspace | 82 | 0.000168356909 | 7.98 | 5.450043 | 0.007322068 |
| 2022preEE | VH | In workspace | 18 | 0.000021557495 | 7.98 | 5.450043 | 0.000937564 |
| 2022preEE | VH | Out workspace | 64 | 0.000146799415 | 7.98 | 5.450043 | 0.006384504 |
| 2022preEE | ttH | Input ROOT tree | 14,716 | 0.008417492109 | 7.98 | 1.293900 | 0.086913316 |
| 2022preEE | ttH | Inclusive workspace | 14,716 | 0.008417492109 | 7.98 | 1.293900 | 0.086913316 |
| 2022preEE | ttH | In workspace | 12,987 | 0.007507526621 | 7.98 | 1.293900 | 0.077517630 |
| 2022preEE | ttH | Out workspace | 1,729 | 0.000909965488 | 7.98 | 1.293900 | 0.009395687 |
| 2022preEE | tHqLep | Input ROOT tree | 17,746 | 0.026260080354 | 7.98 | 0.061576 | 0.012903641 |
| 2022preEE | tHqLep | Inclusive workspace | 17,746 | 0.026260080354 | 7.98 | 0.061576 | 0.012903641 |
| 2022preEE | tHqLep | In workspace | 16,649 | 0.024600452512 | 7.98 | 0.061576 | 0.012088136 |
| 2022preEE | tHqLep | Out workspace | 1,097 | 0.001659627842 | 7.98 | 0.061576 | 0.000815506 |
| 2022preEE | tHqHad | Input ROOT tree | 199 | 0.000416944451 | 7.98 | 0.127424 | 0.000423967 |
| 2022preEE | tHqHad | Inclusive workspace | 199 | 0.000416944451 | 7.98 | 0.127424 | 0.000423967 |
| 2022preEE | tHqHad | In workspace | 198 | 0.000409361983 | 7.98 | 0.127424 | 0.000416257 |
| 2022preEE | tHqHad | Out workspace | 1 | 0.000007582468 | 7.98 | 0.127424 | 0.000007710 |
| 2022preEE | tHW | Input ROOT tree | 24,949 | 0.011541974743 | 7.98 | 0.039044 | 0.003596146 |
| 2022preEE | tHW | Inclusive workspace | 24,949 | 0.011541974743 | 7.98 | 0.039044 | 0.003596146 |
| 2022preEE | tHW | In workspace | 22,257 | 0.010288450817 | 7.98 | 0.039044 | 0.003205584 |
| 2022preEE | tHW | Out workspace | 2,692 | 0.001253523926 | 7.98 | 0.039044 | 0.000390562 |
| 2022preEE | bbH | Input ROOT tree | 2 | -0.000007606180 | 7.98 | 1.196063 | -0.000072598 |
| 2022preEE | bbH | Inclusive workspace | 2 | -0.000007606180 | 7.98 | 1.196063 | -0.000072598 |
| 2022preEE | bbH | In workspace | 2 | -0.000007606180 | 7.98 | 1.196063 | -0.000072598 |
| 2022preEE | bbH | Out workspace | 0 | 0.000000000000 | 7.98 | 1.196063 | 0.000000000 |
| 2022postEE | GluGluH | Input ROOT tree | 15 | 0.000004960601 | 26.68 | 118.562100 | 0.015691556 |
| 2022postEE | GluGluH | Inclusive workspace | 15 | 0.000004960601 | 26.68 | 118.562100 | 0.015691556 |
| 2022postEE | GluGluH | In workspace | 12 | 0.000004325492 | 26.68 | 118.562100 | 0.013682556 |
| 2022postEE | GluGluH | Out workspace | 3 | 0.000000635109 | 26.68 | 118.562100 | 0.002009000 |
| 2022postEE | VBFH | Input ROOT tree | 3 | 0.000004087409 | 26.68 | 9.257060 | 0.001009502 |
| 2022postEE | VBFH | Inclusive workspace | 3 | 0.000004087409 | 26.68 | 9.257060 | 0.001009502 |
| 2022postEE | VBFH | In workspace | 1 | 0.000004463335 | 26.68 | 9.257060 | 0.001102347 |
| 2022postEE | VBFH | Out workspace | 2 | -0.000000375926 | 26.68 | 9.257060 | -0.000092845 |
| 2022postEE | VH | Input ROOT tree | 204 | 0.000282268434 | 26.68 | 5.450043 | 0.041043848 |
| 2022postEE | VH | Inclusive workspace | 204 | 0.000282268434 | 26.68 | 5.450043 | 0.041043848 |
| 2022postEE | VH | In workspace | 40 | 0.000010032378 | 26.68 | 5.450043 | 0.001458779 |
| 2022postEE | VH | Out workspace | 164 | 0.000272236056 | 26.68 | 5.450043 | 0.039585068 |
| 2022postEE | ttH | Input ROOT tree | 41,095 | 0.007765499087 | 26.68 | 1.293900 | 0.268074751 |
| 2022postEE | ttH | Inclusive workspace | 41,095 | 0.007765499087 | 26.68 | 1.293900 | 0.268074751 |
| 2022postEE | ttH | In workspace | 36,158 | 0.006817087468 | 26.68 | 1.293900 | 0.235334394 |
| 2022postEE | ttH | Out workspace | 4,937 | 0.000948411618 | 26.68 | 1.293900 | 0.032740356 |
| 2022postEE | tHqLep | Input ROOT tree | 39,954 | 0.022401461948 | 26.68 | 0.061576 | 0.036802348 |
| 2022postEE | tHqLep | Inclusive workspace | 39,954 | 0.022401461948 | 26.68 | 0.061576 | 0.036802348 |
| 2022postEE | tHqLep | In workspace | 37,677 | 0.021065965979 | 26.68 | 0.061576 | 0.034608322 |
| 2022postEE | tHqLep | Out workspace | 2,277 | 0.001335495969 | 26.68 | 0.061576 | 0.002194026 |
| 2022postEE | tHqHad | Input ROOT tree | 443 | 0.000285126287 | 26.68 | 0.127424 | 0.000969335 |
| 2022postEE | tHqHad | Inclusive workspace | 443 | 0.000285126287 | 26.68 | 0.127424 | 0.000969335 |
| 2022postEE | tHqHad | In workspace | 429 | 0.000277852195 | 26.68 | 0.127424 | 0.000944606 |
| 2022postEE | tHqHad | Out workspace | 14 | 0.000007274091 | 26.68 | 0.127424 | 0.000024730 |
| 2022postEE | tHW | Input ROOT tree | 67,200 | 0.010539763307 | 26.68 | 0.039044 | 0.010979207 |
| 2022postEE | tHW | Inclusive workspace | 67,200 | 0.010539763307 | 26.68 | 0.039044 | 0.010979207 |
| 2022postEE | tHW | In workspace | 59,985 | 0.009364304201 | 26.68 | 0.039044 | 0.009754739 |
| 2022postEE | tHW | Out workspace | 7,215 | 0.001175459106 | 26.68 | 0.039044 | 0.001224469 |
| 2022postEE | bbH | Input ROOT tree | 6 | 0.000019910415 | 26.68 | 1.196063 | 0.000635360 |
| 2022postEE | bbH | Inclusive workspace | 6 | 0.000019910415 | 26.68 | 1.196063 | 0.000635360 |
| 2022postEE | bbH | In workspace | 6 | 0.000019910415 | 26.68 | 1.196063 | 0.000635360 |
| 2022postEE | bbH | Out workspace | 0 | 0.000000000000 | 26.68 | 1.196063 | 0.000000000 |
| 2023preBPix | GluGluH | Input ROOT tree | 8 | -0.000000731073 | 17.96 | 118.562100 | -0.001556730 |
| 2023preBPix | GluGluH | Inclusive workspace | 8 | -0.000000731073 | 17.96 | 118.562100 | -0.001556730 |
| 2023preBPix | GluGluH | In workspace | 6 | 0.000000267639 | 17.96 | 118.562100 | 0.000569904 |
| 2023preBPix | GluGluH | Out workspace | 2 | -0.000000998712 | 17.96 | 118.562100 | -0.002126633 |
| 2023preBPix | VBFH | Input ROOT tree | 7 | 0.000016232465 | 17.96 | 9.257060 | 0.002698758 |
| 2023preBPix | VBFH | Inclusive workspace | 7 | 0.000016232465 | 17.96 | 9.257060 | 0.002698758 |
| 2023preBPix | VBFH | In workspace | 4 | 0.000008510579 | 17.96 | 9.257060 | 0.001414942 |
| 2023preBPix | VBFH | Out workspace | 3 | 0.000007721886 | 17.96 | 9.257060 | 0.001283816 |
| 2023preBPix | VH | Input ROOT tree | 136 | 0.000276174599 | 17.96 | 5.450043 | 0.027032735 |
| 2023preBPix | VH | Inclusive workspace | 136 | 0.000276174599 | 17.96 | 5.450043 | 0.027032735 |
| 2023preBPix | VH | In workspace | 34 | 0.000056398670 | 17.96 | 5.450043 | 0.005520458 |
| 2023preBPix | VH | Out workspace | 102 | 0.000219775930 | 17.96 | 5.450043 | 0.021512277 |
| 2023preBPix | ttH | Input ROOT tree | 18,488 | 0.008310248233 | 17.96 | 1.293900 | 0.193117238 |
| 2023preBPix | ttH | Inclusive workspace | 18,488 | 0.008310248233 | 17.96 | 1.293900 | 0.193117238 |
| 2023preBPix | ttH | In workspace | 16,296 | 0.007330356062 | 17.96 | 1.293900 | 0.170346069 |
| 2023preBPix | ttH | Out workspace | 2,192 | 0.000979892171 | 17.96 | 1.293900 | 0.022771169 |
| 2023preBPix | tHqLep | Input ROOT tree | 50,666 | 0.025531698189 | 17.96 | 0.061576 | 0.028235753 |
| 2023preBPix | tHqLep | Inclusive workspace | 50,666 | 0.025531698189 | 17.96 | 0.061576 | 0.028235753 |
| 2023preBPix | tHqLep | In workspace | 47,660 | 0.023689302776 | 17.96 | 0.061576 | 0.026198230 |
| 2023preBPix | tHqLep | Out workspace | 3,006 | 0.001842395413 | 17.96 | 0.061576 | 0.002037523 |
| 2023preBPix | tHqHad | Input ROOT tree | 537 | 0.000292119616 | 17.96 | 0.127424 | 0.000668526 |
| 2023preBPix | tHqHad | Inclusive workspace | 537 | 0.000292119616 | 17.96 | 0.127424 | 0.000668526 |
| 2023preBPix | tHqHad | In workspace | 520 | 0.000295534972 | 17.96 | 0.127424 | 0.000676342 |
| 2023preBPix | tHqHad | Out workspace | 17 | -0.000003415356 | 17.96 | 0.127424 | -0.000007816 |
| 2023preBPix | tHW | Input ROOT tree | 6,813 | 0.011076087944 | 17.96 | 0.039044 | 0.007766888 |
| 2023preBPix | tHW | Inclusive workspace | 6,813 | 0.011076087944 | 17.96 | 0.039044 | 0.007766888 |
| 2023preBPix | tHW | In workspace | 6,078 | 0.009836708819 | 17.96 | 0.039044 | 0.006897798 |
| 2023preBPix | tHW | Out workspace | 735 | 0.001239379126 | 17.96 | 0.039044 | 0.000869090 |
| 2023preBPix | bbH | Input ROOT tree | 10 | 0.000031299132 | 17.96 | 1.196063 | 0.000672346 |
| 2023preBPix | bbH | Inclusive workspace | 10 | 0.000031299132 | 17.96 | 1.196063 | 0.000672346 |
| 2023preBPix | bbH | In workspace | 10 | 0.000031299132 | 17.96 | 1.196063 | 0.000672346 |
| 2023preBPix | bbH | Out workspace | 0 | 0.000000000000 | 17.96 | 1.196063 | 0.000000000 |
| 2023postBPix | GluGluH | Input ROOT tree | 2 | 0.000000337256 | 9.68 | 118.562100 | 0.000387062 |
| 2023postBPix | GluGluH | Inclusive workspace | 2 | 0.000000337256 | 9.68 | 118.562100 | 0.000387062 |
| 2023postBPix | GluGluH | In workspace | 1 | 0.000000458284 | 9.68 | 118.562100 | 0.000525964 |
| 2023postBPix | GluGluH | Out workspace | 1 | -0.000000121028 | 9.68 | 118.562100 | -0.000138902 |
| 2023postBPix | VBFH | Input ROOT tree | 4 | 0.000027937122 | 9.68 | 9.257060 | 0.002503399 |
| 2023postBPix | VBFH | Inclusive workspace | 4 | 0.000027937122 | 9.68 | 9.257060 | 0.002503399 |
| 2023postBPix | VBFH | In workspace | 2 | 0.000016957965 | 9.68 | 9.257060 | 0.001519575 |
| 2023postBPix | VBFH | Out workspace | 2 | 0.000010979157 | 9.68 | 9.257060 | 0.000983824 |
| 2023postBPix | VH | Input ROOT tree | 65 | 0.000215763299 | 9.68 | 5.450043 | 0.011382898 |
| 2023postBPix | VH | Inclusive workspace | 65 | 0.000215763299 | 9.68 | 5.450043 | 0.011382898 |
| 2023postBPix | VH | In workspace | 11 | -0.000028558788 | 9.68 | 5.450043 | -0.001506659 |
| 2023postBPix | VH | Out workspace | 54 | 0.000244322087 | 9.68 | 5.450043 | 0.012889558 |
| 2023postBPix | ttH | Input ROOT tree | 10,528 | 0.007833152636 | 9.68 | 1.293900 | 0.098109861 |
| 2023postBPix | ttH | Inclusive workspace | 10,528 | 0.007833152636 | 9.68 | 1.293900 | 0.098109861 |
| 2023postBPix | ttH | In workspace | 9,265 | 0.007053344270 | 9.68 | 1.293900 | 0.088342798 |
| 2023postBPix | ttH | Out workspace | 1,263 | 0.000779808366 | 9.68 | 1.293900 | 0.009767062 |
| 2023postBPix | tHqLep | Input ROOT tree | 18,441 | 0.024106886757 | 9.68 | 0.061576 | 0.014369109 |
| 2023postBPix | tHqLep | Inclusive workspace | 18,441 | 0.024106886757 | 9.68 | 0.061576 | 0.014369109 |
| 2023postBPix | tHqLep | In workspace | 17,453 | 0.022951553313 | 9.68 | 0.061576 | 0.013680463 |
| 2023postBPix | tHqLep | Out workspace | 988 | 0.001155333444 | 9.68 | 0.061576 | 0.000688646 |
| 2023postBPix | tHqHad | Input ROOT tree | 267 | 0.000200472154 | 9.68 | 0.127424 | 0.000247275 |
| 2023postBPix | tHqHad | Inclusive workspace | 267 | 0.000200472154 | 9.68 | 0.127424 | 0.000247275 |
| 2023postBPix | tHqHad | In workspace | 258 | 0.000209898403 | 9.68 | 0.127424 | 0.000258902 |
| 2023postBPix | tHqHad | Out workspace | 9 | -0.000009426250 | 9.68 | 0.127424 | -0.000011627 |
| 2023postBPix | tHW | Input ROOT tree | 3,525 | 0.011398425805 | 9.68 | 0.039044 | 0.004307989 |
| 2023postBPix | tHW | Inclusive workspace | 3,525 | 0.011398425805 | 9.68 | 0.039044 | 0.004307989 |
| 2023postBPix | tHW | In workspace | 3,149 | 0.010166437816 | 9.68 | 0.039044 | 0.003842364 |
| 2023postBPix | tHW | Out workspace | 376 | 0.001231987989 | 9.68 | 0.039044 | 0.000465625 |
| 2023postBPix | bbH | Input ROOT tree | 2 | 0.000011684556 | 9.68 | 1.196063 | 0.000135282 |
| 2023postBPix | bbH | Inclusive workspace | 2 | 0.000011684556 | 9.68 | 1.196063 | 0.000135282 |
| 2023postBPix | bbH | In workspace | 2 | 0.000011684556 | 9.68 | 1.196063 | 0.000135282 |
| 2023postBPix | bbH | Out workspace | 0 | 0.000000000000 | 9.68 | 1.196063 | 0.000000000 |

## Observed data: combined eras

Data has no XS/luminosity multiplier or generator-level in/out split. Events in the designated blinded region are counted, without modifying the files.

| Version | Events | Σ weight | Nonunit-weight events |
| --- | --- | --- | --- |
| Input data | 32 | 18283329714864060416.000000 | 1 |
| Data workspace | 32 | 32.000000 | 0 |

### Data mass regions

| Mass region | Definition (GeV) | Input data: events | Input data: Σ weight | Data workspace: events | Data workspace: Σ weight |
| --- | --- | --- | --- | --- | --- |
| Below range | m < 100 | 0 | 0.000000 | 0 | 0.000000 |
| Lower sideband | 100 ≤ m < 120 | 17 | 17.000000 | 18 | 18.000000 |
| Blinded region | 120 ≤ m ≤ 130 | 5 | 5.000000 | 5 | 5.000000 |
| Upper sideband | 130 < m ≤ 180 | 9 | 9.000000 | 9 | 9.000000 |
| Above range | m > 180 | 1 | 18283329714864060416.000000 | 0 | 0.000000 |
| Invalid mass | Nonfinite | 0 | 0.000000 | 0 | 0.000000 |
| Sidebands combined | 100 ≤ m < 120 or 130 < m ≤ 180 | 26 | 26.000000 | 27 | 27.000000 |
| Fit range total | 100 ≤ m ≤ 180 | 31 | 31.000000 | 32 | 32.000000 |
| Total | All entries | 32 | 18283329714864060416.000000 | 32 | 32.000000 |

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
| Data | Input = workspace | DIFFERENCE |

Checks compare event counts and summed weights. Input versus inclusive differences may indicate conversion selections or a mismatch between input and workspace versions.

## Source ROOT files

| Sample/version | File | ROOT object |
| --- | --- | --- |
| GluGluH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022preEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022preEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022preEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022preEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022preEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022preEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022preEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2022preEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022preEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2022postEE/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2022postEE/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2022postEE/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2022postEE/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2022postEE/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2022postEE/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2022postEE/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2022postEE / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2022postEE/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023preBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023preBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023preBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023preBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023preBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023preBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023preBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2023preBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023preBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root | ggh_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_incl/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_incl.root | ggh_incl_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_in/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_in.root | ggh_in_125_13TeV_tH_lep_2 |
| GluGluH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/GluGluH_2023postBPix/ws_ggh_out/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_ggh_out.root | ggh_out_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root | vbf_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_incl/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_incl.root | vbf_incl_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_in/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_in.root | vbf_in_125_13TeV_tH_lep_2 |
| VBFH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VBFH_2023postBPix/ws_vbf_out/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8_vbf_out.root | vbf_out_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root | vh_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_incl/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_incl.root | vh_incl_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_in/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_in.root | vh_in_125_13TeV_tH_lep_2 |
| VH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/VH_2023postBPix/ws_vh_out/output_VHToGG_M125_13TeV_amcatnlo_pythia8_vh_out.root | vh_out_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root | tth_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root | tth_incl_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_in/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_in.root | tth_in_125_13TeV_tH_lep_2 |
| ttH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/ttH_2023postBPix/ws_tth_out/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_out.root | tth_out_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root | tHqLep_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_incl/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_incl.root | tHqLep_incl_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_in/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_in.root | tHqLep_in_125_13TeV_tH_lep_2 |
| tHqLep / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqLep_2023postBPix/ws_tHqLep_out/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8_tHqLep_out.root | tHqLep_out_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root | tHqHad_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_incl/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_incl.root | tHqHad_incl_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_in/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_in.root | tHqHad_in_125_13TeV_tH_lep_2 |
| tHqHad / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHqHad_2023postBPix/ws_tHqHad_out/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8_tHqHad_out.root | tHqHad_out_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root | tHW_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_incl/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_incl.root | tHW_incl_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_in/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_in.root | tHW_in_125_13TeV_tH_lep_2 |
| tHW / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/tHW_2023postBPix/ws_tHW_out/output_THWtoGG_M125_13TeV_madgraph_pythia8_tHW_out.root | tHW_out_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / input | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root | bbh_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / incl | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_incl/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_incl.root | bbh_incl_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / in | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_in/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_in.root | bbh_in_125_13TeV_tH_lep_2 |
| bbH / 2023postBPix / out | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/bbH_2023postBPix/ws_bbh_out/output_BBHToGG_M125_13TeV_powheg_pythia8_bbh_out.root | bbh_out_125_13TeV_tH_lep_2 |
| Input data | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/allData.root | Data_13TeV_tH_lep_2 |
| Data workspace | /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs_27June/Data/ws/allData.root | Data_13TeV_tH_lep_2 |
