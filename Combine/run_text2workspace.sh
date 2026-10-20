#!/usr/bin/env bash
# Prepare a self-contained run folder and build its combined workspace.
set -eo pipefail
usage() {
cat <<'HELP'
Usage: bash run_text2workspace.sh --datacard FILE --models DIR --outdir DIR [options]
  --datacard FILE    Current datacard; moved into the output folder
  --models DIR      Current model folder beside the datacard; moved with it
  --outdir DIR      New run folder, e.g. DCB, SoG or CombineFit
  --mass VALUE      Workspace mass (default 125.09)
  --mode NAME       Entry in models.py (default r_2D_fiducial)
  --dry-run         Validate and print plan; do not move files or run Combine
  --help            Show help
Run from an active CMSSW environment, or allow this script to initialize it.
Output: workspace.root, text2workspace.log, t2w_jobs/, audit/ and moved inputs.
Relative shape paths must stay inside the supplied model folder. Absolute or
parent-relative shape paths are rejected; the datacard is never rewritten.
No snapshot, scans or other fits are launched.
HELP
}
card=; modeldir=; outdir=; mass=125.09; mode=r_2D_fiducial; dry=0
while (( $# )); do
 case "$1" in
 --help|-h) usage; exit 0;;
 --dry-run) dry=1;shift;;
 --datacard|--models|--outdir|--mass|--mode)
  (( $# >= 2 )) || { echo "Missing value for $1" >&2;exit 2; }
  case "$1" in --datacard) card="$2";;--models) modeldir="$2";;--outdir) outdir="$2";;--mass) mass="$2";;--mode) mode="$2";;esac
  shift 2;;
 *) echo "Unknown option: $1" >&2;usage >&2;exit 2;;
 esac
done
[[ -n "$card" && -n "$modeldir" && -n "$outdir" ]] || { usage >&2;exit 2; }
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# Missing inputs fail before creating folders or initializing CMSSW.
[[ -s "$card" ]] || { echo "Missing or empty datacard: $card" >&2;exit 2; }
[[ -d "$modeldir" ]] || { echo "Missing model folder: $modeldir" >&2;exit 2; }
card="$(realpath -e -- "$card")"; modeldir="$(realpath -e -- "$modeldir")"; outdir="$(realpath -m -- "$outdir")"
if (( ! dry )); then
 cd "$script_dir"
 source /cvmfs/cms.cern.ch/cmsset_default.sh
 eval "$(scram runtime -sh)"
 source ../setup.sh
 export PYTHONDONTWRITEBYTECODE=1
fi
python3 -B - "$card" "$modeldir" "$outdir" "$mass" "$mode" "$dry" "$script_dir" <<'PY'
import sys,pathlib,shutil,runpy,shlex,json,hashlib,datetime,math,os
card,modelsdir,outdir,mass,mode,dry,scriptdir=sys.argv[1:]
card,modelsdir,outdir,scriptdir=map(pathlib.Path,[card,modelsdir,outdir,scriptdir]);dry=int(dry)
def require(ok,msg):
 if not ok:raise SystemExit(msg)
require(not outdir.exists(),f'Output folder already exists: {outdir}; refusing overwrite')
require(math.isfinite(float(mass)) and float(mass)>0,'Invalid mass')
require(modelsdir.parent==card.parent,'Datacard and model folder must be beside each other')
require(modelsdir.name!=card.name,'Conflicting input names')
require(modelsdir not in outdir.parents and outdir!=modelsdir,'Output folder cannot be inside model inputs')
require(card.name not in {'workspace.root','text2workspace.log','audit','t2w_jobs'},'Reserved datacard filename')
require(modelsdir.name not in {'audit','t2w_jobs','snapshot','scans','plots','limits','impacts','significance'},'Reserved model folder name')
model_options=runpy.run_path(str(scriptdir/'models.py'))['models'];require(mode in model_options,'Unknown model: '+mode)
paths=set()
for line in card.read_text().splitlines():
 parts=line.split()
 if not parts or parts[0]!='shapes':continue
 require(len(parts)>=4,'Malformed shapes line')
 name=parts[3]
 if name=='FAKE':continue
 rel=pathlib.Path(name)
 require(not rel.is_absolute() and '..' not in rel.parts and rel.parts[0]==modelsdir.name,'Shape path must be relative inside '+modelsdir.name+': '+name)
 f=card.parent/rel
 require(f.is_file(),'Missing shape file: '+str(f))
 require(f.resolve().is_relative_to(modelsdir),'Shape file points outside supplied model folder: '+name)
 paths.add(rel)
require(paths,'No model files referenced by datacard')
# Reject external symlinks: moving this directory must preserve its inputs.
for f in modelsdir.rglob('*'):
 if f.is_symlink():require(f.resolve().is_relative_to(modelsdir),'External symlink in models: '+str(f))
binary=shutil.which('text2workspace.py') or 'text2workspace.py'
cmd=[binary,str(outdir/card.name),'-o',str(outdir/'workspace.root'),'-m',mass]+shlex.split(model_options[mode])
print('Move datacard:',card,'->',outdir/card.name)
print('Move models:  ',modelsdir,'->',outdir/modelsdir.name)
print('Verified referenced model files:',len(paths))
print('Build command:',shlex.join(cmd),flush=True)
if dry:print('Dry run only; no files moved or written.');sys.exit(0)
require(shutil.which('text2workspace.py') is not None,'text2workspace.py unavailable after CMSSW setup')
# Audit all bytes before moving either input.
files=[card]+sorted(f for f in modelsdir.rglob('*') if f.is_file())
records=[{'source':str(f),'destination':str(outdir/f.relative_to(card.parent)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files]
outdir.mkdir(parents=True,exist_ok=False);audit=outdir/'audit';audit.mkdir();jobs=outdir/'t2w_jobs';jobs.mkdir()
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':mode,'mass':float(mass),'command':cmd,'input_files':records,'status':'PREPARED_FOR_MOVE'}
def save(): (audit/'build_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
save();shutil.copy2(scriptdir/'run_text2workspace.sh',audit/'executed_build_runner.sh');shutil.copy2(scriptdir/'models.py',audit/'models_at_build.py')
shutil.move(str(card),str(outdir/card.name));shutil.move(str(modelsdir),str(outdir/modelsdir.name))
for r in records:require(hashlib.sha256(pathlib.Path(r['destination']).read_bytes()).hexdigest()==r['sha256'],'Checksum mismatch: '+r['destination'])
manifest['status']='INPUTS_MOVED_AND_VERIFIED';save()
job=jobs/'build_workspace.sh'
job.write_text('#!/usr/bin/env bash\nset -eo pipefail\ncd -- '+shlex.quote(str(outdir))+'\n[[ ! -e workspace.root ]] || { echo "workspace.root already exists; refusing overwrite" >&2; exit 2; }\n'+shlex.join(cmd)+'\n')
job.chmod(0o755)
PY
if (( dry )); then exit 0; fi
cd "$outdir"
set +e
bash "$outdir/t2w_jobs/build_workspace.sh" 2>&1 | tee "$outdir/text2workspace.log"
results=("${PIPESTATUS[@]}")
set -e
rc=${results[0]}; (( results[1] == 0 )) || rc=1
printf '%s\n' "$rc" > "$outdir/audit/build_exit_status.txt"
(( rc == 0 )) || { echo "Workspace build failed; inputs and log retained in $outdir" >&2;exit "$rc"; }
python3 -B - "$outdir" <<'PY'
import sys,pathlib,json,ROOT
p=pathlib.Path(sys.argv[1]);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit');f=ROOT.TFile.Open(str(p/'workspace.root'));assert f and not f.IsZombie(),'Missing/unreadable workspace'
w=f.Get('w');assert w and w.obj('ModelConfig') and w.pdf('model_s') and w.data('data_obs'),'Missing workspace objects'
m=json.loads((p/'audit/build_manifest.json').read_text());m['status']='WORKSPACE_BUILT_STRUCTURAL_CHECK_PASSED';m['pois']=[x.GetName() for x in w.obj('ModelConfig').GetParametersOfInterest()];m['nuisance_count']=w.obj('ModelConfig').GetNuisanceParameters().getSize();(p/'audit/build_manifest.json').write_text(json.dumps(m,indent=2)+'\n');print('Workspace built:',p/'workspace.root');print('POIs:',m['pois'],'Nuisances:',m['nuisance_count']);print('No fitting stages have been started.')
PY
