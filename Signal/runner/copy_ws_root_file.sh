#!/bin/bash

YEARS=("2022preEE" "2022postEE" "2023preBPix" "2023postBPix")

SRC_BASE="/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_25May2026/workspaces_fiducial"
DEST="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/all_eras_ws_signal_tth_th_analysis_fiducial"

mkdir -p "${DEST}"

for YEAR in "${YEARS[@]}"; do

    SRC_DIR="${SRC_BASE}/${YEAR}/ws_signal"

    for FILE in "${SRC_DIR}"/*.root; do

        BASENAME=$(basename "${FILE}" .root)

        cp "${FILE}" "${DEST}/${BASENAME}_${YEAR}.root"

        echo "Copied: ${FILE} -> ${DEST}/${BASENAME}_${YEAR}.root"

    done

done
