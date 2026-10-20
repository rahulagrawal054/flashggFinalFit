#!/usr/bin/env bash
# Build a card from one explicitly selected, successful yield run. No yield extraction.
set -eo pipefail
base="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)";project="$(cd "$base/.." && pwd)"
model=;yields=;out=;mass=125.09;threshold=0.001;dry=0
usage() { cat <<'HELP'
Usage: bash run_makeDatacard.sh --model DCB|SoG --yields YIELD_RUN --outdir NEW_DIR [options]
 --mass VALUE             Hypothesis mass, default 125.09
 --prune-threshold VALUE  True-yield fraction, default 0.001 (0.1%)
 --dry-run                Check input selection and print command without writing
Input must be a successful run_makeYields.sh output with yields_MODEL/*.pkl.
Uses systematics, true-yield pruning, skipCOWCorr and saved dataframe.
MC-stat uncertainty is intentionally not enabled. No Combine fits are started.
Outputs: Datacard_MODEL.txt, Dataframe/, makeDatacard.log and provenance/exit status.
HELP
}
while (( $# ));do
 case "$1" in
 --help|-h) usage;exit 0;;--dry-run) dry=1;shift;;
 --model|--yields|--outdir|--mass|--prune-threshold)
  (( $#>=2 )) || { echo "Missing value: $1" >&2;exit 2; }
  case "$1" in --model) model="$2";;--yields) yields="$2";;--outdir) out="$2";;--mass) mass="$2";;--prune-threshold) threshold="$2";;esac;shift 2;;
 *) echo "Unknown option: $1" >&2;exit 2;;esac
done
[[ "$model" == DCB || "$model" == SoG ]] && [[ -n "$yields" && -n "$out" ]] || { usage >&2;exit 2; }
yields="$(realpath -e "$yields")";out="$(realpath -m "$out")"
[[ ! -e "$out" ]] || { echo "Output exists: $out" >&2;exit 2; }
python3 -B - "$yields" "$model" "$mass" "$threshold" <<'PY'
import sys,pathlib,json,math
src,model,mass,threshold=sys.argv[1:];p=pathlib.Path(src)
assert math.isfinite(float(mass)) and float(mass)>0;assert math.isfinite(float(threshold)) and 0<=float(threshold)<1
assert (p/'exit_status.txt').read_text().strip()=='0','Yield run did not finish successfully'
m=json.loads((p/'manifest.json').read_text());assert m['model']==model
files=list((p/('yields_'+model)).glob('*.pkl'));assert files and {f.stem for f in files}==set(m['categories']),'Missing/extra category pickles'
print('Selected verified yield run:',src,'categories:',len(files))
PY
cmd=(python3 -B -u "$base/makeDatacard.py" --inputFiles "$yields" --ext "$model" --outputDir "$out" --output "Datacard_$model" --years 2022preEE,2022postEE,2023preBPix,2023postBPix --analysis tth_th_analysis_fiducial --mass "$mass" --prune --pruneThreshold "$threshold" --doTrueYield --doSystematics --skipCOWCorr --saveDataFrame)
printf '%q ' "${cmd[@]}";printf '\n'
if (( dry ));then echo 'Dry run only.';exit 0;fi
cd "$base";source /cvmfs/cms.cern.ch/cmsset_default.sh;eval "$(scram runtime -sh)";source "$project/setup.sh"
export PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
export PYTHONPATH="$base:$project/commonTools:${PYTHONPATH:-}"
mkdir -p "$(dirname "$out")";mkdir "$out"
trap 'rc=$?; printf "%s\n" "$rc" > "$out/exit_status.txt"' EXIT
cp "$base/run_makeDatacard.sh" "$out/executed_runner.sh"
printf '%q ' "${cmd[@]}" > "$out/command.sh";printf '\n' >> "$out/command.sh"
python3 -B - "$yields" "$out" "$model" "$mass" "$threshold" <<'PY'
import pathlib,sys,json,hashlib
src,out,model,mass,threshold=sys.argv[1:];base=pathlib.Path.cwd();names=['makeDatacard.py','systematics.py','datacardTools/calcSystematics.py','datacardTools/writeToDatacard.py','datacardTools/XSBR.py','../Signal/tools/XSBRMap.py','theory_uncertainties/theory_uncs_ad_interim_13p6TeV.json']
records={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in pathlib.Path(src, 'yields_'+model).glob('*.pkl')};sources={n:hashlib.sha256((base/n).read_bytes()).hexdigest() for n in names}
pathlib.Path(out,'manifest.json').write_text(json.dumps(dict(model=model,yield_input=src,yield_sha256=records,source_sha256=sources,mass=float(mass),pruneThreshold=float(threshold),MCStatUncertainty=False),indent=2)+'\n')
PY
"${cmd[@]}" 2>&1 | tee "$out/makeDatacard.log"
if rg -n '\[ERROR\]|\*\*\* ERROR|Traceback \(most recent call last\)' "$out/makeDatacard.log";then exit 1;fi
python3 -B - "$out" "$model" "$yields" <<'PY'
import sys,pathlib,json,re,pandas as pd
out,model,src=sys.argv[1:];p=pathlib.Path(out);card=p/f'Datacard_{model}.txt';assert card.is_file() and card.stat().st_size>0
assert (p/'Dataframe'/f'Datacard_{model}.pkl').is_file()
m=json.loads(pathlib.Path(src,'manifest.json').read_text());text=card.read_text();indices=re.findall(r'^\s*pdfindex_\S+\s+discrete\s*$',text,re.M);assert len(indices)==len(m['categories']),'Unexpected background index count'
for line in text.splitlines():
 row=line.split()
 if row and row[0]=='shapes' and row[3]!='FAKE':assert pathlib.Path(row[3]).is_file(),row[3]
print('Card output checks passed:',card,'categories:',len(indices));print('Physics prescriptions (caps, missing PDF migrations, MC statistics) still require review.')
PY
