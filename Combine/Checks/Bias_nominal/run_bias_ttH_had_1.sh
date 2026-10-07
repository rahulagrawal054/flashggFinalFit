#!/bin/bash
# Bias-nominal study for ttH_had_1, single POI r_ttH, using the
# "Goldilocks" fit range for this category: r_ttH = [-80, 80].
#
# Usage:
#   ./run_bias_ttH_had_1.sh            # dry run only (prints every combine cmd, no execution)
#   ./run_bias_ttH_had_1.sh --run      # actually execute toys -> fits -> plots
#
# Everything is logged under BiasLogs/, toys under BiasToys/, fits under
# BiasFits/, plots+JSON under BiasPlots/ - same layout as before, so this
# will OVERWRITE the earlier -1,3 run's fit/plot outputs for the same
# (function, truth) pairs. Back up BiasPlots/ first if you want to keep
# the previous results for comparison.

set -e  # stop immediately if any step fails, rather than continuing on broken output

CATEGORY="ttH_had_1"
POI="r_ttH"
POI_RANGE_MIN="-80"
POI_RANGE_MAX="80"

DATACARD="Datacard_${CATEGORY}_r_1D_ttH_fixedtHq.root"
SCRIPT="RunBiasStudy_1D_ttH.py"
NTOYS=1000
GRID="0,1,2,3,4,5"
SEED=12345   # fixed, so toys/fits/plots in this run line up, and the run is reproducible later

MODE="dryrun"
if [[ "$1" == "--run" ]]; then
    MODE="run"
fi

echo "=============================================="
echo " Bias study: ${CATEGORY}, POI=${POI}"
echo " Range: [${POI_RANGE_MIN}, ${POI_RANGE_MAX}]"
echo " Grid (truth values): ${GRID}"
echo " nToys: ${NTOYS}   seed: ${SEED}"
echo " Mode: ${MODE}"
echo "=============================================="
echo

if [[ ! -f "$DATACARD" ]]; then
    echo "ERROR: datacard ${DATACARD} not found in $(pwd). Aborting."
    exit 1
fi

DRYFLAG=""
if [[ "$MODE" == "dryrun" ]]; then
    DRYFLAG="--dryRun"
fi

echo "--- Step 1: toys ---"
python3 "$SCRIPT" -d "$DATACARD" \
    --toys -n "$NTOYS" --grid "$GRID" -s "$SEED" $DRYFLAG

echo
echo "--- Step 2: fits (range ${POI_RANGE_MIN},${POI_RANGE_MAX}) ---"
python3 "$SCRIPT" -d "$DATACARD" \
    --fits -n "$NTOYS" --grid "$GRID" -s "$SEED" \
    --rMin "$POI_RANGE_MIN" --rMax "$POI_RANGE_MAX" $DRYFLAG

if [[ "$MODE" == "dryrun" ]]; then
    echo
    echo "Dry run complete - no plots step (nothing was actually fit)."
    echo "Check the printed commands above, and BiasLogs/*.log, then rerun with --run."
    exit 0
fi

echo
echo "--- Step 3: plots ---"
python3 "$SCRIPT" -d "$DATACARD" \
    --plots -n "$NTOYS" --grid "$GRID" -s "$SEED"

echo
echo "--- Step 4: FASTEXIT / negative-pdf counts, for comparison against the -1,3 run ---"
for truth in ${GRID//,/ }; do
    for f in BiasLogs/fits_*_ttH${truth}.log; do
        [[ -e "$f" ]] || continue
        n=$(grep -c "Number of events is negative" "$f" || true)
        echo "$f : $n occurrences"
    done
done

echo
echo "--- Step 5: summary from JSON ---"
python3 - <<PYEOF
import json, glob
files = sorted(glob.glob("BiasPlots/BiasResults_r_ttH_seed${SEED}.json"))
for fn in files:
    with open(fn) as f:
        data = json.load(f)
    print(f"{'key':30s} {'bias':>10s} {'sigma':>8s} {'succeeded':>12s} {'status':>8s}")
    for key, v in data.items():
        print(f"{key:30s} {v['gaussianBias']:+10.4f} {v['gaussianSigma']:8.3f} "
              f"{v['nToysSucceeded']:5d}/{v['nToysRequested']:<6d} {v['status_0p14']:>8s}")
PYEOF

echo
echo "Done. Compare these bias numbers against the earlier -1,3 run's BiasResults JSON."
