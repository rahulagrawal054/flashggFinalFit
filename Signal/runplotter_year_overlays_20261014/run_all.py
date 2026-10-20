from pathlib import Path
import subprocess,sys,json,math
base=Path.cwd();out=base/'runplotter_year_overlays_20261014';records=[]
years='2022preEE,2022postEE,2023preBPix,2023postBPix'
for model in ['DCB','SoG']:
 inputdir=base/'packaged_all_years_20261014'/model;cats=sorted(p.name[len('CMS-HGG_sigfit_packaged_'+model+'_'):-5] for p in inputdir.glob('*.root'));assert len(cats)==16
 for cat in cats:
  dest=out/model;png=dest/'Plots'/f'smodel_{cat}.png';pdf=png.with_suffix('.pdf');sigma=dest/'Plots'/f'effSigma_{cat}.json';log=out/f'{model}_{cat}.log'
  cmd=[sys.executable,'-u',str(base/'RunPlotter.py'),'--procs','all','--years',years,'--plot-years-separate','--cats',cat,'--ext','packaged_'+model,'--inputDir',str(inputdir),'--outputDir',str(dest),'--mass','125','--MH','125','--label','Simulation Private Work']
  print('RUNPLOTTER',model,cat,flush=True)
  if not (png.exists() and pdf.exists() and sigma.exists()):
   with log.open('w') as lf:r=subprocess.run(cmd,stdout=lf,stderr=subprocess.STDOUT)
   assert r.returncode==0,(model,cat,log)
  assert png.is_file() and png.stat().st_size>0 and pdf.is_file() and pdf.stat().st_size>0
  values=json.loads(sigma.read_text());assert set(values)==set(['combined']+years.split(','));assert all(math.isfinite(v) and v>0 for v in values.values())
  records.append({'model':model,'category':cat,'png':str(png),'pdf':str(pdf),'sigma':values,'log':str(log),'command':cmd})
  (out/'manifest.json').write_text(json.dumps(records,indent=2));print('VERIFIED',len(records),'/32',flush=True)
report='''# RunPlotter combined-year and individual-year overlays

Produced with the existing RunPlotter.py and plotSignalModel implementation, without changing either script or any fitting configuration/workspace. DCB/Plots and SoG/Plots each contain 16 category PNG/PDF pairs plus effSigma JSON files. manifest.json records the exact command, outputs, logs and five effective widths per category.

The actual enabling flag is --plot-years-separate; the parser help text is misleading, but the drawing code displays per-year dashed coloured curves when this flag is true. The combined parametric model is solid blue and the combined MC points are black. Individual curves are luminosity-weighted contributions, not each independently normalized to the same peak: 2022preEE light blue, 2022postEE green, 2023preBPix yellow/olive, 2023postBPix gray-blue. The gray fill marks the implementation's combined effective-width band. The code uses the local year luminosities, mass=125 for MC and MH=125 for PDFs. Default data/PDF bins are 160/3200; --doFWHM was not requested.

Default threshold=0.001 prunes contributions below 0.1% of the signed category norm; in these packages that omits negative and zero-rate components too. This changes the plotted selection only, not the underlying workspaces, and does not resolve their physical negative-rate issue. These plots are therefore not identical to the earlier signed-weight aggregate diagnostics that retained every contribution. The existing code's displayed sigma_eff is a histogram-based effective width, not the DCB Gaussian-core sigma. Plots do not resolve optimizer failures, boundaries, selection validation or closure.

| Category | DCB plot | SoG plot | Combined sigma_eff DCB [GeV] | Combined sigma_eff SoG [GeV] |
|---|---|---|---:|---:|
'''
for cat in cats:
 d=next(r for r in records if r['model']=='DCB' and r['category']==cat);s=next(r for r in records if r['model']=='SoG' and r['category']==cat)
 report+=f'| {cat} | [PNG](DCB/Plots/smodel_{cat}.png) | [PNG](SoG/Plots/smodel_{cat}.png) | {d["sigma"]["combined"]:.3f} | {s["sigma"]["combined"]:.3f} |\n'
(out/'README.md').write_text(report);print('COMPLETE 32 PNG, 32 PDF, 32 effective-width JSON files',flush=True)
