"""Reproduce the current, qualified DCB/SoG comparison from saved fit outputs."""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
COMBINE=OUT.parent.parent/'Combine'
impact_paths={'DCB':COMBINE/'DCB/impacts/collected_20261017/impacts.json','SoG':COMBINE/'SoG/impacts/collected_auto/impacts.json'}
summary_paths={'DCB':COMBINE/'DCB/plots/scans/custom/summary.json','SoG':COMBINE/'SoG/plots/scans/refined/custom/summary.json'}
impacts={k:json.loads(v.read_text()) for k,v in impact_paths.items()}
summaries={k:json.loads(v.read_text()) for k,v in summary_paths.items()}
records={}
for model in impacts:
 records[model]={'pois':{},'snapshot_validation':json.loads((COMBINE/model/'snapshot/validation.json').read_text())}
 assert len(impacts[model]['params'])==91
 for poi in ('r_ttH','r_tHq'):
  ps=sorted(impacts[model]['params'],key=lambda e:e['impact_'+poi],reverse=True)
  smear=next(e for e in ps if e['name']=='CMS_hgg_nuisance_Smearing');v=smear[poi]
  total=summaries[model]['pois'][poi]['total'];stat=summaries[model]['pois'][poi]['statOnly']
  z=json.loads((COMBINE/model/'significance'/poi/'total/profile_other/results.json').read_text())
  records[model]['pois'][poi]={'best_fit':total['best_fit'],'total68':total['crossings']['1'],'stat68':stat['crossings']['1'],
   'smearing_down':v[0]-v[1],'smearing_up':v[2]-v[1],'smearing_rank':ps.index(smear)+1,'smearing_nuisance_fit':smear['fit'],
   'expected_Z':z['expected_local_Z']}
 records[model]['tHq_limit']=json.loads((COMBINE/model/'limits/r_tHq/total/profile_other/results.json').read_text())['expected_median_95CLs']
records['qualification']='Separate model-generated Asimov datasets; DCB and SoG grids differ. Raw likelihood curves are not recentered or smoothed. Snapshot fit statuses/covariance and internal fit warnings remain. This is not a calibrated signal-PDF goodness-of-fit test or an explanation of historical changes.'
(OUT/'combine_comparison.json').write_text(json.dumps(records,indent=2)+'\n')
# Compare raw likelihoods on their common displayed domain; never bridge invalid points.
fig,axes=plt.subplots(1,2,figsize=(11,4.3))
for ax,poi,xlim,label in zip(axes,('r_ttH','r_tHq'),((0,2.5),(-8,15)),(r'$r_{ttH}$',r'$r_{tHq}$')):
 for model,color in [('DCB','#175caa'),('SoG','#d66b0b')]:
  mode='profile_other__refined' if model=='SoG' else 'profile_other'
  for scenario,style in [('total','-'),('statOnly','--')]:
   p=COMBINE/model/'scans'/poi/scenario/mode/'points.csv'
   rows=[{k:float(v) for k,v in r.items()} for r in csv.DictReader(p.open())]
   rows=sorted([r for r in rows if r['quantileExpected']>=0],key=lambda r:r['poi'])
   idx=np.array([i for i,r in enumerate(rows) if np.isfinite(r['deltaNLL']) and -.001<=r['deltaNLL']<999])
   for j,group in enumerate(np.split(idx,np.where(np.diff(idx)>1)[0]+1)):
    ax.plot([rows[i]['poi'] for i in group],[2*rows[i]['deltaNLL'] for i in group],color=color,ls=style,lw=1.7,label=f'{model}: '+('total' if scenario=='total' else 'stat only') if j==0 else None)
 for q in [1,3.841458820694124]:ax.axhline(q,color='0.6',lw=.8,ls=':')
 ax.set(xlim=xlim,ylim=(0,8),xlabel=label,ylabel=r'$2\Delta\mathrm{NLL}$')
 ax.legend(fontsize=8);ax.grid(alpha=.15)
fig.suptitle('DCB+Gaussian versus SoG: expected profile scans',fontsize=13)
fig.text(.5,.015,'Other strength profiled; separate Asimov datasets. Snapshot warnings retained. No smoothing or recentering.',ha='center',fontsize=8)
fig.tight_layout(rect=(0,.04,1,.94))
for ext in ['png','pdf']:fig.savefig(OUT/f'combine_scan_comparison.{ext}',dpi=180)
plt.close(fig)
# Postfit nuisance +/-1sigma endpoints, not bare theta +/-1 conditional PDF scans.
fig,axes=plt.subplots(1,2,figsize=(10,3.6))
for ax,poi in zip(axes,('r_ttH','r_tHq')):
 for y,model,color in [(1,'DCB','#175caa'),(0,'SoG','#d66b0b')]:
  r=records[model]['pois'][poi]
  ax.barh(y+.12,r['smearing_down'],height=.2,color=color,alpha=.55)
  ax.barh(y-.12,r['smearing_up'],height=.2,color=color)
 ax.axvline(0,color='black',lw=.8)
 ax.set_yticks([1,0],[f"DCB (rank {records['DCB']['pois'][poi]['smearing_rank']})",f"SoG (rank {records['SoG']['pois'][poi]['smearing_rank']})"])
 ax.set_xlabel('Shift in '+(r'$r_{ttH}$' if poi=='r_ttH' else r'$r_{tHq}$'));ax.grid(axis='x',alpha=.2)
fig.suptitle('Photon smearing: profiled signal-strength impacts',fontsize=13)
fig.text(.5,.01,'Lighter: lower nuisance endpoint; darker: upper. Separate Asimov datasets; snapshot warnings retained.',ha='center',fontsize=8)
fig.tight_layout(rect=(0,.05,1,.92))
for ext in ['png','pdf']:fig.savefig(OUT/f'smearing_impact_comparison.{ext}',dpi=180)
plt.close(fig)
rows=[]
for poi in ('r_ttH','r_tHq'):
 for model in ('DCB','SoG'):
  r=records[model]['pois'][poi]
  label=poi.replace('_', chr(92)+'_')
  rows.append(f"{label} & {model} & {r['smearing_down']:+.4f} & {r['smearing_up']:+.4f} & {r['smearing_rank']} " + chr(92)*2)
# Explicit row endings avoid shell escaping and keep generated TeX reviewable.
metrics=[]
for model in ('DCB','SoG'):
 a=records[model]['pois']['r_ttH'];b=records[model]['pois']['r_tHq']
 metrics.append(f"{model} & [{a['total68'][0]:.3f}, {a['total68'][1]:.3f}] & [{b['total68'][0]:.3f}, {b['total68'][1]:.3f}] & {a['expected_Z']:.3f} & {records[model]['tHq_limit']:.3f} "+'\\\\')
block=r'''
% BEGIN CURRENT COMBINE COMPARISON
\begin{frame}{Current impacts: smearing is fourth for ttH in both families}
\begin{center}\small
\begin{tabular}{llrrr}\toprule
POI & Model & Lower-endpoint shift & Upper-endpoint shift & Rank\\\midrule
IMPACTROWS
\bottomrule\end{tabular}\end{center}
\begin{center}\includegraphics[width=0.87\linewidth,height=0.40\textheight,keepaspectratio]{smearing_impact_comparison.png}\end{center}
\small Both ttH impacts are nearly symmetric; DCB is modestly larger. This result does not support a general rule that SoG impacts must be symmetric and DCB impacts asymmetric.
\vfill\tiny All 91 constrained nuisances collected in each model, other strength profiled. Endpoints use fitted nuisance intervals, not the bare conditional shape scan. Original JSON values retained; no nuisance removal or recentering.
\end{frame}
\begin{frame}{Expected profile scans: very similar over the relevant intervals}
\begin{center}\includegraphics[width=\linewidth,height=0.75\textheight,keepaspectratio]{combine_scan_comparison.png}\end{center}
\small Solid: total uncertainties. Dashed: stat only. Raw likelihoods; invalid DCB tail points omitted without bridging gaps. SoG refined scans have no invalid grid points.
\vfill\tiny Displayed ranges overlap; scan grids differ. Each family uses its own saved SM-injected Asimov. Snapshot status/covariance warnings remain; these are provisional expected comparisons, not a common-dataset closure test.
\end{frame}
\begin{frame}{Numerical comparison and what it establishes}
\begin{center}\small
\begin{tabular}{lcccc}\toprule
Model & ttH total 68\% interval & tHq total 68\% interval & ttH $Z$ & tHq median limit\\\midrule
METRICROWS
\bottomrule\end{tabular}\end{center}
\begin{itemize}
\item Expected POI intervals, significances and the reported tHq upper limit are nearly unchanged. The limit is a dimensionless strength, at 95\% CLs.
\item Smearing is fourth for ttH in both models. Its smaller SoG impact does not by itself select the preferred signal PDF.
\item Base PDF choice on signal-MC agreement and stability. The shown SoG shape failures and DCB counterexamples need component-level review.
\item Remaining qualifications: DCB snapshot status 1/covariance 2; SoG status 3/covariance 3. Both best fits are near $(1.042,1.020)$, rather than exact closure at $(1,1)$.
\item These are matched-workflow, separate-Asimov results. A shared reference dataset is still needed to isolate the fitted-family effect; the cause of the historical DCB impact change is not established.
\end{itemize}
\vfill\tiny Sources: Combine/DCB and Combine/SoG saved scan summaries, significance/limit results and collected impacts; reproducible table inputs in combine\_comparison.json.
\end{frame}
% END CURRENT COMBINE COMPARISON
'''.replace('IMPACTROWS','\n'.join(rows)).replace('METRICROWS','\n'.join(metrics))
p=OUT/'signal_model_comparison.tex';s=p.read_text()
if '% BEGIN CURRENT COMBINE COMPARISON' in s:
 s=s.split('% BEGIN CURRENT COMBINE COMPARISON')[0]+'\\end{document}\n'
s=s.replace('Smearing impact: verified change, matched SoG comparison pending','Historical DCB change: a separate question')
s=s.replace(r'\textbf{Pending:} matched SoG scans/impacts and a controlled explanation of the historical change.',r'\textbf{Update:} current SoG results follow. A controlled explanation of the historical DCB change remains pending.')
s=s.replace('\\end{document}',block+'\n\\end{document}')
p.write_text(s)
print('Wrote comparison figures, numeric JSON and updated slides.')
