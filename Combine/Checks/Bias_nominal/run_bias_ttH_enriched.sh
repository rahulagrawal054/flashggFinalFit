#!/bin/bash
# Nominal bias study for ONE ttH-enriched category (Group A), using the
# 2D workspace with r_tHq held FIXED at its SM value (1) and r_ttH measured.
#
# Put this file in  .../Combine/Checks/Bias_nominal/  next to
# RunBiasStudy_twoPOI.py and biasUtils.py. Datacards are read from
# .../Combine/Checks/inputs_DCB/Datacard_<category>_r_2D_fiducial.root
#
# DRY RUN is the default: nothing is executed until you pass --run.
#
#   ./run_bias_ttH_enriched.sh                          # dry run, ttH_had_1, pilot
#   ./run_bias_ttH_enriched.sh --run                    # pilot: bern1, 100 toys, truth 0,1,2
#   ./run_bias_ttH_enriched.sh --stage full --run       # all functions, 1000 toys, truth 0,1,2,3
#   ./run_bias_ttH_enriched.sh --stage full --step plots --run   # redo plots only
#
# Every run goes in its own folder, so runs with different ranges never
# overwrite each other:
#   BiasStudy_<category>/<stage>_rMin<..>_rMax<..>_n<..>_seed<..>/

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/RunBiasStudy_twoPOI.py"
DCB_DIR="$SCRIPT_DIR/../inputs_DCB"

# ---------------------------------------------------------------- defaults
CATEGORY="ttH_had_1"
STAGE="pilot"          # pilot | full
STEP="all"             # all | toys | fits | plots | summary
SEED=12345
MH=125.09
RMIN=""                # per-category, see below
RMAX=15
FIT_START=0.5          # start of the measured POI; keep it OUT of the truth grid
NTOYS=""
GRID=""
SELECT="__unset__"
RUN=0
WALL_WARN=0.05         # >5% of best fits on the lower wall => Gaussian pull not trustworthy

usage() { sed -n '2,19p' "$0" | sed 's/^# \{0,1\}//'; echo
cat <<'EOF'
Options:
  --category NAME   ttH_had_1..4 or ttH_lep_1..4         (default ttH_had_1)
  --stage pilot|full                                      (default pilot)
                      pilot: bern1 only, 100 toys, truth 0,1,2
                      full : all functions, 1000 toys, truth 0,1,2,3
  --step all|toys|fits|plots|summary                      (default all)
  --rmin X          lower r_ttH limit (REQUIRED for categories other than ttH_had_1)
  --rmax X          upper r_ttH limit                     (default 15)
  --nToys N   --grid 0,1,2   --functions bern1   --seed N   --mH X   --fitStart X
  --run             actually execute (default is a dry run)
EOF
}

# ---------------------------------------------------------------- arguments
ORIG_ARGS=("$@")
SCRIPT_PATH="$SCRIPT_DIR/$(basename "${BASH_SOURCE[0]}")"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --category)  CATEGORY="$2"; shift 2 ;;
    --stage)     STAGE="$2"; shift 2 ;;
    --step)      STEP="$2"; shift 2 ;;
    --rmin)      RMIN="$2"; shift 2 ;;
    --rmax)      RMAX="$2"; shift 2 ;;
    --nToys)     NTOYS="$2"; shift 2 ;;
    --grid)      GRID="$2"; shift 2 ;;
    --functions) SELECT="$2"; shift 2 ;;
    --seed)      SEED="$2"; shift 2 ;;
    --mH)        MH="$2"; shift 2 ;;
    --fitStart)  FIT_START="$2"; shift 2 ;;
    --run)       RUN=1; shift ;;
    -h|--help)   usage; exit 0 ;;
    *) echo "Unknown option: $1"; usage; exit 1 ;;
  esac
done

die() { echo "ERROR: $*" >&2; exit 1; }
is_num() { [[ "$1" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; }

# ---------------------------------------------------------------- category
case "$CATEGORY" in
  ttH_had_1|ttH_had_2|ttH_had_3|ttH_had_4|ttH_lep_1|ttH_lep_2|ttH_lep_3|ttH_lep_4) ;;
  tH_*|bkg_*)
    die "$CATEGORY is not a ttH-enriched category. tH_* categories need BOTH POIs real (r_tHq profiled, two-POI grid) and bkg_* is a different regime - this runner only does r_ttH with r_tHq fixed." ;;
  *) die "Unknown category '$CATEGORY'" ;;
esac

# Lower r_ttH limit must keep signal+background positive, which depends on the
# category's background density. It has only been checked for ttH_had_1.
if [[ -z "$RMIN" ]]; then
  case "$CATEGORY" in
    ttH_had_1) RMIN="-0.5" ;;
    *) die "No validated lower limit for $CATEGORY (the -0.5 for ttH_had_1 was checked against that category's background density only). Pass --rmin explicitly after checking positivity for this category." ;;
  esac
fi

case "$STAGE" in
  pilot) : "${NTOYS:=100}";  : "${GRID:=0,1,2}";   [[ "$SELECT" == "__unset__" ]] && SELECT="bern1" ;;
  full)  : "${NTOYS:=1000}"; : "${GRID:=0,1,2,3}"; [[ "$SELECT" == "__unset__" ]] && SELECT="" ;;
  *) die "--stage must be pilot or full" ;;
esac
[[ "$SELECT" == "__unset__" ]] && SELECT=""

case "$STEP" in all|toys|fits|plots|summary) ;; *) die "--step must be all|toys|fits|plots|summary" ;; esac
for v in "$RMIN" "$RMAX" "$FIT_START" "$MH"; do is_num "$v" || die "'$v' is not a number"; done
[[ "$SEED" =~ ^[0-9]+$ && "$NTOYS" =~ ^[0-9]+$ ]] || die "--seed and --nToys must be non-negative integers"

# ---------------------------------------------------------------- inputs
DATACARD="$(cd "$DCB_DIR" 2>/dev/null && pwd)/Datacard_${CATEGORY}_r_2D_fiducial.root" || die "inputs_DCB not found at $DCB_DIR"
[[ -f "$DATACARD" ]] || die "Datacard not found: $DATACARD"
[[ -f "$PY_SCRIPT" ]] || die "Not found: $PY_SCRIPT"
python3 -c "import ROOT" 2>/dev/null || die "Cannot import ROOT. Run 'cmsenv' in your CMSSW area first."
if [[ $RUN -eq 1 && ( "$STEP" == "all" || "$STEP" == "toys" || "$STEP" == "fits" ) ]]; then
  command -v combine >/dev/null || die "'combine' not in PATH. Run 'cmsenv' in your CMSSW area first."
fi

RUN_DIR="$SCRIPT_DIR/BiasStudy_${CATEGORY}/${STAGE}_rMin${RMIN}_rMax${RMAX}_n${NTOYS}_seed${SEED}"

FIT_OPTIONS="--cminDefaultMinimizerStrategy 0 --robustFit 1 --setRobustFitStrategy 0 --freezeParameters MH --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"

EXTRA=()
[[ -n "$SELECT" ]] && EXTRA+=(--selectFunction "$SELECT")
COMMON=(-d "$DATACARD" --poi r_ttH --floatOtherPOIs 0
        --gridTtH "$GRID" --gridTHq 1
        "--rMinTtH=$RMIN" "--rMaxTtH=$RMAX"
        --combineOptions "$FIT_OPTIONS"
        -m "$MH" -s "$SEED" -n "$NTOYS" ${EXTRA[@]+"${EXTRA[@]}"})

echo "=============================================================="
echo " Category      : $CATEGORY   (POI r_ttH, r_tHq fixed at 1)"
echo " Stage         : $STAGE      Step: $STEP"
echo " Functions     : ${SELECT:-all in the envelope}"
echo " Truth grid    : r_ttH = $GRID"
echo " Fit range     : r_ttH in [$RMIN, $RMAX]   (start $FIT_START)"
echo " Toys / seed   : $NTOYS / $SEED       mH: $MH"
echo " Run folder    : $RUN_DIR"
echo " Mode          : $([[ $RUN -eq 1 ]] && echo EXECUTE || echo 'DRY RUN (add --run to execute)')"
echo "=============================================================="

pyrun() { python3 -B -u "$PY_SCRIPT" "$@"; }

# ---------------------------------------------------------------- dry run
if [[ $RUN -eq 0 ]]; then
  cd "$SCRIPT_DIR"      # the script writes nothing in dry-run mode
  case "$STEP" in
    all|toys|fits)
      pyrun "${COMMON[@]}" --toys --fits --fitStart "$FIT_START" --dryRun ;;
    plots|summary)
      echo "Nothing to preview for step '$STEP' (it only reads existing results)." ;;
  esac
  echo
  echo "Dry run only. Check: --floatOtherPOIs 0, the r_ttH range, '--setParameters r_ttH=$FIT_START,r_tHq=1' in the fit lines, -m $MH."
  exit 0
fi

# ---------------------------------------------------------------- real run
mkdir -p "$RUN_DIR"
cd "$RUN_DIR"
{
  echo "date      : $(date -u +%FT%TZ)"
  echo "host      : $(hostname)"
  printf 'command   : bash %q' "$SCRIPT_PATH"
  if (( ${#ORIG_ARGS[@]} )); then printf ' %q' "${ORIG_ARGS[@]}"; fi
  printf '\n'
  echo "script sha: $(sha256sum "$PY_SCRIPT" | cut -d' ' -f1)"
  echo "datacard  : $DATACARD"
} >> run_info.txt

stamp() { echo; echo "---- $* ----"; }

if [[ "$STEP" == "all" || "$STEP" == "toys" ]]; then
  stamp "toys"
  pyrun "${COMMON[@]}" --toys 2>&1 | tee -a runner_toys.log
fi
if [[ "$STEP" == "all" || "$STEP" == "fits" ]]; then
  stamp "fits"
  pyrun "${COMMON[@]}" --fits --fitStart "$FIT_START" 2>&1 | tee -a runner_fits.log
fi
if [[ "$STEP" == "all" || "$STEP" == "plots" ]]; then
  stamp "plots"
  # same options as the fits, so the saved-command check in the script passes
  pyrun "${COMMON[@]}" --plots --gaussianFit 2>&1 | tee -a runner_plots.log
fi

# ---------------------------------------------------------------- summary
if [[ "$STEP" == "all" || "$STEP" == "plots" || "$STEP" == "summary" ]]; then
  stamp "summary"
  JSON="BiasPlots/BiasResults_r_ttH_seed${SEED}.json"
  [[ -f "$JSON" ]] || die "$JSON not found - run the plots step first"
  python3 - "$JSON" "$WALL_WARN" <<'PYEOF'
import json, sys, math, statistics as st
d = json.load(open(sys.argv[1])); wall_warn = float(sys.argv[2])
def finite(x):
    return isinstance(x, (int, float)) and math.isfinite(x)
fmt = lambda x, f: "   n/a" if not finite(x) else format(x, f)
# log lines that show the minimiser reached a negative pdf (the bias script itself only counts the first)
PATTERNS = ("Number of events is negative", "underflow to", "FASTEXIT")
def scan(entry):
    if not entry.get("fitLogs"):
        return None
    counts = [0, 0, 0]
    for rec in entry.get("fitLogs", []):
        try:
            with open(rec["log"], errors="replace") as fh:
                for line in fh:
                    for i, pat in enumerate(PATTERNS):
                        if pat.lower() in line.lower(): counts[i] += 1
        except (OSError, KeyError):
            return None
    return counts
print(f"{'function_truth':28s} {'ok/req':>9s} {'wall%':>6s} {'mean(bf-t)':>10s} {'median':>8s} "
      f"{'gaus bias':>10s} {'sigma':>6s} {'neg/under/fastexit':>20s}  flag")
for k, e in d.items():
    poi = e["poi"]; truth = e["truth_" + poi]
    lo = e["metadata"]["fitRanges"][poi][0]; tol = e["boundaryTolerance"]
    bf = [t["values"]["bestFit"] for t in e["toyDiagnostics"] if "values" in t and finite(t["values"].get("bestFit"))]
    dx = [x - truth for x in bf]
    wall = sum(abs(x - lo) <= tol for x in bf) / len(bf) if bf else float("nan")
    bias = e.get("bias")
    invalid = False
    for t in e["toyDiagnostics"]:
        v = t.get("values", {})
        if not all(finite(v.get(key)) for key in ("lower", "bestFit", "upper")):
            invalid = True
        elif not v["lower"] < v["bestFit"] < v["upper"]:
            invalid = True
    failures = e.get("failedToys", 0) or e.get("missingToyResults", 0)
    flags = []
    if failures or invalid or not bf:
        flags.append("REVIEW invalid/missing intervals")
    if wall > wall_warn:
        flags.append("WALL (pull mean unreliable)")
    if not finite(bias):
        flags.append("REVIEW no gaussian fit")
    elif abs(bias) < 0.14:
        flags.append("PULL-ONLY <0.14; review coverage/domain")
    elif abs(bias) < 0.20:
        flags.append("WARN pull mean")
    else:
        flags.append("FAIL pull mean")
    g = e.get("gaussianFit") or {}
    if g.get("status") != 0:
        flags.append("REVIEW gaussian fit status")
    flag = "; ".join(flags)
    pos = scan(e)
    if pos is None:             posstr = "logs unreadable"; flag += " [pdf check impossible]"
    else:
        posstr = "/".join(str(n) for n in pos)
        if any(pos):            flag += " [LOG-WARNING: inspect fit logs]"
    if not e["metadata"].get("fitSettingsVerified", False): flag += " [settings unverified]"
    name = k.replace("_seed%d" % e["seed"], "")
    print(f"{name:28s} {e['pullEntries']:4d}/{e['metadata']['nToysRequested']:<4d} {100*wall:6.1f} "
          f"{(st.mean(dx) if dx else float('nan')):+10.3f} {(st.median(dx) if dx else float('nan')):+8.3f} "
          f"{fmt(bias, '+10.3f'):>10s} {fmt(e.get('sigma'), '6.2f'):>6s} {posstr:>20s}  {flag}")
print(f"\nwall% = fraction of best fits sitting on the lower r_ttH limit. Above {100 * wall_warn:.0f}% the pull "
      "histogram has substantial boundary accumulation; its mean alone cannot validate bias.")
print("mean(bf-t) and median are descriptive statistics; boundaries, fit failures and model validity still require review.")
print("neg/under/fastexit = log lines 'Number of events is negative' / 'underflow to' / 'FASTEXIT'. Zero only means the "
      "listed messages were not found; it does NOT establish PDF positivity. Underflow and FASTEXIT alone do not diagnose a negative PDF.")
PYEOF
fi

echo
echo "Done. Results in: $RUN_DIR"
