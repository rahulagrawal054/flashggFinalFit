#!/usr/bin/env bash
# Same conversion loop as 15OCT26, using current DCB cards and MH=125.09.
set -eo pipefail
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
combine_dir="$script_dir"
cd "$combine_dir"
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval "$(scram runtime -sh)"
source ../setup.sh
export PYTHONDONTWRITEBYTECODE=1
cd "$combine_dir/Checks/inputs_DCB"
for cat in ttH_had_1 ttH_had_2 ttH_had_3 ttH_had_4 ttH_lep_1 ttH_lep_2 ttH_lep_3 ttH_lep_4 tH_had_1 tH_had_2 tH_had_3 tH_had_4 tH_lep_1 tH_lep_2 bkg_had bkg_lep; do
    python3 -B -u "$combine_dir/RunText2Workspace.py" \
      --mode r_2D_fiducial --ext "$cat" \
      --common_opts "-m 125.09" --batch local \
      2>&1 | tee "text2workspace_${cat}.log"
    test -s "Datacard_${cat}_r_2D_fiducial.root"
done
