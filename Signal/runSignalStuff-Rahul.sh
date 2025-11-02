#!/usr/bin/env bash
#====================================================
# Automated signal workflow with debug + timing info
# Author: Rahul
#====================================================

# Exit on errors, undefined vars, or failed pipes
set -euo pipefail

# Enable command tracing (debug)
set -x

# Start timer
start_time=$(date +%s)

# Source environment
echo ">>> Setting up environment..."
source ../setup.sh

# Define eras
#eras=(2022preEE 2022postEE 2023preBPix 2023postBPix)
eras=(2022preEE)

# Create log folder
mkdir -p logs

#====================================================
# 1. Run fTest and signalFit for all eras
#====================================================
for era in "${eras[@]}"; do
  echo "===================================================="
  echo ">>> Processing era: $era"
  echo "===================================================="

  # fTest
  echo ">>> Running fTest for $era..."
  { time python3 RunSignalScripts.py \
    --inputConfig config_${era}.py \
    --mode fTest \
    --modeOpts "--doPlots --skipWV" \
    2>&1 | tee logs/fTest_${era}.log; } || {
      echo "❌ fTest failed for $era"; exit 1;
    }

  # calcPhotonSyst
  echo ">>> Running calcPhotonSyst for $era..."
  { time python3 RunSignalScripts.py \
    --inputConfig config_${era}.py \
    --mode calcPhotonSyst
    2>&1 | tee logs/calcPhotonSyst_${era}.log; } || {
      echo "�~]~calcPhotonSyst failed for $era"; exit 1;
    }

  # SignalFit
  echo ">>> Running signalFit for $era..."
  { time python3 RunSignalScripts.py \
    --inputConfig config_${era}.py \
    --mode signalFit \
    --groupSignalFitJobsByCat \
    --modeOpts "--skipVertexScenarioSplit --skipSystematics --doPlots" \
    2>&1 | tee logs/signalFit_${era}.log; } || {
      echo "❌ signalFit failed for $era"; exit 1;
    }
done

#====================================================
# 2. Collect all signal workspaces
#====================================================
echo ">>> Collecting all workspaces..."
mkdir -p ./all_eras_ws_signal
for era in "${eras[@]}"; do
  for f in /eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_30Oct2025/workspaces/${era}/ws_signal/*.root; do
    base=$(basename "$f" .root)
    cp -v "$f" ./all_eras_ws_signal/${base}_${era}.root
  done
done

#====================================================
# 3. Run Packager
#====================================================
echo ">>> Running RunPackager..."
{ time python3 RunPackager.py \
  --cats auto \
  --inputWSDir ./all_eras_ws_signal \
  --exts tth_th_analysis_2022preEE_StatOnly,tth_th_analysis_2022postEE_StatOnly,tth_th_analysis_2023preBPix_StatOnly,tth_th_analysis_2023postBPix_StatOnly \
  --mergeYears \
  --massPoints 125 \
  --batch local \
  --mergeYears \
  --outputExt _StatOnly \
  2>&1 | tee logs/packager.log; } || {
    echo "❌ Packager failed!"; exit 1;
  }

#====================================================
# 4. Run Plotter for all categories
#====================================================
echo ">>> Running RunPlotter for all categories..."
cats=(tH_lep_1 tH_lep_2 ttH_lep_1 ttH_lep_2 tH_had_1 tH_had_2 ttH_had_1 ttH_had_2)
for cat in "${cats[@]}"; do
  { time python3 RunPlotter.py \
    --procs all \
    --years 2022preEE,2022postEE,2023preBPix,2023postBPix \
    --cats $cat \
    --ext packaged_StatOnly \
    2>&1 | tee logs/plot_${cat}.log; } || {
      echo "❌ Plotting failed for $cat"; exit 1;
    }
done

#====================================================
# 5. Done — show total runtime
#====================================================
end_time=$(date +%s)
runtime=$((end_time - start_time))
echo "===================================================="
echo "✅ All steps completed successfully!"
echo "🕒 Total runtime: $((runtime / 3600))h $(((runtime % 3600) / 60))m $((runtime % 60))s"
echo "Logs saved in ./logs/"
echo "===================================================="

