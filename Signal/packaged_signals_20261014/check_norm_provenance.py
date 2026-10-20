from pathlib import Path
import csv,json,math
import ROOT
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
p=Path('packaged_signals_20261014');rows=list(csv.DictReader((p/'workspace_validation.csv').open()));checks=[]
for era in ['2022preEE','2022postEE','2023preBPix','2023postBPix']:
 for kind in ['zero','negative']:
  eligible=[r for r in rows if r['model']=='DCB' and r['era']==era and (float(r['norm_at_MH125p09'])==0 if kind=='zero' else float(r['norm_at_MH125p09'])<0)]
  if not eligible:continue
  r=eligible[0];proc,cat=r['process'],r['category'];src=next(Path('runs',era+'_DCB').glob(f'*/Signal/outdir_*/signalFit/output/*_{proc}_{era}_{cat}.root'))
  f=ROOT.TFile.Open(str(src),'READ');w=f.Get('wsig_13TeV');w.var('MH').setVal(125.09)
  for v in w.allVars():
   if v.GetName().startswith('CMS_hgg_nuisance_'):v.setVal(0)
  name=f'{proc}_{era}_{cat}_13TeV';val=w.function('hggpdfsmrel_'+name+'_norm').getVal();sumw=w.data('sig_mass_m125_'+name).sumEntries();assert math.isclose(val,float(r['norm_at_MH125p09']),rel_tol=1e-10,abs_tol=1e-15);assert math.isclose(sumw,float(r['dataset_sumw']),rel_tol=1e-10,abs_tol=1e-15)
  checks.append({'era':era,'process':proc,'category':cat,'kind':kind,'input_norm':val,'packaged_norm':float(r['norm_at_MH125p09']),'input_sumw':sumw,'matches_source':True});f.Close()
(p/'normalization_provenance.json').write_text(json.dumps(checks,indent=2));print('Verified',len(checks),'zero/negative packaged norms against original source workspaces.')
