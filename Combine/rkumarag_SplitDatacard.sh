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
    outfile="Datacard_${c}.txt"

    # Create datacard
    combineCards.py /eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/Datacard.txt --ic "$c" > "$outfile"

    # Keep only matching pdfindex line, remove others
    sed -i "/pdfindex_/!b; /pdfindex_${c}_13TeV/b; d" "$outfile"

    echo "Processed $outfile"
done
