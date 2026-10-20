from pathlib import Path
import ROOT,csv,json,collections
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit');ROOT.gROOT.SetBatch(True)
p=Path('runplotter_year_overlays_20261014');models=list(csv.DictReader(Path('packaged_all_years_20261014/source_match_validation.csv').open()));lum={'2022preEE':7980.,'2022postEE':26670.,'2023preBPix':18063.,'2023postBPix':9693.};rows=[];stats=[]
for model in ['DCB','SoG']:
 for cat in sorted({r['category'] for r in models}):
  f=ROOT.TFile.Open(str(Path('packaged_all_years_20261014')/model/f'CMS-HGG_sigfit_packaged_{model}_{cat}.root'),'READ');w=f.Get('wsig_13TeV');w.var('MH').setVal(125.)
  for v in w.allVars():
   if v.GetName().startswith('CMS_hgg_nuisance_'):v.setVal(0)
  values=[]
  for r in [r for r in models if r['model']==model and r['category']==cat]:
   era,proc=r['era'],r['process'];w.var('IntLumi').setVal(lum[era]);norm=w.function(f'hggpdfsmrel_{proc}_{era}_{cat}_13TeV_normThisLumi');values.append((norm.getVal(),era,proc))
  total=sum(v for v,era,proc in values);assert total>0;cut=.001*total
  for v,era,proc in values:rows.append({'model':model,'category':cat,'era':era,'process':proc,'yield_MH125':v,'signed_category_total':total,'threshold':cut,'pruned':v<cut,'reason':'negative rate' if v<0 else 'zero rate' if v==0 else 'positive below threshold' if v<cut else 'retained'})
  stats.append({'model':model,'category':cat,'total':total,'cut':cut,'kept':sum(v>=cut for v,_,_ in values),'negative_pruned':sum(v<0 for v,_,_ in values),'zero_pruned':sum(v==0 for v,_,_ in values),'positive_pruned':sum(0<v<cut for v,_,_ in values)});f.Close()
with (p/'pruning_audit.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
summary={model:{k:sum(r[k] for r in stats if r['model']==model) for k in ['kept','negative_pruned','zero_pruned','positive_pruned']} for model in ['DCB','SoG']};summary['all_category_totals_positive']=True;summary['all_negative_and_zero_rates_pruned']=all(r['pruned'] for r in rows if r['yield_MH125']<=0)
(p/'pruning_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary))
