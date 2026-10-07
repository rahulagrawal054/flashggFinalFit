#!/bin/bash

cats=(
ttH_had_1
ttH_had_2
ttH_had_3
ttH_had_4
ttH_lep_1
ttH_lep_2
ttH_lep_3
ttH_lep_4
tH_had_1
tH_had_2
tH_had_3
tH_had_4
tH_lep_1
tH_lep_2
bkg_had
bkg_lep
)

for c in "${cats[@]}"; do
    outfile="Datacard_${c}.txt"

    # Create datacard
    combineCards.py /eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/Datacard_fiducial_allCats_0p001_SoG.txt --ic "$c" > "$outfile"

    # Keep only matching pdfindex line, remove others
    sed -i "/pdfindex_/!b; /pdfindex_${c}_13TeV/b; d" "$outfile"

    echo "Processed $outfile"
done
