"""Compare completed postfit-regenerated scans with preserved production scans."""
from pathlib import Path
import csv,json,math,re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
BASE=HERE.parent.parent/'Combine'
report={}
fig,axes=plt.subplots(2,2,figsize=(11.8,7.2))
for row,model in enumerate(['DCB','SoG']):
 root=BASE/model/'postfit_asimov_test';manifest=json.loads((root/'manifest.json').read_text())
 assert manifest.get('complete') and manifest['original_dataset']['data_sha256']!=manifest['new_dataset']['data_sha256']
 old=json.loads((BASE/model/('plots/scans/custom/summary.json' if model=='DCB' else 'plots/scans/refined/custom/summary.json')).read_text())
 report[model]={'dataset':{k:manifest[k] for k in ['original_dataset','new_dataset']},'scans':{}}
 for col,poi in enumerate(['r_ttH','r_tHq']):
  ax=axes[row,col]
  for scenario,style in [('total','-'),('statOnly','--')]:
   stage=root/'scans'/poi/scenario
   raw=list(csv.DictReader((stage/'points.csv').open()))
   assert len(raw)==301
   best=[r for r in raw if float(r['quantileExpected'])<0];assert len(best)==1
   grid=sorted([(float(r[poi]),2*float(r['deltaNLL'])) for r in raw if float(r['quantileExpected'])>=0])
   assert len(grid)==300 and all(math.isfinite(y) and -.002<=y<1998 for x,y in grid)
   bf=float(best[0][poi])
   def interval(level):
    crosses=[]
    for (x,y),(xx,yy) in zip(grid,grid[1:]):
     if (y-level)*(yy-level)<=0 and yy!=y:crosses.append(x+(level-y)*(xx-x)/(yy-y))
    left=[x for x in crosses if x<bf];right=[x for x in crosses if x>bf]
    return [max(left) if left else None,min(right) if right else None]
   new={'best_fit':bf,'interval68':interval(1),'interval95':interval(3.841458820694124),'grid_points':300,'minimum_grid_deltaNLL':min(y/2 for x,y in grid)}
   prior=old['pois'][poi][scenario]
   log=stage/'run.log';counts={'nonzero_minimizer_messages':0,'boundary_warning_messages':0}
   with log.open(errors='replace') as h:
    for line in h:
     if re.search(r'(?:status\s*=\s*|Status\s*:\s*)[1-9]',line):counts['nonzero_minimizer_messages']+=1
     if '[WARNING]' in line and ('boundary' in line or 'boundaries' in line):counts['boundary_warning_messages']+=1
   new.update(counts)
   entry={'original':{'best_fit':prior['best_fit'],'interval68':prior['crossings']['1']},'regenerated':new}
   oldwidth=prior['crossings']['1'][1]-prior['crossings']['1'][0]
   newwidth=new['interval68'][1]-new['interval68'][0]
   entry['width68_change_percent']=100*(newwidth/oldwidth-1)
   report[model]['scans'][poi+'_'+scenario]=entry
   label='Stat only' if scenario=='statOnly' else 'Total'
   ax.plot(*zip(*grid),color='#d4660d',ls=style,lw=1.6,label='Regenerated: '+label)
   mode='profile_other' if model=='DCB' else 'profile_other__refined'
   oldrows=list(csv.DictReader((BASE/model/'scans'/poi/scenario/mode/'points.csv').open()))
   oldgrid=sorted([(float(r['poi']),2*float(r['deltaNLL'])) for r in oldrows if float(r['quantileExpected'])>=0])
   # Insert NaN for invalid values: do not draw across missing/failed points.
   ax.plot([x for x,y in oldgrid],[y if math.isfinite(y) and -.002<=y<1998 else float('nan') for x,y in oldgrid],color='#175caa',ls=style,lw=1.4,label='Original: '+label)
  ax.axvline(1,color='0.5',ls=':',lw=.9)
  for q in [1,3.841458820694124]:ax.axhline(q,color='0.6',ls=':',lw=.7)
  ax.set(title=model,xlabel=r'$r_{ttH}$' if poi=='r_ttH' else r'$r_{tHq}$',ylabel=r'$2\Delta\mathrm{NLL}$',xlim=(0,2.5) if poi=='r_ttH' else (-8,15),ylim=(0,6))
  ax.legend(fontsize=7,loc='upper right');ax.grid(alpha=.12)
report['qualification']='Raw likelihoods; linear crossing interpolation; no smoothing or recentering. 300 valid grid points per new scan; internal minimizer/boundary warnings remain. Different expected datasets, source-snapshot stat-only freeze anchor. Not a calibrated PDF goodness-of-fit test.'
(HERE/'postfit_asimov_comparison.json').write_text(json.dumps(report,indent=2)+'\n')
fig.suptitle('CMS Private work | Original vs postfit-regenerated Asimov data',fontsize=14)
fig.text(.5,.012,'Other POI and background envelope profiled; raw curves. Dashed: stat only. Each signal family has its own datasets.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.035,1,.95))
for ext in ['png','pdf']:fig.savefig(HERE/f'postfit_asimov_comparison.{ext}',dpi=180)
lines=[]
for model in ['DCB','SoG']:
 for poi in ['r_ttH','r_tHq']:
  for sc in ['total','statOnly']:
   r=report[model]['scans'][poi+'_'+sc];a=r['original'];b=r['regenerated']
   lines.append(f"{model} & "+('ttH' if poi=='r_ttH' else 'tHq')+' & '+('Stat only' if sc=='statOnly' else 'Total')+f" & {a['best_fit']:.4f} & {b['best_fit']:.4f} & [{b['interval68'][0]:.3f}, {b['interval68'][1]:.3f}] & {r['width68_change_percent']:+.2f}\\% "+r'\\')
tex=r'''\begin{frame}{Postfit-regenerated Asimov test: all eight scans completed}
\begin{center}\includegraphics[width=.97\linewidth,height=.68\textheight,keepaspectratio]{postfit_asimov_comparison.png}\end{center}
\small Orange: new postfit-conditioned data. Blue: original saved data. Solid: total; dashed: stat only. Raw curves; no smoothing or recentering.
\vfill\tiny Each new scan has 300 finite grid points plus one fit-reference row. The same new dataset is reused within each family's four scans; DCB/SoG datasets are separate. Original DCB grids have invalid far-tail points omitted without bridging gaps.
\end{frame}
\begin{frame}{Regeneration restores near-unity best fits; widths barely change}
\begin{center}\scriptsize\renewcommand{\arraystretch}{1.15}\setlength{\tabcolsep}{5pt}
\begin{tabular}{lllrrrr}\toprule
Model & POI & Scenario & Original best fit & New best fit & New 68\% interval & Width change\\\midrule
ROWS
\bottomrule\end{tabular}\end{center}
\begin{itemize}
\item The expected data changed: both models' dataset hashes differ from their originals. Resetting strengths alone while reusing the old data would not do this.
\item DCB and SoG remain very similar. Near-unity best fits are consistent with generation from the loaded postfit background settings; this is not an independent PDF goodness-of-fit test.
\item No invalid new grid points, but internal minimizer/boundary messages remain. Tiny negative grid $\Delta\mathrm{NLL}$ values (up to about $1.5\times10^{-4}$ in magnitude) indicate finite minimization precision. Source-snapshot warnings are retained.
\end{itemize}
\vfill\tiny Stat-only freezes constrained nuisances at the source snapshot; background parameters/indices and other POI remain profiled. Intervals use raw $2\Delta\mathrm{NLL}=1$ crossings with linear interpolation. Width changes compare with original grids, whose spacings differ.
\end{frame}
'''.replace('ROWS','\n'.join(lines))
(HERE/'postfit_asimov_results.tex').write_text(tex)
for m in ['DCB','SoG']:
 for k,v in report[m]['scans'].items():print(m,k,json.dumps(v))
