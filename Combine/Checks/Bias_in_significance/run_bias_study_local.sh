#!/bin/bash
set -u

# ============================================================
# Bias in Significance - 2 POI study
#
# Usage:
#   ./run_bias_study.sh -w <workspace.root> -l <label> -n <nToys>
#
# Example:
#   ./run_bias_study.sh -w ../Datacard/Datacard_ttH_had_1_r_2D_fiducial.root \
#                        -l ttH_had_1 -n 5000
#
# Output folder (created by RunBiasInSignificance_twoPOIs.py) is
# <label>_<nToys>toys/ - this script computes that same name so the
# plotting step at the end points at the right place automatically.
# ============================================================

SCRIPT="RunBiasInSignificance_twoPOIs.py"
PLOT_SCRIPT="SummaryBiasSignificance.py"

usage() {
    echo "Usage: $0 -w <workspace.root> -l <label> -n <nToys>"
    exit 1
}

WS=""
LABEL=""
NTOYS=""

while getopts "w:l:n:" opt; do
    case "$opt" in
        w) WS="$OPTARG" ;;
        l) LABEL="$OPTARG" ;;
        n) NTOYS="$OPTARG" ;;
        *) usage ;;
    esac
done

if [[ -z "$WS" || -z "$LABEL" || -z "$NTOYS" ]]; then
    echo "ERROR: -w, -l and -n are all required."
    usage
fi

OUT_DIR="${LABEL}_${NTOYS}toys"

echo "=============================================="
echo " Bias in Significance"
echo " Workspace : $WS"
echo " Label     : $LABEL"
echo " Toys      : $NTOYS"
echo " Output    : $OUT_DIR"
echo "=============================================="

run_step() {
    local desc="$1"
    shift
    echo ""
    echo "$desc"
    python3 "$SCRIPT" "$@"
    if [ $? -ne 0 ]; then
        echo "ERROR: $desc failed!"
        exit 1
    fi
}

# ------------------------------------------------------------
# 1. Setup
# ------------------------------------------------------------
run_step "[1/6] Setup..." \
    --inputWSFile "$WS" --nToys "$NTOYS" --label "$LABEL" --mode setup

# ------------------------------------------------------------
# 2. Generate toys
# ------------------------------------------------------------
run_step "[2/6] Generating toys..." \
    --inputWSFile "$WS" --nToys "$NTOYS" --label "$LABEL" --mode generate

# ------------------------------------------------------------
# 3-4. Fixed mode - both POIs
# ------------------------------------------------------------
run_step "[3/6] Fixed significance - r_ttH..." \
    --inputWSFile "$WS" --nToys "$NTOYS" --label "$LABEL" --mode fixed --POI r_ttH

run_step "[4/6] Fixed significance - r_tHq..." \
    --inputWSFile "$WS" --nToys "$NTOYS" --label "$LABEL" --mode fixed --POI r_tHq

# ------------------------------------------------------------
# 5-6. Envelope mode - both POIs
# ------------------------------------------------------------
run_step "[5/6] Envelope significance - r_ttH..." \
    --inputWSFile "$WS" --nToys "$NTOYS" --label "$LABEL" --mode envelope --POI r_ttH

run_step "[6/6] Envelope significance - r_tHq..." \
    --inputWSFile "$WS" --nToys "$NTOYS" --label "$LABEL" --mode envelope --POI r_tHq

echo ""
echo "=============================================="
echo " ALL COMBINE JOBS COMPLETED"
echo "=============================================="

# ------------------------------------------------------------
# 7. Plot
# ------------------------------------------------------------
echo ""
echo "Making plots..."
python3 "$PLOT_SCRIPT" -i "$OUT_DIR"
if [ $? -ne 0 ]; then
    echo "ERROR: Plotting failed!"
    exit 1
fi

echo ""
echo "=============================================="
echo " DONE: $OUT_DIR/plots/"
echo "=============================================="
