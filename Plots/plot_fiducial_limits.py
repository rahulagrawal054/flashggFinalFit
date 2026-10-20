#!/usr/bin/env python3
"""Expected 95% CLs strength-limit summaries using the five Combine quantiles."""
import argparse,pathlib,json,math,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Patch
from matplotlib.lines import Line2D
from matplotlib import ticker
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',required=True);p.add_argument('--label');p.add_argument('--include-tth-diagnostic',action='store_true',help='Also regenerate ttH/combined diagnostic plots in diagnostics/');a=p.parse_args();run=pathlib.Path(a.run_dir).resolve();out=run/'plots/limits';out.mkdir(parents=True,exist_ok=True)
selected=['r_ttH','r_tHq'] if a.include_tth_diagnostic else ['r_tHq']
diag=out/'diagnostics'
if a.include_tth_diagnostic:diag.mkdir(exist_ok=True)
info={};labels={'r_ttH':r'$\mu_{t\bar{t}H+tHW}$','r_tHq':r'$\mu_{tHq}$'}
for poi in selected:
 src=run/'limits'/poi/'total/profile_other/results.json';d=json.loads(src.read_text());assert d['poi']==poi and d['mode']=='limit';rows=d['rows'];assert len(rows)==5
 assert all(abs(r['quantile']-q)<.002 for r,q in zip(rows,[.025,.16,.5,.84,.975]))
 values=[r['value'] for r in rows];assert all(math.isfinite(x) and x>0 for x in values);assert values==sorted(values)
 info[poi]={'values':values,'provisional':bool(d.get('closure_warning_lines')),'warnings':d.get('closure_warning_lines',[]),'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
legend=[Line2D([0],[0],color='black',lw=2,linestyle='--',label='Median expected'),Patch(facecolor='#68c13f',label=r'Expected $\pm1\sigma$'),Patch(facecolor='#f5cf29',label=r'Expected $\pm2\sigma$'),Line2D([0],[0],color='0.45',lw=1.2,linestyle=':',label='SM strength = 1')]
def band(ax,poi,y):
 q0,q1,median,q3,q4=info[poi]['values'];ax.add_patch(Rectangle((q0,y-.19),q4-q0,.38,facecolor='#f5cf29',edgecolor='none'));ax.add_patch(Rectangle((q1,y-.19),q3-q1,.38,facecolor='#68c13f',edgecolor='none'));ax.vlines(median,y-.23,y+.23,color='black',lw=2,linestyle='--');ax.text(median,y+.28,f'{median:.3f}',ha='center',va='bottom',fontsize=12)
def decorate(ax):
 ax.axvline(1,color='.45',ls=':',lw=1.2,zorder=0);ax.tick_params(axis='x',which='both',direction='out',top=False,bottom=True,labelsize=11,pad=5);ax.tick_params(axis='y',which='both',left=False,right=False,pad=10);ax.set_xlabel(r'95% CLs upper limit on signal strength $\mu$',fontsize=12,labelpad=10);ax.spines[['top','right']].set_visible(False)
if a.include_tth_diagnostic:
 fig,ax=plt.subplots(figsize=(8.8,5.6));fig.subplots_adjust(left=.24,right=.96,bottom=.25,top=.72)
 for poi,y in [('r_ttH',1),('r_tHq',0)]:band(ax,poi,y)
 ax.set_yticks([1,0],[labels['r_ttH']+(' *' if info['r_ttH']['provisional'] else ''),labels['r_tHq']+(' *' if info['r_tHq']['provisional'] else '')],fontsize=16);ax.set_ylim(-.55,1.55);ax.set_xscale('log');ax.set_xlim(min(v['values'][0] for v in info.values())*.65,max(v['values'][-1] for v in info.values())*1.45);decorate(ax)
 lo,hi=ax.get_xlim();ticks=[x for x in [.2,.3,.5,1,2,3,5,10,20,30,50,100] if lo<=x<=hi];ax.xaxis.set_major_locator(ticker.FixedLocator(ticks));ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x,pos:f'{x:g}'));ax.xaxis.set_minor_locator(ticker.NullLocator());ax.set_xlabel(r'95% CLs upper limit on signal strength $\mu$ (log scale)',fontsize=12,labelpad=10);ax.grid(axis='x',color='0.9',lw=.6,zorder=0)
 fig.text(.24,.95,'CMS',fontsize=20,fontweight='bold');fig.text(.33,.95,'Private work',fontsize=15,fontstyle='italic');fig.text(.96,.95,a.label or run.name,ha='right',fontsize=13);fig.text(.24,.89,'Expected limits · target-zero reference',fontsize=13);fig.legend(handles=legend,loc='upper left',bbox_to_anchor=(.23,.86),ncol=2,frameon=False,fontsize=10)
 fig.text(.24,.09,'Other signal strength profiled; no observed-data limit shown.',fontsize=10)
 if any(v['provisional'] for v in info.values()):fig.text(.24,.045,'* Provisional: auxiliary-Asimov closure warning requires review.',fontsize=10,color='#a12622')
 for ext in ['png','pdf']:fig.savefig(diag/f'expected_limits.{ext}',dpi=180,bbox_inches='tight',pad_inches=.15)
 plt.close(fig)

for poi in selected:
 fig,ax=plt.subplots(figsize=(8.0,4.2));fig.subplots_adjust(left=.22,right=.96,bottom=.30,top=.62);band(ax,poi,0);ax.set_xlim(0,info[poi]['values'][-1]*1.18);ax.set_ylim(-.5,.65);ax.set_yticks([0],[labels[poi]],fontsize=15);decorate(ax)
 ticks=ticker.MaxNLocator(nbins=5,steps=[1,2,2.5,5,10]).tick_values(0,info[poi]['values'][-1]*1.08);ax.set_xlim(0,ticks[-1]);ax.xaxis.set_major_locator(ticker.FixedLocator(ticks));ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x,pos:f'{x:g}'));ax.xaxis.set_minor_locator(ticker.NullLocator());ax.grid(axis='x',color='0.92',lw=.6,zorder=0)
 fig.text(.22,.93,'CMS',fontsize=20,fontweight='bold');fig.text(.37,.93,'Private work',fontsize=15,fontstyle='italic');fig.text(.96,.93,a.label or run.name,ha='right',fontsize=13);fig.text(.22,.84,'Expected limits · target-zero reference',fontsize=12);fig.legend(handles=legend,loc='upper left',bbox_to_anchor=(.21,.79),ncol=2,frameon=False,fontsize=9)
 fig.text(.22,.075,'Other signal strength profiled; bands describe expected upper limits.',fontsize=9)
 if info[poi]['provisional']:fig.text(.22,.025,'Provisional: auxiliary-Asimov closure warning requires review.',fontsize=9,color='#a12622')
 for ext in ['png','pdf']:fig.savefig((diag if poi=='r_ttH' else out)/f'{poi}.{ext}',dpi=180,bbox_inches='tight',pad_inches=.15)
 plt.close(fig)
for ext in ['png','pdf']:__import__('shutil').copy2(out/f'r_tHq.{ext}',out/f'expected_limits.{ext}')
(out/'plot_inputs.json').write_text(json.dumps({'inputs':info,'band_meaning':'Expected upper-limit quantiles at 2.5%, 16%, 50%, 84%, 97.5%; approximately +/-2sigma and +/-1sigma. Not measurement errors or significance intervals.','data_definition':'Target-zero auxiliary reference with the other strength profiled; input SM Asimov used for conditional calibration; no observed-data limit.'},indent=2)+'\n');print('Expected-limit plots saved:',out)
