#!/bin/bash
#
# Convert inputs_10Nov MC trees to workspaces (stat-only, partial Run 3).
#
#   ./run_Tree2WS_script.sh                        -> inclusive (ws_<proc>_incl)
#   ./run_Tree2WS_script.sh --doInOutSplitting     -> fiducial  (ws_<proc>_in / ws_<proc>_out)
#
# Run only some jobs (space-separated <DIR>_<YEAR> names):
#   ONLY="VH_2024 ttH_2024" ./run_Tree2WS_script.sh --doInOutSplitting
#
# Logs: logs_10Nov/<inclusive|fiducial>_<timestamp>/
#   run.log               full driver output
#   <DIR>_<YEAR>.log      converter output for each job
#   config_used.py        frozen copy of the config actually used by every job
#
# Data (run separately):
# python3 trees2ws_data.py --inputConfig config_ttH_tH_partial_run3.py --inputTreeFile inputs_10Nov/Data/allData.root --applyMassCut --massCutRange 100,180

set -o pipefail

Tree2WSDIR="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS"
CONFIG_SRC="$Tree2WSDIR/config_ttH_tH_partial_run3.py"
BASE="$Tree2WSDIR/inputs_10Nov"

MODE="inclusive"
[[ " $* " == *" --doInOutSplitting "* ]] && MODE="fiducial"

LOGDIR="$Tree2WSDIR/logs_10Nov/${MODE}_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$LOGDIR" || exit 1

# Freeze the config so later edits cannot change jobs mid-run
CONFIG="$LOGDIR/config_used.py"
cp "$CONFIG_SRC" "$CONFIG" || exit 1

exec > >(tee -a "$LOGDIR/run.log") 2>&1

YEARS=(2022preEE 2022postEE 2023preBPix 2023postBPix 2024)

PROCESSES=(
    "GluGluH ggh output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root"
    "VBFH vbf output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root"
    "VH vh output_VHToGG_M125_13TeV_amcatnlo_pythia8.root"
    "bbH bbh output_BBHToGG_M125_13TeV_powheg_pythia8.root"
    "tHqHad tHqHad output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root"
    "tHqLep tHqLep output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root"
    "ttH tth output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root"
    "tHW tHW output_THWtoGG_M125_13TeV_madgraph_pythia8.root"
)

echo "Mode: $MODE   extra args: $*"
echo "Config: $CONFIG_SRC (frozen copy: $CONFIG)"
echo "Started: $(date)"

DONE=(); MISSING=()

for YEAR in "${YEARS[@]}"; do
    for PROCESS in "${PROCESSES[@]}"; do

        read -r DIR PMODE FILE <<< "$PROCESS"
        JOB="${DIR}_${YEAR}"

        if [[ -n "$ONLY" && " $ONLY " != *" $JOB "* ]]; then
            continue
        fi

        INPUT="$BASE/${JOB}/${FILE}"

        if [[ ! -f "$INPUT" ]]; then
            echo "WARNING: Missing file: $INPUT"
            MISSING+=("$JOB")
            continue
        fi

        echo "[$(date +%H:%M:%S)] Running $JOB ($PMODE) -> $LOGDIR/${JOB}.log"

        python3 "$Tree2WSDIR/trees2ws.py" \
            --inputConfig "$CONFIG" \
            --inputTreeFile "$INPUT" \
            --inputMass 125 \
            --productionMode "$PMODE" \
            --year "$YEAR" \
            "$@" > "$LOGDIR/${JOB}.log" 2>&1

        if [ $? -ne 0 ]; then
            echo "ERROR: $JOB failed! Last lines of $LOGDIR/${JOB}.log:"
            tail -n 20 "$LOGDIR/${JOB}.log"
            exit 1
        fi
        DONE+=("$JOB")

    done
done

echo
echo "Finished: $(date)"
echo "Completed (${#DONE[@]}): ${DONE[*]}"
if (( ${#MISSING[@]} )); then
    echo "SKIPPED, input missing (${#MISSING[@]}): ${MISSING[*]}"
    exit 2
fi
echo "All jobs completed!"
