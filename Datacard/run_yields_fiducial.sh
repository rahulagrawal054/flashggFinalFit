#!/bin/bash

# Exit immediately if a command exits with a non-zero status,
# treat unset variables as an error, and prevent pipeline errors from being masked.
set -euo pipefail

# Define an extension tag for organizing your output files
EXT="production_v1"
LOG_FILE="yields_${EXT}.log"

echo "========================================================================" | tee -a ${LOG_FILE}
echo " Starting Datacard Yield Generation Pipeline (Run 3: 2022 & 2023) " | tee -a ${LOG_FILE}
echo "========================================================================" | tee -a ${LOG_FILE}

# Define Workspace Directories for Run 3 years
WS_2022PRE="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/fiducial/2022preEE/ws_signal"
WS_2022POST="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/fiducial/2022postEE/ws_signal"
WS_2023PRE="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/fiducial/2023preBPix/ws_signal"
WS_2023POST="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/workspaces/fiducial/2023postBPix/ws_signal"

# Construct the input directory map string
WS_MAP="2022preEE=${WS_2022PRE},2022postEE=${WS_2022POST},2023preBPix=${WS_2023PRE},2023postBPix=${WS_2023POST}"

echo "--> Input Workspace Map configured successfully." | tee -a ${LOG_FILE}
echo "--> Executing yield generation script locally..." | tee -a ${LOG_FILE}

# Execute the core python framework script and log all output
python3 RunYields.py \
    --cats auto \
    --procs auto \
    --ext "${EXT}" \
    --mergeYears \
    --doSystematics \
    --batch local \
    --inputWSDirMap "${WS_MAP}" \
    --skipZeroes \
    --skipCOWCorr 2>&1 | tee -a ${LOG_FILE}

# NOTE ON USER MODIFICATIONS TO UPSTREAM CODE:
# --------------------------------------------------------------------------
# 1. --skipZeroes: Hardcoded tolerance inside 'makeYields.py' modified 
#    from (sumw == 0.) to (sumw <= 1e-9). Drops zero, negative, and micro-yields.
# 2. --skipCOWCorr: Explicitly passed as 'centralObjectWeight' branch does not 
#    exist in these workspaces.
# --------------------------------------------------------------------------

echo "========================================================================" | tee -a ${LOG_FILE}
echo " Yield generation complete! Outputs saved to logs and yields_${EXT}/" | tee -a ${LOG_FILE}
echo "========================================================================" | tee -a ${LOG_FILE}
