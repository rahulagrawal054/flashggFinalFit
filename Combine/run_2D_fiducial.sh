#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOM'
Usage: bash run_2D_fiducial.sh --steps <list> [options]

Steps (comma-separated):
  snapshot      Create the postfit workspace (Asimov or Observed)
  scan-syst     Run 1D profile likelihood scans with full systematics
  scan-stat     Run 1D profile likelihood scans with stat-only uncertainties
  limit         Calculate expected/observed upper limit for a specific POI
  significance  Calculate expected/observed significance for a specific POI

Options:
  --workspace <file>    Path to the input ROOT workspace (default: Datacard_fiducial_allCats_noMCStat_r_2D_fiducial.root)
  --mass <value>        Higgs mass (default: 125.08)
  --pois <list>         Comma-separated list of POIs to scan (default: r_tHq,r_ttH)
  --ranges <ranges>     Parameter ranges (default: r_tHq=-20,25:r_ttH=-0.5,3.0)
  --points <N>          Number of points for grid scans (default: 50)
  --no-asimov           Run on observed data instead of expected Asimov (-t -1)
  -h, --help            Show this help message

Example:
  bash run_2D_fiducial.sh --steps snapshot,scan-syst,scan-stat,limit,significance
EOM
}

# --- Default Configuration ---
WORKSPACE="Datacard_fiducial_allCats_r_2D_fiducial.root"
MASS="125.08"
POIS="r_tHq,r_ttH"
RANGES="r_tHq=-20,25:r_ttH=-0.5,3.0"
POINTS="100"
ASIMOV=1
STEPS=""

# --- Argument Parsing ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --workspace) WORKSPACE="$2"; shift 2 ;;
    --mass) MASS="$2"; shift 2 ;;
    --pois) POIS="$2"; shift 2 ;;
    --ranges) RANGES="$2"; shift 2 ;;
    --points) POINTS="$2"; shift 2 ;;
    --steps) STEPS="$2"; shift 2 ;;
    --no-asimov) ASIMOV=0; shift 1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "[ERROR] Unknown option: $1" >&2; usage >&2; exit 1 ;;
  esac
done

if [[ -z "${STEPS}" ]]; then
  echo "[ERROR] --steps is required." >&2
  usage >&2
  exit 1
fi

# --- Setup Shared Flags ---
DATA_FLAG="-t -1"
SNAPSHOT_PREFIX="Asimov"
if [[ ${ASIMOV} -eq 0 ]]; then
  DATA_FLAG=""
  SNAPSHOT_PREFIX="Observed"
fi

# The exact minimizer settings you validated
MINIMIZER_OPTS="--cminDefaultMinimizerStrategy 0 \
  --X-rtd MINIMIZER_freezeDisassociatedParams \
  --X-rtd MINIMIZER_multiMin_hideConstants \
  --X-rtd MINIMIZER_multiMin_maskConstraints \
  --X-rtd MINIMIZER_multiMin_maskChannels=2"

SNAPSHOT_WS="higgsCombine_${SNAPSHOT_PREFIX}Postfit.MultiDimFit.mH${MASS}.root"

# Parse steps into an associative array (Florian-style)
IFS=',' read -ra STEP_LIST <<< "${STEPS}"
declare -A DO
for s in "${STEP_LIST[@]}"; do
  DO["${s// /}"]=1
done

IFS=',' read -ra POI_ARRAY <<< "${POIS}"

# ==============================================================================
# EXECUTION STEPS
# ==============================================================================

# 1. SNAPSHOT
if [[ -n "${DO[snapshot]:-}" ]]; then
  echo ">>> Running Snapshot (${SNAPSHOT_PREFIX})..."
  combine -M MultiDimFit "${WORKSPACE}" -m "${MASS}" ${DATA_FLAG} \
    --setParameters r_tHq=1,r_ttH=1,MH="${MASS}" \
    --freezeParameters MH \
    --saveWorkspace --saveFitResult -n "_${SNAPSHOT_PREFIX}Postfit" \
    -P r_tHq -P r_ttH --floatOtherPOIs 1 \
    ${MINIMIZER_OPTS}
fi

# 2. SYSTEMATIC SCANS
if [[ -n "${DO[scan-syst]:-}" ]]; then
  for POI in "${POI_ARRAY[@]}"; do
    echo ">>> Running Syst Scan for ${POI}..."
    combine -M MultiDimFit "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
      -n "_scan_syst_${POI}" \
      --algo grid --points "${POINTS}" \
      -P "${POI}" --floatOtherPOIs 1 \
      --setParameters MH="${MASS}",r_tHq=1,r_ttH=1 \
      --setParameterRanges "${RANGES}" \
      --freezeParameters MH \
      --saveSpecifiedNuis all \
      ${MINIMIZER_OPTS}
  done
fi

# 3. STAT-ONLY SCANS
if [[ -n "${DO[scan-stat]:-}" ]]; then
  for POI in "${POI_ARRAY[@]}"; do
    echo ">>> Running Stat-Only Scan for ${POI}..."
    combine -M MultiDimFit "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
      -n "_scan_stat_${POI}" \
      --algo grid --points "${POINTS}" \
      -P "${POI}" --floatOtherPOIs 1 \
      --setParameters MH="${MASS}",r_tHq=1,r_ttH=1 \
      --setParameterRanges "${RANGES}" \
      --freezeParameters MH,allConstrainedNuisances \
      --saveSpecifiedNuis all \
      ${MINIMIZER_OPTS}
  done
fi

# 4. LIMITS (Defaulting to r_tHq as the signal target)
if [[ -n "${DO[limit]:-}" ]]; then
  TARGET_POI="r_tHq" # Usually we limit tH
  echo ">>> Calculating Limits for ${TARGET_POI}..."
  
  LIMIT_RUN_MODE="--run expected"
  if [[ ${ASIMOV} -eq 0 ]]; then LIMIT_RUN_MODE="--run blind"; fi # Or remove entirely for observed

  combine -M AsymptoticLimits "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
    ${LIMIT_RUN_MODE} \
    --redefineSignalPOI "${TARGET_POI}" \
    --rMin 0 --rMax 25 \
    --setParameters MH="${MASS}",r_tHq=1,r_ttH=1 \
    --freezeParameters MH \
    -n "_limit_${TARGET_POI}" \
    ${MINIMIZER_OPTS}
fi

# 5. SIGNIFICANCE (Defaulting to r_ttH as the signal target)
if [[ -n "${DO[significance]:-}" ]]; then
  TARGET_POI="r_ttH" # Usually we want the significance of ttH
  echo ">>> Calculating Significance for ${TARGET_POI}..."
  combine -M Significance "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
    --redefineSignalPOI "${TARGET_POI}" \
    --rMin 0 --rMax 5 \
    --setParameters MH="${MASS}",r_tHq=1,r_ttH=1 \
    --freezeParameters MH \
    -n "_significance_${TARGET_POI}" \
    ${MINIMIZER_OPTS}
fi

echo ">>> All requested steps completed successfully."
