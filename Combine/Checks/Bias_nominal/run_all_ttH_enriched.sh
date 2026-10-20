#!/bin/bash
# Run the bias study back to back for the remaining ttH-enriched categories,
# using run_bias_ttH_enriched.sh (same folder) for each one.
#
#   ./run_all_ttH_enriched.sh pilot                 # DRY RUN of the pilots (default, nothing executes)
#   ./run_all_ttH_enriched.sh pilot --run           # pilots: bern1, 100 toys, truth 0,1,2, all categories
#   ./run_all_ttH_enriched.sh full  --run --only ttH_had_3,ttH_had_4   # full stage for chosen categories
#
# Options after the stage are passed on to the runner (e.g. --run, --mH 125.09,
# --seed 12345, --nToys 500). Do NOT pass --category, --rmin, --stage or --step here.
# --only  a,b,c   restrict to some categories.
#
# --allow-unvalidated  lets the full stage run on a category whose rmin is not in VALIDATED below.
#
# One failing category does NOT stop the others; a status table is printed at the end.
# "completed" only means the commands ran. Whether the bias passed is in the results column
# and the summary tables. Numerical completion is not physics validation.
# Logs: BiasStudy_all_logs/<category>_<stage>.log

set -uo pipefail          # deliberately no -e: keep going after a failure

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUNNER="$SCRIPT_DIR/run_bias_ttH_enriched.sh"
LOGDIR="$SCRIPT_DIR/BiasStudy_all_logs"

# category:rmin. rmin is about 0.8 x the estimated positivity floor of r_ttH, which was
# worked out from the yield table (rough). Pilot logs alone cannot validate positivity.
# These ranges are exploratory; inspect the actual workspace and fit diagnostics.
CATEGORIES=(
  "ttH_had_2:-1.0"
  "ttH_had_3:-4.1"
  "ttH_had_4:-4.9"
  "ttH_lep_1:-0.1"
  "ttH_lep_2:-0.6"
  "ttH_lep_3:-0.9"
  "ttH_lep_4:-1.1"
)

# No ranges are validated yet. Add a category only after an explicit review.
VALIDATED=()

[[ $# -ge 1 ]] || { sed -n '2,17p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }
STAGE="$1"; shift
[[ "$STAGE" == "pilot" || "$STAGE" == "full" ]] || { echo "First argument must be pilot or full"; exit 1; }
[[ -x "$RUNNER" || -f "$RUNNER" ]] || { echo "Runner not found: $RUNNER"; exit 1; }

ONLY=""; FWD=(); RUN=0; ALLOW_UNVAL=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --only) ONLY="$2"; shift 2 ;;
    --category|--rmin|--stage|--step) echo "Do not pass $1 here (the driver sets it)"; exit 1 ;;
    --allow-unvalidated) ALLOW_UNVAL=1; shift ;;
    --run) RUN=1; FWD+=("$1"); shift ;;
    *) FWD+=("$1"); shift ;;
  esac
done

if [[ -n "$ONLY" ]]; then
  valid=" "; for e in "${CATEGORIES[@]}"; do valid+="${e%%:*} "; done
  IFS=',' read -ra want <<< "$ONLY"
  for w in "${want[@]}"; do
    [[ "$valid" == *" $w "* ]] || { echo "Unknown category '$w' in --only. Valid:$valid"; exit 1; }
  done
fi

mkdir -p "$LOGDIR"
declare -a NAMES=() STATUS=() MINUTES=() RMINS=() RESULT=() SUMOUT=()

for entry in "${CATEGORIES[@]}"; do
  cat="${entry%%:*}"; rmin="${entry##*:}"
  if [[ -n "$ONLY" && ",$ONLY," != *",$cat,"* ]]; then continue; fi

  if [[ $RUN -eq 1 && "$STAGE" == "full" && $ALLOW_UNVAL -eq 0 && " ${VALIDATED[*]-} " != *" $cat "* ]]; then
    echo; echo "SKIPPED $cat: rmin $rmin is not in VALIDATED (check positivity on the real workspace, then add it, or pass --allow-unvalidated)."
    NAMES+=("$cat"); RMINS+=("$rmin"); MINUTES+=("0"); STATUS+=("skipped"); RESULT+=("-"); SUMOUT+=("")
    continue
  fi
  echo; echo "################################################################"
  echo "# $cat   stage=$STAGE   rmin=$rmin   $(date '+%F %T')"
  echo "################################################################"
  start=$SECONDS
  bash "$RUNNER" --category "$cat" --rmin "$rmin" --stage "$STAGE" ${FWD[@]+"${FWD[@]}"} \
      2>&1 | tee -a "$LOGDIR/${cat}_${STAGE}.log"
  rc=${PIPESTATUS[0]}

  NAMES+=("$cat"); RMINS+=("$rmin"); MINUTES+=("$(( (SECONDS - start) / 60 ))")
  if [[ $rc -ne 0 ]]; then STATUS+=("FAILED(rc=$rc)")
  elif [[ $RUN -eq 1 ]]; then STATUS+=("completed")
  else STATUS+=("dry-run"); fi
  RESULT+=("-"); SUMOUT+=("")
done

# collect each completed category's summary table and count its flags
if [[ $RUN -eq 1 ]]; then
  for i in "${!NAMES[@]}"; do
    [[ "${STATUS[$i]}" == completed ]] || continue
    out="$(bash "$RUNNER" --category "${NAMES[$i]}" --rmin "${RMINS[$i]}" --stage "$STAGE" \
        ${FWD[@]+"${FWD[@]}"} --step summary 2>&1 | sed -n '/---- summary/,/^Done/p')"
    summary_rc=$?
    SUMOUT[$i]="$out"
    if [[ $summary_rc -ne 0 || "$out" != *function_truth* ]]; then
      STATUS[$i]="FAILED(summary)"
      RESULT[$i]="summary unavailable; inspect logs"
      continue
    fi
    rows="$(grep -E '^[A-Za-z0-9_.]+ +[0-9]+/[0-9]+' <<< "$out")"
    cnt() { grep -c "$1" <<< "$rows" || true; }
    RESULT[$i]="PULL-ONLY $(cnt 'PULL-ONLY') REVIEW $(cnt 'REVIEW') WARN $(cnt 'WARN') FAIL $(cnt 'FAIL') WALL $(cnt 'WALL') LOG-WARNING $(cnt 'LOG-WARNING')"
  done
fi

echo; echo "=================== overview ($STAGE) ==================="
printf '%-12s %-7s %-14s %-4s %s\n' category rmin status min "results (rows of the summary table)"
nfail=0; nran=0
for i in "${!NAMES[@]}"; do
  printf '%-12s %-7s %-14s %-4s %s\n' "${NAMES[$i]}" "${RMINS[$i]}" "${STATUS[$i]}" "${MINUTES[$i]}" "${RESULT[$i]}"
  [[ "${STATUS[$i]}" == FAILED* ]] && nfail=$((nfail+1))
  [[ "${STATUS[$i]}" == completed || "${STATUS[$i]}" == dry-run ]] && nran=$((nran+1))
done
echo '"completed" = commands ran, NOT a physics pass. PULL-ONLY is a numerical criterion; WALL/REVIEW/LOG-WARNING require inspection.'
[[ $nran -gt 0 ]] || echo "Nothing was run."

if [[ $RUN -eq 1 ]]; then
  echo; echo "=================== summary tables ==================="
  for i in "${!NAMES[@]}"; do
    [[ -n "${SUMOUT[$i]}" ]] || continue
    echo; echo "##### ${NAMES[$i]} (rmin ${RMINS[$i]})"; echo "${SUMOUT[$i]}"
  done
fi

if [[ $nfail -ne 0 ]]; then echo; echo "Failed categories: $nfail. See $LOGDIR/<category>_${STAGE}.log"; fi
if [[ $nran -eq 0 && $nfail -eq 0 ]]; then exit 2; fi
exit $nfail
