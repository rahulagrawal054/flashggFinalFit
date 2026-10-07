#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOM'
Usage: bash run_2D_fiducial.sh --steps <list> --workspace <file> [options]

Steps (comma-separated):
  snapshot      Create the postfit workspace (Asimov or Observed)
  scan-syst     Run 1D profile likelihood scans with full systematics
  scan-stat     Run 1D profile likelihood scans with stat-only uncertainties
  limit         Calculate expected/observed upper limit for a specific POI
  significance  Calculate expected/observed significance for a specific POI

Options:
  --workspace <file>     Path to the input ROOT workspace (required, no default --
                          past confusion came from a silently-wrong default here)
  --mass <value>         Higgs mass (default: 125.08)
  --pois <list>          Comma-separated list of POIs to scan (default: r_tHq,r_ttH)
  --ranges <ranges>      Parameter ranges (default: r_tHq=-20,25:r_ttH=-0.5,3.0)
  --points <N>           Number of points for grid scans (default: 100)
  --limit-poi <name>     POI to compute the limit for (default: r_tHq)
  --significance-poi <n> POI to compute significance for (default: r_ttH)
  --freeze-extra <list>  Comma-separated name=value pairs to fix at a specific
                          value AND freeze, on top of MH, for every step --
                          e.g. to test removing a systematic's effect:
                          --freeze-extra "CMS_hgg_nuisance_Smearing=0"
                          Multiple: --freeze-extra "paramA=0,paramB=1"
  --no-asimov            Run on observed data instead of expected Asimov (-t -1)
  -h, --help             Show this help message

Example:
  bash run_2D_fiducial.sh --workspace Datacard_fiducial_allCats_SoG_r_2D_fiducial.root \
    --steps snapshot,scan-syst,scan-stat,limit,significance

Example, removing Smearing's effect:
  bash run_2D_fiducial.sh --workspace Datacard_fiducial_allCats_DCB_r_2D_fiducial.root \
    --steps significance,limit \
    --freeze-extra "CMS_hgg_nuisance_Smearing=0"
EOM
}

# --- Default Configuration ---
WORKSPACE=""
MASS="125.08"
POIS="r_tHq,r_ttH"
RANGES="r_tHq=-20,25:r_ttH=-0.5,3.0"
POINTS="100"
LIMIT_POI="r_tHq"
SIGNIFICANCE_POI="r_ttH"
FREEZE_EXTRA=""
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
    --limit-poi) LIMIT_POI="$2"; shift 2 ;;
    --significance-poi) SIGNIFICANCE_POI="$2"; shift 2 ;;
    --freeze-extra) FREEZE_EXTRA="$2"; shift 2 ;;
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

if [[ -z "${WORKSPACE}" ]]; then
  echo "[ERROR] --workspace is required (no default -- this is what silently" >&2
  echo "        picked up the wrong file before)." >&2
  usage >&2
  exit 1
fi

if [[ ! -f "${WORKSPACE}" ]]; then
  echo "[ERROR] Workspace not found: ${WORKSPACE}" >&2
  exit 1
fi

# --- Build the extra set/freeze parameter strings ---
# FREEZE_EXTRA looks like "paramA=0,paramB=1" -- split into the values
# needed for --setParameters (name=value, comma list) and --freezeParameters
# (just names, comma list).
EXTRA_SET=""
EXTRA_FREEZE=""
if [[ -n "${FREEZE_EXTRA}" ]]; then
  IFS=',' read -ra PAIRS <<< "${FREEZE_EXTRA}"
  for pair in "${PAIRS[@]}"; do
    name="${pair%%=*}"
    EXTRA_SET="${EXTRA_SET},${pair}"
    EXTRA_FREEZE="${EXTRA_FREEZE},${name}"
  done
  echo ">>> Freezing extra parameter(s): ${FREEZE_EXTRA}"
fi

# --- Setup Shared Flags ---
DATA_FLAG="-t -1"
SNAPSHOT_PREFIX="Asimov"
if [[ ${ASIMOV} -eq 0 ]]; then
  DATA_FLAG=""
  SNAPSHOT_PREFIX="Observed"
fi

# Validated minimizer configuration. strategy 0 (the previous default here)
# converges fast but under-converges on this fit -- 16 categories, discrete
# background envelope, 2 correlated POIs is genuinely hard, and strategy 0
# was traced to giving wrong central values before. strategy 2 + a realistic
# tolerance + the X-rtd flags (which correctly freeze inactive discrete
# background-envelope parameters) is what actually converges cleanly here --
# confirmed via matching joint-fit and grid-scan results and clean per-
# category status=0 fits. No --robustFit / --cminFallbackAlgo needed with
# this combination; those were previously masking (not fixing) the same
# Hessian-validity failure that the X-rtd flags address directly.
MINIMIZER_OPTS="--cminDefaultMinimizerStrategy 2 \
  --cminDefaultMinimizerTolerance 0.1 \
  --X-rtd MINIMIZER_freezeDisassociatedParams \
  --X-rtd MINIMIZER_multiMin_hideConstants \
  --X-rtd MINIMIZER_multiMin_maskConstraints \
  --X-rtd MINIMIZER_multiMin_maskChannels=2"

SNAPSHOT_WS="higgsCombine_${SNAPSHOT_PREFIX}Postfit.MultiDimFit.mH${MASS}.root"

# Parse steps into an associative array
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
  LOGFILE="log_snapshot_${SNAPSHOT_PREFIX}.log"
  eval combine -M MultiDimFit "${WORKSPACE}" -m "${MASS}" ${DATA_FLAG} \
    --setParameters "r_tHq=1,r_ttH=1,MH=${MASS}${EXTRA_SET}" \
    --freezeParameters "MH${EXTRA_FREEZE}" \
    --saveWorkspace -n "_${SNAPSHOT_PREFIX}Postfit" \
    -P r_tHq -P r_ttH --floatOtherPOIs 1 \
    --verbose 3 \
    ${MINIMIZER_OPTS} 2>&1 | tee "${LOGFILE}"

  if grep -qE "MultiDimFit failed|Aborting" "${LOGFILE}"; then
    echo "[WARNING] Snapshot did not converge cleanly -- check ${LOGFILE} before trusting downstream steps." >&2
  fi
fi

# 2. SYSTEMATIC SCANS
if [[ -n "${DO[scan-syst]:-}" ]]; then
  if [[ ! -f "${SNAPSHOT_WS}" ]]; then
    echo "[ERROR] Snapshot workspace not found: ${SNAPSHOT_WS}. Run --steps snapshot first." >&2
    exit 1
  fi
  for POI in "${POI_ARRAY[@]}"; do
    echo ">>> Running Syst Scan for ${POI}..."
    eval combine -M MultiDimFit "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
      -n "_scan_syst_${POI}" \
      --algo grid --points "${POINTS}" \
      -P "${POI}" --floatOtherPOIs 1 \
      --setParameters "MH=${MASS},r_tHq=1,r_ttH=1${EXTRA_SET}" \
      --setParameterRanges "${RANGES}" \
      --freezeParameters "MH${EXTRA_FREEZE}" \
      --saveSpecifiedNuis all \
      ${MINIMIZER_OPTS} 2>&1 | tee "log_scan_syst_${POI}.log"
  done
fi

# 3. STAT-ONLY SCANS
if [[ -n "${DO[scan-stat]:-}" ]]; then
  if [[ ! -f "${SNAPSHOT_WS}" ]]; then
    echo "[ERROR] Snapshot workspace not found: ${SNAPSHOT_WS}. Run --steps snapshot first." >&2
    exit 1
  fi
  for POI in "${POI_ARRAY[@]}"; do
    echo ">>> Running Stat-Only Scan for ${POI}..."
    eval combine -M MultiDimFit "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
      -n "_scan_stat_${POI}" \
      --algo grid --points "${POINTS}" \
      -P "${POI}" --floatOtherPOIs 1 \
      --setParameters "MH=${MASS},r_tHq=1,r_ttH=1${EXTRA_SET}" \
      --setParameterRanges "${RANGES}" \
      --freezeParameters "MH,allConstrainedNuisances${EXTRA_FREEZE}" \
      --saveSpecifiedNuis all \
      ${MINIMIZER_OPTS} 2>&1 | tee "log_scan_stat_${POI}.log"
  done
fi

# 4. LIMIT
if [[ -n "${DO[limit]:-}" ]]; then
  if [[ ! -f "${SNAPSHOT_WS}" ]]; then
    echo "[ERROR] Snapshot workspace not found: ${SNAPSHOT_WS}. Run --steps snapshot first." >&2
    exit 1
  fi
  echo ">>> Calculating Limit for ${LIMIT_POI}..."

  LIMIT_RUN_MODE="--run expected"
  if [[ ${ASIMOV} -eq 0 ]]; then LIMIT_RUN_MODE="--run blind"; fi

  eval combine -M AsymptoticLimits "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
    ${LIMIT_RUN_MODE} \
    --redefineSignalPOI "${LIMIT_POI}" \
    --rMin 0 --rMax 25 \
    --setParameters "MH=${MASS},r_tHq=1,r_ttH=1${EXTRA_SET}" \
    --freezeParameters "MH${EXTRA_FREEZE}" \
    -n "_limit_${LIMIT_POI}" \
    ${MINIMIZER_OPTS} 2>&1 | tee "log_limit_${LIMIT_POI}.log"
fi

# 5. SIGNIFICANCE
if [[ -n "${DO[significance]:-}" ]]; then
  if [[ ! -f "${SNAPSHOT_WS}" ]]; then
    echo "[ERROR] Snapshot workspace not found: ${SNAPSHOT_WS}. Run --steps snapshot first." >&2
    exit 1
  fi
  echo ">>> Calculating Significance for ${SIGNIFICANCE_POI}..."
  eval combine -M Significance "${SNAPSHOT_WS}" --snapshotName MultiDimFit -m "${MASS}" ${DATA_FLAG} \
    --redefineSignalPOI "${SIGNIFICANCE_POI}" \
    --rMin 0 --rMax 5 \
    --setParameters "MH=${MASS},r_tHq=1,r_ttH=1${EXTRA_SET}" \
    --freezeParameters "MH${EXTRA_FREEZE}" \
    -n "_significance_${SIGNIFICANCE_POI}" \
    ${MINIMIZER_OPTS} 2>&1 | tee "log_significance_${SIGNIFICANCE_POI}.log"
fi

echo ">>> All requested steps completed successfully."
