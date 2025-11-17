#!/bin/bash

cats=(
tH_had_1
tH_had_2
ttH_had_1
ttH_had_2
tH_lep_1
tH_lep_2
ttH_lep_1
ttH_lep_2
)

for c in "${cats[@]}"; do
    combineCards.py Datacard.txt --ic $c > Datacard_${c}.txt
done

