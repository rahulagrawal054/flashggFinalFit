from pathlib import Path
import subprocess,sys,json,csv,math,collections
import ROOT,numpy as np
from scipy.stats import gamma
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
base=Path.cwd();out=base/'packaged_all_years_20261014';eras=['2022preEE','2022postEE','2023preBPix','2023postBPix'];lumi={'2022preEE':7980.,'2022postEE':26670.,'2023preBPix':18063.,'2023postBPix':9693.}
sourcecheck={(r['model'],r['era'],r['category'],r['process']):r for r in csv.DictReader((base/'packaged_signals_20261014/workspace_validation.csv').open())}
manifest=[];validations=[]
for model in ['DCB','SoG']:
 stage=out/'inputs'/model;stage.mkdir(parents=True,exist_ok=True);dest=out/model;dest.mkdir(exist_ok=True);exts=[]
 for era in eras:
  ext=f'fiducial_{era}_{model}';exts.append(ext);run=next((base/'runs'/f'{era}_{model}').glob('*/run.log')).parent
  link=stage/f'outdir_{ext}';assert not link.exists();link.symlink_to(run/'Signal'/f'outdir_{ext}',target_is_directory=True)
 cats=sorted({k[2] for k in sourcecheck if k[0]==model});assert len(cats)==16
 for cat in cats:
  target=dest/f'CMS-HGG_sigfit_packaged_{model}_{cat}.root';assert not target.exists()
  cmd=[sys.executable,str(base/'scripts/packageSignal.py'),'--cat',cat,'--exts',','.join(exts),'--inputDir',str(stage),'--outputDir',str(dest),'--outputExt',model,'--massPoints','125','--mergeYears']
  print('MERGING',model,cat,flush=True)
  with (dest/(cat+'.log')).open('w') as lf:r=subprocess.run(cmd,stdout=lf,stderr=subprocess.STDOUT)
  assert r.returncode==0,(model,cat,r.returncode)
  f=ROOT.TFile.Open(str(target),'READ');assert f and not f.IsZombie();ws=f.Get('wsig_13TeV');assert ws;ws.var('MH').setVal(125.09);x=ws.var('CMS_hgg_mass');x.setVal(125.09);aset=ROOT.RooArgSet(x)
  for v in ws.allVars():
   if v.GetName().startswith('CMS_hgg_nuisance_'):v.setVal(0)
  keys=[k for k in sourcecheck if k[0]==model and k[2]==cat];assert len(keys)==64
  for k in keys:
   _,era,_,proc=k;name=f'{proc}_{era}_{cat}_13TeV';pdf=ws.pdf('hggpdfsmrel_'+name);norm=ws.function(pdf.GetName()+'_norm') if pdf else None;data=ws.data('sig_mass_m125_'+name);assert pdf and norm and data,(target,k)
   old=sourcecheck[k];assert data.numEntries()==int(old['dataset_entries']);assert math.isclose(norm.getVal(),float(old['norm_at_MH125p09']),rel_tol=1e-9,abs_tol=1e-14);assert math.isclose(data.sumEntries(),float(old['dataset_sumw']),rel_tol=1e-9,abs_tol=1e-14)
   assert math.isclose(pdf.getVal(aset),float(old['pdf_at_m125p09']),rel_tol=1e-8,abs_tol=1e-12)
   validations.append({'model':model,'era':era,'process':proc,'category':cat,'source_matches':True,'norm':norm.getVal()})
  merged=ws.data('sig_mass_m125_'+cat);assert bool(merged)==(cat!='bkg_had');f.Close()
  manifest.append({'model':model,'category':cat,'output':str(target),'eras':eras,'process_year_models':64});(out/'manifest.json').write_text(json.dumps(manifest,indent=2));print('VERIFIED',len(manifest),'/32',flush=True)
with (out/'source_match_validation.csv').open('w',newline='') as vf:
 w=csv.DictWriter(vf,fieldnames=list(validations[0]));w.writeheader();w.writerows(validations)
print('ALL PACKAGES VERIFIED; starting signed-weight aggregate diagnostics',flush=True)
plots=out/'comparison';plots.mkdir();results=[]
for cat in cats:
 files=[];spectra={};hist=None;variance=None;expect={};neg={};zero={}
 for model in ['DCB','SoG']:
  f=ROOT.TFile.Open(str(out/model/f'CMS-HGG_sigfit_packaged_{model}_{cat}.root'),'READ');files.append(f);ws=f.Get('wsig_13TeV');ws.var('MH').setVal(125.09)
  for v in ws.allVars():
   if v.GetName().startswith('CMS_hgg_nuisance_'):v.setVal(0)
  x=ws.var('CMS_hgg_mass');x.setBins(80);aset=ROOT.RooArgSet(x);edges=np.linspace(x.getMin(),x.getMax(),81);centers=(edges[1:]+edges[:-1])/2;bw=edges[1]-edges[0];grid=np.linspace(110,140,1501);curve=np.zeros(len(grid));prediction=np.zeros(80);h=np.zeros(80);var=np.zeros(80);total=0.;negative=0;zeros=0
  for k in [k for k in sourcecheck if k[0]==model and k[2]==cat]:
   _,era,_,proc=k;name=f'{proc}_{era}_{cat}_13TeV';pdf=ws.pdf('hggpdfsmrel_'+name);norm=ws.function(pdf.GetName()+'_norm');yieldv=norm.getVal()*lumi[era];total+=yieldv;negative+=yieldv<0;zeros+=yieldv==0
   for i,m in enumerate(grid):x.setVal(float(m));curve[i]+=yieldv*pdf.getVal(aset)
   for i,m in enumerate(centers):x.setVal(float(m));prediction[i]+=yieldv*pdf.getVal(aset)*bw
   if model=='DCB':
    data=ws.data('sig_mass_m125_'+name);xs=ws.function(f'fxs_{proc}_13TeV');br=ws.function('fbr_13TeV');assert xs and br;factor=xs.getVal()*br.getVal()*lumi[era]
    dh=ROOT.RooDataHist('audit_'+name,'audit_'+name,ROOT.RooArgSet(x),data)
    for i in range(dh.numEntries()):
     pos=dh.get(i).getRealValue('CMS_hgg_mass');idx=np.searchsorted(edges,pos,side='right')-1
     if not 0<=idx<80:continue
     val=dh.weight();err=dh.weightError(ROOT.RooAbsData.SumW2);h[idx]+=factor*val;var[idx]+=factor**2*err**2
  assert np.isfinite(curve).all();spectra[model]=(curve,prediction);expect[model]=total;neg[model]=negative;zero[model]=zeros
  if model=='DCB':hist=h;variance=var
 err=np.sqrt(variance);valid=(hist!=0)&(variance>0)&(centers>=110)&(centers<=140);neff=hist[valid]**2/variance[valid];scale=abs(hist[valid])/neff
 lower=gamma.interval(.68,neff,scale=scale)[0];upper=gamma.interval(.68,neff+1,scale=scale)[1];err[valid]=np.maximum(abs(lower-hist[valid]),abs(upper-hist[valid]));terms={};pulls={}
 for model in ['DCB','SoG']:
  pulls[model]=(spectra[model][1][valid]-hist[valid])/err[valid];terms[model]=float(np.sum(pulls[model]**2))
 row={'category':cat,'DCB_aggregate_chi2':terms['DCB'],'SoG_aggregate_chi2':terms['SoG'],'nonzero_bins_in_range':int(valid.sum()),'DCB_signed_expected_total':expect['DCB'],'SoG_signed_expected_total':expect['SoG'],'negative_components':neg['DCB'],'zero_components':zero['DCB'],'aggregate_nonnegative_DCB_on_grid':bool((spectra['DCB'][0]>=0).all()),'aggregate_nonnegative_SoG_on_grid':bool((spectra['SoG'][0]>=0).all())};results.append(row)
 fig,axs=plt.subplots(2,2,figsize=(12,8),gridspec_kw={'height_ratios':[3,1]})
 for col in range(2):
  ax=axs[0,col];ax.errorbar(centers,hist/bw,yerr=err/bw,fmt='.',color='black',ms=3,label='Signed MC sum, all processes + eras')
  for model,color in [('DCB','tab:blue'),('SoG','tab:orange')]:
   ax.plot(grid,spectra[model][0],color=color,label=f'{model}: aggregate chi2={terms[model]:.2f} (no ndof/p-value)');axs[1,col].plot(centers[valid],pulls[model],'.-',color=color,ms=3)
  limits=(120,130) if col==0 else (110,140);ax.set_xlim(*limits);axs[1,col].set_xlim(*limits);ax.set_ylabel('Signed expected events / GeV');ax.legend(fontsize=7);axs[1,col].set_ylabel('(model-MC)/error');axs[1,col].set_xlabel('Diphoton mass [GeV]');axs[1,col].axhline(0,color='black',lw=.7)
 axs[0,1].set_yscale('log');axs[0,1].set_ylim(max(1e-5,expect['DCB']*1e-6),max(spectra['DCB'][0].max(),spectra['SoG'][0].max())*2)
 fig.suptitle(f'{cat}: all 4 eras, 16 processes/era; MH=125.09, photon nuisances=0\nSigned-weight diagnostic; {neg["DCB"]} negative-rate and {zero["DCB"]} zero-rate components retained',fontsize=10)
 fig.tight_layout();fig.savefig(plots/(cat+'.png'),dpi=140);fig.savefig(plots/(cat+'.pdf'));plt.close(fig)
 for f in files:f.Close()
 print('PLOT',cat,'DCB',round(terms['DCB'],2),'SoG',round(terms['SoG'],2),flush=True)
with (out/'aggregate_comparison.csv').open('w',newline='') as vf:
 w=csv.DictWriter(vf,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
(out/'summary.json').write_text(json.dumps({'files_per_model':16,'total_files':32,'verified_process_year_models':len(validations),'plots':len(results),'eras':eras,'lumi_pb':lumi},indent=2))
report='''# All-era category packages and aggregate shape comparison

DCB/ and SoG/ each contain 16 category ROOT files. Each wsig_13TeV contains 64 distinct process/year PDFs, normalization functions and individual datasets (16 processes × 4 eras). These models are collected in one file, not refitted or replaced by one summed PDF. Years remain identified by object names. Correlated nuisance names are shared through the existing packager's RecycleConflictNodes behavior. MH and IntLumi remain shared variables; set their intended downstream treatment in the datacard/Combine workflow. No production source workspace or fitting configuration changed.

Packaging used the existing scripts/packageSignal.py --mergeYears implementation with links to the completed run outputs. The summed unweighted-by-cross-section category dataset is retained except bkg_had, where the existing code skips it to avoid ROOT buffer limits. It is not itself the luminosity-weighted physics sum used in the diagnostic plots.

All 32 files were reopened and all 2,048 process/year PDFs, normalization functions and datasets verified against the previous per-era package validation: entries, signed sums, central norms and single-point PDF values agree. See manifest.json and source_match_validation.csv. This does not validate full nuisance ranges or fit convergence.

## Aggregate plots and chi-square

For each category, comparison/ contains PNG and PDF overlays of all process/year models against the same luminosity-weighted signed MC sum. We use MH=125.09, m in 110–140, 80 bins over the observable range, photon nuisances zero. Luminosities (pb^-1): 2022preEE 7980, 2022postEE 26670, 2023preBPix 18063, 2023postBPix 9693, matching the local lumiMap. Curve = sum(norm_process,era × luminosity_era × PDF_process,era). MC weights are multiplied by production cross section × BR × luminosity. Input MC masses remain 125: the plotted PDF translates to 125.09, but the histogram is the original 125 MC, not shifted/regenerated. This 0.09 GeV hypothesis difference contributes to these residuals; compare equal mass hypotheses for a clean family-choice test.

Negative and zero rates are retained explicitly without clipping or omission. These curves are signed expected-spectrum diagnostics, not a validation that every component is a physical nonnegative probability PDF. Negative process rates must be resolved before final statistical use. Some total spectra can look acceptable while bad low-yield component shapes are hidden by the sum.

The aggregate chi-square uses nonzero bin contents in 110–140 and weighted gamma-interval errors, taking the larger error side, as in the central objective prescription. It is freshly calculated for the sum; it is not the sum of original chi-squares and no chi2/ndof or p-value is assigned. Aggregation hides process/era-specific discrepancies and parameter-count/model-selection differences; the number of independent fitted coefficients and effective degrees of freedom are not inferred from this plot. Diagnostic values do not identify a universal model winner and are not a substitute for the matched individual-shape review. Original fit failures, bounds, Gaussian-count-selection issues and negative-rate treatment remain unresolved.

| Category | DCB aggregate chi2 | SoG aggregate chi2 | Bins used | Negative components | Plot |
|---|---:|---:|---:|---:|---|
'''
for r in results:report+=f'| {r["category"]} | {r["DCB_aggregate_chi2"]:.2f} | {r["SoG_aggregate_chi2"]:.2f} | {r["nonzero_bins_in_range"]} | {r["negative_components"]} | [PNG](comparison/{r["category"]}.png) |\n'
(out/'README.md').write_text(report);print('COMPLETE 32 merged category files + 16 comparison plots',flush=True)
