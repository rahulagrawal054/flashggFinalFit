#!/usr/bin/env python3
"""Sequential saved-Asimov closure checks; preserve original production outputs."""
import json, shlex, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
import ROOT
ROOT.gROOT.SetBatch(True)
base=Path(__file__).resolve().parent/'DCB'
source=base/'snapshot/higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH125.09.123456.root'
out=base/'checks'/('validated_closure_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
if len(sys.argv)==3 and sys.argv[1]=='--resume-tolerance':out=Path(sys.argv[2]).resolve()
out.mkdir(exist_ok=True)
indices=json.loads((base/'checks/asimov_closure_20261016_150317/background_indices.json').read_text())['generation_input_indices']
common=['-m','125.09','-P','r_ttH','-P','r_tHq','--floatOtherPOIs','1','--freezeParameters','MH','--X-rtd','MINIMIZER_freezeDisassociatedParams','--X-rtd','MINIMIZER_multiMin_hideConstants','--X-rtd','MINIMIZER_multiMin_maskConstraints','--X-rtd','MINIMIZER_multiMin_maskChannels=2','--saveWorkspace','--saveFitResult','--saveSpecifiedIndex',','.join(indices),'-v','2']
results=json.loads((out/'results.json').read_text()) if (out/'results.json').exists() else {}
def execute(name,cmd):
 d=out/name; d.mkdir()
 (d/'command.sh').write_text('#!/bin/bash\n'+shlex.join(cmd)+'\n')
 print('RUN',name,flush=True)
 with (d/'fit.log').open('w') as log:
  rc=subprocess.call(cmd,cwd=d,stdout=log,stderr=subprocess.STDOUT)
 (d/'exit_status.txt').write_text(str(rc)+'\n')
 if rc:raise RuntimeError(f'{name} exit {rc}; inspect {d}')
 return d
def inspect(d):
 f=ROOT.TFile.Open(str(d/'multidimfit_Check.root'))
 if not f or f.IsZombie():raise RuntimeError('Missing fit result '+str(d))
 r=f.Get('fit_mdf')
 if not r:raise RuntimeError('Missing fit_mdf '+str(d))
 vals={v.GetName():v.getVal() for v in r.floatParsFinal()}
 answer=dict(status=int(r.status()),edm=float(r.edm()),covQual=int(r.covQual()),minNll=float(r.minNll()),poi={p:vals.get(p) for p in ['r_ttH','r_tHq']})
 f.Close()
 wf=next(d.glob('higgsCombine_Check.MultiDimFit*.root'))
 f=ROOT.TFile.Open(str(wf)); w=f.Get('w'); w.loadSnapshot('MultiDimFit')
 answer['indices']={n:int(w.cat(n).getIndex()) for n in indices}
 f.Close();answer['workspace']=str(wf)
 (d/'validation.json').write_text(json.dumps(answer,indent=2)+'\n')
 print(d.name,answer,flush=True)
 results[d.name]=answer;(out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
 return answer
def fit(name,workspace,toys,start,strategy=0,tolerance=.01,fixed=False):
 cmd=['combine','-M','MultiDimFit',str(workspace),'--snapshotName','MultiDimFit','-t','-1','--toysFile',str(toys),'--algo','none']+common+['--cminDefaultMinimizerStrategy',str(strategy),'--cminDefaultMinimizerTolerance',str(tolerance),'--setParameters',','.join(f'{k}={v}' for k,v in dict(MH=125.09,**start).items()),'-n','_Check']
 if fixed:
  ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
  ff=ROOT.TFile.Open(str(workspace));ww=ff.Get('w');ww.loadSnapshot('MultiDimFit')
  for k,v in indices.items():ww.cat(k).setIndex(v)
  active=set();allbg=set()
  for pdf in ww.allPdfs():
   if pdf.InheritsFrom('RooMultiPdf'):
    allbg.update(v.GetName() for v in pdf.getVariables() if v.InheritsFrom('RooRealVar'))
    active.update(v.GetName() for v in pdf.getCurrentPdf().getVariables() if v.InheritsFrom('RooRealVar'))
  inactive=sorted(n for n in allbg-active if not ww.var(n).isConstant())
  ff.Close()
  cmd[cmd.index('--freezeParameters')+1]=','.join(['MH']+list(indices)+inactive)
 return inspect(execute(name,cmd))
def clean(r):return r['status']==0 and r['edm']<.001 and r['covQual']>=2
if len(sys.argv)==3 and sys.argv[1]=='--resume-tolerance':
 for tol in [.1,.01]:
  fit('fixed_indices_activeonly_tol_'+str(tol),source,source,dict(r_ttH=1,r_tHq=1,**indices),tolerance=tol,fixed=True)
 sys.exit(0)
chosen=None
for strategy in [0,1,2]:
 r=fit('clean_snapshot_strategy'+str(strategy),source,source,dict(r_ttH=1,r_tHq=1),strategy)
 if clean(r):chosen=r;break
if chosen is None:raise RuntimeError('No validated snapshot; Method 2 generation blocked. Inspect results.json.')
snapshot=Path(chosen['workspace'])
d=execute('method2_generation',['combine','-M','GenerateOnly',str(snapshot),'--snapshotName','MultiDimFit','-m','125.09','-t','-1','--setParameters','MH=125.09,r_ttH=1,r_tHq=1','--freezeParameters','MH','--saveToys','-s','123456','-n','_CleanMethod2'])
toys=next(d.glob('higgsCombine*.root'))
fit('method2_closure',snapshot,toys,dict(r_ttH=1,r_tHq=1))
for name,tt,th,idx in [('generation_indices',1,1,indices),('low_strengths',.5,0,indices),('high_strengths',1.5,2,chosen['indices']),('zero_indices',1,1,{k:0 for k in indices})]:
 fit('start_'+name,source,source,dict(r_ttH=tt,r_tHq=th,**idx))
for tol in [.1,.01]:
 fit('fixed_indices_tol_'+str(tol),source,source,dict(r_ttH=1,r_tHq=1,**indices),tolerance=tol,fixed=True)
print('COMPLETED',out,flush=True)
print('Compare minNll only after checking its likelihood reference/offset; raw per-fit values are not asserted to share a reference.',flush=True)
