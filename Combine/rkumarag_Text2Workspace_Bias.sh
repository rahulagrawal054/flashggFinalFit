#!/bin/bash

# ttH categories
ttH_cats=(
ttH_had_1
ttH_had_2
ttH_lep_1
ttH_lep_2
)

for c in "${ttH_cats[@]}"; do
    python3 RunText2Workspace.py --mode r_ttH_1D_Bias --batch local --ext StatOnly_$c
done


# tH categories
tH_cats=(
tH_had_1
tH_had_2
tH_lep_1
tH_lep_2
)

for c in "${tH_cats[@]}"; do
    python3 RunText2Workspace.py --mode r_tHq_plus_tHW_1D_Bias --batch local --ext StatOnly_$c
done

