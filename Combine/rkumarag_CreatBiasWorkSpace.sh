#!/bin/bash

ttH_cats=(
ttH_had_1
ttH_had_2
ttH_lep_1
ttH_lep_2
)

tH_cats=(
tH_had_1
tH_had_2
tH_lep_1
tH_lep_2
)

for c in "${ttH_cats[@]}"; do
    python3 RunText2Workspace.py --mode r_ttH_1D --ext lumi5Times_${c} --batch local --outputDir Datacard_lumi5times --outputName Datacard_${c}.root
done

for c in "${tH_cats[@]}"; do
    python3 RunText2Workspace.py --mode r_tHq_plus_tHW_1D --ext lumi5Times_${c} --batch local --outputDir Datacard_lumi5times --outputName Datacard_${c}.root
done
