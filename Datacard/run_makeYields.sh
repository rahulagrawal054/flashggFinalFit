#!/usr/bin/env bash
# Extract yields only; never builds a datacard or starts a fit.
set -eo pipefail
base="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"; project="$(cd "$base/.." && pwd)"
model=; out=; category=all; signal=; background="$project/Background/outdir_tth_th_analysis"; wsbase="$project/Trees2WS/workspaces/fiducial"; dry=0
usage() { cat <<'HELP'
Usage: bash run_makeYields.sh --model DCB|SoG --outdir NEW_DIR [options]
 --category NAME|all   Default all categories found in signal packages
 --signal-dir DIR     Default ../Signal/packaged_all_years_20261014/MODEL
 --background-dir DIR Default ../Background/outdir_tth_th_analysis
 --ws-base DIR        Default ../Trees2WS/workspaces/fiducial
 --dry-run            Print commands; no files written or calculations started
Outputs: yields_MODEL/CATEGORY.pkl, logs/, commands.sh, manifest.json, exit_status.txt.
Uses four eras, input mass 125, accEff, mergeYears, doSystematics, skipCOWCorr.
Calculates categories sequentially. Existing output folders are never overwritten.
HELP
}
while (( $# )); do
 case "$1" in
 --help|-h) usage;exit 0;; --dry-run) dry=1;shift;;
 --model|--outdir|--category|--signal-dir|--background-dir|--ws-base)
  (( $#>=2 )) || { echo "Missing value: $1" >&2;exit 2; }
  case "$1" in --model) model="$2";;--outdir) out="$2";;--category) category="$2";;--signal-dir) signal="$2";;--background-dir) background="$2";;--ws-base) wsbase="$2";;esac;shift 2;;
 *) echo "Unknown option: $1" >&2;exit 2;; esac
done
[[ "$model" == DCB || "$model" == SoG ]] && [[ -n "$out" ]] || { usage >&2;exit 2; }
signal="${signal:-$project/Signal/packaged_all_years_20261014/$model}"
signal="$(realpath -e "$signal")";background="$(realpath -e "$background")";wsbase="$(realpath -e "$wsbase")";out="$(realpath -m "$out")"
[[ ! -e "$out" ]] || { echo "Output already exists: $out" >&2;exit 2; }
map=;for era in 2022preEE 2022postEE 2023preBPix 2023postBPix;do
 [[ -d "$wsbase/$era/ws_signal" ]] || { echo "Missing input workspace folder for $era" >&2;exit 2; }
 map+="${map:+,}$era=$wsbase/$era/ws_signal"
done
shopt -s nullglob
files=("$signal"/CMS-HGG_sigfit_packaged_"$model"_*.root)
(( ${#files[@]} )) || { echo 'No signal packages found' >&2;exit 2; }
cats=();for file in "${files[@]}";do
 c="${file##*/}";c="${c#CMS-HGG_sigfit_packaged_${model}_}";c="${c%.root}"
 if [[ "$category" == all || "$category" == "$c" ]];then
  [[ -s "$background/CMS-HGG_multipdf_${c}.root" ]] || { echo "Missing background for $c" >&2;exit 2; };cats+=("$c")
 fi
done
(( ${#cats[@]} )) || { echo "Category not found: $category" >&2;exit 2; }
if (( ! dry ));then
 cd "$base";source /cvmfs/cms.cern.ch/cmsset_default.sh;eval "$(scram runtime -sh)";source "$project/setup.sh"
 export PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 export PYTHONPATH="$base:$project/commonTools:${PYTHONPATH:-}"
 mkdir -p "$(dirname "$out")";mkdir "$out";mkdir "$out/logs"
 cp "$base/run_makeYields.sh" "$out/executed_runner.sh"
 trap 'rc=$?; printf "%s\n" "$rc" > "$out/exit_status.txt"' EXIT
 python3 -B - "$out" "$model" "$signal" "$background" "$map" "${cats[@]}" <<'PY'
import sys,json,pathlib,hashlib
out,model,signal,background,wsmap,*cats=sys.argv[1:];base=pathlib.Path.cwd()
names=['makeYields.py','systematics.py'];hashes={n:hashlib.sha256((base/n).read_bytes()).hexdigest() for n in names}
pathlib.Path(out,'manifest.json').write_text(json.dumps(dict(model=model,signal_dir=signal,background_dir=background,input_ws_map=wsmap,categories=cats,input_mass=125,weight_scheme='accEff',skipCOWCorr=True,source_sha256=hashes),indent=2)+'\n')
PY
fi
for c in "${cats[@]}";do
 cmd=(python3 -B -u "$base/makeYields.py" --inputWSDirMap "$map" --cat "$c" --procs auto --ext "$model" --outputYieldsDir "$out" --mass 125 --mergeYears --doSystematics --skipCOWCorr --systWeightScheme accEff --sigModelWSDir "$signal" --sigModelExt "packaged_$model" --bkgModelWSDir "$background" --bkgModelExt multipdf)
 printf '%q ' "${cmd[@]}";printf '\n'
 if (( ! dry ));then
  printf '%q ' "${cmd[@]}" >> "$out/commands.sh";printf '\n' >> "$out/commands.sh"
  "${cmd[@]}" 2>&1 | tee "$out/logs/${c}.log"
  if rg -n '\[ERROR\]|\*\*\* ERROR|Traceback \(most recent call last\)' "$out/logs/${c}.log";then exit 1;fi
  python3 -B - "$out/yields_$model/$c.pkl" "$c" <<'PY'
import sys,pathlib,pandas as pd,numpy as np
p,c=sys.argv[1:];d=pd.read_pickle(p);s=d[d.type=='sig'];assert len(s)>0 and set(s.cat)=={c}
assert set(s.year)=={'2022preEE','2022postEE','2023preBPix','2023postBPix'}
cols=[n for n in s if n.endswith('_yield')]+['sumw2','numEvents'];a=s[cols].apply(pd.to_numeric,errors='raise');assert np.isfinite(a.to_numpy()).all()
assert (a.sumw2>=0).all() and (a.numEvents>=0).all();assert (a.numEvents%1==0).all()
assert all(pathlib.Path(f).is_file() for f in d.modelWSFile)
print('Validated:',p,'signal rows:',len(s),'negative nominal rows:',int((s.nominal_yield<0).sum()))
PY
 fi
done
if (( dry ));then echo 'Dry run only.';else echo "Yield run complete: $out";fi
