#!/bin/bash

# Usage: ./publish.sh <NAME>
NAME=$1
[ -z "$NAME" ] && { echo "Usage: $0 <directory_name>"; exit 1; }

BASE_DIR="/eos/user/r/rkumarag/www"
DEST_DIR="${BASE_DIR}/${NAME}"

COMBINE_DIR="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine"
DEST_DIR2="${COMBINE_DIR}/${NAME}"

echo ">> Creating web directory: $DEST_DIR"
mkdir -p "$DEST_DIR"

echo ">> Copying plots..."
find runFits_* -path "*/Plots/CombinePlot*" \( -name "*.pdf" -o -name "*.png" -o -name "*.root" \) -exec cp {} "$DEST_DIR" \;
find Impacts_* \( -name "*.pdf" \) -exec cp {} "$DEST_DIR" \;

echo ">> Updating index..."
cd "$BASE_DIR" && [ -f copy_index.sh ] && ./copy_index.sh

echo ">> Creating combine directory: $DEST_DIR2"
mkdir -p "$DEST_DIR2"

echo ">> Moving combine inputs..."

cd "$COMBINE_DIR"

mv Datacard* "$DEST_DIR2"
mv Models "$DEST_DIR2"
mv t2w_jobs "$DEST_DIR2"
mv runFits_r* "$DEST_DIR2"
mv runFits_Z* "$DEST_DIR2"
mv runFits_limit* "$DEST_DIR2"
mv Impacts_* "$DEST_DIR2"

echo "========================================================"
echo "Done!"
echo "Web: https://rkumarag.web.cern.ch/rkumarag/${NAME}/"
echo "Combine dir: $DEST_DIR2"
echo "========================================================"

