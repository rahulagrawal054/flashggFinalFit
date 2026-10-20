from pathlib import Path
import ROOT,numpy as np,json,csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
base=Path.cwd();out=base/'smearing_pdf_scan_20261015';proc,cat='tth_in','ttH_had_1';mh=125.09;grid=np.linspace(110,140,1501);shifts=[-2,-1,0,1,2];eras=['2022preEE','2022postEE','2023preBPix','2023postBPix'];results={};csvrows=[]
previous=json.loads((base/'shape_review_20261014/selected_shapes.json').read_text());statuses={(r['era'],model):r[model+'_success'] for r in previous if r['process']==proc and r['category']==cat for model in ['DCB','SoG']}
for era in eras:
 curves={};details={}
 for model in ['DCB','SoG']:
  path=base/'packaged_all_years_20261014'/model/f'CMS-HGG_sigfit_packaged_{model}_{cat}.root';f=ROOT.TFile.Open(str(path),'READ');assert f and not f.IsZombie();ws=f.Get('wsig_13TeV');assert ws;ws.var('MH').setVal(mh)
  for v in ws.allVars():
   if v.GetName().startswith('CMS_hgg_nuisance_'):v.setVal(0.)
  nuisance=ws.var('CMS_hgg_nuisance_Smearing');assert nuisance;name=f'{proc}_{era}_{cat}_13TeV';pdf=ws.pdf('hggpdfsmrel_'+name);norm=ws.function(pdf.GetName()+'_norm');assert pdf and norm;x=ws.var('CMS_hgg_mass');aset=ROOT.RooArgSet(x);fullgrid=np.linspace(x.getMin(),x.getMax(),4001);ds=ws.data('sig_mass_m125_'+name)
  details[model]={'file':str(path),'nuisance':nuisance.GetName(),'MH':mh,'fit_success_from_log':statuses[(era,model)],'dataset_entries':ds.numEntries(),'dataset_sumw':ds.sumEntries(),'scan':{}}
  for shift in shifts:
   nuisance.setVal(float(shift));values=[];full=[]
   for m in grid:x.setVal(float(m));values.append(pdf.getVal(aset))
   for m in fullgrid:x.setVal(float(m));full.append(pdf.getVal(aset))
   values=np.asarray(values);full=np.asarray(full);assert np.isfinite(full).all() and (full>=0).all();integral=float(np.trapz(full,fullgrid));assert abs(integral-1)<.002
   curves[(model,shift)]=values
   funcs={fn.GetName():fn.getVal() for fn in ws.allFunctions() if fn.GetName().endswith('_'+name) and (fn.GetName().startswith('mean_') or (fn.GetName().startswith('sigma_') and not fn.GetName().startswith('sigma_fit_')))}
   low=(grid>=mh-5)&(grid<=mh-2);high=(grid>=mh+2)&(grid<=mh+5)
   details[model]['scan'][str(shift)]={'norm':norm.getVal(),'full_integral':integral,'parameters':funcs,'low_window_probability':float(np.trapz(values[low],grid[low])),'high_window_probability':float(np.trapz(values[high],grid[high]))}
   for m,val in zip(grid,values):csvrows.append({'era':era,'model':model,'theta':shift,'mass':float(m),'pdf':float(val)})
  for shift in [-1,1]:
   nominal=details[model]['scan']['0'];varied=details[model]['scan'][str(shift)]
   varied['norm_relative_change']=varied['norm']/nominal['norm']-1
   varied['width_scale_ratios']={k:v/nominal['parameters'][k] for k,v in varied['parameters'].items() if k.startswith('sigma_')}
   varied['mean_shifts_GeV']={k:v-nominal['parameters'][k] for k,v in varied['parameters'].items() if k.startswith('mean_')}
  details[model]['up_down_density_nonlinearity_L1_110_140']=float(np.trapz(abs(curves[(model,1)]+curves[(model,-1)]-2*curves[(model,0)]),grid))
  f.Close()
 assert details['DCB']['dataset_entries']==details['SoG']['dataset_entries'];assert abs(details['DCB']['dataset_sumw']-details['SoG']['dataset_sumw'])<1e-12
 results[era]=details
 for tail in [False,True]:
  fig,axs=plt.subplots(2,2,figsize=(12,7),sharex=True,gridspec_kw={'height_ratios':[2,1]});limits=(110,140) if tail else (118,132);allratios=[];colors={-1:'tab:blue',0:'black',1:'tab:red'}
  for col,model in enumerate(['DCB','SoG']):
   p0=curves[(model,0)];mask=p0>1e-5*p0.max()
   for shift in [-1,0,1]:axs[0,col].plot(grid,curves[(model,shift)],color=colors[shift],label=f'Smearing theta={shift:+d}')
   for shift in [-1,1]:
    ratio=np.full_like(p0,np.nan);ratio[mask]=100*(curves[(model,shift)][mask]/p0[mask]-1);axs[1,col].plot(grid,ratio,color=colors[shift]);use=mask&(grid>=limits[0])&(grid<=limits[1]);allratios.extend(ratio[use])
   axs[0,col].set_title(f'{model}: nominal fit success={statuses[(era,model)]}');axs[0,col].set_ylabel('Normalized signal PDF [1/GeV]');axs[0,col].legend(fontsize=8);axs[1,col].set_ylabel('Change / nominal [%]');axs[1,col].set_xlabel('Diphoton mass [GeV]');axs[1,col].axhline(0,color='gray',lw=.8)
   for ax in axs[:,col]:ax.set_xlim(*limits);ax.grid(alpha=.2)
   if tail:axs[0,col].set_yscale('log');axs[0,col].set_ylim(1e-6,1.)
  low,high=min(allratios),max(allratios);pad=.05*max(high-low,1)
  for ax in axs[1]:ax.set_ylim(low-pad,high+pad)
  if not tail:
   peak=max(curves[(m,s)].max() for m in ['DCB','SoG'] for s in [-1,0,1])
   for ax in axs[0]:ax.set_ylim(0,1.1*peak)
  fig.suptitle(f'{proc} / {cat}, {era}, MH={mh}: only Smearing varied; other nuisances zero\nConditional PDF scan, no refit or likelihood profiling',fontsize=11);fig.tight_layout();stem=era+('_tails' if tail else '_peak');fig.savefig(out/(stem+'.png'),dpi=140);fig.savefig(out/(stem+'.pdf'));plt.close(fig)
 print('SCANNED',era,flush=True)
(out/'scan_results.json').write_text(json.dumps(results,indent=2))
with (out/'curves.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(csvrows[0]));w.writeheader();w.writerows(csvrows)
report='''# Smearing response of current DCB and SoG signal PDFs

This is a read-only scan of the latest packaged tth_in / ttH_had_1 model in each era, not a new fit or a profile-likelihood impact calculation. All photon nuisance values start at zero. MH is fixed to 125.09. Only CMS_hgg_nuisance_Smearing is assigned -2,-1,0,+1,+2 in memory; figures show -1,0,+1. A constant RooRealVar can still be assigned values with setVal; it need not be floated for this conditional evaluation. Its interpretation as ±1 standard deviation requires the downstream unit-Gaussian constraint prescription.

Normalized PDFs use RooFit's observable normalization set over the full mass range. The peak view is 118–132 and log-tail view 110–140. Ratio panels show 100*(PDF(theta)/PDF(0)-1), masking nominal density below 1e-5 of the peak to avoid ratios of numerically tiny tails. Means and widths are checked, along with total normalization and full-range integral; ±2 scans are stored in curves.csv and scan_results.json. Left/right window probabilities use [MH-5,MH-2] and [MH+2,MH+5]. No plotting pruning or summed-process weights are involved: this is one process/category PDF per era, matched between families.

The current source constructs photon responses in tools/finalModel.py:327–395. Widths are multiplied by max(0.01, 1+c_sigma*theta); mean and rate can also respond if the corresponding stored coefficients pass their inclusion thresholds. Inspect the measured parameter shifts below rather than assuming a pure width effect. DCB tail parameters and fractions and SoG component fractions are not directly changed by this nuisance. The six DCB parameters are not refitted for each theta.

A left/right asymmetric shape is different from an up/down nonlinear response. Even a single Gaussian changes nonlinearly with width, so the ±1 density changes need not be equal and opposite. A SoG with distinct means need not be symmetric about a common center. These PDFs therefore cannot establish a general rule that SoG impacts must be symmetric and DCB impacts asymmetric. Signal-strength impacts additionally depend on the background likelihood, normalization, constraints and profiling. Once datacards exist, the actual impact question requires the corresponding Combine fits. Full-range PDF integrals, measured responses and original fit success flags are recorded; some nominal production fits did not converge and their scans do not resolve that issue.

| Era | Peak scan | Tail scan | DCB nominal fit success | SoG nominal fit success |
|---|---|---|---|---|
'''
for era in eras:report+=f'| {era} | [PNG]({era}_peak.png) | [PNG]({era}_tails.png) | {statuses[(era,"DCB")]} | {statuses[(era,"SoG")]} |\n'
report+='\n## Measured ±1 responses\n\n'
for era in eras:
 for model in ['DCB','SoG']:
  d=results[era][model];u=d['scan']['1'];n=d['scan']['-1'];report+=f'- {era} {model}: width ratios +1={list(u["width_scale_ratios"].values())}, -1={list(n["width_scale_ratios"].values())}; maximum absolute mean shift={max([abs(v) for v in u["mean_shifts_GeV"].values()]+[abs(v) for v in n["mean_shifts_GeV"].values()]):.6g} GeV; relative rate shifts +1={u["norm_relative_change"]:.6g}, -1={n["norm_relative_change"]:.6g}.\n'
report+='\nInputs were opened READ; no workspace, nuisance constants, fit settings, datacard or source script was changed. All generated plots and scan tables are in this directory.\n'
(out/'README.md').write_text(report);print('COMPLETE: 8 PNG/PDF pairs, five-point scan tables.',flush=True)
