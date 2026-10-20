from pathlib import Path
import subprocess,sys,json
base=Path.cwd();out=base/'runplotter_individual_years_20261014';eras=['2022preEE','2022postEE','2023preBPix','2023postBPix'];records=[]
for model in ['DCB','SoG']:
 for era in eras:
  source=base/'packaged_signals_20261014'/model/era;files=sorted(source.glob('*.root'));assert len(files)==16
  stage=out/'inputs'/model/era;stage.mkdir(parents=True,exist_ok=True);dest=out/model/era;dest.mkdir(parents=True,exist_ok=True)
  for src in files:
   prefix=f'CMS-HGG_sigfit_packaged_{model}_';assert src.name.startswith(prefix) and src.name.endswith('_'+era+'.root');cat=src.name[len(prefix):-(len(era)+6)]
   link=stage/f'{prefix}{cat}.root'
   if not link.exists():link.symlink_to(src)
   assert link.resolve()==src.resolve()
   png=dest/'Plots'/f'smodel_{cat}_{era}.png';pdf=png.with_suffix('.pdf');log=dest/(cat+'.log')
   cmd=[sys.executable,'-u',str(base/'RunPlotter.py'),'--procs','all','--years',era,'--cats',cat,'--ext','packaged_'+model,'--inputDir',str(stage),'--outputDir',str(dest),'--mass','125','--MH','125','--label','Simulation Private Work']
   print('RUNPLOTTER',model,era,cat,flush=True)
   if not(png.exists() and pdf.exists()):
    with log.open('w') as f:r=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
    assert r.returncode==0,(model,era,cat,log)
   assert png.is_file() and png.stat().st_size>0 and pdf.is_file() and pdf.stat().st_size>0
   text=log.read_text(errors='replace');assert 'Traceback' not in text and '*** Break ***' not in text
   records.append({'model':model,'era':era,'category':cat,'input_package':str(src),'png':str(png),'pdf':str(pdf),'log':str(log),'command':cmd})
   (out/'manifest.json').write_text(json.dumps(records,indent=2));print('VERIFIED',len(records),'/128',flush=True)
report='''# Individual-era category signal plots

Each model family has 64 plots: 16 categories × 4 eras. DCB and SoG are separate, giving 128 PNG/PDF pairs in total. In `<model>/<era>/Plots/`, each plot compares the sum of all requested processes in that category with the MC of that same era. Models and MC use mass 125. Individual process contributions are not separately drawn; these are category sums for one era at a time. RunPlotter.py was used unchanged with --procs all and a single --years value. The year appears on the plot. Input symlinks only adapt the per-era package filenames to RunPlotter's naming convention; the packages themselves are unchanged.

The default 0.1% pruning is evaluated relative to this individual era/category's signed yield, not the four-era total. It suppresses tiny positive, zero and negative-rate contributions for display when the signed category total is positive. It does not remove negative events inside retained datasets or fix rates in the workspaces. Numerical fit warnings and the Gaussian-count-selection issue remain unresolved. Single-year RunPlotter does not emit the multi-year effSigma JSON file; its effective width appears in the legend.

manifest.json preserves exact commands, input and output paths and logs. No fits, configs, plotting source scripts or ROOT package contents were changed.
'''
cats=sorted({r['category'] for r in records})
for model in ['DCB','SoG']:
 report+=f'\n## {model}\n\n| Category | 2022preEE | 2022postEE | 2023preBPix | 2023postBPix |\n|---|---|---|---|---|\n'
 for cat in cats:report+='| '+cat+' | '+' | '.join(f'[PNG]({model}/{era}/Plots/smodel_{cat}_{era}.png)' for era in eras)+' |\n'
(out/'README.md').write_text(report);print('COMPLETE 128 PNG and 128 PDF plots: 64 per model',flush=True)
