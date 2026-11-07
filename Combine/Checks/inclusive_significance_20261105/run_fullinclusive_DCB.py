#!/usr/bin/env python3
"""DCB-only inclusive ttH+tHW significance with inclusive tHq profiled; exact saved clean Asimov."""
from pathlib import Path
import ROOT,subprocess,json,re,shlex,hashlib,math,sys
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
OUT=Path(__file__).resolve().parent;BASE=OUT.parents[1]
RTD=sum((['--X-rtd',x] for x in ['MINIMIZER_freezeDisassociatedParams','MINIMIZER_multiMin_hideConstants','MINIMIZER_multiMin_maskConstraints','MINIMIZER_multiMin_maskChannels=2']),[])
SOURCES={'DCB':'validated_closure_20261024T050616Z'}
results=json.loads((OUT/'results.json').read_text()) if (OUT/'results.json').exists() else {}
def save(): (OUT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
def run(stage,cmd):
 stage.mkdir(parents=True,exist_ok=True);log=stage/'run.log'
 if (stage/'exit_status.txt').exists() and (stage/'exit_status.txt').read_text().strip()=='0':return
 (stage/'command.sh').write_text('#!/usr/bin/env bash\ncd '+shlex.quote(str(stage))+'\n'+shlex.join(cmd)+'\n')
 print('RUN',stage.relative_to(OUT),flush=True)
 with log.open('w') as h:
  rc=subprocess.call(cmd,cwd=stage,stdout=h,stderr=subprocess.STDOUT)
 (stage/'exit_status.txt').write_text(str(rc)+'\n')
 if rc:raise RuntimeError(f'Failed {stage}, exit {rc}; inspect log')
 print('DONE',stage.relative_to(OUT),flush=True)
def openw(p):
 f=ROOT.TFile.Open(str(p));assert f and not f.IsZombie(),str(p);w=f.Get('w');assert w;return f,w
for model,folder in SOURCES.items():
 check=BASE/model/'checks'/folder;src=check/'clean_snapshot_strategy0/higgsCombine_Check.MultiDimFit.mH125.09.root';toy=check/'method2_generation/higgsCombine_CleanMethod2.GenerateOnly.mH125.09.123456.root'
 val=json.loads((check/'clean_snapshot_strategy0/validation.json').read_text());assert val['status']==0 and val['covQual']>=2 and val['edm']<.001
 sf,sw=openw(src);assert sw.loadSnapshot('MultiDimFit');sw.var('r_ttH').setVal(1);sw.var('r_tHq').setVal(1);sw.var('MH').setVal(125.09)
 tf=ROOT.TFile.Open(str(toy));data=tf.Get('toys/toy_asimov');assert data;data_hash=hashlib.sha256()
 for i in range(data.numEntries()):
  row=data.get(i);values=sorted((v.GetName(),int(v.getIndex()) if v.InheritsFrom('RooAbsCategory') else float(v.getVal())) for v in row);data_hash.update(json.dumps([values,float(data.weight())]).encode())
 tf.Close()
 card=BASE/model/f'Datacard_{model}.txt';lines=card.read_text().splitlines();names=[l.split() for l in lines];idx=next(i for i,x in enumerate(names) if x and x[0]=='process');sigpairs=[(c,p) for c,p,i in zip(names[idx-1][1:],names[idx][1:],names[idx+1][1:]) if int(i)<=0];assert len(sigpairs)==563
 for case in ['test5_inclusive_ttH_tHW_tHq_inclusive_profiled']:
  profile_tHq=True
  combined_signal=True
  key=model+'_'+case
  if results.get(key,{}).get('complete'):continue
  d=OUT/model/case;d.mkdir(parents=True,exist_ok=True);raw=d/'text2workspace/workspace.root'
  if case=='fiducial_baseline':f,w=openw(src);assert w.loadSnapshot('MultiDimFit')
  else:
   tdir=raw.parent;tdir.mkdir(exist_ok=True);newcard=tdir/f'Datacard_{model}.txt';newlines=[]
   for line in lines:
    t=line.split()
    if t and t[0]=='shapes' and t[3]!='FAKE':
     path=Path(t[3]);path=path if path.is_absolute() else (card.parent/path).resolve();assert path.is_file(),path;t[3]=str(path);line=' '.join(t)
    newlines.append(line)
   newcard.write_text('\n'.join(newlines)+'\n')
   maps=['map=.*/.*:1']
   if combined_signal:
    maps+=['map=.*/(tth|tHW)_(in|out)_.*:r_ttH[1,0,5]']
   else:maps+=['map=.*/tth_(in|out)_.*:r_ttH[1,0,5]']
   if profile_tHq:maps+=['map=.*/tHq(Had|Lep)_(in|out)_.*:r_tHq[1,-25,25]']
   cmd=['text2workspace.py',str(newcard),'-m','125.09','-P','HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel','-o',str(raw)]
   for m in maps:cmd+=['--PO',m]
   run(tdir,cmd);assert raw.exists();f,w=openw(raw)
  # Copy values and indices, not fit-constant flags, from the validated generation settings.
  copied=0
  for v in sw.allVars():
   t=w.var(v.GetName())
   if t:t.setVal(v.getVal());copied+=1
  for cat in sw.allCats():
   t=w.cat(cat.GetName())
   if t:t.setIndex(cat.getIndex())
  for n in ['r_ttH','r_tHq']:
   if w.var(n):w.var(n).setVal(1);w.var(n).setConstant(False)
  w.var('r_ttH').setRange(0,5);w.var('MH').setVal(125.09);w.var('MH').setConstant(True)
  discrepancies=[];dependencies=[]
  for cat,proc in sigpairs:
   n=f'n_exp_bin{cat}_proc_{proc}';old=sw.function(n);new=w.function(n);assert old and new,n
   oldval=float(old.getVal());newval=float(new.getVal())
   if abs(oldval-newval)>1e-8*max(abs(oldval),1e-6):discrepancies.append([n,oldval,newval])
   target=(proc.startswith(('tth_in_','tHW_in_')) if case=='fiducial_baseline' else proc.startswith(('tth_in_','tth_out_','tHW_in_','tHW_out_')) if combined_signal else proc.startswith(('tth_in_','tth_out_')))
   assert bool(new.dependsOn(w.var('r_ttH')))==target,(case,n,target)
   qdep=bool(w.var('r_tHq')) and bool(new.dependsOn(w.var('r_tHq')))
   assert qdep==(profile_tHq and proc.startswith(('tHqHad_in_','tHqHad_out_','tHqLep_in_','tHqLep_out_'))),(case,n,'tHq dependency')
   dependencies.append(dict(category=cat,process=proc,scaled_by_tested_poi=target,expected_at_SM=newval))
  assert not discrepancies,discrepancies[:5]
  snapshot=w.allVars();snapshot.add(w.allCats());w.saveSnapshot('comparisonStart',snapshot,True);prepared=d/'workspace.root';w.writeToFile(str(prepared));f.Close()
  metadata={'model':model,'case':case,'source_snapshot':str(src),'source_fit_validation':val,'dataset':str(toy),'dataset_sha256':data_hash.hexdigest(),'copied_variables':copied,'matching_signal_yields_at_SM':563,'target_scaled_contributions':sum(x['scaled_by_tested_poi'] for x in dependencies),'tHq_treatment':'IN and OUT share one profiled strength' if profile_tHq else 'IN and OUT nominal; nuisance uncertainties float','normalization_mapping':dependencies}
  (d/'inputs.json').write_text(json.dumps(metadata,indent=2)+'\n')
  common=['-d',str(prepared),'--snapshotName','comparisonStart','-m','125.09','-t','-1','--toysFile',str(toy),'--freezeParameters','MH','--setParameters','MH=125.09,r_ttH=1'+(',r_tHq=1' if profile_tHq else ''),'--setParameterRanges','r_ttH=0,5','--cminDefaultMinimizerStrategy','0','--cminDefaultMinimizerTolerance','0.01']+RTD
  closure=d/'closure';cmd=['combine','-M','MultiDimFit']+common+['--algo','none','--saveWorkspace','--saveFitResult','-P','r_ttH','--floatOtherPOIs','1','--saveInactivePOI','1','-v','2','-n','_Closure'];run(closure,cmd)
  rf=ROOT.TFile.Open(str(closure/'multidimfit_Closure.root'));assert rf and not rf.IsZombie();fr=rf.Get('fit_mdf');assert fr
  fit={'status':int(fr.status()),'covQual':int(fr.covQual()),'edm':float(fr.edm()),'r_ttH':float(fr.floatParsFinal().find('r_ttH').getVal()),'r_tHq':float(fr.floatParsFinal().find('r_tHq').getVal())};rf.Close()
  if not(fit['status']==0 and fit['covQual']>=2 and fit['edm']<.001):raise RuntimeError(f'Unreliable closure {key}: {fit}')
  stage=d/'significance';cmd=['combine','-M','Significance']+common+['--redefineSignalPOIs','r_ttH']
  if profile_tHq:cmd+=['--floatParameters','r_tHq']
  cmd+=['--saveWorkspace','--saveToys','-v','3','-n','_Expected'];run(stage,cmd)
  outputs=list(stage.glob('higgsCombine_Expected.Significance.mH125.09*.root'));assert len(outputs)==1;output=outputs[0];ff=ROOT.TFile.Open(str(output));assert ff and not ff.IsZombie();tree=ff.Get('limit');assert tree and tree.GetEntries()==1;tree.GetEntry(0);z=float(tree.limit);ff.Close();assert math.isfinite(z) and z>=0
  log=(stage/'run.log').read_text();statuses=re.findall(r'Minimization finished with status=(-?\d+)',log);assert statuses and all(x=='0' for x in statuses),(key,{x:statuses.count(x) for x in set(statuses)})
  results[key]={'complete':True,'model':model,'case':case,'expected_local_Z':z,'q0':z*z,'approx_Z_at_137fb':z*math.sqrt(137/62.4),'scaling_qualification':'sqrt(luminosity) approximation only; 13.6 vs 13 TeV and systematics differ','dataset_sha256':data_hash.hexdigest(),'source_snapshot':str(src),'dataset':str(toy),'closure':fit,'logged_status_counts':{x:statuses.count(x) for x in set(statuses)},'target_scaled_contributions':metadata['target_scaled_contributions'],'input_audit':str(d/'inputs.json')};save();print('RESULT',key,json.dumps(results[key]),flush=True)
 sf.Close()
print('DCB FULL-INCLUSIVE tHq PROFILE CHECK COMPLETE',flush=True)
