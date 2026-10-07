#!/usr/bin/env bash
set -euo pipefail

# ==============================================================================
# Full 2D scan pipeline: snapshot -> regenerate Asimov -> parallel grid scans
# (stat+syst AND stat-only) -> merge -> plot (single-tree each, run twice)
#
# Usage: bash run_2d_scan.sh
# Edit the CONFIG block below to match your setup.
# ==============================================================================

# --- CONFIG ---
WORKSPACE="Datacard_fiducial_allCats_SoG_r_2D_fiducial.root"
MASS="125.08"
X_RANGE="r_tHq=-20,25"
Y_RANGE="r_ttH=-0.5,3.0"
XPARAM="r_tHq:-20,25"
YPARAM="r_ttH:-0.5,3.0"
TOTAL_POINTS=10000
NCHUNKS=16          # match your nproc; each chunk does TOTAL_POINTS/NCHUNKS points
PLOT_SCRIPT="make2DPlot.py"   # path to the corrected single-tree plotter

SNAPSHOT_WS="higgsCombine_AsimovPostfit.MultiDimFit.mH${MASS}.root"
TOY_FILE="higgsCombineSMAsimov_postfit.GenerateOnly.mH${MASS}.0.root"

MINIM_OPTS="--cminDefaultMinimizerStrategy 0 \
  --X-rtd MINIMIZER_freezeDisassociatedParams \
  --X-rtd MINIMIZER_multiMin_hideConstants \
  --X-rtd MINIMIZER_multiMin_maskConstraints \
  --X-rtd MINIMIZER_multiMin_maskChannels=2"

# --- STEP 1: snapshot (skip if already present) ---
if [[ ! -f "${SNAPSHOT_WS}" ]]; then
  echo ">>> [Step 1] Fitting once, saving snapshot..."
  combine -M MultiDimFit "${WORKSPACE}" \
    -m "${MASS}" -t -1 \
    --setParameters r_tHq=1,r_ttH=1,MH="${MASS}" \
    --freezeParameters MH \
    --saveWorkspace --saveFitResult -n _AsimovPostfit \
    -P r_tHq -P r_ttH --floatOtherPOIs 1 \
    ${MINIM_OPTS}
else
  echo ">>> [Step 1] Snapshot already exists, skipping: ${SNAPSHOT_WS}"
fi

# --- STEP 2: regenerate Asimov from snapshot (skip if already present) ---
if [[ ! -f "${TOY_FILE}" ]]; then
  echo ">>> [Step 2] Regenerating Asimov from snapshot..."
  combine -M GenerateOnly "${SNAPSHOT_WS}" \
    -m "${MASS}" -t -1 \
    --snapshotName MultiDimFit \
    --saveWorkspace --saveToys -n SMAsimov_postfit -s 0 \
    --setParameters r_tHq=1,r_ttH=1,MH="${MASS}" --freezeParameters MH
else
combine -M GenerateOnly Datacard_fiducial_allCats_SoG_r_2D_fiducial.root \
  -m 125.08 -t -1 \
  --setParameters r_tHq=1,r_ttH=1,MH=125.08 --freezeParameters MH \
  --saveWorkspace --saveToys \
  -n SMAsimov_postfit -s 0
