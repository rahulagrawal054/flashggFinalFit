#!/bin/bash
# Sequential significance calibration. Setup needs an explicitly chosen dataset.
# -c ttH: test r_ttH, other fixed at 1. -c tHq: test r_tHq, other profiled.
# -c combined: choose test with -p r_ttH or -p r_tHq; other profiled.
# -v changes the other strength's null generating truth (profiled default 0).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
usage() {
  echo "Usage: bash $0 -w workspace.root -l label -n toys -c ttH|tHq|combined -D dataset [-p r_ttH|r_tHq] [-v otherTruth] [-S setup|generate|fixed|envelope|plots|all] [-m mass] [-s seed] [-d]"
  echo "Default stage: setup. -d previews commands without fitting. No parallel jobs."
}
WS= LABEL= NTOYS= CASE= DATASET= POI= OTHER_VALUE= STAGE=setup MH=125.09 SEED=12345 DRY=()
while getopts 'w:l:n:c:D:p:v:S:m:s:dh' opt; do
  case "$opt" in
    w) WS="$OPTARG";; l) LABEL="$OPTARG";; n) NTOYS="$OPTARG";; c) CASE="$OPTARG";;
    D) DATASET="$OPTARG";; p) POI="$OPTARG";; v) OTHER_VALUE="$OPTARG";; S) STAGE="$OPTARG";;
    m) MH="$OPTARG";; s) SEED="$OPTARG";; d) DRY=(--dryRun);; h) usage; exit 0;; *) usage; exit 1;;
  esac
done
[[ -n "$WS" && -n "$LABEL" && -n "$NTOYS" && -n "$CASE" && -n "$DATASET" ]] || { usage; exit 1; }
case "$CASE" in
 ttH) [[ -z "$POI" || "$POI" == r_ttH ]] || exit 1; POI=r_ttH; TREATMENT=fixed; : "${OTHER_VALUE:=1}"; OTHER=r_tHq;;
 tHq) [[ -z "$POI" || "$POI" == r_tHq ]] || exit 1; POI=r_tHq; TREATMENT=profiled; : "${OTHER_VALUE:=0}"; OTHER=r_ttH;;
 combined) [[ "$POI" == r_ttH || "$POI" == r_tHq ]] || { echo 'Choose combined target with -p'; exit 1; }; TREATMENT=profiled; : "${OTHER_VALUE:=0}"; if [[ "$POI" == r_ttH ]]; then OTHER=r_tHq; else OTHER=r_ttH; fi;;
 *) usage; exit 1;;
esac
case "$STAGE" in setup|generate|fixed|envelope|plots|all) ;; *) usage; exit 1;; esac
COMMON=(--inputWSFile "$WS" --label "$LABEL" --nToys "$NTOYS" --POI "$POI" --otherMode "$TREATMENT" --otherValue "$OTHER_VALUE" --dataset "$DATASET" --MH "$MH" --seed "$SEED" --outDir "$SCRIPT_DIR")
run_step() { python3 -B -u "$SCRIPT_DIR/RunBiasInSignificance_twoPOIs.py" "${COMMON[@]}" "${DRY[@]}" --mode "$1"; }
if [[ "$STAGE" == all ]]; then
  for step in setup generate fixed envelope; do run_step "$step"; done
elif [[ "$STAGE" != plots ]]; then
  run_step "$STAGE"
fi
if [[ "$STAGE" == all || "$STAGE" == plots ]]; then
  if (( ${#DRY[@]} )); then echo 'Dry run: plotting skipped.'; exit 0; fi
  VALUE_TAG="$(python3 -c 'import sys; print(format(float(sys.argv[1]), "g"))' "$OTHER_VALUE")"
  OUT="$SCRIPT_DIR/${LABEL}_${POI}_${OTHER}_${TREATMENT}${VALUE_TAG}_${NTOYS}toys"
  python3 -B "$SCRIPT_DIR/SummaryBiasSignificance.py" -i "$OUT" --expectedToys "$NTOYS"
fi
