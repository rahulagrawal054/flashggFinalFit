#!/bin/bash

set -euo pipefail

# Extensions to loop through
EXTENSIONS=("DCB" "SoG")

# Prune thresholds from 0% (0.000) to 1.0% (0.010) in steps of 0.1% (0.001)
PRUNE_THRESHOLDS=(
    0.000 0.001 0.002 0.003 0.004 0.005 0.006 0.007 0.008 0.009 0.010
)

for EXT in "${EXTENSIONS[@]}"; do
    for PRUNE in "${PRUNE_THRESHOLDS[@]}"; do
        # Replace '.' with 'p' (e.g., 0.001 -> 0p001)
        PRUNE_STR="${PRUNE//./p}"
        
        OUTPUT_NAME="Datacard_fiducial_allCats_${PRUNE_STR}_${EXT}"
        LOGFILE="${OUTPUT_NAME}.log"

        echo "=================================================="
        echo " Running makeDatacard.py"
        echo " Extension:       ${EXT}"
        echo " Prune Threshold: ${PRUNE} (${PRUNE_STR})"
        echo " Output Name:     ${OUTPUT_NAME}"
        echo "=================================================="

        python3 makeDatacard.py \
            --inputFiles ./ \
            --outputDir ./ \
            --years 2022preEE,2022postEE,2023preBPix,2023postBPix \
            --analysis tth_th_analysis_fiducial \
            --mass 125.08 \
            --prune \
            --pruneThreshold "${PRUNE}" \
            --skipCOWCorr \
            --doSystematics \
            --doTrueYield \
            --output "${OUTPUT_NAME}" \
            2>&1 | tee "${LOGFILE}"

        # Identify generated datacard file (.txt extension or raw output name)
        CARD_FILE="${OUTPUT_NAME}.txt"
        if [ ! -f "${CARD_FILE}" ] && [ -f "${OUTPUT_NAME}" ]; then
            CARD_FILE="${OUTPUT_NAME}"
        fi

        # Replace 'Models' -> 'Models_EXT' and 'packaged' -> 'packaged_EXT' in place
        if [ -f "${CARD_FILE}" ]; then
            sed -i -e "s/Models/Models_${EXT}/g" -e "s/packaged/packaged_${EXT}/g" "${CARD_FILE}"
            echo "[+] Updated paths in ${CARD_FILE}:"
            echo "    - Models   -> Models_${EXT}"
            echo "    - packaged -> packaged_${EXT}"
        else
            echo "[!] Warning: Datacard file ${CARD_FILE} not found for string replacement."
        fi

        echo "Completed: ${OUTPUT_NAME}"
        echo ""
    done
done

echo "All datacards generated and updated successfully."
