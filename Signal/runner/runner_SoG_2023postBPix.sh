#!/bin/bash

# ==============================================================================
# 1. SET THE YEAR HERE
# ==============================================================================
YEAR="2023postBPix"
CONFIG="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/config/fiducial/SumOfGaussian/config_${YEAR}.py"

mkdir -p logs_SoG

echo "==================================================="
echo " Starting Signal Scripts for Year: $YEAR"
echo "==================================================="

# ==============================================================================
# Step 1: fTest
# ==============================================================================
MODE1="fTest"
LOG1="logs_SoG/${MODE1}_${YEAR}.log"

echo "[$(date +'%T')] Running ${MODE1}..."

# Added -u flag here!
python3 -u RunSignalScripts.py --inputConfig "$CONFIG" --mode "$MODE1" --modeOpts "--doPlots --skipWV" 2>&1 | tee "$LOG1"

echo "[$(date +'%T')] ${MODE1} complete. Sleeping for 10 seconds..."
sleep 10


# ==============================================================================
# Step 2: calcPhotonSyst
# ==============================================================================
MODE2="calcPhotonSyst"
LOG2="logs_SoG/${MODE2}_${YEAR}.log"

echo "[$(date +'%T')] Running ${MODE2}..."

# Added -u flag here!
python3 -u RunSignalScripts.py --inputConfig "$CONFIG" --mode "$MODE2" 2>&1 | tee "$LOG2"

echo "[$(date +'%T')] ${MODE2} complete. Sleeping for 10 seconds..."
sleep 10


# ==============================================================================
# Step 3: signalFit
# ==============================================================================
MODE3="signalFit"
LOG3="logs_SoG/${MODE3}_${YEAR}.log"

echo "[$(date +'%T')] Running ${MODE3}..."

# Added -u flag here!
python3 -u RunSignalScripts.py --inputConfig "$CONFIG" --mode "$MODE3" --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --doPlots" 2>&1 | tee "$LOG3"

echo "==================================================="
echo " All tasks finished successfully!"
echo "==================================================="
