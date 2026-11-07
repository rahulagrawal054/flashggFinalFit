#!/usr/bin/env python3
"""Evaluate saved fits with one common Combine NLL, including envelope penalties."""
import json,sys
from pathlib import Path
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
ROOT.gInterpreter.Declare('#include "HiggsAnalysis/CombinedLimit/interface/CachingNLL.h"')
out=Path(sys.argv[1]).resolve()
base=out.parent.parent
if base.name not in ['DCB','SoG']:raise ValueError('Expected MODEL/checks/RUN output folder')
src=ROOT.TFile.Open(str(base/'snapshot/higgsCombine_Fiducial_AsimovPostfit.MultiDimFit.mH125.09.123456.root'))
w=src.Get('w');mc=w.obj('ModelConfig');data=src.Get('toys/toy_asimov')
w.loadSnapshot('MultiDimFit');w.saveSnapshot('comparison_reference',w.allVars())
nll=ROOT.cacheutils.CachingSimNLL(mc.GetPdf(),data,mc.GetNuisanceParameters())
nll.setZeroPoint()
rows={}
for d in sorted(out.iterdir()):
 if not (d/'validation.json').exists() or d.name.startswith('method2_closure'):continue
 rec=json.loads((d/'validation.json').read_text())
 w.loadSnapshot('comparison_reference')
 for name,value in rec['indices'].items():w.cat(name).setIndex(value)
 f=ROOT.TFile.Open(str(d/'multidimfit_Check.root'));r=f.Get('fit_mdf')
 w.allVars().assignValueOnly(r.constPars());w.allVars().assignValueOnly(r.floatParsFinal())
 val=float(nll.getVal())
 rows[d.name]=dict(common_reference_penalized_nll=val,**{k:rec[k] for k in ['status','edm','covQual','poi','indices']})
 f.Close()
if rows:
 best=min(r['common_reference_penalized_nll'] for r in rows.values())
 for r in rows.values():r['twice_delta_nll']=2*(r['common_reference_penalized_nll']-best)
(out/'common_nll_comparison.json').write_text(json.dumps(rows,indent=2)+'\n')
for name,r in rows.items():print(name,r['status'],r['poi'],'2dNLL',r['twice_delta_nll'])
