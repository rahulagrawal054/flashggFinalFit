#!/usr/bin/env bash
#====================================================
# Automated background workflow with debug + timing
# Author: Rahul
#====================================================

# Exit on error, unset vars, or failed pipes
set -euo pipefail
# Print commands for debugging
set -x

# Start timer
start_time=$(date +%s)

#====================================================
# 1. Setup CMSSW environment
#====================================================
echo ">>> Setting up CMSSW environment..."
source ../setup.sh
cmsenv

#====================================================
# 2. Cleanup old output
#====================================================
echo ">>> Cleaning old background output..."
rm -rfv ./outdir_tth_th_analysis || true
mkdir -p logs

#====================================================
# 3. Run background fTest in parallel
#====================================================
echo ">>> Running background fTest in parallel..."
{ time python3 RunBackgroundScripts.py \
  --inputConfig config_FM.py \
  --mode fTestParallel \
  2>&1 | tee logs/background_fTestParallel.log; } || {
    echo "❌ Background fTest failed!"; exit 1;
  }

#====================================================
# 4. Done — show runtime
#====================================================
end_time=$(date +%s)
runtime=$((end_time - start_time))

echo "===================================================="
echo "✅ Background workflow completed successfully!"
echo "🕒 Total runtime: $((runtime / 60))m $((runtime % 60))s"
echo "📁 Logs stored in ./logs/background_fTestParallel.log"
echo "===================================================="

