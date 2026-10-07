#!/bin/bash

set -euo pipefail

LOGFILE="Datacard_fiducial_0.001.log"

python3 makeDatacard.py \
    --inputFiles ./ \
    --outputDir ./ \
    --years 2022preEE,2022postEE,2023preBPix,2023postBPix \
    --analysis tth_th_analysis_fiducial \
    --mass 125.08 \
    --prune \
    --pruneThreshold 0.001 \
    --skipCOWCorr \
    --doSystematics \
    --doTrueYield 
    2>&1 | tee "${LOGFILE}"

echo "Datacard creation completed."
