#!/usr/bin/env python3
"""Nominal expected yields from current Combine normalization functions, after card pruning."""
import argparse,pathlib,json,csv,math,re
import ROOT
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--workspace',required=True);p.add_argument('--outdir',required=True);p.add_argument('--mass',type=float,default=125.09);a=p.parse_args()
out=pathlib.Path(a.outdir).resolve();assert not out.exists();out.mkdir(parents=True)
f=ROOT.TFile.Open(str(pathlib.Path(a.workspace).resolve()),'READ');assert f and not f.IsZombie();w=f.Get('w');assert w
mc=w.obj('ModelConfig');assert mc
for n in mc.GetNuisanceParameters():
 if n.InheritsFrom('RooRealVar') and not n.GetName().startswith(('shapeBkg','env_pdf')):n.setVal(0)
for name in ['r_ttH','r_tHq']:assert w.var(name);w.var(name).setVal(1)
w.var('MH').setVal(a.mass)
def family(proc):
 p=proc.lower()
 for token,label in [('tth','ttH'),('thq','tHq'),('thw','tHW'),('ggh','ggH'),('vbf','VBF'),('qqh','VBF'),('vh','VH'),('wh','VH'),('zh','VH'),('bbh','bbH')]:
  if token in p:return label
 raise ValueError('Unknown process '+proc)
rows=[]
for fun in w.allFunctions():
 name=fun.GetName()
 if not name.startswith('n_exp_final_bin') or '_proc_' not in name:continue
 cat,proc=name[len('n_exp_final_bin'):].split('_proc_',1)
 if proc=='bkg_mass':continue
 value=float(fun.getVal());assert math.isfinite(value) and value>=0,(name,value)
 assert '_in_' in proc or '_out_' in proc,proc
 rows.append(dict(cat=cat,proc=proc,production=family(proc),region='in' if '_in_' in proc else 'out',yield_events=value))
assert len(rows)==563,len(rows)
df=pd.DataFrame(rows);df.to_csv(out/'workspace_yields.csv',index=False)
cats=[f'ttH_had_{i}' for i in range(1,5)]+[f'ttH_lep_{i}' for i in range(1,5)]+[f'tH_had_{i}' for i in range(1,5)]+['tH_lep_1','tH_lep_2','bkg_had','bkg_lep'];assert set(df.cat)==set(cats)
x=w.var('CMS_hgg_mass');x.setVal(a.mass);obs=ROOT.RooArgSet(x);bkg={}
for cat in cats:
 norm=w.function(f'n_exp_final_bin{cat}_proc_bkg_mass');pdf=w.pdf(f'shapeBkg_bkg_mass_{cat}');assert norm and pdf,cat
 bkg[cat]=float(norm.getVal()*pdf.getVal(obs));assert math.isfinite(bkg[cat])
def escape(s):return s.replace('_',r'\_').replace('%',r'\%').replace('&',r'\&')
def render(name,table,title,note):
 table.to_csv(out/f'{name}.csv')
 display=table.copy().applymap(lambda v:f'{v:.3f}')
 latex=[r'\documentclass[10pt]{article}',r'\usepackage[landscape,margin=1cm]{geometry}',r'\usepackage{graphicx}',r'\begin{document}',r'\thispagestyle{empty}',r'\begin{center}',r'\textbf{'+escape(title)+r'}\\[1em]',r'\resizebox{\textwidth}{!}{%',r'\begin{tabular}{l'+'r'*len(table.columns)+'}',r'\hline','Category & '+' & '.join(escape(c) for c in table.columns)+r' \\',r'\hline']
 for index,row in display.iterrows():latex.append(escape(str(index))+' & '+' & '.join(row)+r' \\')
 latex.extend([r'\hline',r'\end{tabular}}',r'\\[1em]',escape(note),r'\end{center}',r'\end{document}']);(out/f'{name}.tex').write_text('\n'.join(latex)+'\n')
 fig,ax=plt.subplots(figsize=(16,8));ax.axis('off');ax.set_title('CMS Private work — '+title,fontsize=13,pad=18)
 tab=ax.table(cellText=display.values,rowLabels=display.index,colLabels=display.columns,loc='center',cellLoc='right');tab.auto_set_font_size(False);tab.set_fontsize(9);tab.scale(1,1.65)
 for (i,j),cell in tab.get_celld().items():
  if i==0 or i==len(display):cell.set_facecolor('#d9e5f0');cell.set_text_props(weight='bold')
  elif i%2==0:cell.set_facecolor('#f1f3f5')
 fig.text(.04,.04,note,fontsize=9);fig.subplots_adjust(left=.13,right=.98,top=.88,bottom=.10)
 for ext in ['pdf','png']:fig.savefig(out/f'{name}.{ext}',dpi=200,bbox_inches='tight')
 plt.close(fig)
productions=['ttH','tHq','tHW','ggH','VBF','VH','bbH']
for region in ['all','in','out']:
 subset=df if region=='all' else df[df.region==region]
 t=subset.pivot_table(index='cat',columns='production',values='yield_events',aggfunc='sum',fill_value=0).reindex(index=cats,columns=productions,fill_value=0);t.insert(0,'Total Higgs',t.sum(axis=1));t.loc['Total']=t.sum();t['Bkg / GeV at MH']=[bkg[c] for c in cats]+[sum(bkg.values())]
 render('yield_table_'+region,t,f'DCB nominal yields, {region}, MH = {a.mass:g} GeV','Four eras combined; strengths = 1, constrained nuisances = 0; after 0.1% card pruning. Higgs yields: events over 100–180 GeV. Bkg: continuum density, not events in the full mass range.')
 def grouped(row):
  if row.production in ['ttH','tHW']:return 'ttH+tHW '+row.region
  if row.production=='tHq':return 'tHq '+row.region
  return row.production
# Group signal POIs with in/out separated, Higgs backgrounds inclusive.
df['group']=df.apply(grouped,axis=1)
order=['ttH+tHW in','tHq in','ttH+tHW out','tHq out','ggH','VBF','VH','bbH']
t=df.pivot_table(index='cat',columns='group',values='yield_events',aggfunc='sum',fill_value=0).reindex(index=cats,columns=order,fill_value=0);t.insert(0,'Total Higgs',t.sum(axis=1));t.loc['Total']=t.sum()
render('yield_table_grouped',t,f'DCB nominal grouped yields, MH = {a.mass:g} GeV','Four eras combined; expected events after card pruning; ttH+tHW share r_ttH, tHq uses r_tHq. All strengths = 1. No observed data counts.')
# Percentage denominator: all retained Higgs production in this category.
def percentages(table):
 result=table.copy()
 total=result['Total Higgs'].copy()
 for column in result.columns:
  if column!='Total Higgs':result[column+' (%)']=100*result[column]/total
 result=result[['Total Higgs']+[c+' (%)' for c in table.columns if c!='Total Higgs']]
 return result
render('yield_table_grouped_percent',percentages(t),f'DCB process composition, MH = {a.mass:g} GeV','Total Higgs is an event count; every other column is percent of that row total. Four eras combined, after card pruning. No continuum background in the denominator.')
for region in ['all','in','out']:
 subset=df if region=='all' else df[df.region==region]
 production_table=subset.pivot_table(index='cat',columns='production',values='yield_events',aggfunc='sum',fill_value=0).reindex(index=cats,columns=productions,fill_value=0)
 production_table.insert(0,'Total Higgs',production_table.sum(axis=1));production_table.loc['Total']=production_table.sum()
 render('yield_table_'+region+'_percent',percentages(production_table),f'DCB {region} production fractions, MH = {a.mass:g} GeV','Total Higgs is an event count; process columns are percentages of that row total within the selected in/out/all region. Total row uses yield-weighted fractions.')
compact=df.copy()
compact['component']=compact.production.map(lambda name:'ttH+tHW' if name in ['ttH','tHW'] else ('tHq' if name=='tHq' else 'Resonant Higgs bkg'))
compact_table=compact.pivot_table(index='cat',columns='component',values='yield_events',aggfunc='sum',fill_value=0).reindex(index=cats,columns=['ttH+tHW','tHq','Resonant Higgs bkg'],fill_value=0)
compact_table.insert(0,'Total Higgs',compact_table.sum(axis=1));compact_table.loc['Total']=compact_table.sum()
render('yield_table_three_components',compact_table,f'DCB three Higgs components, MH = {a.mass:g} GeV','Expected events, in+out and all four eras combined. Resonant Higgs bkg = ggH+VBF+VH+bbH; excludes continuum background. Nominal strengths = 1, after pruning.')
render('yield_table_three_components_percent',percentages(compact_table),f'DCB three-component fractions, MH = {a.mass:g} GeV','Total Higgs is an event count; the three components are percent of that row total. Resonant Higgs bkg = ggH+VBF+VH+bbH, excludes continuum. In+out included.')
summary={'workspace':str(pathlib.Path(a.workspace).resolve()),'mass':a.mass,'normalization_functions':len(df),'categories':len(cats),'total_higgs_events':float(df.yield_events.sum()),'poi_values':{'r_ttH':1,'r_tHq':1},'nuisances':'constrained real nuisances set to zero; background parameters/index values retained from input workspace','pruning':'current card retained contributions only','background_density':bkg,'background_note':'Input workspace background model settings, not an observed global fit. Density at MH, not full-range count.','rendering':'standalone TeX source; PDF/PNG tables rendered by matplotlib from the same numerical dataframe'}
(out/'inputs.json').write_text(json.dumps(summary,indent=2)+'\n');f.Close();print(json.dumps(summary,indent=2))
