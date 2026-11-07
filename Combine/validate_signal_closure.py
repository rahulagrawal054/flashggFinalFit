#!/usr/bin/env python3
"""Sequential saved-Asimov closure checks; preserve original production outputs."""
import argparse, json, shlex, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
import ROOT
ROOT.gROOT.SetBatch(True)
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--model',choices=['DCB','SoG'],required=True)
parser.add_argument('--resume-method2',type=Path)
args=parser.parse_args()
base=Path(__file__).resolve().parent/args.model
source=base/'snapshot/higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH125.09.123456.root'
out=base/'checks'/('validated_closure_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
if args.resume_method2:out=args.resume_method2.resolve()
out.mkdir(parents=True,exist_ok=True)
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
ff=ROOT.TFile.Open(str(base/'workspace.root'));ww=ff.Get('w')
indices={c.GetName():int(c.getIndex()) for c in ww.allCats() if c.GetName().startswith('pdfindex_')}
ff.Close()
(out/'generation_indices.json').write_text(json.dumps(indices,indent=2)+'\n')
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
if args.resume_method2:
 chosen=next(r for n,r in results.items() if n.startswith('clean_snapshot_') and clean(r))
 snapshot=Path(chosen['workspace']);toys=next((out/'method2_generation').glob('higgsCombine*.root'))
 for strategy in [1,2]:
  r=fit('method2_closure_strategy'+str(strategy),snapshot,toys,dict(r_ttH=1,r_tHq=1),strategy=strategy)
  if clean(r) and r['covQual']==3:break
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
fit('generation_indices_fixed',source,source,dict(r_ttH=1,r_tHq=1,**indices),fixed=True)
print('COMPLETED',out,flush=True)
subprocess.run([sys.executable,str(Path(__file__).with_name('compare_DCB_closure_nll.py')),str(out)],check=True)
