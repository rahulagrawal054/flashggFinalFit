#!/usr/bin/env python3
"""Fix only constrained nuisances at zero; compare profiled/fixed background indices."""
import json,shlex,subprocess
from pathlib import Path
from datetime import datetime,timezone
import ROOT
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
base=Path(__file__).resolve().parent
runs={'DCB':'validated_closure_20261024T050616Z','SoG':'validated_closure_20261024T052559Z'}
for model,run in runs.items():
 origin=base/model/'checks'/run
 out=base/model/'checks'/('np_zero_control_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));out.mkdir(parents=True)
 # Read the actual constraints instead of depending on a moved plot-study CSV.
 card=base/model/f'Datacard_{model}.txt'
 names=[fields[0] for line in card.read_text().splitlines() if len(fields:=line.split())>1 and fields[1] in ('lnN','param')]
 assert len(names)==91 and len(set(names))==91
 ff=ROOT.TFile.Open(str(base/model/'workspace.root'));ww=ff.Get('w')
 assert all(ww.var(n) and ww.var(n).getVal()==0 for n in names)
 indices={c.GetName():int(c.getIndex()) for c in ww.allCats() if c.GetName().startswith('pdfindex_')}
 active=set();allbg=set()
 for pdf in ww.allPdfs():
  if pdf.InheritsFrom('RooMultiPdf'):
   allbg.update(v.GetName() for v in pdf.getVariables() if v.InheritsFrom('RooRealVar'))
   active.update(v.GetName() for v in pdf.getCurrentPdf().getVariables() if v.InheritsFrom('RooRealVar'))
 inactive=sorted(n for n in allbg-active if not ww.var(n).isConstant());ff.Close()
 results={}
 for fixed in [False,True]:
  name='indices_fixed' if fixed else 'indices_profiled';d=out/name;d.mkdir()
  cmd=shlex.split((origin/'clean_snapshot_strategy0/command.sh').read_text().splitlines()[-1])
  freeze=['MH']+names+(list(indices)+inactive if fixed else [])
  cmd[cmd.index('--freezeParameters')+1]=','.join(freeze)
  settings=dict(MH=125.09,r_ttH=1,r_tHq=1,**{n:0 for n in names},**indices)
  cmd[cmd.index('--setParameters')+1]=','.join(f'{k}={v}' for k,v in settings.items())
  (d/'command.sh').write_text('#!/bin/bash\n'+shlex.join(cmd)+'\n')
  print('RUN',model,name,str(d),flush=True)
  with (d/'fit.log').open('w') as log:rc=subprocess.call(cmd,cwd=d,stdout=log,stderr=subprocess.STDOUT)
  if rc:raise RuntimeError(f'{model} {name}: exit {rc}')
  f=ROOT.TFile.Open(str(d/'multidimfit_Check.root'));r=f.Get('fit_mdf')
  vals={v.GetName():v.getVal() for v in r.floatParsFinal()}
  row=dict(status=int(r.status()),edm=float(r.edm()),covQual=int(r.covQual()),poi={n:vals[n] for n in ['r_ttH','r_tHq']},constrained_nuisances={n:0 for n in names})
  f.Close();g=ROOT.TFile.Open(str(d/'higgsCombine_Check.MultiDimFit.mH125.09.root'));w=g.Get('w');w.loadSnapshot('MultiDimFit')
  assert all(w.var(n).isConstant() and w.var(n).getVal()==0 for n in names)
  row['indices']={n:int(w.cat(n).getIndex()) for n in indices};g.Close()
  results[name]=row;(out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
  print(model,name,row['poi'],'status',row['status'],'covQual',row['covQual'],flush=True)
 print('COMPLETED',out,flush=True)
