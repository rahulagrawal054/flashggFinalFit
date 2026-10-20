#!/usr/bin/env python3
"""Compact slide tables: expected events with row percentages in parentheses."""
import argparse,pathlib,json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input-dir',required=True);p.add_argument('--output-name',default='slide_tables');a=p.parse_args();src=pathlib.Path(a.input_dir).resolve();out=src/a.output_name;out.mkdir(exist_ok=False)
def esc(s):return str(s).replace('_',r'\_').replace('%',r'\%').replace('&',r'\&')
stems=['three_components','all','in','out','grouped']
for region in ['incl','in','out']:
 source=src/('yield_table_all.csv' if region=='incl' else f'yield_table_{region}.csv')
 raw=pd.read_csv(source,index_col=0)
 compact=pd.DataFrame(index=raw.index)
 compact['Total Higgs']=raw['Total Higgs']
 compact['ttH+tHW']=raw['ttH']+raw['tHW']
 compact['tHq']=raw['tHq']
 compact['Resonant Higgs bkg']=raw[['ggH','VBF','VH','bbH']].sum(axis=1)
 assert abs(compact[['ttH+tHW','tHq','Resonant Higgs bkg']].sum(axis=1)-compact['Total Higgs']).max()<1e-8
 stem='three_components_'+region
 compact.to_csv(src/f'yield_table_{stem}.csv');stems.append(stem)
for stem in stems:
 df=pd.read_csv(src/f'yield_table_{stem}.csv',index_col=0);columns=[c for c in df.columns if c!='Bkg / GeV at MH'];df=df[columns];assert (df['Total Higgs']>0).all()
 show=pd.DataFrame(index=df.index);show['Total']=df['Total Higgs'].map(lambda v:f'{v:.2f}')
 for col in columns:
  if col=='Total Higgs':continue
  show[col]=[f'{v:.2f} ({100*v/t:.1f}%)' for v,t in zip(df[col],df['Total Higgs'])]
 show=show.rename(columns={'Resonant Higgs bkg':'Res. Higgs bkg'})
 show.to_csv(out/f'{stem}_counts_percent.csv')
 # No stretched cells: size follows the number of columns and rows.
 width=2.0+1.65*len(show.columns);height=.31*(len(show)+1)+.8
 fig,ax=plt.subplots(figsize=(width,height));ax.axis('off')
 table=ax.table(cellText=show.values,rowLabels=show.index,colLabels=show.columns,loc='center',cellLoc='center',bbox=[.12,.065,.88,.86])
 table.auto_set_font_size(False);table.set_fontsize(9)
 for (i,j),cell in table.get_celld().items():
  cell.PAD=.035;cell.set_linewidth(.45);cell.set_edgecolor('#777777')
  if i==0 or i==len(show):cell.set_facecolor('#dce6ee');cell.set_text_props(weight='bold')
  elif i%2==0:cell.set_facecolor('#f3f5f7')
 ax.text(0,1,'DCB · '+stem.replace('_',' ')+' · nominal expected yields',transform=ax.transAxes,fontsize=10,weight='bold',va='top')
 fig.text(.02,.015,'Entries: events (row % within selected region). incl = in+out. Four eras; MH = 125.09 GeV; after pruning.',fontsize=8)
 fig.subplots_adjust(left=.01,right=.995,top=.98,bottom=.035)
 for ext in ['png','pdf']:fig.savefig(out/f'{stem}_counts_percent.{ext}',dpi=220,bbox_inches='tight',pad_inches=.035)
 plt.close(fig)
 lines=[r'\documentclass[9pt]{article}',r'\usepackage[landscape,margin=5mm]{geometry}',r'\usepackage{graphicx}',r'\begin{document}',r'\thispagestyle{empty}',r'\setlength{\tabcolsep}{3pt}',r'\renewcommand{\arraystretch}{1.05}',r'\begin{center}',r'\resizebox{\textwidth}{!}{\begin{tabular}{l'+'r'*len(show.columns)+'}',r'\hline','Category & '+' & '.join(esc(x) for x in show.columns)+r' \\',r'\hline']
 for idx,row in show.iterrows():lines.append(esc(idx)+' & '+' & '.join(esc(v) for v in row)+r' \\')
 lines += [r'\hline',r'\end{tabular}}',r'\\ Entries: expected events (row percentage); total column: events.',r'\end{center}',r'\end{document}'];(out/f'{stem}_counts_percent.tex').write_text('\n'.join(lines)+'\n')
print('Saved compact slide tables:',out)
