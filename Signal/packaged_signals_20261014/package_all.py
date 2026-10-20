from pathlib import Path
import subprocess,json,datetime,csv,sys
import ROOT
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
base=Path.cwd();out=base/'packaged_signals_20261014';records=[];validation=[]
for model in ['DCB','SoG']:
 for era in ['2022preEE','2022postEE','2023preBPix','2023postBPix']:
  runs=sorted((base/'runs'/f'{era}_{model}').glob('*/run.log'));assert len(runs)==1
  run=runs[0].parent;assert 'All stages finished.' in runs[0].read_text()
  ext=f'fiducial_{era}_{model}';source=run/'Signal'/f'outdir_{ext}'/'signalFit'/'output';files=list(source.glob('*.root'));assert len(files)==256
  cats=sorted({f.name.rsplit('_'+era+'_',1)[1][:-5] for f in files});assert len(cats)==16
  dest=out/model/era;dest.mkdir(parents=True,exist_ok=True)
  for cat in cats:
   inputs=[f for f in files if f.name.endswith('_'+era+'_'+cat+'.root')];assert len(inputs)==16
   target=dest/f'CMS-HGG_sigfit_packaged_{model}_{cat}_{era}.root';assert not target.exists(),target
   cmd=[sys.executable,str(base/'scripts/packageSignal.py'),'--cat',cat,'--exts',ext,'--inputDir',str(run/'Signal'),'--outputDir',str(dest),'--outputExt',model,'--massPoints','125','--year',era]
   logfile=dest/(cat+'.log');print('PACKAGING',model,era,cat,flush=True)
   start=datetime.datetime.now().isoformat()
   with logfile.open('w') as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
   assert r.returncode==0,(cmd,r.returncode,logfile)
   f=ROOT.TFile.Open(str(target),'READ');assert f and not f.IsZombie();ws=f.Get('wsig_13TeV');assert ws
   ws.var('MH').setVal(125.09)
   for v in ws.allVars():
    if v.GetName().startswith('CMS_hgg_nuisance_'):v.setVal(0)
   x=ws.var('CMS_hgg_mass');x.setVal(125.09);aset=ROOT.RooArgSet(x)
   for src in inputs:
    proc=src.name[len('CMS-HGG_sigfit_'+ext+'_'):].rsplit('_'+era+'_',1)[0];name=f'{proc}_{era}_{cat}_13TeV';pdf=ws.pdf('hggpdfsmrel_'+name);norm=ws.function('hggpdfsmrel_'+name+'_norm');data=ws.data('sig_mass_m125_'+name)
    assert pdf and norm and data,(target,proc)
    row={'model':model,'era':era,'category':cat,'process':proc,'dataset_entries':data.numEntries(),'dataset_sumw':data.sumEntries(),'norm_at_MH125p09':norm.getVal(),'pdf_at_m125p09':pdf.getVal(aset)}
    import math
    row['finite_positive_norm']=math.isfinite(row['norm_at_MH125p09']) and row['norm_at_MH125p09']>0
    row['finite_nonnegative_pdf_at_test_point']=math.isfinite(row['pdf_at_m125p09']) and row['pdf_at_m125p09']>=0
    validation.append(row)
   merged=ws.data('sig_mass_m125_'+cat)
   assert bool(merged)==(cat!='bkg_had')
   f.Close();records.append({'model':model,'era':era,'category':cat,'input_files':16,'output':str(target),'log':str(logfile),'started':start,'finished':datetime.datetime.now().isoformat(),'verified_process_models':16,'merged_dataset':cat!='bkg_had'})
   (out/'packaging_manifest.json').write_text(json.dumps(records,indent=2))
   with (out/'workspace_validation.csv').open('w',newline='') as vf:
    writer=csv.DictWriter(vf,fieldnames=list(validation[0]));writer.writeheader();writer.writerows(validation)
   print('VERIFIED',len(records),'/128',model,era,cat,flush=True)
summary={'packaged_files':len(records),'process_models_verified':len(validation),'nonpositive_or_nonfinite_norms':sum(not r['finite_positive_norm'] for r in validation),'invalid_pdf_test_values':sum(not r['finite_nonnegative_pdf_at_test_point'] for r in validation)}
(out/'summary.json').write_text(json.dumps(summary,indent=2));print('COMPLETE',json.dumps(summary),flush=True)
(out/'README.md').write_text('''# Packaged DCB and SoG signals

Outputs are separated by model and era: `DCB/<era>/` and `SoG/<era>/`. Each contains 16 category ROOT files, each with `wsig_13TeV` and all 16 process PDFs, normalization functions and individual nominal datasets. This packaging does not refit or change the source signalFit workspaces, Gaussian counts or optimizer settings. Years and model families were not merged.

The existing packager omits the category-summed dataset for `bkg_had` to avoid the ROOT buffer limit; individual process datasets remain present. Other categories include their summed nominal dataset at mass 125.

`packaging_manifest.json` records inputs/output locations and completion. `workspace_validation.csv` records each process dataset, normalization and one PDF evaluation at MH=125.09, m=125.09, photon nuisances zero. These numerical settings were made only in the reopened READ workspaces in memory, not written back to disk. The saved MH value is not guaranteed to be 125.09; set the intended hypothesis downstream. `summary.json` gives the validation totals. Category logs are alongside their outputs; `packaging.log` tracks the overall run.

The completed fits still contain previously documented convergence/boundary and Gaussian-count-selection issues. Packaging and structural checks do not resolve those issues, validate full-range PDF positivity, nuisance responses, luminosity handling or Asimov closure. The user's visual review authorized packaging both existing model families.
''')
