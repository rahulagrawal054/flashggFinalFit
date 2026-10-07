#!/bin/bash

set -euo pipefail

COMBINE_DIR="/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine"
DATACARD_DIR="/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Datacard"

EXTENSIONS=("DCB" "SoG")
PRUNE_STRS=(
    "0p000" "0p001" "0p002" "0p003" "0p004" 
    "0p005" "0p006" "0p007" "0p008" "0p009" "0p010"
)

# Navigate to Combine directory
cd "${COMBINE_DIR}"

for EXT in "${EXTENSIONS[@]}"; do
    for PRUNE_STR in "${PRUNE_STRS[@]}"; do
        EXT_NAME="fiducial_allCats_${PRUNE_STR}_${EXT}"
        CARD_NAME="Datacard_${EXT_NAME}.txt"
        
        # Link datacard from Datacard dir to current dir if not already present
        if [ -f "${DATACARD_DIR}/${CARD_NAME}" ]; then
            ln -sf "${DATACARD_DIR}/${CARD_NAME}" "./${CARD_NAME}"
        else
            echo "[!] Warning: Datacard ${DATACARD_DIR}/${CARD_NAME} not found!"
            continue
        fi

        echo "=================================================="
        echo " Running RunText2Workspace.py"
        echo " Datacard:  ${CARD_NAME}"
        echo " Extension: ${EXT_NAME}"
        echo "=================================================="

        python3 RunText2Workspace.py \
            --mode r_2D_fiducial \
            --ext "${EXT_NAME}" \
            --common_opts "-m 125.08" \
            --batch local

        echo "Completed workspace creation for ${EXT_NAME}"
        echo ""
    done
done

echo "All workspaces created successfully."
