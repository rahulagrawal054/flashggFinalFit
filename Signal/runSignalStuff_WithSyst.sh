#!/usr/bin/env bash
#====================================================
# Automated signal workflow
# Author: Rahul
#====================================================

set -euo pipefail

# Define eras
eras=(2022preEE 2022postEE 2023preBPix 2023postBPix)

#====================================================
# 1. Run fTest and signalFit for all eras
#====================================================
for era in "${eras[@]}"; do
  echo "Processing era: $era"

  # fTest
  python3 RunSignalScripts.py --inputConfig config_${era}_WithSyst.py --mode fTest --modeOpts "--doPlots --skipWV"

  # calcPhotonSyst
  python3 RunSignalScripts.py --inputConfig config_${era}_WithSyst.py --mode calcPhotonSyst

  # getDiagProc
  python3 RunSignalScripts.py --inputConfig config_${era}_WithSyst.py --mode getDiagProc

  # SignalFit
  python3 RunSignalScripts.py --inputConfig config_${era}_WithSyst.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --doPlots"
done
# Exit after step 1
#exit 0
#====================================================
# 2. Collect all signal workspaces
#====================================================
mkdir -p ./all_eras_ws_signal_WithSyst
for era in "${eras[@]}"; do
  for f in /eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/workspaces/${era}/ws_signal/*.root; do
    base=$(basename "$f" .root)
    cp "$f" ./all_eras_ws_signal_WithSyst/${base}_${era}.root
  done
done

#====================================================
# 3. Run Packager
#====================================================
python3 RunPackager.py \
  --cats auto \
  --inputWSDir ./all_eras_ws_signal_WithSyst \
  --exts tth_th_analysis_2022preEE_WithSyst,tth_th_analysis_2022postEE_WithSyst,tth_th_analysis_2023preBPix_WithSyst,tth_th_analysis_2023postBPix_WithSyst \
  --mergeYears \
  --massPoints 125 \
  --batch local 


#====================================================
# 4. Run Plotter for all categories
#====================================================
cats=(tH_lep_1 tH_lep_2 ttH_lep_1 ttH_lep_2 tH_had_1 tH_had_2 ttH_had_1 ttH_had_2)
for cat in "${cats[@]}"; do
  python3 RunPlotter.py --procs all --years 2022preEE,2022postEE,2023preBPix,2023postBPix --cats $cat --ext packaged --doFWHM
done

mv outdir_packaged outdir_packaged_WithSyst

echo "All steps completed successfully!"

