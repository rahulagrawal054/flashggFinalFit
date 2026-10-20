#!/usr/bin/env bash
# Incremental r_2D_fiducial workflow: snapshot and individual likelihood scans.
set -eo pipefail
usage() {
cat <<'HELP'
Usage: bash runner_r_2D_fiducial.sh --workspace FILE --outdir DIR --step snapshot|scan|plot|significance|limit|plot-limits|impacts [options]
Required:
  --workspace FILE          Input combined ROOT workspace (moved into output folder)
  --outdir DIR             Analysis folder, e.g. /absolute/path/DCB
  --step snapshot|scan|plot|significance|limit|plot-limits|impacts     Snapshot, individual scan, or two-POI scan plots
Options:
  --mass VALUE             Fixed MH (default 125.09)
  --set-parameters LIST     Snapshot injection / scan initial values
                           Snapshot default r_tHq=1,r_ttH=1; scans retain snapshot
                           values unless explicitly supplied; MH uses --mass
  --ranges LIST            name=min,max:name=min,max (default: workspace ranges)
  --strategy 0|1|2         Snapshot default 2; scan/significance default 0
  --tolerance VALUE        Snapshot default 0.1; scan/significance default 0.01
  --seed INTEGER           Positive random seed (default 123456)
  --dry-run                Print paths and exact command; no output files or fits
  --poi r_ttH|r_tHq        Required for scan or significance
  --scenario total|statOnly  Required for scan
  --scan-range LOW,HIGH    Required for scan; sets the scanned POI range
  --points INTEGER         Scan points (default 300)
  --other-poi profile|fixed  Other signal strength treatment (default profile)
  --other-value VALUE      Required when fixing the other signal strength
  --impact-stage initial|pilot|fit|retry  Staged impacts
  --nuisance NAME          Required for retry; also explicitly supply --strategy 1 or 2
  --scan-tag NAME          Optional separate name for repeat/refined scans
  --grid-start LIST        Optional starting values for grid fits only
                           e.g. r_ttH=2.9; does not freeze the parameter
  --help                   Show help

Snapshot moves the input to <outdir>/workspace.root; creates snapshot/ and audit/.
Existing snapshot directories are never overwritten. Use a new output folder
for a repeat. No observed-data fitting is performed. Scan defaults are strategy 0,
tolerance 0.01; snapshot defaults are strategy 2, tolerance 0.1. Scans require the
saved snapshot and exact saved Asimov. Plot makes custom and standard total/stat-only overlays for both POIs.
Significance requires --poi and --ranges; its target range must start at 0.
Limit also requires --poi and a nonnegative --ranges; computes expected 95% CLs.
Impacts: initial, pilot (five photons), fit (remaining nuisances, sequential).
Failed pilot/fit nuisances retry with strategies 1 then 2; attempts are archived.
Unresolved failures are recorded; other nuisances continue, with final exit 1.
www publication is not implemented yet.
HELP
}
workspace= outdir= step= mass=125.09
parameters='r_tHq=1,r_ttH=1'; ranges=; strategy=2; tolerance=0.1; seed=123456; dry_run=0
poi=; scenario=; scan_range=; points=300; other_mode=profile; other_value=; grid_start=; scan_tag=
impact_nuisance=; impact_stage=initial
strategy_given=0; tolerance_given=0; parameters_given=0
while (( $# )); do
 case "$1" in
 --help|-h) usage; exit 0;;
 --dry-run) dry_run=1; shift;;
 --workspace|--outdir|--step|--mass|--set-parameters|--ranges|--strategy|--tolerance|--seed|--poi|--scenario|--scan-range|--points|--other-poi|--other-value|--grid-start|--scan-tag|--impact-stage|--nuisance)
  (( $# >= 2 )) || { echo "Missing value for $1" >&2; exit 2; }
  case "$1" in
   --workspace) workspace="$2";; --outdir) outdir="$2";; --step) step="$2";;
   --mass) mass="$2";; --set-parameters) parameters="$2"; parameters_given=1;; --ranges) ranges="$2";;
   --strategy) strategy="$2"; strategy_given=1;; --tolerance) tolerance="$2"; tolerance_given=1;; --seed) seed="$2";;
   --poi) poi="$2";; --scenario) scenario="$2";; --scan-range) scan_range="$2";; --points) points="$2";;
   --other-poi) other_mode="$2";; --other-value) other_value="$2";; --grid-start) grid_start="$2";; --scan-tag) scan_tag="$2";; --impact-stage) impact_stage="$2";; --nuisance) impact_nuisance="$2";;
  esac; shift 2;;
 *) echo "Unknown option: $1" >&2; usage >&2; exit 2;;
 esac
done
[[ -n "$workspace" && -n "$outdir" && ( "$step" == snapshot || "$step" == scan || "$step" == plot || "$step" == significance || "$step" == limit || "$step" == plot-limits || "$step" == impacts ) ]] || { usage >&2; exit 2; }
[[ -z "$scan_tag" || "$scan_tag" =~ ^[A-Za-z0-9_-]+$ ]] || { echo 'Invalid scan tag' >&2; exit 2; }
[[ "$strategy" =~ ^[012]$ && "$seed" =~ ^[1-9][0-9]*$ ]] || { echo "Invalid strategy or seed" >&2; exit 2; }
python3 -B - "$mass" "$tolerance" "$parameters" "$ranges" <<'PY'
import sys,math,re
mass,tol,params,ranges=sys.argv[1:]
def number(s):
 v=float(s); assert math.isfinite(v), 'Nonfinite value'; return v
assert number(mass)>0 and number(tol)>0, 'Mass and tolerance must be positive'
names=set()
for token in params.split(','):
 n,v=token.split('='); assert re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*',n),n
 assert n not in names and n!='MH', 'Duplicate parameter or MH: use --mass'
 names.add(n); number(v)
assert {'r_ttH','r_tHq'}<=names, 'Set both injected signal strengths explicitly'
seen=set()
for token in ranges.split(':') if ranges else []:
 n,limits=token.split('='); lo,hi=map(number,limits.split(','))
 assert n in {'r_ttH','r_tHq'} and n not in seen and lo<hi, 'Invalid POI range'
 seen.add(n)
PY
if [[ "$step" == impacts && ( "$impact_stage" == pilot || "$impact_stage" == fit || "$impact_stage" == retry ) ]];then
 [[ "$other_mode" == profile && "$parameters_given" == 0 ]] || { echo 'Pilot retains initial impact settings and profiles both strengths' >&2;exit 2; }
 workspace="$(realpath -e -- "$workspace")";outdir="$(realpath -e -- "$outdir")"
 combine_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
 if (( ! dry_run ));then
  cd "$combine_dir";source /cvmfs/cms.cern.ch/cmsset_default.sh;eval "$(scram runtime -sh)";source ../setup.sh
  export PYTHONDONTWRITEBYTECODE=1
 fi
 python3 -B - "$workspace" "$outdir" "$mass" "$ranges" "$strategy_given" "$strategy" "$tolerance_given" "$tolerance" "$dry_run" "$combine_dir" "$impact_stage" "$impact_nuisance" <<'PYPILOT'
import sys,pathlib,json,hashlib,shlex,subprocess,math,re,datetime,shutil
ws,out,mass,ranges,sg,strategy,tg,tol,dry,tools,run_mode,retry_name=sys.argv[1:];out=pathlib.Path(out);stage=out/'impacts';dry=int(dry)
def require(ok,msg):
 if not ok:raise SystemExit(msg)
m=json.loads((stage/'manifest.json').read_text());sm=json.loads((out/'snapshot/manifest.json').read_text());snapshot=pathlib.Path(m['input_snapshot']);require(float(mass)==m['mass'],'Mass differs from initial impacts');require(pathlib.Path(ws).resolve()==(out/'workspace.root').resolve(),'Use this run workspace');require(hashlib.sha256(pathlib.Path(ws).read_bytes()).hexdigest()==sm['input_sha256'],'Workspace changed');require(hashlib.sha256(snapshot.read_bytes()).hexdigest()==m['input_sha256'],'Saved impact input changed')
require(not ranges or ranges==m['ranges'],'Keep initial impact ranges');require(run_mode=='retry' or not int(sg) or int(strategy)==m['strategy'],'Keep initial impact strategy');require(not int(tg) or float(tol)==m['tolerance'],'Keep initial impact tolerance')
validation=json.loads((stage/'validation/initial.json').read_text());require(validation['structurally_complete'],'Initial impacts incomplete');require(all(c['last_logged_status']=='0' for c in validation['checks']),'Review initial final statuses before pilot')
photon_names=(stage/'pilot.txt').read_text().splitlines();require(len(photon_names)==5 and set(photon_names)<=set(m['nuisances']),'Invalid photon list')
if run_mode=='retry':
 require(retry_name in m['nuisances'],'Specify --nuisance from this impact run');require(int(sg) and int(strategy) in [1,2],'Retry requires explicit --strategy 1 or 2')
 names=[retry_name]
else:names=m['nuisances'] if run_mode=='fit' else photon_names
known={}
if run_mode=='pilot' and (stage/'validation/pilot.json').exists():
 known.update({c['nuisance']:c for c in json.loads((stage/'validation/pilot.json').read_text())['checks']})
if run_mode in ['fit','retry']:
 pilot=json.loads((stage/'validation/pilot.json').read_text());require(pilot['structurally_complete'] and all(c['last_logged_status']=='0' for c in pilot['checks']),'Pilot must finish successfully before full fits');known.update({c['nuisance']:c for c in pilot['checks']})
 prior=stage/'validation/fit.json'
 if prior.exists():known.update({c['nuisance']:c for c in json.loads(prior.read_text())['checks']})
base=m['commands']['r_ttH'];common=[];i=0
while i<len(base):
 if base[i] in ['-P','-n']:i+=2;continue
 if base[i]=='--algo':common+=['--algo','impact'];i+=2;continue
 common.append(base[i]);i+=1
if run_mode=='retry':
 for flag in ['--cminDefaultMinimizerStrategy','--setRobustFitStrategy']:common[common.index(flag)+1]=strategy
commands={n:common+['-P',n,'-n','_paramFit_'+m['name']+'_'+n] for n in names}
def root_path(n):return stage/f"higgsCombine_paramFit_{m['name']}_{n}.MultiDimFit.mH{float(mass):g}.root"
def accepted(item):return item.get('structurally_complete',False) and item.get('exit_status')==0 and item.get('last_logged_status')=='0'
existing=[n for n in names if root_path(n).exists() and n in known and accepted(known[n])]
pending=[n for n in names if n not in existing]
for n in names:
 require(not root_path(n).exists() or n in known,'Existing unrecorded result: '+n+'; inspect before proceeding')
if run_mode=='retry':
 require(retry_name in known,'Retry needs a recorded failed result')
 old=known[retry_name];require(not (old['structurally_complete'] and old['last_logged_status']=='0' and old['exit_status']==0),'Result is already accepted; no retry needed')
 existing=[];pending=[retry_name]
print('Sequential impact stage:',run_mode,'selected:',len(names),'existing:',len(existing),'pending:',len(pending),flush=True)
for n in pending[:3]:print(n,shlex.join(commands[n]),flush=True)
if dry:print('Dry run only; no fits started. Remaining commands use the same settings, changing only nuisance name.');sys.exit(0)
import ROOT
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
for poi in ['r_ttH','r_tHq']:
 f=ROOT.TFile.Open(str(stage/f"higgsCombine_initialFit_{m['name']}_POI_{poi}.MultiDimFit.mH{float(mass):g}.root"));require(f and not f.IsZombie(),'Unreadable initial result');t=f.Get('limit');require(t and t.GetEntries()==3,'Initial result incomplete');f.Close()
def check(n,rc,log):
 path=root_path(n);item={'nuisance':n,'exit_status':rc,'file':str(path),'log':str(log),'structurally_complete':False};f=ROOT.TFile.Open(str(path)) if path.exists() else None
 if f and not f.IsZombie():
  t=f.Get('limit')
  if t and t.GetEntries()==3:
   values={x:[float(getattr(e,x)) for e in t] for x in [n,'r_ttH','r_tHq']};v=values[n];item.update(values=values,structurally_complete=all(math.isfinite(v) for row in values.values() for v in row) and v[1]<v[0]<v[2])
  f.Close()
 text=pathlib.Path(log).read_text();statuses=re.findall(r'Minimization finished with status=(-?\d+)',text);item.update(logged_status_counts={v:statuses.count(v) for v in set(statuses)},last_logged_status=statuses[-1] if statuses else None,boundary_warning_lines=[l for l in text.splitlines() if '[WARNING]' in l]);return item
def accepted(item):return item['structurally_complete'] and item['exit_status']==0 and item['last_logged_status']=='0'
lock=out/'.runner.lock';lock.mkdir(exist_ok=False)
try:
 stamp=datetime.datetime.now().strftime('%Y%m%d_%H%M%S');audit=stage/(run_mode+'_runs')/stamp;audit.mkdir(parents=True,exist_ok=False);shutil.copy2(pathlib.Path(tools)/'runner_r_2D_fiducial.sh',audit/'executed_runner.sh');(audit/'commands.json').write_text(json.dumps({n:commands[n] for n in pending},indent=2)+'\n');checks=[]
 def save():
  report={'checks':checks,'expected_nuisances':len(names),'completed_nuisances':len(checks),'structurally_complete':len(checks)==len(names) and all(accepted(x) for x in checks),'review_required':True,'execution':'sequential','failed_nuisances':[x['nuisance'] for x in checks if not accepted(x)],'accepted_nuisances':sum(accepted(x) for x in checks),'qualification':'Automatic strategy escalation preserves all attempts. Review internal statuses, boundaries and response stability; unresolved failures prohibit finalization.'}
  (stage/'validation'/(run_mode+'.json')).write_text(json.dumps(report,indent=2)+'\n');(audit/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
 for n in existing:
  c=check(n,known[n]['exit_status'],known[n]['log']);c['reused']=True;checks.append(c);save();require(accepted(c),'Existing result failed revalidation: '+n);print('Retaining:',n,flush=True)
 for n in pending:
  attempts=[]
  if n in known:
   previous=known[n];attempts=list(previous.get('attempts',[])) or [previous.copy()]
  def archive_current(label):
   path=root_path(n)
   if path.exists():
    dest=audit/n/label;dest.mkdir(parents=True,exist_ok=False)
    shutil.move(str(path),str(dest/path.name))
    if attempts:attempts[-1]['archived_file']=str(dest/path.name)
    (dest/'previous_validation.json').write_text(json.dumps(known.get(n,attempts[-1] if attempts else {}),indent=2)+'\n')
  archive_current('before_resume')
  first=int(strategy) if run_mode=='retry' else int(m['strategy'])
  if run_mode!='retry' and n in known and not accepted(known[n]):
   first=min(2,max(1,int(known[n].get('strategy',known[n].get('retry_strategy',0)))+1))
  for attempt_strategy in range(first,3):
   cmd=list(commands[n])
   for flag in ['--cminDefaultMinimizerStrategy','--setRobustFitStrategy']:cmd[cmd.index(flag)+1]=str(attempt_strategy)
   log=stage/'logs'/f'{run_mode}_{stamp}_{n}_strategy{attempt_strategy}.log'
   log.with_suffix('.command.json').write_text(json.dumps(cmd,indent=2)+'\n')
   print('Starting:',n,'strategy',attempt_strategy,'log',log,flush=True)
   with log.open('w') as h:rc=subprocess.run(cmd,cwd=str(stage),stdout=h,stderr=subprocess.STDOUT).returncode
   log.with_suffix('.exit').write_text(str(rc)+'\n');c=check(n,rc,log)
   c.update(reused=False,strategy=attempt_strategy);attempts.append(c.copy());c['attempts']=list(attempts)
   checks[:]=[x for x in checks if x['nuisance']!=n];checks.append(c);save()
   print('Finished:',n,'strategy',attempt_strategy,'accepted',accepted(c),'log',log,flush=True)
   if accepted(c):break
   if attempt_strategy<2:
    archive_current('failed_strategy'+str(attempt_strategy));c['attempts']=list(attempts);save()
  if not accepted(c):print('UNRESOLVED:',n,'continuing to next nuisance; finalization remains blocked',flush=True)

 save()
 if run_mode=='retry':
  prior=stage/'validation/fit.json';full=json.loads(prior.read_text());replacement=checks[0];replacement['retry_strategy']=replacement.get('strategy',int(strategy));replacement['retry_audit']=str(audit);full['checks']=[replacement if c['nuisance']==retry_name else c for c in full['checks']];full['completed_nuisances']=len(full['checks']);full['structurally_complete']=len(full['checks'])==full['expected_nuisances'] and all(accepted(c) for c in full['checks']);prior.write_text(json.dumps(full,indent=2)+'\n')
 print('Stage finished; review:',stage/'validation'/(run_mode+'.json'),flush=True)
 require(all(accepted(c) for c in checks),'Unresolved impact failures remain; see failed_nuisances in validation report')
finally:lock.rmdir()
PYPILOT
 exit $?
fi
if [[ "$step" == impacts ]];then
 [[ "$impact_stage" == initial ]] || { echo 'Only --impact-stage initial is implemented so far' >&2;exit 2; }
 [[ "$other_mode" == profile && "$parameters_given" == 0 ]] || { echo 'Impacts profile the other POI and retain snapshot starts' >&2;exit 2; }
 (( strategy_given )) || strategy=0
 (( tolerance_given )) || tolerance=0.01
 workspace="$(realpath -e -- "$workspace")";outdir="$(realpath -e -- "$outdir")"
 combine_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
 if (( ! dry_run ));then
  cd "$combine_dir";source /cvmfs/cms.cern.ch/cmsset_default.sh;eval "$(scram runtime -sh)";source ../setup.sh
  export PYTHONDONTWRITEBYTECODE=1
 fi
 python3 -B - "$workspace" "$outdir" "$mass" "$ranges" "$strategy" "$tolerance" "$dry_run" "$combine_dir" <<'PYIMPACT'
import sys,pathlib,json,hashlib,math,shlex,subprocess,shutil,re,datetime
ws,out,mass,ranges,strategy,tol,dry,tools=sys.argv[1:];out=pathlib.Path(out);dry=int(dry)
def require(ok,msg):
 if not ok:raise SystemExit(msg)
m=json.loads((out/'snapshot/manifest.json').read_text());require(float(mass)==float(m['mass']),'Mass must match snapshot');require(pathlib.Path(ws).resolve()==(out/'workspace.root').resolve(),'Use run folder workspace');require(hashlib.sha256(pathlib.Path(ws).read_bytes()).hexdigest()==m['input_sha256'],'Workspace changed')
snapshot=out/'snapshot'/f"higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH{float(mass):g}.{m['seed']}.root";require(snapshot.is_file(),'Missing saved snapshot');stage=out/'impacts';require(not stage.exists(),'Impact folder already exists; do not overwrite initial fits')
common=['combine','-M','MultiDimFit',str(snapshot),'--snapshotName','MultiDimFit','-m',mass,'-t','-1','--toysFile',str(snapshot),'--algo','singles','--redefineSignalPOIs','r_ttH,r_tHq','--floatOtherPOIs','1','--saveInactivePOI','1','--setParameters','MH='+mass,'--freezeParameters','MH','--robustFit','1','--cminDefaultMinimizerStrategy',strategy,'--cminDefaultMinimizerTolerance',tol,'--setRobustFitStrategy',strategy,'--setRobustFitTolerance',tol,'--stepSize','0.05','--setCrossingTolerance','0.00005','--X-rtd','MINIMIZER_freezeDisassociatedParams','--X-rtd','MINIMIZER_multiMin_hideConstants','--X-rtd','MINIMIZER_multiMin_maskConstraints','--X-rtd','MINIMIZER_multiMin_maskChannels=2','-v','3']
if ranges:common+=['--setParameterRanges',ranges]
commands={poi:common+['-P',poi,'-n','_initialFit_FiducialImpacts_POI_'+poi] for poi in ['r_ttH','r_tHq']}
print('Initial impact fits only. Exact saved SM Asimov; both POIs profiled in turn; MH fixed.');print('Output:',stage)
for cmd in commands.values():print(shlex.join(cmd),flush=True)
if dry:print('Dry run: no fits started or files written.');sys.exit(0)
import ROOT
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit');f=ROOT.TFile.Open(str(snapshot));require(f and not f.IsZombie(),'Unreadable snapshot');w=f.Get('w');require(w and w.getSnapshot('MultiDimFit'),'Missing snapshot');w.loadSnapshot('MultiDimFit');require(f.Get('toys/toy_asimov'),'Missing saved Asimov');require(all(not w.var(n).isConstant() for n in commands),'Saved POI frozen')
indices=sorted(c.GetName() for c in w.allCats() if c.GetName().startswith('pdfindex_'));names=sorted(x.GetName() for x in w.obj('ModelConfig').GetNuisanceParameters());require(all(not w.var(n).isConstant() for n in names),'Constrained nuisance frozen')
for cmd in commands.values():cmd+=['--saveSpecifiedIndex',','.join(indices)]
lock=out/'.runner.lock';lock.mkdir(exist_ok=False)
try:
 stage.mkdir(exist_ok=False);(stage/'logs').mkdir();(stage/'validation').mkdir();shutil.copy2(pathlib.Path(tools)/'runner_r_2D_fiducial.sh',stage/'executed_initial_runner.sh');(stage/'nuisances.txt').write_text('\n'.join(names)+'\n');(stage/'pilot.txt').write_text('\n'.join('CMS_hgg_nuisance_'+n for n in ['Smearing','ScaleEB','ScaleEE','Material','FNUF'])+'\n')
 metadata={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input_snapshot':str(snapshot),'input_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),'mass':float(mass),'ranges':ranges or 'inherited snapshot ranges','strategy':int(strategy),'tolerance':float(tol),'background_indices':indices,'nuisances':names,'name':'FiducialImpacts','status':'INITIAL_RUNNING','commands':commands};(stage/'manifest.json').write_text(json.dumps(metadata,indent=2)+'\n')
 checks=[]
 for poi,cmd in commands.items():
  (stage/f'initial_{poi}.command.sh').write_text(shlex.join(cmd)+'\n')
  with (stage/'logs'/f'initial_{poi}.log').open('w') as log:
   proc=subprocess.Popen(cmd,cwd=str(stage),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   for line in proc.stdout:print(line,end='',flush=True);log.write(line);log.flush()
   rc=proc.wait()
  (stage/'logs'/f'initial_{poi}.exit').write_text(str(rc)+'\n');require(rc==0,'Initial fit process failed: '+poi)
  result=stage/f'higgsCombine_initialFit_FiducialImpacts_POI_{poi}.MultiDimFit.mH{float(mass):g}.root';rf=ROOT.TFile.Open(str(result));require(rf and not rf.IsZombie(),'Missing/unreadable output');t=rf.Get('limit');require(t and t.GetEntries()==3,'Expected best-fit plus two endpoints');v=[float(getattr(e,poi)) for e in t];require(all(math.isfinite(x) for x in v) and v[1]<v[0]<v[2],'Invalid interval')
  text=(stage/'logs'/f'initial_{poi}.log').read_text();st=re.findall(r'Minimization finished with status=(-?\d+)',text);checks.append({'poi':poi,'best_fit':v[0],'lower':v[1],'upper':v[2],'logged_status_counts':{x:st.count(x) for x in set(st)},'last_logged_status':st[-1] if st else None,'review_required':True})
 (stage/'validation/initial.json').write_text(json.dumps({'structurally_complete':True,'checks':checks,'qualification':'Inspect endpoint fits, status histories and boundaries; structural success alone is not convergence validation.'},indent=2)+'\n');metadata['status']='INITIAL_FINISHED_REQUIRES_REVIEW';(stage/'manifest.json').write_text(json.dumps(metadata,indent=2)+'\n');print(json.dumps(checks,indent=2),flush=True)
finally:lock.rmdir()
PYIMPACT
 exit $?
fi
if [[ "$step" == plot-limits ]];then
 outdir="$(realpath -e -- "$outdir")";combine_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
 test -s "$outdir/limits/r_tHq/total/profile_other/results.json"
 if (( dry_run ));then echo "Plot tHq expected limit with +/-1sigma and +/-2sigma bands in $outdir/plots/limits; no fit or plot started.";exit 0;fi
 cd "$combine_dir";source /cvmfs/cms.cern.ch/cmsset_default.sh;eval "$(scram runtime -sh)"
 export PYTHONDONTWRITEBYTECODE=1
 mkdir -p "$outdir/plots/limits"
 cmd=(python3 -B "$combine_dir/../Plots/plot_fiducial_limits.py" --run-dir "$outdir")
 printf '%q ' "${cmd[@]}" > "$outdir/plots/limits/command.sh";printf '\n' >> "$outdir/plots/limits/command.sh"
 "${cmd[@]}" 2>&1 | tee "$outdir/plots/limits/plot.log"
 exit 0
fi
if [[ "$step" == significance || "$step" == limit ]]; then
 (( strategy_given )) || strategy=0
 (( tolerance_given )) || tolerance=0.01
 [[ "$poi" == r_ttH || "$poi" == r_tHq ]] || { echo 'Supply --poi r_ttH or r_tHq' >&2;exit 2; }
 [[ "$other_mode" == profile && -z "$other_value" ]] || { echo 'Significance currently supports the other POI profiled only' >&2;exit 2; }
 [[ -z "$scenario" || "$scenario" == total ]] || { echo 'Significance currently supports total uncertainties only' >&2;exit 2; }
 [[ -n "$ranges" && "$parameters_given" == 0 ]] || { echo 'Supply --ranges; significance retains snapshot starting values, so omit --set-parameters' >&2;exit 2; }
 workspace="$(realpath -e -- "$workspace")";outdir="$(realpath -e -- "$outdir")"
 combine_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
 snapshot="$(python3 -B - "$outdir" "$workspace" "$mass" "$poi" "$ranges" <<'PYSIGINPUT'
import pathlib,json,sys,hashlib
out,ws,mass,poi,ranges=sys.argv[1:];out=pathlib.Path(out);m=json.loads((out/'snapshot/manifest.json').read_text());assert float(mass)==float(m['mass']),'Mass must match snapshot';assert pathlib.Path(ws).resolve()==(out/'workspace.root').resolve();assert hashlib.sha256(pathlib.Path(ws).read_bytes()).hexdigest()==m['input_sha256'],'Workspace changed'
r={n:tuple(map(float,v.split(','))) for n,v in (x.split('=') for x in ranges.split(':'))};assert poi in r and r[poi][0]==0 and r[poi][1]>0,'Target range must start at 0'
p=out/'snapshot'/f"higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH{float(mass):g}.{m['seed']}.root";assert p.is_file();print(p)
PYSIGINPUT
)"
 other=r_tHq;[[ "$poi" != r_tHq ]] || other=r_ttH
 method=Significance;stage_root=significance;job_name=_Fiducial_Significance;stage_log=significance.log
 if [[ "$step" == limit ]];then method=AsymptoticLimits;stage_root=limits;job_name=_Fiducial_ExpectedLimit;stage_log=expectedLimit.log;fi
 stage_dir="$outdir/$stage_root/$poi/total/profile_other${scan_tag:+__$scan_tag}"
 [[ ! -e "$stage_dir" ]] || { echo "Output exists: $stage_dir" >&2;exit 2; }
 cmd=(combine -M "$method" "$snapshot" --snapshotName MultiDimFit -m "$mass" -t -1 --toysFile "$snapshot"
  --redefineSignalPOIs "$poi" --floatParameters "$other" --setParameters "MH=$mass" --freezeParameters MH
  --setParameterRanges "$ranges" --cminDefaultMinimizerStrategy "$strategy" --cminDefaultMinimizerTolerance "$tolerance"
  --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants
  --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
  --saveWorkspace --saveToys -v 3 -n "$job_name")
 [[ "$step" != limit ]] || cmd+=(--run expected --rule CLs --cl 0.95 --picky)
 if [[ "$step" == significance ]];then
  echo "Expected local significance on exact saved SM Asimov; null $poi=0; $other profiled"
 else
  echo "Expected 95% CLs limit: $poi; $other profiled. Saved SM Asimov used for conditional calibration; target-zero expected reference."
 fi
 echo "Output: $stage_dir";printf '%q ' "${cmd[@]}";printf '\n'
 if (( dry_run ));then echo 'Dry run only; no fit started.';exit 0;fi
 cd "$combine_dir";source /cvmfs/cms.cern.ch/cmsset_default.sh;eval "$(scram runtime -sh)";source ../setup.sh
 export PYTHONDONTWRITEBYTECODE=1
 python3 -B - "$snapshot" <<'PYSIGROOT'
import ROOT,sys
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit');f=ROOT.TFile.Open(sys.argv[1]);assert f and not f.IsZombie();w=f.Get('w');assert w and w.getSnapshot('MultiDimFit');w.loadSnapshot('MultiDimFit');assert f.Get('toys/toy_asimov');assert all(not w.var(n).isConstant() for n in ['r_ttH','r_tHq'])
PYSIGROOT
 mkdir "$outdir/.runner.lock"
 cleanup_sig() { rc=$?;trap - EXIT;if [[ -d "$stage_dir" ]];then printf '%s\n' "$rc" > "$stage_dir/exit_status.txt";fi;rmdir "$outdir/.runner.lock";exit "$rc"; }
 trap cleanup_sig EXIT
 mkdir -p "$(dirname "$stage_dir")";mkdir "$stage_dir"
 cp "$combine_dir/runner_r_2D_fiducial.sh" "$stage_dir/executed_runner.sh"
 printf '%q ' "${cmd[@]}" > "$stage_dir/command.sh";printf '\n' >> "$stage_dir/command.sh"
 sha256sum "$snapshot" > "$stage_dir/input_snapshot.sha256"
 cd "$stage_dir"
 "${cmd[@]}" 2>&1 | tee "$stage_dir/$stage_log"
 python3 -B - "$stage_dir" "$poi" "$other" "$step" "$stage_log" <<'PYSIGRESULT'
import sys,pathlib,json,math,re,ROOT
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit');stage,poi,other,mode,logname=sys.argv[1:];p=pathlib.Path(stage);files=list(p.glob('higgsCombine*.root'));assert len(files)==1
f=ROOT.TFile.Open(str(files[0]));assert f and not f.IsZombie();t=f.Get('limit');assert t
rows=[{'quantile':float(e.quantileExpected),'value':float(e.limit)} for e in t];assert all(math.isfinite(r['value']) and r['value']>=0 for r in rows)
s=(p/logname).read_text();v=re.findall(r'Minimization finished with status=(-?\d+)',s)
r={'poi':poi,'other_poi':other,'other_mode':'profiled','input_dataset':'exact saved SM-injected Asimov, not observed collision data','mode':mode,'rows':rows,'logged_status_counts':{x:v.count(x) for x in set(v)},'last_logged_status':v[-1] if v else None,'review_required':True,'qualification':'Review all status histories, boundaries and reference stability; successful exit alone is insufficient.'}
if mode=='significance':
 assert len(rows)==1;z=rows[0]['value'];r.update(expected_local_Z=z,q0=z*z,null=poi+'=0')
else:
 assert len(rows)==5 and all(abs(a['quantile']-b)<0.002 for a,b in zip(rows,[0.025,0.16,0.5,0.84,0.975])),'Missing/misordered expected limit bands'
 assert all(a['value']<=b['value'] for a,b in zip(rows,rows[1:]));r.update(expected_median_95CLs=rows[2]['value'],reference='target-zero auxiliary expected reference; other strength profiled; saved SM Asimov conditions the auxiliary fit',units='dimensionless signal strength, not cross section in fb',closure_warning_lines=[l for l in s.splitlines() if 'asimov' in l.lower() and any(x in l.lower() for x in ['warn','should','not','fail'])])
(p/'results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
PYSIGRESULT
 exit 0
fi
if [[ "$step" == plot ]]; then
 outdir="$(realpath -e -- "$outdir")"
 combine_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
 plot_mode=profile_other
 if [[ "$other_mode" == fixed ]]; then
  [[ -n "$other_value" ]] || { echo 'Fixed plotting requires --other-value' >&2; exit 2; }
  plot_mode="fixed_other_$(python3 -B -c 'import sys; print(str(float(sys.argv[1])).replace("-","minus").replace(".","p"))' "$other_value")"
 elif [[ "$other_mode" != profile ]]; then echo 'Invalid --other-poi' >&2; exit 2; fi
 [[ -z "$scan_tag" ]] || plot_mode+="__$scan_tag"
 for scan_poi in r_ttH r_tHq; do
  for scan_kind in total statOnly; do
   test -s "$outdir/scans/$scan_poi/$scan_kind/$plot_mode/points.csv"
  done
 done
 if (( dry_run )); then
  echo "Plot both POIs: total vs stat-only; mode=$plot_mode"
  echo "Input: $outdir/scans; output: $outdir/plots/scans/{custom,combine}"
  echo 'Dry run only: no plots written.'; exit 0
 fi
 cd "$combine_dir"
 source /cvmfs/cms.cern.ch/cmsset_default.sh
 eval "$(scram runtime -sh)"
 source ../setup.sh
 export PYTHONPATH="${CMSSW_BASE}/python:${PYTHONPATH:-}"
 export PYTHONDONTWRITEBYTECODE=1
 plot_base="$outdir/plots/scans"
 [[ -z "$scan_tag" ]] || plot_base+="/$scan_tag"
 if [[ "$other_mode" != profile ]]; then
  echo 'Custom fixed-mode plots currently require the standalone plotter; runner plotting supports profile_other only.' >&2; exit 2
 fi
 mkdir -p "$plot_base/combine" "$plot_base/custom"
 python3 -B "$combine_dir/../Plots/plot_fiducial_scans.py" --run-dir "$outdir" --other-mode "$plot_mode" --output-dir "$plot_base/custom" 2>&1 | tee "$plot_base/custom/plot.log"
 mass_label="$(python3 -B -c 'import json,sys; print(format(json.load(open(sys.argv[1]))["mass"],"g"))' "$outdir/snapshot/manifest.json")"
 python3 -B - "$plot_base/combine/labels.json" <<'PYLABELS'
import json,sys,pathlib
pathlib.Path(sys.argv[1]).write_text(json.dumps({'r_ttH':'#mu_{t#bar{t}H+tHW}','r_tHq':'#mu_{tHq}'},indent=2)+'\n')
PYLABELS
 cd "$plot_base/combine"
 for scan_poi in r_ttH r_tHq; do
  total_file="$outdir/scans/$scan_poi/total/$plot_mode/higgsCombine_Fiducial_Scan.MultiDimFit.mH${mass_label}.root"
  stat_file="$outdir/scans/$scan_poi/statOnly/$plot_mode/higgsCombine_Fiducial_Scan.MultiDimFit.mH${mass_label}.root"
  cmd=(python3 -B "$combine_dir/../Plots/plot1DScan_fiducial.py" "$total_file" --POI "$scan_poi" --main-label 'Total Uncert.' --others "$stat_file:Stat-Only:2" --breakdown Syst,Stat --stat-first --translate "$plot_base/combine/labels.json" --y-cut 20 --y-max 20 --logo-sub Internal -o "$scan_poi")
  printf '%q ' "${cmd[@]}" > "$scan_poi.command.sh"; printf '\n' >> "$scan_poi.command.sh"
  "${cmd[@]}" 2>&1 | tee "$scan_poi.log"
  test -s "$scan_poi.pdf"; test -s "$scan_poi.png"
 done
 echo "Plots saved under $plot_base"; exit 0
fi
if [[ "$step" == scan ]]; then
 (( strategy_given )) || strategy=0
 (( tolerance_given )) || tolerance=0.01
 [[ "$poi" == r_ttH || "$poi" == r_tHq ]] || { echo 'Scan requires --poi r_ttH or r_tHq' >&2; exit 2; }
 [[ "$scenario" == total || "$scenario" == statOnly ]] || { echo 'Scan requires --scenario total or statOnly' >&2; exit 2; }
 [[ -n "$scan_range" && "$points" =~ ^[1-9][0-9]*$ && "$points" -ge 2 ]] || { echo 'Supply --scan-range LOW,HIGH and at least 2 points' >&2; exit 2; }
 [[ "$other_mode" == profile || "$other_mode" == fixed ]] || { echo 'Invalid --other-poi' >&2; exit 2; }
 [[ "$other_mode" != fixed || -n "$other_value" ]] || { echo 'Fixed mode requires --other-value' >&2; exit 2; }
 [[ "$other_mode" != profile || -z "$other_value" ]] || { echo '--other-value is only for fixed mode' >&2; exit 2; }
 workspace="$(realpath -e -- "$workspace")"; outdir="$(realpath -e -- "$outdir")"
 combine_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
 if (( ! dry_run )); then
  cd "$combine_dir"
  source /cvmfs/cms.cern.ch/cmsset_default.sh
  eval "$(scram runtime -sh)"
  source ../setup.sh
  export PYTHONDONTWRITEBYTECODE=1
 fi
 python3 -B - "$workspace" "$outdir" "$mass" "$poi" "$scenario" "$scan_range" "$points" "$other_mode" "$other_value" "$ranges" "$strategy" "$tolerance" "$grid_start" "$dry_run" "$combine_dir" "$parameters_given" "$parameters" "$scan_tag" <<'PYSCAN'
import sys,pathlib,json,math,hashlib,subprocess,shlex,shutil,re,datetime,csv
(ws,out,mass,poi,scenario,span,points,other_mode,other_value,ranges,strategy,tol,grid_start,dry,tools,params_given,params,scan_tag)=sys.argv[1:]
out=pathlib.Path(out);points=int(points);dry=int(dry);other='r_tHq' if poi=='r_ttH' else 'r_ttH'
def require(ok,msg):
 if not ok:raise SystemExit(msg)
def number(s):
 v=float(s);require(math.isfinite(v),'Nonfinite number');return v
lo,hi=map(number,span.split(','));require(lo<hi,'Invalid scan range');require(number(tol)>0,'Invalid tolerance')
meta=json.loads((out/'snapshot/manifest.json').read_text());require(float(mass)==float(meta['mass']),'--mass must match saved snapshot')
require(pathlib.Path(ws).resolve()==(out/'workspace.root').resolve(),'Use this run folder’s workspace.root')
require(hashlib.sha256(pathlib.Path(ws).read_bytes()).hexdigest()==meta['input_sha256'],'Input workspace changed since snapshot')
snapshot=out/'snapshot'/f"higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH{float(mass):g}.{meta['seed']}.root"
require(snapshot.is_file(),'Missing saved snapshot: '+str(snapshot))
rr={}
for item in ranges.split(':') if ranges else []:
 n,v=item.split('=');require(n!=poi,'Use --scan-range, not --ranges, for scanned POI');rr[n]=v
rr[poi]=span
range_opt=':'.join(n+'='+v for n,v in rr.items())
starts={}
for item in params.split(',') if int(params_given) else []:
 n,v=item.split('=');starts[n]=v
starts['MH']=mass
if other_mode=='fixed':
 number(other_value);require(other not in starts or number(starts[other])==number(other_value),'Conflicting fixed value and --set-parameters');starts[other]=other_value
freeze=['MH']+(['allConstrainedNuisances'] if scenario=='statOnly' else [])+([other] if other_mode=='fixed' else [])
if grid_start:
 for item in grid_start.split(','):
  n,v=item.split('=');require(n in ['r_ttH','r_tHq'],'Grid seed must name a POI');number(v);require(not (n==other and other_mode=='fixed'),'Cannot seed a frozen POI')
mode_dir='profile_other' if other_mode=='profile' else 'fixed_other_'+str(number(other_value)).replace('-','minus').replace('.','p')
if scan_tag:mode_dir+='__'+scan_tag
stage=out/'scans'/poi/scenario/mode_dir;require(not stage.exists(),'Scan output exists; preserve it and choose a new run folder for repeats: '+str(stage))
cmd=['combine','-M','MultiDimFit',str(snapshot),'--snapshotName','MultiDimFit','-m',mass,'-t','-1','--toysFile',str(snapshot),'--algo','grid','--points',str(points),'--alignEdges','1','-P',poi,'--floatOtherPOIs','1','--saveInactivePOI','1','--setParameterRanges',range_opt,'--setParameters',','.join(n+'='+v for n,v in starts.items()),'--freezeParameters',','.join(freeze),'--cminDefaultMinimizerStrategy',strategy,'--cminDefaultMinimizerTolerance',tol,'--X-rtd','MINIMIZER_freezeDisassociatedParams','--X-rtd','MINIMIZER_multiMin_hideConstants','--X-rtd','MINIMIZER_multiMin_maskConstraints','--X-rtd','MINIMIZER_multiMin_maskChannels=2','--saveWorkspace','--saveSpecifiedNuis','all','-v','2','-n','_Fiducial_Scan']
if grid_start:cmd+=['--setParametersForGrid',grid_start]
# Names are read from snapshot metadata without ROOT for a true no-write dry run.
print('Saved Asimov/snapshot:',snapshot);print('Scan directory:',stage);print('Command:',shlex.join(cmd),flush=True)
print('Snapshot numerical/covariance warnings are retained; this command refits the likelihood reference.',flush=True)
if dry:print('Dry run: no files written or fits started.');sys.exit(0)
import ROOT
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
f=ROOT.TFile.Open(str(snapshot));require(f and not f.IsZombie(),'Unreadable snapshot');w=f.Get('w');require(w and w.getSnapshot('MultiDimFit'),'Missing snapshot');w.loadSnapshot('MultiDimFit');require(f.Get('toys/toy_asimov'),'Missing saved Asimov')
for n in ['r_ttH','r_tHq']:require(not w.var(n).isConstant(),'Snapshot POI is frozen: '+n)
for n,v in starts.items():
 var=w.var(n);require(bool(var),'Unknown starting parameter: '+n)
 if n=='MH':continue
 a,b=map(float,rr[n].split(',')) if n in rr else (var.getMin(),var.getMax())
 require(a<=number(v)<=b,'Starting value outside allowed range: '+n)
indices=sorted(x.GetName() for x in w.allCats() if x.GetName().startswith('pdfindex_'))
if indices:cmd+=['--saveSpecifiedIndex',','.join(indices)]
lock=out/'.runner.lock';lock.mkdir(exist_ok=False)
try:
 stage.mkdir(parents=True,exist_ok=False);shutil.copy2(pathlib.Path(tools)/'runner_r_2D_fiducial.sh',stage/'executed_runner.sh')
 (stage/'command.sh').write_text(shlex.join(cmd)+'\n')
 report={'stage':'scan','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'poi':poi,'scenario':scenario,'other_poi':other,'other_mode':other_mode,'other_value':other_value or None,'points':points,'scan_range':[lo,hi],'snapshot':str(snapshot),'snapshot_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),'command':cmd,'status':'RUNNING','snapshot_validation':json.loads((out/'snapshot/validation.json').read_text())}
 (stage/'manifest.json').write_text(json.dumps(report,indent=2)+'\n')
 with (stage/'scan.log').open('w') as log:
  process=subprocess.Popen(cmd,cwd=str(stage),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
  for line in process.stdout:print(line,end='',flush=True);log.write(line);log.flush()
  rc=process.wait()
 (stage/'exit_status.txt').write_text(str(rc)+'\n');require(rc==0,'Combine scan failed; inspect scan.log')
 result=stage/f'higgsCombine_Fiducial_Scan.MultiDimFit.mH{float(mass):g}.root';rf=ROOT.TFile.Open(str(result));require(rf and not rf.IsZombie(),'Missing scan ROOT file');tree=rf.Get('limit');require(bool(tree),'Missing limit tree')
 rows=[{'poi':float(getattr(e,poi)),'other_poi':float(getattr(e,other)),'deltaNLL':float(e.deltaNLL),'quantileExpected':float(e.quantileExpected)} for e in tree]
 bad=[i for i,x in enumerate(rows) if not all(math.isfinite(v) for v in x.values()) or x['deltaNLL']>=999 or x['deltaNLL'] < -0.001]
 with (stage/'points.csv').open('w') as h:
  writer=csv.DictWriter(h,fieldnames=['poi','other_poi','deltaNLL','quantileExpected']);writer.writeheader();writer.writerows(rows)
 log=(stage/'scan.log').read_text();statuses=re.findall(r'Minimization finished with status=(-?\d+)',log)
 validation={'root_entries':len(rows),'expected_entries':points+1,'entries_complete':len(rows)==points+1,'invalid_row_indices':bad,'logged_status_counts':{x:statuses.count(x) for x in set(statuses)},'last_logged_status':statuses[-1] if statuses else None,'review_required':True,'qualification':'Check point-level convergence, physical range, likelihood reference and interval coverage; count and process exit alone are insufficient.'}
 (stage/'validation.json').write_text(json.dumps(validation,indent=2)+'\n');report['status']='FINISHED_REQUIRES_REVIEW';(stage/'manifest.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(validation,indent=2))
 require(validation['entries_complete'] and not bad,'Scan has missing/invalid points; review before plotting or extracting intervals')
finally:lock.rmdir()
PYSCAN
 exit $?
fi
workspace="$(realpath -e -- "$workspace")"
[[ -s "$workspace" ]] || { echo "Input is empty" >&2; exit 2; }
outdir="$(realpath -m -- "$outdir")"
combine_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
input="$outdir/workspace.root"; stage_dir="$outdir/snapshot"
cmd=(combine -M MultiDimFit "$input" -m "$mass" -t -1 --algo none
 --setParameters "$parameters,MH=$mass" --freezeParameters MH
 -P r_tHq -P r_ttH --floatOtherPOIs 1
 --cminDefaultMinimizerStrategy "$strategy" --cminDefaultMinimizerTolerance "$tolerance"
 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants
 --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
 --saveWorkspace --saveFitResult --saveToys -s "$seed" -n _Fiducial_AsimovPostfit)
[[ -z "$ranges" ]] || cmd+=(--setParameterRanges "$ranges")
printf 'Source: %s\nMoved input: %s\nStage directory: %s\n' "$workspace" "$input" "$stage_dir"
printf 'Command: '; printf '%q ' "${cmd[@]}"; printf '\n'
if (( dry_run )); then echo 'Dry run only: no files written and no fit started.'; exit 0; fi
if [[ -e "$input" && "$workspace" != "$(realpath -e -- "$input")" ]]; then
 echo 'Destination workspace exists; supply it directly or choose a new output folder.' >&2; exit 2
fi
[[ ! -e "$stage_dir" ]] || { echo "Snapshot folder exists; use a new output folder for a repeat." >&2; exit 2; }
cd "$combine_dir"
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval "$(scram runtime -sh)"
source ../setup.sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="${CMSSW_BASE}/python:${PYTHONPATH:-}"
command -v combine >/dev/null
# Read-only input check, including free POIs and caller-supplied values/ranges.
python3 -B - "$workspace" "$parameters" "$ranges" <<'PY'
import sys,ROOT
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
p,params,ranges=sys.argv[1:];f=ROOT.TFile.Open(p);assert f and not f.IsZombie()
w=f.Get('w');assert w and w.obj('ModelConfig') and w.pdf('model_s') and w.data('data_obs')
assert {x.GetName() for x in w.obj('ModelConfig').GetParametersOfInterest()}=={'r_ttH','r_tHq'}
assert w.var('MH')
rr={}
for token in ranges.split(':') if ranges else []:
 n,v=token.split('=');rr[n]=tuple(map(float,v.split(',')))
for n in ['r_ttH','r_tHq']:assert not w.var(n).isConstant(), 'POI must float: '+n
for token in params.split(','):
 n,v=token.split('=');x=w.var(n);assert x, 'Unknown parameter: '+n
 lo,hi=rr.get(n,(x.getMin(),x.getMax()));assert lo<=float(v)<=hi, 'Initial value outside range: '+n
print('Input workspace checks passed; both POIs float and background parameters retain workspace settings.')
PY
mkdir -p "$outdir"
mkdir "$outdir/.runner.lock" || { echo "Another runner owns this output folder." >&2; exit 2; }
owns_stage=0
cleanup() { rc=$?; trap - EXIT; if (( owns_stage )); then printf '%s\n' "$rc" > "$stage_dir/exit_status.txt"; fi; rmdir "$outdir/.runner.lock"; exit "$rc"; }
trap cleanup EXIT
# Recheck after acquiring lock.
[[ ! -e "$stage_dir" ]] || { echo 'Snapshot already exists' >&2; exit 2; }
mkdir -p "$outdir/audit"
mkdir "$stage_dir"
owns_stage=1
if [[ -e "$input" ]]; then
 [[ "$workspace" == "$(realpath -e -- "$input")" ]] || { echo 'Destination workspace already exists; refusing replacement. Supply that workspace directly or use a new output folder.' >&2; exit 2; }
else
 # Record provenance before the source path is removed; verify bytes after move.
 sha256sum -- "$workspace" > "$outdir/audit/source_workspace.sha256"
 source_digest="$(sha256sum -- "$workspace")"; source_digest="${source_digest%% *}"
 mv -n -- "$workspace" "$input"
 [[ ! -e "$workspace" && -s "$input" ]] || { echo 'Workspace move did not complete' >&2; exit 2; }
 moved_digest="$(sha256sum -- "$input")"; moved_digest="${moved_digest%% *}"
 [[ "$source_digest" == "$moved_digest" ]] || { echo 'Workspace checksum changed' >&2; exit 2; }
fi
cp -- "$combine_dir/runner_r_2D_fiducial.sh" "$stage_dir/executed_runner.sh"
printf '%q ' "${cmd[@]}" > "$stage_dir/command.sh"; printf '\n' >> "$stage_dir/command.sh"
python3 -B - "$workspace" "$input" "$stage_dir" "$mass" "$parameters" "$ranges" "$strategy" "$tolerance" "$seed" "${cmd[@]}" <<'PY'
import sys,json,hashlib,pathlib,datetime
src,dst,stage,mass,params,ranges,strategy,tol,seed,*cmd=sys.argv[1:]
d={'stage':'snapshot','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_workspace':src,'workspace':dst,'input_handling':'moved into output folder (or already located there)','input_sha256':hashlib.sha256(pathlib.Path(dst).read_bytes()).hexdigest(),'mass':float(mass),'set_parameters':params,'ranges':ranges or 'inherited from workspace','strategy':int(strategy),'tolerance':float(tol),'seed':int(seed),'command':cmd,'other_poi':'profiled; both POIs float','data':'expected Asimov; generated and saved in this stage'}
pathlib.Path(stage,'manifest.json').write_text(json.dumps(d,indent=2)+'\n')
PY
cd "$stage_dir"
set +e
"${cmd[@]}" 2>&1 | tee "$stage_dir/fit.log"
pipeline_status=("${PIPESTATUS[@]}")
rc=${pipeline_status[0]}
(( pipeline_status[1] == 0 )) || rc=1
set -e
(( rc == 0 )) || { echo "Combine failed with exit $rc" >&2; exit "$rc"; }
python3 -B - "$stage_dir" "$mass" "$seed" <<'PY'
import sys,pathlib,json,math,ROOT
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
stage,mass,seed=sys.argv[1:];p=pathlib.Path(stage)
f=ROOT.TFile.Open(str(p/f'higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH{float(mass):g}.{seed}.root'))
assert f and not f.IsZombie(), 'Missing saved workspace file'
w=f.Get('w');assert w and w.getSnapshot('MultiDimFit');w.loadSnapshot('MultiDimFit')
d=f.Get('toys/toy_asimov');assert d, 'Missing saved Asimov dataset'
g=ROOT.TFile.Open(str(p/'multidimfit_Fiducial_AsimovPostfit.root'));assert g and not g.IsZombie()
r=g.Get('fit_mdf');assert r, 'Missing fit_mdf'
values={n:w.var(n).getVal() for n in ['r_ttH','r_tHq','MH']}
assert all(math.isfinite(v) for v in values.values())
assert abs(values['MH']-float(mass))<1e-7 and w.var('MH').isConstant()
report={'structurally_complete':True,'fit_status':int(r.status()),'covariance_quality':int(r.covQual()),'edm':float(r.edm()),'parameters':values,'asimov_entries':int(d.numEntries()),'asimov_sum_weights':float(d.sumEntries()),'saved_workspace':str(f.GetName()),'review_required':True,'qualification':'Numerical fit status, covariance, boundaries and closure require review before downstream stages; successful execution is not physics validation.'}
(p/'validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
PY
echo "Snapshot stage finished. Review $stage_dir/validation.json and fit.log before continuing."
