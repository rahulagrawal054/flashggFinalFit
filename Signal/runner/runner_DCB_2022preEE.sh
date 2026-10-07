#!/bin/bash

# ==============================================================================
# 1. SET THE YEAR HERE
# ==============================================================================
YEAR="2022preEE"
CONFIG="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/config/fiducial/DCBplusGaussian/config_${YEAR}.py"
LOGDIR="$(pwd)/logs_DCB"

echo "Creating log directory: $LOGDIR"
mkdir -p "$LOGDIR"

if [ ! -d "$LOGDIR" ]; then
    echo "ERROR: Failed to create $LOGDIR"
    exit 1
fi

echo "==================================================="
echo " Starting Signal Scripts for Year: $YEAR"
echo "==================================================="

# ==============================================================================
# Step 1: calcPhotonSyst (Moved to second place)
# ==============================================================================
MODE2="calcPhotonSyst"
LOG2="${LOGDIR}/${MODE2}_${YEAR}.log"

echo "[$(date +'%T')] Running ${MODE2}..."
python3 -u RunSignalScripts.py --inputConfig "$CONFIG" --mode "$MODE2" 2>&1 | tee "$LOG2"
echo "[$(date +'%T')] ${MODE2} complete."

# ==============================================================================
# Step 2: signalFit
# ==============================================================================
MODE3="signalFit"
LOG3="${LOGDIR}/${MODE3}_${YEAR}.log"

echo "[$(date +'%T')] Running ${MODE3}..."
python3 -u RunSignalScripts.py --inputConfig "$CONFIG" --mode "$MODE3" --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --doPlots --useDCB" 2>&1 | tee "$LOG3"

echo "==================================================="
echo " All tasks finished successfully!"
echo "==================================================="
