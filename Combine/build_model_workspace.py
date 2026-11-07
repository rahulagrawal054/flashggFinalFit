#!/usr/bin/env python3
"""Build a named physics model in a new folder, without moving source inputs."""
import argparse, collections, hashlib, json, math, os, pathlib, re, runpy, shlex, shutil, subprocess, sys
BASE=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--datacard',type=pathlib.Path,required=True)
p.add_argument('--model',required=True,help='Exact key in Combine/models.py')
p.add_argument('--outdir',type=pathlib.Path,required=True,help='New, model-specific output folder')
p.add_argument('--mass',type=float,default=125.09)
g=p.add_mutually_exclusive_group();g.add_argument('--run',action='store_true',help='Build; default is a no-write dry run');g.add_argument('--dry-run',action='store_true')
a=p.parse_args()
def require(ok,message):
 if not ok:p.error(message)
card=a.datacard.resolve();out=a.outdir.resolve();require(card.is_file(),'Missing datacard: '+str(card));require(not out.exists(),'Output exists; choose a new folder: '+str(out));require(math.isfinite(a.mass) and a.mass>0,'Invalid mass')
models_file=BASE/'models.py';models=runpy.run_path(str(models_file))['models'];require(a.model in models,'Unknown model: '+a.model)
opts=shlex.split(models[a.model]);text=card.read_text();rows=[line.split() for line in text.splitlines()]
proc_indices=[i for i,row in enumerate(rows) if row and row[0]=='process'];require(len(proc_indices)==2,'Expected process-name and process-ID lines')
i=next((i for i in proc_indices if not rows[i][1].lstrip('-').isdigit()),None);require(i is not None and rows[i-1][0]=='bin','Malformed process table')
names=rows[i][1:];bins=rows[i-1][1:];ids=rows[next(j for j in proc_indices if j!=i)][1:];require(len(names)==len(bins)==len(ids),'Mismatched process table columns');cats=set(bins)
for channel in ['had','lep']:
 if a.model.endswith('__ttH_'+channel):require(cats=={f'ttH_{channel}_{j}' for j in range(1,5)},'This model alias requires its four-category '+channel+' card; it does not select categories from a full card')
# Preserve all non-shape text; resolve shape files in the copy so it can live elsewhere.
newlines=[];shape_files=set()
for line in text.splitlines():
 row=line.split()
 if row and row[0]=='shapes' and len(row)>=4 and row[3]!='FAKE':
  path=pathlib.Path(row[3]);path=path if path.is_absolute() else (card.parent/path).resolve();require(path.is_file(),'Missing ROOT shape file: '+str(path));row[3]=str(path);shape_files.add(str(path));line=' '.join(row)
 newlines.append(line)
require(shape_files,'No ROOT shape files found')
# Audit the official last-matching-map behavior for the analysis MultiSignalModels.
maps=[];declared=set()
for j,arg in enumerate(opts):
 if arg=='--PO' and opts[j+1].startswith('map='):
  pattern,scale=opts[j+1][4:].split(':',1);maps.append((pattern,scale.split('[')[0]))
  if '[' in scale:declared.add(scale.split('[')[0])
counts=collections.Counter()
for cat,name,ident in zip(bins,names,ids):
 if int(ident)>0:continue
 scale='1'
 for pattern,value in maps:
  if re.match(pattern,cat+'/'+name):scale=value
 counts[scale]+=1
if maps:
 require(declared,'No signal strengths declared')
 for name in declared:require(counts[name]>0,'Declared strength does not scale any retained signal contribution: '+name)
binary=shutil.which('text2workspace.py') or 'text2workspace.py';copied=out/'Datacard.txt';workspace=out/'workspace.root';cmd=[binary,str(copied),'-o',str(workspace),'-m',f'{a.mass:g}']+opts
print('Model:',a.model);print('Categories:',','.join(sorted(cats)));print('Signal mapping counts:',dict(counts));print('Output:',out);print('Command:',shlex.join(cmd),flush=True)
if not a.run:print('DRY RUN: no files created, moved or fitted. Add --run to build the workspace.');sys.exit(0)
require(shutil.which('text2workspace.py') is not None,'Run cmsenv and source ../setup.sh first')
out.mkdir(parents=True,exist_ok=False);copied.write_text('\n'.join(newlines)+'\n');shutil.copy2(models_file,out/'models_at_build.py')
(out/'command.sh').write_text('#!/usr/bin/env bash\nset -eo pipefail\ncd '+shlex.quote(str(out))+'\n'+shlex.join(cmd)+'\n')
manifest=dict(model=a.model,mass=a.mass,source_datacard=str(card),source_sha256=hashlib.sha256(card.read_bytes()).hexdigest(),models_sha256=hashlib.sha256(models_file.read_bytes()).hexdigest(),categories=sorted(cats),shape_files=sorted(shape_files),signal_mapping_counts=dict(counts),command=cmd,status='BUILDING')
def save(): (out/'build.json').write_text(json.dumps(manifest,indent=2)+'\n')
save();env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
try:
 with (out/'build.log').open('w') as log:
  proc=subprocess.Popen(cmd,cwd=out,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
  try:
   for line in proc.stdout:print(line,end='',flush=True);log.write(line);log.flush()
   rc=proc.wait()
  except BaseException:proc.terminate();proc.wait();raise
 manifest['exit_code']=rc;save();require(rc==0 and workspace.is_file(),'Build failed; inspect '+str(out/'build.log'))
 import ROOT
 ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit');f=ROOT.TFile.Open(str(workspace));assert f and not f.IsZombie();w=f.Get('w');assert w and w.obj('ModelConfig') and w.pdf('model_s') and w.data('data_obs')
 actual_pois={v.GetName() for v in w.obj('ModelConfig').GetParametersOfInterest()}
 if declared:assert actual_pois==declared,(actual_pois,declared)
 channel=w.cat('CMS_channel');assert channel;actual_cats={channel.lookupType(j).GetName() for j in range(channel.numTypes())};assert actual_cats==cats,(actual_cats,cats)
 assert w.var('MH') and abs(w.var('MH').getVal()-a.mass)<1e-6
 manifest.update(status='WORKSPACE_BUILT',pois=sorted(actual_pois));f.Close();save();print('Workspace built and structurally checked:',workspace);print('No fit was run. Keep MH explicitly fixed in subsequent fixed-mass fits.')
except BaseException as error:
 manifest.update(status='FAILED',error=str(error));save();raise
