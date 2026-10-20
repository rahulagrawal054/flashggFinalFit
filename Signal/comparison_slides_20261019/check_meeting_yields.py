"""Read-only SoG normalization check against the saved DCB prefit yield table."""
from pathlib import Path
import csv,json,math
import ROOT
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
base=Path(__file__).resolve().parent
combine=base.parent.parent/'Combine'
reference={ (r['cat'],r['proc']):r for r in csv.DictReader((combine/'DCB/yield_tables_20261017/workspace_yields.csv').open()) }
f=ROOT.TFile.Open(str(combine/'SoG/workspace.root'),'READ');assert f and not f.IsZombie()
w=f.Get('w');assert w
for n in w.obj('ModelConfig').GetNuisanceParameters():
 if n.InheritsFrom('RooRealVar') and not n.GetName().startswith(('shapeBkg','env_pdf')):n.setVal(0)
for name in ('r_ttH','r_tHq'):w.var(name).setVal(1)
w.var('MH').setVal(125.09)
rows=[]
for fun in w.allFunctions():
 name=fun.GetName()
 if not name.startswith('n_exp_final_bin') or '_proc_' not in name:continue
 cat,proc=name[len('n_exp_final_bin'):].split('_proc_',1)
 if proc=='bkg_mass':continue
 val=float(fun.getVal());assert math.isfinite(val) and val>=0
 key=(cat,proc);assert key in reference,key
 ref=float(reference[key]['yield_events'])
 rows.append(dict(cat=cat,proc=proc,DCB=ref,SoG=val,difference=val-ref))
assert len(rows)==len(reference)==563
out=base/'meeting_inputs';out.mkdir(exist_ok=True)
with (out/'yield_comparison.csv').open('w') as h:
 writer=csv.DictWriter(h,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
summary=dict(rows=len(rows),mass=125.09,poi_values={'r_ttH':1,'r_tHq':1},nuisances='constrained real nuisances zero',
 DCB_total=sum(r['DCB'] for r in rows),SoG_total=sum(r['SoG'] for r in rows),
 max_absolute_difference=max(abs(r['difference']) for r in rows),
 max_relative_difference=max(abs(r['difference'])/max(abs(r['DCB']),1e-12) for r in rows),
 qualification='Prefit retained Higgs normalization functions after card pruning. No continuum events or observed counts. No workspace was changed.')
(out/'yield_comparison.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2),flush=True)
f.Close()
