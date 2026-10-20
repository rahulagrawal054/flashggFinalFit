#!/usr/bin/env bash
# Continue the current SoG run sequentially; no observed-data fits.
# bash continue_SoG.sh --dry-run
# nohup bash continue_SoG.sh --with-impacts > SoG/continuation.log 2>&1 &
set -euo pipefail
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="$BASE/SoG"
POINTS=300
TTH_RANGE='-0.5,3'
THQ_RANGE='-10,15'
GRID_START='r_ttH=2.9' # matches the existing DCB tHq scans
SCAN_TAG=
IMPACTS=0
DRY=0
while (( $# )); do
 case "$1" in
  --with-impacts) IMPACTS=1; shift;;
  --dry-run) DRY=1; shift;;
  --outdir|--points|--tth-range|--thq-range|--scan-tag)
   (( $# >= 2 )) || { echo "Missing value for $1"; exit 2; }
   case "$1" in --outdir) OUT="$2";; --points) POINTS="$2";; --tth-range) TTH_RANGE="$2";; --thq-range) THQ_RANGE="$2";; --scan-tag) SCAN_TAG="$2";; esac
   shift 2;;
  *) echo "Unknown option: $1"; exit 2;;
 esac
done
OUT="$(realpath -e "$OUT")"
[[ "$POINTS" =~ ^[1-9][0-9]*$ ]] || { echo 'Invalid points'; exit 2; }
[[ -z "$SCAN_TAG" || "$SCAN_TAG" =~ ^[A-Za-z0-9_-]+$ ]] || { echo 'Invalid scan tag'; exit 2; }
MODE_DIR=profile_other
[[ -z "$SCAN_TAG" ]] || MODE_DIR+="__$SCAN_TAG"
RUNNER="$BASE/runner_r_2D_fiducial.sh"
COMMON=(--workspace "$OUT/workspace.root" --outdir "$OUT" --mass 125.09)
# A separate lock prevents two continuation scripts from racing. It is distinct
# from the main runner lock, so this script can wait for the current scan.
if (( ! DRY )); then
 mkdir "$OUT/.continuation.lock" || { echo 'Another continuation is running (or its lock needs inspection).'; exit 1; }
 trap 'rc=$?; printf "%s\n" "$rc" > "$OUT/continuation_exit_status.txt"; rmdir "$OUT/.continuation.lock"' EXIT
fi
run() {
 printf '\n[%s] ' "$(date -Is)"; printf '%q ' bash "$RUNNER" "${COMMON[@]}" "$@"; printf '\n'
 if (( ! DRY )); then bash "$RUNNER" "${COMMON[@]}" "$@"; fi
}
check_scan() {
 python3 - "$1" "$POINTS" "$2" <<'PY'
from pathlib import Path
import json,sys
p=Path(sys.argv[1]);expected=int(sys.argv[2])+1
assert (p/'exit_status.txt').read_text().strip()=='0', 'Scan command failed'
v=json.loads((p/'validation.json').read_text())
assert v['entries_complete'] and v['root_entries']==expected and not v['invalid_row_indices'], 'Missing/invalid scan points; inspect validation.json'
m=json.loads((p/'manifest.json').read_text())
assert m['status']=='FINISHED_REQUIRES_REVIEW'
assert m['scan_range']==[float(x) for x in sys.argv[3].split(',')], 'Existing scan range differs from requested range'
print('Scan structurally complete:',p,'; convergence/closure still require physics review.')
PY
}
# Do not overwrite an already completed scan on restart.
scan() {
 local poi="$1" scenario="$2" span="$3"
 local stage="$OUT/scans/$poi/$scenario/$MODE_DIR"
 if (( ! DRY )) && [[ -d "$stage" ]]; then check_scan "$stage" "$span"; return; fi
 local opts=(--step scan --poi "$poi" --scenario "$scenario" --scan-range "$span" --points "$POINTS" --other-poi profile --strategy 0 --tolerance 0.01)
 if [[ -n "$SCAN_TAG" ]]; then opts+=(--scan-tag "$SCAN_TAG"); fi
 if [[ "$poi" == r_tHq ]]; then opts+=(--grid-start "$GRID_START"); fi
 run "${opts[@]}"
 if (( ! DRY )); then check_scan "$stage" "$span"; fi
}
CURRENT="$OUT/scans/r_ttH/total/$MODE_DIR"
if (( ! DRY )) && [[ -z "$SCAN_TAG" ]]; then
 echo 'Waiting for the current total ttH scan to finish (up to 48 hours).'
 deadline=$((SECONDS + 172800)); idle=0
 until [[ -f "$CURRENT/validation.json" && ! -d "$OUT/.runner.lock" ]]; do
  if [[ -f "$CURRENT/exit_status.txt" && "$(cat "$CURRENT/exit_status.txt")" != 0 ]]; then echo 'Current scan failed.'; exit 1; fi
  if [[ ! -d "$OUT/.runner.lock" ]]; then idle=$((idle+1)); else idle=0; fi
  (( idle < 10 && SECONDS < deadline )) || { echo 'Scan did not complete cleanly; inspect current scan output and lock.'; exit 1; }
  sleep 30
 done
 check_scan "$CURRENT" "$TTH_RANGE"
fi
if [[ -n "$SCAN_TAG" ]]; then
 scan r_ttH total "$TTH_RANGE"
fi
echo 'PROVISIONAL: SoG snapshot status 3 and DCB snapshot warnings remain; completion is not model validation.'
scan r_ttH statOnly "$TTH_RANGE"
scan r_tHq total "$THQ_RANGE"
scan r_tHq statOnly "$THQ_RANGE"
if [[ -n "$SCAN_TAG" ]]; then run --step plot --scan-tag "$SCAN_TAG"; else run --step plot; fi
run --step significance --poi r_ttH --ranges 'r_ttH=0,5' --other-poi profile --strategy 0 --tolerance 0.01
run --step significance --poi r_tHq --ranges 'r_tHq=0,25' --other-poi profile --strategy 0 --tolerance 0.01
# Only tHq upper limit, following the selected DCB presentation.
run --step limit --poi r_tHq --ranges 'r_tHq=0,50' --other-poi profile --strategy 0 --tolerance 0.01
run --step plot-limits
if (( IMPACTS )); then
 run --step impacts --impact-stage initial --ranges 'r_ttH=-1,3:r_tHq=-25,25' --strategy 0 --tolerance 0.01
 run --step impacts --impact-stage pilot
 run --step impacts --impact-stage fit
 echo 'Nuisance fits finished. Collection/impact plotting remains a separate reviewed step.'
fi
echo 'Continuation completed. Inspect logs and numerical warnings before interpreting comparisons.'
