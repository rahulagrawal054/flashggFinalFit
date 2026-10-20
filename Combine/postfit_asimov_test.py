#!/usr/bin/env python3
"""Isolated postfit-conditioned Asimov comparison; no observed-data fit."""
import argparse, csv, hashlib, json, math, os, pathlib, shlex, shutil, subprocess, sys
BASE=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--model',choices=['DCB','SoG'],required=True)
p.add_argument('--points',type=int,default=300)
p.add_argument('--tth-range',default='0,2.5')
p.add_argument('--thq-range',default='-8,15')
p.add_argument('--strategy',type=int,choices=[0,1,2],default=0)
p.add_argument('--tolerance',type=float,default=.01)
p.add_argument('--outdir',type=pathlib.Path)
p.add_argument('--run',action='store_true',help='Execute; default is a no-write dry run')
a=p.parse_args()
if a.points<2 or not math.isfinite(a.tolerance) or a.tolerance<=0:p.error('Invalid points/tolerance')
spans={ 'r_ttH':a.tth_range,'r_tHq':a.thq_range }
for key,span in spans.items():
 try: lo,hi=map(float,span.split(',')); assert math.isfinite(lo) and math.isfinite(hi) and lo<1<hi
 except Exception:p.error(key+' range must be finite, increasing and contain generation truth 1')
model=BASE/a.model
meta=json.loads((model/'snapshot/manifest.json').read_text())
mass=str(meta['mass']); mass=f'{float(mass):g}'
snapshot=model/'snapshot'/f'higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH{mass}.{meta["seed"]}.root'
if not snapshot.is_file():p.error('Missing snapshot: '+str(snapshot))
out=(a.outdir or model/'postfit_asimov_test').resolve()
if out==model or model in out.parents and out in [model/'snapshot',model/'scans']:p.error('Protected output directory')
seed='123456'
common=['-m',mass,'-t','-1','--setParameters',f'r_ttH=1,r_tHq=1,MH={mass}','--freezeParameters','MH']
input_args=['-d',str(snapshot),'--snapshotName','MultiDimFit']
rtd=sum((['--X-rtd',s] for s in ['MINIMIZER_freezeDisassociatedParams','MINIMIZER_multiMin_hideConstants','MINIMIZER_multiMin_maskConstraints','MINIMIZER_multiMin_maskChannels=2']),[])
toy=out/'generation'/f'higgsCombine_PostfitAsimov.GenerateOnly.mH{mass}.{seed}.root'
generate=['combine','-M','GenerateOnly']+input_args+common+['--saveToys','-s',seed,'-n','_PostfitAsimov']
stages=[('generation',generate,toy)]
for poi in ['r_ttH','r_tHq']:
 other='r_tHq' if poi=='r_ttH' else 'r_ttH'
 for scenario in ['total','statOnly']:
  cmd=['combine','-M','MultiDimFit']+input_args+common+['--toysFile',str(toy),'--algo','grid','--points',str(a.points),'--alignEdges','1','-P',poi,'--floatOtherPOIs','1','--saveInactivePOI','1','--setParameterRanges',f'{poi}={spans[poi]}:'+other+('=-25,25' if other=='r_tHq' else '=-1,3'),'--cminDefaultMinimizerStrategy',str(a.strategy),'--cminDefaultMinimizerTolerance',str(a.tolerance)]+rtd+['--saveWorkspace','--saveFitResult','-v','2','-n','_PostfitScan']
  if scenario=='statOnly':cmd[cmd.index('--freezeParameters')+1]='MH,allConstrainedNuisances'
  if poi=='r_tHq':cmd+=['--setParametersForGrid','r_ttH=2.9']
  name=f'scans/{poi}/{scenario}'
  stages.append((name,cmd,out/name/f'higgsCombine_PostfitScan.MultiDimFit.mH{mass}.root'))
print('Model:',a.model,'\nSource snapshot:',snapshot,'\nNew output:',out,flush=True)
print('Generation: postfit nuisance/background settings, strengths reset to 1.\nAll four scans reuse the NEW dataset. Stat-only freezes constrained nuisances at the SOURCE snapshot values.',flush=True)
for name,cmd,_ in stages:print('\n'+name+'\n'+shlex.join(cmd),flush=True)
if not a.run:print('\nDRY RUN: no files written; add --run to execute.');sys.exit(0)
if not shutil.which('combine'):p.error('combine unavailable: run cmsenv and source ../setup.sh')
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
def require(ok,msg):
 if not ok:raise RuntimeError(msg)
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def data_info(path):
 f=ROOT.TFile.Open(str(path)); require(f and not f.IsZombie(),'Unreadable '+str(path))
 d=f.Get('toys/toy_asimov'); require(bool(d),'Missing toys/toy_asimov in '+str(path))
 h=hashlib.sha256()
 for i in range(d.numEntries()):
  row=d.get(i)
  values=sorted((v.GetName(),int(v.getIndex()) if v.InheritsFrom('RooAbsCategory') else float(v.getVal())) for v in row)
  h.update(json.dumps([values,float(d.weight())],separators=(',',':')).encode())
 info={'entries':d.numEntries(),'sum_weights':d.sumEntries(),'data_sha256':h.hexdigest()}; f.Close();return info
f=ROOT.TFile.Open(str(snapshot));require(f and not f.IsZombie(),'Unreadable source snapshot')
w=f.Get('w');require(w and w.getSnapshot('MultiDimFit'),'Missing MultiDimFit snapshot');w.loadSnapshot('MultiDimFit')
indices=sorted(v.GetName() for v in w.allCats() if v.GetName().startswith('pdfindex_'))
for n in ['r_ttH','r_tHq']:require(w.var(n) and not w.var(n).isConstant(),'Frozen/missing POI '+n)
for n in ['r_ttH','r_tHq']:require(w.var(n).getMin()<=1<=w.var(n).getMax(),'Generation 1 outside workspace range')
f.Close()
# Refuse reuse: separate output folders prevent mixing datasets or partial scans.
out.mkdir(parents=True,exist_ok=False)
record={'model':a.model,'mass':mass,'points':a.points,'ranges':spans,'source_snapshot':str(snapshot),'source_sha256':digest(snapshot),'original_dataset':data_info(snapshot),'statOnly_freeze_anchor':'source MultiDimFit snapshot','other_POI':'profiled','stages':{}}
manifest=out/'manifest.json'
def save():manifest.write_text(json.dumps(record,indent=2)+'\n')
save()
try:
 for name,cmd,result in stages:
  folder=out/name;folder.mkdir(parents=True)
  if name!='generation' and indices:cmd+=['--saveSpecifiedIndex',','.join(indices)]
  (folder/'command.sh').write_text('#!/usr/bin/env bash\nset -euo pipefail\ncd '+shlex.quote(str(folder))+'\n'+shlex.join(cmd)+'\n')
  print('\nRUNNING '+name,flush=True)
  with (folder/'run.log').open('w') as log:
   proc=subprocess.Popen(cmd,cwd=folder,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
   try:
    for line in proc.stdout:print(line,end='',flush=True);log.write(line);log.flush()
    rc=proc.wait()
   except BaseException:
    proc.terminate();proc.wait();raise
  record['stages'][name]={'exit_code':rc,'result':str(result)};save()
  require(rc==0 and result.is_file(),'Failed/incomplete '+name+'; outputs preserved')
  if name=='generation':
   record['new_dataset']=data_info(toy);save()
  else:
   rf=ROOT.TFile.Open(str(result));require(rf and not rf.IsZombie(),'Unreadable scan result');tree=rf.Get('limit');require(bool(tree),'Missing limit tree')
   poi=name.split('/')[1];rows=[]
   for entry in tree:rows.append({poi:float(getattr(entry,poi)),'deltaNLL':float(entry.deltaNLL),'quantileExpected':float(entry.quantileExpected)})
   rf.Close()
   with (folder/'points.csv').open('w',newline='') as h:
    writer=csv.DictWriter(h,fieldnames=[poi,'deltaNLL','quantileExpected']);writer.writeheader();writer.writerows(rows)
   bad=[r for r in rows if not math.isfinite(r['deltaNLL']) or r['deltaNLL']>=999 or r['deltaNLL']<-.001]
   valid=len(rows)==a.points+1 and not bad
   record['stages'][name].update(entries=len(rows),invalid_points=len(bad),structurally_valid=valid);save()
   require(valid,'Invalid/incomplete scan '+name+'; inspect run.log and points.csv')
 record['complete']=True;save()
 print('\nDONE: four scans complete. Results and commands: '+str(out),flush=True)
except BaseException as error:
 record['error']=str(error);save();raise
