#!/bin/bash

set -e

# Target www directory
WWW_DIR="/eos/user/r/rkumarag/www/Combine"
mkdir -p "${WWW_DIR}"

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <folder1> [folder2 ...]"
    echo "Example: $0 DCB_noPrune"
    echo "Example: $0 /path/to/folders/*"
    exit 1
fi

for DIR in "$@"; do
    if [ ! -d "$DIR" ]; then
        continue
    fi

    FOLDER_NAME=$(basename "$DIR")
    echo "Processing folder: ${FOLDER_NAME}"

    # Copy and prefix CombinePlot_r_tHq files
    for file in "${DIR}"/CombinePlot_r_tHq*; do
        if [ -f "$file" ]; then
            fname=$(basename "$file")
            cp "$file" "${WWW_DIR}/${FOLDER_NAME}_${fname}"
        fi
    done

    # Copy and prefix CombinePlot_r_ttH files
    for file in "${DIR}"/CombinePlot_r_ttH*; do
        if [ -f "$file" ]; then
            fname=$(basename "$file")
            cp "$file" "${WWW_DIR}/${FOLDER_NAME}_${fname}"
        fi
    done

    # Copy and prefix results_summary.txt
    if [ -f "${DIR}/results_summary.txt" ]; then
        cp "${DIR}/results_summary.txt" "${WWW_DIR}/${FOLDER_NAME}_results_summary.txt"
    fi
done

echo ""
echo "Done. All renamed files copied to:"
echo "${WWW_DIR}"
