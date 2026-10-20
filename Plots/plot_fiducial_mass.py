#!/usr/bin/env python3
"""Plot saved Asimov weights and bin-integrated post-fit mass models; never reads data_obs."""
import argparse, pathlib, json, csv, math
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--run-dir',required=True)
p.add_argument('--output-dir',required=True)
p.add_argument('--bins',type=int,default=80)
p.add_argument('--category',default='all')
a=p.parse_args();run=pathlib.Path(a.run_dir).resolve();out=pathlib.Path(a.output_dir).resolve()
assert a.bins>0 and not out.exists(),'Choose a new output directory and positive bin count'
validation=json.loads((run/'snapshot/validation.json').read_text())
paths=list((run/'snapshot').glob('higgsCombine_Fiducial_AsimovPostfit.MultiDimFit*.root'));assert len(paths)==1
f=ROOT.TFile.Open(str(paths[0]),'READ');assert f and not f.IsZombie()
w=f.Get('w');d=f.Get('toys/toy_asimov');assert w and d,'Missing workspace or saved Asimov'
assert w.getSnapshot('MultiDimFit'),'Missing post-fit snapshot';w.loadSnapshot('MultiDimFit')
x=w.var('CMS_hgg_mass');chan=w.cat('CMS_channel');sb=w.pdf('model_s');b=w.pdf('model_b');assert x and chan and sb and b
cats=[]
for i in range(chan.numTypes()):
 chan.setIndex(i);cats.append(str(chan.getLabel()))
if a.category!='all':assert a.category in cats;cats=[a.category]
edges=np.linspace(x.getMin(),x.getMax(),a.bins+1);centres=(edges[:-1]+edges[1:])/2;width=edges[1]-edges[0]
data={c:np.zeros(a.bins) for c in cats}
for i in range(d.numEntries()):
 row=d.get(i);c=str(row.getCatLabel('CMS_channel'))
 if c not in data:continue
 mass=row.getRealValue('CMS_hgg_mass');weight=d.weight();assert math.isfinite(mass) and math.isfinite(weight)
 j=int(np.searchsorted(edges,mass,side='right')-1)
 if mass==edges[-1]:j=a.bins-1
 if 0<=j<a.bins:data[c][j]+=weight
obs=ROOT.RooArgSet(x)
def expected(pdf):
 total=pdf.expectedEvents(obs);values=[]
 for lo,hi in zip(edges[:-1],edges[1:]):
  x.setRange('plot_bin',float(lo),float(hi))
  integral=pdf.createIntegral(obs,ROOT.RooFit.NormSet(obs),ROOT.RooFit.Range('plot_bin'))
  values.append(total*integral.getVal())
 values=np.array(values);assert np.isfinite(values).all();assert abs(values.sum()-total)<1e-4*max(1,abs(total))
 return values
out.mkdir(parents=True);summary={'input':str(paths[0]),'dataset':'toys/toy_asimov','snapshot':'MultiDimFit','bins':a.bins,'snapshot_validation':validation,'categories':{},'qualification':'Diagnostic expected mass distributions; no observed data, no uncertainty bands, no refit. Asimov points have no Poisson error bars. Signal curve includes all modeled Higgs processes.'}
totals=[np.zeros(a.bins) for _ in range(3)]
def draw(name,values):
 yy,ss,bb=values
 fig,(ax,res)=plt.subplots(2,1,figsize=(8.2,7),sharex=True,gridspec_kw={'height_ratios':[3,1]})
 ax.plot(centres,yy,'o',ms=3,color='black',label='Saved SM Asimov')
 ax.stairs(ss,edges,color='#c62828',lw=1.5,label='Post-fit S+B')
 ax.stairs(bb,edges,color='#2458a6',ls='--',label='Post-fit continuum background')
 ax.set_ylabel(f'Expected events / {width:g} GeV');ax.legend(frameon=False,fontsize=9)
 ax.set_title('CMS Private work · '+run.name+' · '+name,fontsize=11)
 res.axhline(0,color='0.6',lw=.8);res.plot(centres,yy-bb,'o',ms=3,color='black',label='Asimov − B')
 res.stairs(ss-bb,edges,color='#c62828',label='All Higgs signal');res.set_ylabel('Events − B');res.set_xlabel(r'$m_{\gamma\gamma}$ [GeV]');res.legend(frameon=False,fontsize=8)
 fig.text(.12,.012,f'Snapshot fit status {validation["fit_status"]}; diagnostic, no uncertainty bands.',fontsize=8)
 fig.tight_layout(rect=[0,.035,1,1])
 for ext in ['png','pdf']:fig.savefig(out/f'{name}.{ext}',dpi=160)
 plt.close(fig)
 with (out/f'{name}.csv').open('w') as handle:
  writer=csv.writer(handle);writer.writerow(['mass_low','mass_high','asimov','postfit_sb','postfit_continuum_b','all_higgs_signal'])
  writer.writerows(zip(edges[:-1],edges[1:],yy,ss,bb,ss-bb))
for c in cats:
 chan.setLabel(c);values=[data[c],expected(sb.getPdf(c)),expected(b.getPdf(c))]
 draw(c,values)
 summary['categories'][c]={'asimov':float(values[0].sum()),'sb':float(values[1].sum()),'continuum_b':float(values[2].sum()),'all_higgs_signal':float((values[1]-values[2]).sum())}
 for total,value in zip(totals,values):total+=value
 print('Finished',c,summary['categories'][c],flush=True)
if len(cats)>1:draw('all_categories',totals)
(out/'plot_inputs.json').write_text(json.dumps(summary,indent=2)+'\n')
f.Close();print('Saved plots:',out)
