#!/usr/bin/env bash
set -eo pipefail

# Run from any directory. Each invocation has an isolated working directory.
signal_dir="$(cd -- "$(dirname -- "$(realpath -- "${BASH_SOURCE[0]}")")/../.." && pwd)"
run_dir="$signal_dir/runs/SoG/2023preBPix/$(date +%Y%m%d_%H%M%S)_$$"
mkdir -p "$run_dir/Signal"
echo "Running SoG, 2023preBPix. All output: $run_dir/run.log"
exec > >(tee "$run_dir/run.log") 2>&1
trap 'status=$?; echo "$status" > "$run_dir/exit_status.txt"; echo "Script exit status: $status"' EXIT

# Initialize CMSSW and use the existing fitting code without copying or editing it.
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd "$signal_dir/../../.."
eval "$(scram runtime -sh)"
cd "$signal_dir"
source ../setup.sh
export PYTHONUNBUFFERED=1
export PYTHONPATH="$signal_dir:$signal_dir/../commonTools:${PYTHONPATH:-}"
export ANALYSIS_PATH="$run_dir"
ln -s "$signal_dir/../commonTools" "$run_dir/commonTools"
ln -s "$signal_dir/tools" "$run_dir/Signal/tools"
ln -s "$signal_dir/scripts" "$run_dir/Signal/scripts"
ln -s "$signal_dir/RunSignalScripts.py" "$run_dir/Signal/RunSignalScripts.py"
cp "$signal_dir/config/SoG/config_2023preBPix_fiducial_SoG.py" "$run_dir/Signal/config_2023preBPix_fiducial_SoG.py"
cd "$run_dir/Signal"

# Generate jobs, then run them directly so a failed command stops this script.
# The local driver otherwise ignores child-job exit codes.
echo "Starting fTest: $(date -Is)"
python3 -u RunSignalScripts.py --inputConfig config_2023preBPix_fiducial_SoG.py --mode fTest --printOnly --modeOpts "--doPlots --skipWV"
for job in outdir_fiducial_2023preBPix_SoG/fTest/jobs/*.sh; do
  echo "Running $job"
  bash "$job"
done
echo "Finished fTest: $(date -Is)"

echo "Starting calcPhotonSyst: $(date -Is)"
python3 -u RunSignalScripts.py --inputConfig config_2023preBPix_fiducial_SoG.py --mode calcPhotonSyst --printOnly
for job in outdir_fiducial_2023preBPix_SoG/calcPhotonSyst/jobs/*.sh; do
  echo "Running $job"
  bash "$job"
done
echo "Finished calcPhotonSyst: $(date -Is)"

echo "Starting signalFit: $(date -Is)"
python3 -u RunSignalScripts.py --inputConfig config_2023preBPix_fiducial_SoG.py --mode signalFit --groupSignalFitJobsByCat --printOnly --modeOpts "--skipVertexScenarioSplit --MHPolyOrder 0 --doPlots"
for job in outdir_fiducial_2023preBPix_SoG/signalFit/jobs/*.sh; do
  echo "Running $job"
  bash "$job"
done
echo "Finished signalFit: $(date -Is)"

echo "All stages finished. Inspect optimizer warnings and outputs before accepting the fits."
