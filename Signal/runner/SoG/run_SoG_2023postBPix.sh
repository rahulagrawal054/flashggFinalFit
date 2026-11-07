#!/usr/bin/env bash
set -eo pipefail
signal_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
output_root="$signal_dir/outdir_2022_2023_v001"
ext="fiducial_2023postBPix_SoG"
config="$signal_dir/config/SoG/config_2023postBPix_fiducial_SoG.py"
outdir="$output_root/outdir_$ext"
if [[ -e "$outdir" || -e "$signal_dir/outdir_$ext" ]]; then
  echo "Output already exists; inspect it before starting a fresh run: $outdir" >&2
  exit 1
fi
mkdir -p "$outdir"
exec > >(tee "$outdir/run.log") 2>&1
trap 'status=$?; echo "$status" > "$outdir/exit_status.txt"' EXIT
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd "$signal_dir/../../.."
eval "$(scram runtime -sh)"
cd "$signal_dir"
source ../setup.sh
export ANALYSIS_PATH="$signal_dir/.."
export PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$signal_dir:$signal_dir/../commonTools:${PYTHONPATH:-}"
cp "$config" "$outdir/"
run_stage() {
  local stage="$1"
  shift
  echo "Starting $stage: $(date -Is)"
  python3 -u RunSignalScripts.py --inputConfig "$config" --mode "$stage" --printOnly "$@"
  mkdir -p "$outdir/$stage"
  mv "$signal_dir/outdir_$ext/$stage/jobs" "$outdir/$stage/jobs"
  rmdir "$signal_dir/outdir_$ext/$stage" "$signal_dir/outdir_$ext"
  for job in "$outdir/$stage/jobs/"*.sh; do
    echo "Running $job"
    bash "$job"
  done
  echo "Finished $stage: $(date -Is)"
}
run_stage fTest --modeOpts "--doPlots --skipWV --outputDir $output_root"
run_stage calcPhotonSyst --modeOpts "--outputDir $output_root"
run_stage signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --MHPolyOrder 0 --doPlots --outputDir $output_root"
echo "Finished. Inspect optimizer warnings and output quality before accepting the fits."
