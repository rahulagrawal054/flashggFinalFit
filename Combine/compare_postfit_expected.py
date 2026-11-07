#!/usr/bin/env python3
"""Repeat saved total significance/limit commands, changing only the input Asimov dataset."""
import argparse,json,pathlib,shlex,subprocess,math,re
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',action='store_true');a=p.parse_args()
base=pathlib.Path(__file__).resolve().parent
jobs=[]
for model in ['DCB','SoG']:
 test=base/model/'postfit_asimov_test';m=json.loads((test/'manifest.json').read_text());assert m['complete']
 toy=pathlib.Path(m['stages']['generation']['result']);assert toy.is_file()
 for kind,poi in [('significance','r_ttH'),('significance','r_tHq'),('limits','r_tHq')]:
  source=base/model/kind/poi/'total/profile_other'
  cmd=shlex.split((source/'command.sh').read_text());cmd[cmd.index('--toysFile')+1]=str(toy)
  stage=test/kind/poi/'total/profile_other'
  jobs.append((model,kind,poi,source,stage,cmd))
  print(model,kind,poi,shlex.join(cmd),flush=True)
if not a.run:print('Dry run; add --run');raise SystemExit
import ROOT
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
summary={}
for model,kind,poi,source,stage,cmd in jobs:
 stage.mkdir(parents=True,exist_ok=False)
 (stage/'command.sh').write_text('#!/usr/bin/env bash\nset -euo pipefail\ncd '+shlex.quote(str(stage))+'\n'+shlex.join(cmd)+'\n')
 print('RUNNING',model,kind,poi,flush=True)
 with (stage/'run.log').open('w') as log:result=subprocess.run(cmd,cwd=stage,stdout=log,stderr=subprocess.STDOUT)
 if result.returncode:raise RuntimeError(f'{stage}: exit {result.returncode}, inspect run.log')
 files=list(stage.glob('higgsCombine*.root'));assert len(files)==1,files
 f=ROOT.TFile.Open(str(files[0]));assert f and not f.IsZombie();t=f.Get('limit');assert t
 rows=[{'quantile':float(x.quantileExpected),'value':float(x.limit)} for x in t];f.Close()
 assert rows and all(math.isfinite(x['value']) for x in rows)
 counts={}
 with (stage/'run.log').open(errors='replace') as h:
  for line in h:
   for v in re.findall(r'(?:status\s*=\s*|Status\s*:\s*)(-?\d+)',line):counts[v]=counts.get(v,0)+1
 original=json.loads((source/'results.json').read_text())
 report={'model':model,'poi':poi,'other_poi':'r_tHq' if poi=='r_ttH' else 'r_ttH','other_mode':'profiled','rows':rows,'logged_status_counts':counts,'input_dataset':cmd[cmd.index('--toysFile')+1],'review_required':True}
 if kind=='significance':
  assert len(rows)==1 and rows[0]['value']>=0
  report['expected_local_Z']=rows[0]['value'];report['original_expected_local_Z']=original['expected_local_Z']
 else:
  matches=[r['value'] for r in rows if abs(r['quantile']-.5)<1e-5];assert len(matches)==1 and len(rows)==5
  report['expected_median_95CLs']=matches[0];report['original_expected_median_95CLs']=original['expected_median_95CLs']
  report['reference']='Matched original AsymptoticLimits --run expected CLs: auxiliary target-zero expected reference; other strength profiled. Saved input Asimov conditions the fit, not a direct limit on injected SM pseudo-observation.'
 (stage/'results.json').write_text(json.dumps(report,indent=2)+'\n')
 summary[model+'_'+kind+'_'+poi]=report
 (base/'postfit_expected_comparison.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('DONE',model,kind,poi,json.dumps(rows),flush=True)
print('ALL SIX CALCULATIONS COMPLETE',flush=True)
