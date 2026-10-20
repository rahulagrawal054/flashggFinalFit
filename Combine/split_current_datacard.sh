#!/usr/bin/env bash
# Split the current DCB card, using the same category loop as 15OCT26.
set -e

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval "$(scram runtime -sh)"
source ../setup.sh
command -v combineCards.py
cd "$script_dir"

card="$(realpath DCB/Datacard_DCB.txt)"
out="$script_dir/Checks/inputs_DCB"
mkdir -p "$out"

for cat in ttH_had_1 ttH_had_2 ttH_had_3 ttH_had_4 ttH_lep_1 ttH_lep_2 ttH_lep_3 ttH_lep_4 tH_had_1 tH_had_2 tH_had_3 tH_had_4 tH_lep_1 tH_lep_2 bkg_had bkg_lep; do
    combineCards.py ".=$card" --ic "^${cat}$" > "$out/Datacard_${cat}.txt" 2> "$out/${cat}.log"
    sed -i "/^pdfindex_/!b; /^pdfindex_${cat}_13TeV[[:space:]]/b; d" "$out/Datacard_${cat}.txt"
    echo "Saved $out/Datacard_${cat}.txt"
done
