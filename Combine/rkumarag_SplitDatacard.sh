#!/bin/bash

cats=(
ttH_had_1
ttH_had_2
ttH_lep_1
ttH_lep_2
tH_had_1
tH_had_2
tH_lep_1
tH_lep_2
)

for c in "${cats[@]}"; do
    combineCards.py /eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/Datacard_lumi5Times.txt --ic $c > Datacard_lumi5Times_${c}.txt
done

