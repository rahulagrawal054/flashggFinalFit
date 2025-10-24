#!/usr/bin/env bash
set -euo pipefail

# which eras to process
eras=(2022postEE)

# NOTE: COMMENT IN ONE AFTER EACH OTHER WHEN THE CONDOR JOBS ARE FINISHED!
for era in "${eras[@]}"; do
  echo ">>> Running signal scripts for era: $era"

  echo ">>> Running fTest..."
  python3 RunSignalScripts.py \
    --inputConfig config_${era}.py \
    --mode fTest \
    --modeOpts "--doPlots"

  echo ">>> Running full signal fit..."
  python3 RunSignalScripts.py \
    --inputConfig config_${era}.py \
    --mode signalFit \
    --groupSignalFitJobsByCat \
    --modeOpts "--skipVertexScenarioSplit --skipSystematics --doPlots"
done

echo ">>> All steps completed."

