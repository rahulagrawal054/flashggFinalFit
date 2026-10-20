from pathlib import Path
import re,json,csv,collections
base=Path.cwd();out=base/'shape_review_20261014';out.mkdir(exist_ok=True)
models={}
for log in sorted((base/'runs').glob('*/*/run.log')):
 era,model=log.parent.parent.name.rsplit('_',1);s=log.read_text();sf=s.split('Starting signalFit:',1)[1]
 for b in re.split(r' --> Running fit for \(proc,cat\) = ',sf)[1:]:
  proc,cat=re.match(r'\(([^,]+),([^\)]+)\)',b).groups()
  m=re.search(r'Optimizer: success=(True|False), status=(\d+), message=([^\n]+)',b);assert m
  ch=re.findall(r'chi2 = ([\d.eE+-]+), n\(dof\) = ([\d.eE+-]+) --> chi2/n\(dof\) = ([\d.eE+-]+)',b);assert ch
  png=Path(re.search(r'png file (.+?\.png) has been created',b)[1]);donor=proc;dc=cat
  if '_from_' in png.stem:
   suffix=png.stem.split('_from_',1)[1];assert suffix.endswith('_'+cat);donor=suffix[:-(len(cat)+1)]
  path=next(log.parent.glob(f'Signal/outdir_*/signalFit/output/*_{proc}_{era}_{cat}.root'))
  n=re.search(r'Fitting function: convolution of nGaussians \((\d+)\)',b)
  models[(era,proc,cat,model)]={'ok':m[1]=='True','chi2':float(ch[-1][0]),'ndof':int(float(ch[-1][1])),'reduced':float(ch[-1][2]),'bounds':re.findall(r'Parameter at boundary: ([^\n]+)',b),'donor':donor,'root':str(path),'log':str(log),'ngauss':int(n[1]) if n else None}
pairs=[]
for (era,proc,cat,model),d in models.items():
 if model!='DCB':continue
 s=models[(era,proc,cat,'SoG')]
 pairs.append({'era':era,'process':proc,'category':cat,'donor_DCB':d['donor'],'donor_SoG':s['donor'],'same_donor':d['donor']==s['donor'],'DCB_success':d['ok'],'SoG_success':s['ok'],'DCB_chi2':d['chi2'],'SoG_chi2':s['chi2'],'DCB_ndof':d['ndof'],'SoG_ndof':s['ndof'],'DCB_reduced':d['reduced'],'SoG_reduced':s['reduced'],'DCB_boundary_count':len(d['bounds']),'SoG_boundary_count':len(s['bounds']),'SoG_N':s['ngauss']})
assert len(pairs)==1024
with (out/'all_pairs.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(pairs[0]));w.writeheader();w.writerows(pairs)
summary={};selected=[]
for era in sorted({p['era'] for p in pairs}):
 ps=[p for p in pairs if p['era']==era];both=[p for p in ps if p['same_donor'] and p['DCB_success'] and p['SoG_success']]
 summary[era]={'pairs':len(ps),'same_donor':sum(p['same_donor'] for p in ps),'both_converged':len(both),'DCB_only_converged':sum(p['DCB_success'] and not p['SoG_success'] for p in ps),'SoG_only_converged':sum(p['SoG_success'] and not p['DCB_success'] for p in ps),'neither_converged':sum(not p['DCB_success'] and not p['SoG_success'] for p in ps)}
 choices=[('reference ttH',next(p for p in ps if p['process']=='tth_in' and p['category']=='ttH_had_1')),('largest SoG reduced-chi2 advantage among both converged',max(both,key=lambda p:p['DCB_reduced']-p['SoG_reduced'])),('largest DCB reduced-chi2 advantage among both converged',max(both,key=lambda p:p['SoG_reduced']-p['DCB_reduced'])),('largest reduced chi2 overall',max(ps,key=lambda p:max(p['DCB_reduced'],p['SoG_reduced'])))]
 seen=set()
 for reason,p in choices:
  k=(p['process'],p['category'])
  if k not in seen:selected.append(dict(p,selection_reason=reason));seen.add(k)
print('LOG SUMMARY',json.dumps(summary),flush=True)
import ROOT,numpy as np
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import gamma
metrics=[]
for row in selected:
 era,proc,cat=row['era'],row['process'],row['category'];files=[];arrays={};curves={};means={};widths={}
 for model in ['DCB','SoG']:
  info=models[(era,proc,cat,model)];f=ROOT.TFile.Open(info['root'],'READ');assert f and not f.IsZombie();files.append(f);ws=f.Get('wsig_13TeV');assert ws
  ws.var('MH').setVal(125.)
  for v in ws.allVars():
   if v.GetName().startswith('CMS_hgg_nuisance_'):v.setVal(0)
  name=f'{proc}_{era}_{cat}_13TeV';pdf=ws.pdf('hggpdfsmrel_'+name);x=ws.var('CMS_hgg_mass');aset=ROOT.RooArgSet(x);assert pdf
  lo,hi=x.getMin(),x.getMax();edges=np.linspace(lo,hi,81);centers=(edges[1:]+edges[:-1])/2;bw=edges[1]-edges[0]
  grid=np.linspace(lo,hi,4001);density=[];pred=[]
  for m in grid:x.setVal(float(m));density.append(pdf.getVal(aset))
  for m in centers:x.setVal(float(m));pred.append(pdf.getVal(aset)*bw)
  density=np.array(density);assert np.isfinite(density).all() and (density>=0).all()
  curves[model]=(grid,density,np.array(pred))
  donor=info['donor'];df=ROOT.TFile.Open(models[(era,donor,cat,model)]['root'],'READ');assert df and not df.IsZombie();files.append(df);dw=df.Get('wsig_13TeV');ds=dw.data(f'sig_mass_m125_{donor}_{era}_{cat}_13TeV');assert ds
  vals=[];weights=[]
  for i in range(ds.numEntries()):vals.append(ds.get(i).getRealValue('CMS_hgg_mass'));weights.append(ds.weight())
  weights=np.asarray(weights);total=weights.sum();assert total>0;weights=weights/total
  h=np.histogram(vals,bins=edges,weights=weights)[0];e2=np.histogram(vals,bins=edges,weights=weights**2)[0];arrays[model]=(h,e2)
  cum=np.r_[0,np.cumsum((density[1:]+density[:-1])/2*np.diff(grid))];integral=float(cum[-1]);cum=cum/integral
  q16,q50,q84=np.interp([.16,.5,.84],cum,grid)
  masklow=grid<=120;maskhi=grid>=130
  row[model+'_shape']={'integral':integral,'mode':float(grid[np.argmax(density)]),'median':float(q50),'half_16_84_width':float((q84-q16)/2),'fraction_below120':float(np.trapz(density[masklow],grid[masklow])/integral),'fraction_above130':float(np.trapz(density[maskhi],grid[maskhi])/integral),'donor_entries':ds.numEntries(),'donor_sumw':float(total),'bounds':info['bounds']}
 assert np.allclose(arrays['DCB'][0],arrays['SoG'][0],rtol=1e-6,atol=1e-10),'Different MC histograms'
 assert np.allclose(curves['DCB'][0],curves['SoG'][0])
 grid,a,_=curves['DCB'];b=curves['SoG'][1];row['total_variation_grid']=float(.5*np.trapz(abs(a-b),grid));row['same_MC_histogram_verified']=True
 h,e2=arrays['DCB'];err=np.sqrt(e2);valid=(h!=0)&(e2>0);neff=h[valid]**2/e2[valid];scale=abs(h[valid])/neff
 low=gamma.interval(.68,neff,scale=scale)[0];high=gamma.interval(.68,neff+1,scale=scale)[1];err[valid]=np.maximum(abs(low-h[valid]),abs(high-h[valid]));valid=valid&(centers>=110)&(centers<=140)
 fig,axs=plt.subplots(2,2,figsize=(12,8),gridspec_kw={'height_ratios':[3,1]})
 for col in range(2):
  ax=axs[0,col];ax.errorbar(centers,h/bw,yerr=err/bw,fmt='.',color='black',ms=3,label=f'MC: {row["donor_DCB"]} / {cat}')
  for model,color in [('DCB','tab:blue'),('SoG','tab:orange')]:
   g,d,pred=curves[model];info=models[(era,proc,cat,model)];label=f'{model}: chi2/ndof={info["reduced"]:.3f}, success={info["ok"]}, bounds={len(info["bounds"])}'
   ax.plot(g,d,color=color,label=label);axs[1,col].plot(centers[valid],((pred-h)/err)[valid],'.-',color=color,ms=3,label=model)
  ax.set_ylabel('Normalized density [1/GeV]');ax.legend(fontsize=7);ax.grid(alpha=.2)
  axs[1,col].axhline(0,color='black',lw=.7);axs[1,col].axhline(2,color='gray',ls=':');axs[1,col].axhline(-2,color='gray',ls=':');axs[1,col].set_ylabel('(model-MC)/error');axs[1,col].set_xlabel('Diphoton mass [GeV]')
  limits=(120,130) if col==0 else (110,140);ax.set_xlim(*limits);axs[1,col].set_xlim(*limits)
 axs[0,1].set_yscale('log');axs[0,1].set_ylim(1e-5,max(a.max(),b.max())*2)
 fig.suptitle(f'{era}: recipient {proc} / {cat}; MH=125, nuisances=0\n{row["selection_reason"]}; normalized shape comparison, not yield comparison',fontsize=10)
 fig.tight_layout();stem=f'{era}_{proc}_{cat}';fig.savefig(out/(stem+'.png'),dpi=140);fig.savefig(out/(stem+'.pdf'));plt.close(fig);row['plot']=stem+'.png';metrics.append(row)
 for f in files:f.Close()
 print('PLOT',stem,'TV',round(row['total_variation_grid'],4),flush=True)
(out/'selected_shapes.json').write_text(json.dumps(metrics,indent=2));(out/'summary.json').write_text(json.dumps(summary,indent=2))
report='# Matched DCB versus SoG shape review\n\nRead-only review of 1,024 recipient pairs from the completed 12 October runs. No fitting settings, selections or workspaces changed. All central comparisons use MH=125 and photon nuisance values zero. all_pairs.csv gives log diagnostics for every pair. selected_shapes.json contains evaluated PDF metrics and the selected plots.\n\n## All-pair convergence\n\n| Era | Same donor | Both converged | DCB only converged | SoG only converged | Neither converged |\n|---|---:|---:|---:|---:|---:|\n'
for era,s in summary.items():report+=f'| {era} | {s["same_donor"]} | {s["both_converged"]} | {s["DCB_only_converged"]} | {s["SoG_only_converged"]} | {s["neither_converged"]} |\n'
report+='\n## Representative shapes\n\nCases include the same ttH reference in each era, the largest reduced-chi-square differences among pairs where both converge, and the largest reduced chi-square overall. These selected examples emphasize differences; they are not an unbiased estimate of overall model quality. MC comes from the corresponding donor own-model saved nominal dataset, after beamspot reweighting. Its normalized histogram was checked to agree between DCB and SoG. Plot points/chi-square describe donor MC when borrowed, not recipient MC.\n\n| Pair | DCB reduced chi2 | SoG reduced chi2 | DCB success | SoG success | PDF total variation | Plot |\n|---|---:|---:|---|---|---:|---|\n'
for r in metrics:report+=f'| {r["era"]} / {r["process"]} / {r["category"]} | {r["DCB_reduced"]} | {r["SoG_reduced"]} | {r["DCB_success"]} | {r["SoG_success"]} | {r["total_variation_grid"]:.4f} | [PNG]({r["plot"]}) |\n'
report+='\nTotal variation is half the absolute PDF difference integrated numerically over the observable range; it measures model differences, not goodness of fit. Pulls use the weighted gamma-interval error prescription of the objective and are shown only for nonzero bins inside 110–140 GeV. PDF curves are sampled; reported chi-square values come from logs. Tail fractions below 120 and above 130 and half the 16–84% quantile width are finite-range metrics, not fitted core sigma. Reduced chi-square alone does not account for model selection and is not a calibrated p-value. The SoG candidate-selection convergence issue remains unresolved. Log convergence is necessary evidence but does not prove global optimality, closure or physical rates. ROOT files were opened READ; analysis artifacts are new outputs only.\n'
(out/'README.md').write_text(report);print('DONE',len(metrics),'plots',flush=True)
