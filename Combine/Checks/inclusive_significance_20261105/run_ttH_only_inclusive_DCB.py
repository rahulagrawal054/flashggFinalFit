#!/usr/bin/env python3
"""Only the three authorized DCB ttH-only expected-significance tests; no scans."""
from pathlib import Path
import ROOT,subprocess,json,re,shlex,hashlib,math
ROOT.gROOT.SetBatch(True);ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit')
OUT=Path(__file__).resolve().parent;BASE=OUT.parents[1];MODEL='DCB'
CHECK=BASE/'DCB/checks/validated_closure_20261024T050616Z'
SOURCE=CHECK/'clean_snapshot_strategy0/higgsCombine_Check.MultiDimFit.mH125.09.root'
TOYS=CHECK/'method2_generation/higgsCombine_CleanMethod2.GenerateOnly.mH125.09.123456.root'
RTD=sum((['--X-rtd',n] for n in ['MINIMIZER_freezeDisassociatedParams','MINIMIZER_multiMin_hideConstants','MINIMIZER_multiMin_maskConstraints','MINIMIZER_multiMin_maskChannels=2']),[])
RESULTS=json.loads((OUT/'results.json').read_text())
CASES=[('test6_ttH_only_inclusive_tHq_profiled_tHW_fixed',{'r_tHq':['tHqHad','tHqLep']}),('test7_ttH_only_independent_tHq_tHW_inclusive_profiled',{'r_tHq':['tHqHad','tHqLep'],'r_tHW':['tHW']}),('test8_ttH_only_common_tH_inclusive_profiled',{'r_tH':['tHqHad','tHqLep','tHW']})]
BOUNDS={'r_ttH':(0.,5.),'r_tHq':(-25.,25.),'r_tHW':(-25.,100.),'r_tH':(-25.,25.)}
def save(): (OUT/'results.json').write_text(json.dumps(RESULTS,indent=2)+'\n')
def run(stage,cmd):
 stage.mkdir(parents=True,exist_ok=True)
 if (stage/'exit_status.txt').exists() and (stage/'exit_status.txt').read_text().strip()=='0':return
 (stage/'command.sh').write_text('#!/usr/bin/env bash\ncd '+shlex.quote(str(stage))+'\n'+shlex.join(cmd)+'\n');print('RUN',stage.relative_to(OUT),flush=True)
 with (stage/'run.log').open('w') as log:rc=subprocess.call(cmd,cwd=stage,stdout=log,stderr=subprocess.STDOUT)
 (stage/'exit_status.txt').write_text(str(rc)+'\n');assert rc==0,(stage,rc);print('DONE',stage.relative_to(OUT),flush=True)
def openw(p):
 f=ROOT.TFile.Open(str(p));assert f and not f.IsZombie(),str(p);w=f.Get('w');assert w;return f,w
def statuses(stage):
 v=re.findall(r'Minimization finished with status=(-?\d+)',(stage/'run.log').read_text());assert v and set(v)=={'0'},(stage,{s:v.count(s) for s in set(v)});return {s:v.count(s) for s in set(v)}
sf,sw=openw(SOURCE);assert sw.loadSnapshot('MultiDimFit')
for name in ['r_ttH','r_tHq']:sw.var(name).setVal(1)
sw.var('MH').setVal(125.09)
tf=ROOT.TFile.Open(str(TOYS));data=tf.Get('toys/toy_asimov');assert data;dh=hashlib.sha256()
for i in range(data.numEntries()):
 row=data.get(i);values=sorted((v.GetName(),int(v.getIndex()) if v.InheritsFrom('RooAbsCategory') else float(v.getVal())) for v in row);dh.update(json.dumps([values,float(data.weight())]).encode())
tf.Close();assert dh.hexdigest()==RESULTS['DCB_test5_inclusive_ttH_tHW_tHq_inclusive_profiled']['dataset_sha256']
card=BASE/'DCB/Datacard_DCB.txt';lines=card.read_text().splitlines();tokens=[l.split() for l in lines];i=next(i for i,t in enumerate(tokens) if t and t[0]=='process');pairs=[(c,p) for c,p,j in zip(tokens[i-1][1:],tokens[i][1:],tokens[i+1][1:]) if int(j)<=0];assert len(pairs)==563
for case,profiles in CASES:
 key='DCB_'+case
 if RESULTS.get(key,{}).get('complete'):continue
 out=OUT/'DCB'/case;tdir=out/'text2workspace';tdir.mkdir(parents=True,exist_ok=True);nc=tdir/'Datacard_DCB.txt';new=[]
 for line in lines:
  t=line.split()
  if t and t[0]=='shapes' and t[3]!='FAKE':
   p=Path(t[3]);p=p if p.is_absolute() else (card.parent/p).resolve();assert p.is_file();t[3]=str(p);line=' '.join(t)
  new.append(line)
 nc.write_text('\n'.join(new)+'\n');maps=['map=.*/.*:1','map=.*/tth_(in|out)_.*:r_ttH[1,0,5]']
 for name,processes in profiles.items():
  lo,hi=BOUNDS[name];maps.append('map=.*/('+'|'.join(processes)+')_(in|out)_.*:'+f'{name}[1,{lo:g},{hi:g}]')
 raw=tdir/'workspace.root';cmd=['text2workspace.py',str(nc),'-m','125.09','-P','HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel','-o',str(raw)]
 for m in maps:cmd+=['--PO',m]
 run(tdir,cmd);f,w=openw(raw)
 for v in sw.allVars():
  t=w.var(v.GetName())
  if t:t.setVal(v.getVal())
 for v in sw.allCats():
  t=w.cat(v.GetName())
  if t:t.setIndex(v.getIndex())
 for name in ['r_ttH']+list(profiles):
  w.var(name).setVal(1);w.var(name).setConstant(False);w.var(name).setRange(*BOUNDS[name])
 w.var('MH').setVal(125.09);w.var('MH').setConstant(True)
 assert {v.GetName() for v in w.obj('ModelConfig').GetParametersOfInterest()}=={'r_ttH'}|set(profiles)
 counts={name:0 for name in ['r_ttH']+list(profiles)};audit=[]
 for cat,proc in pairs:
  name=f'n_exp_bin{cat}_proc_{proc}';a=sw.function(name);b=w.function(name);assert a and b
  va=float(a.getVal());vb=float(b.getVal());assert abs(va-vb)<=1e-8*max(abs(va),1e-6),(name,va,vb)
  dependencies={}
  for strength,processes in {'r_ttH':['tth'],**profiles}.items():
   wanted=any(re.match(re.escape(p)+r'_(in|out)_',proc) for p in processes);actual=bool(b.dependsOn(w.var(strength)));assert wanted==actual,(proc,strength);counts[strength]+=int(actual);dependencies[strength]=actual
  audit.append(dict(category=cat,process=proc,expected_at_SM=vb,dependencies=dependencies))
 snap=w.allVars();snap.add(w.allCats());w.saveSnapshot('comparisonStart',snap,True);workspace=out/'workspace.root';w.writeToFile(str(workspace));f.Close()
 meta=dict(case=case,model='DCB',tested_process='ttH_IN+OUT only',profiled_groups=profiles,fixed_tHW_strength=1 if not any('tHW' in p for p in profiles.values()) else None,dataset=str(TOYS),dataset_sha256=dh.hexdigest(),source_snapshot=str(SOURCE),ranges={k:BOUNDS[k] for k in counts},dependency_counts=counts,matching_SM_yields=563,audit=audit)
 (out/'inputs.json').write_text(json.dumps(meta,indent=2)+'\n')
 initial=','.join(['MH=125.09','r_ttH=1']+[n+'=1' for n in profiles])
 common=['-d',str(workspace),'--snapshotName','comparisonStart','-m','125.09','-t','-1','--toysFile',str(TOYS),'--freezeParameters','MH','--setParameters',initial,'--setParameterRanges',':'.join(f'{n}={BOUNDS[n][0]:g},{BOUNDS[n][1]:g}' for n in counts),'--cminDefaultMinimizerStrategy','0','--cminDefaultMinimizerTolerance','0.01']+RTD
 closure=out/'closure';run(closure,['combine','-M','MultiDimFit']+common+['--algo','none','-P','r_ttH','--floatOtherPOIs','1','--saveInactivePOI','1','--saveWorkspace','--saveFitResult','-v','2','-n','_Closure'])
 rf=ROOT.TFile.Open(str(closure/'multidimfit_Closure.root'));fr=rf.Get('fit_mdf');assert fr
 fit=dict(status=int(fr.status()),covQual=int(fr.covQual()),edm=float(fr.edm()),strengths={n:float(fr.floatParsFinal().find(n).getVal()) for n in counts});rf.Close();assert fit['status']==0 and fit['covQual']>=2 and fit['edm']<.001,(case,fit)
 # A single conditional point verifies profile ranges; this is not a likelihood scan.
 null=out/'null_check';ncommon=common.copy();ncommon[ncommon.index('-d')+1]=str(closure/'higgsCombine_Closure.MultiDimFit.mH125.09.root');ncommon[ncommon.index('--snapshotName')+1]='MultiDimFit';ncommon[ncommon.index('--setParameters')+1]='MH=125.09'
 run(null,['combine','-M','MultiDimFit']+ncommon+['--skipInitialFit','--algo','fixed','--fixedPointPOIs','r_ttH=0','-P','r_ttH','--floatOtherPOIs','1','--saveInactivePOI','1','--saveWorkspace','-v','3','-n','_Null'])
 nf=ROOT.TFile.Open(str(next(null.glob('higgsCombine_Null.MultiDimFit*.root'))));tree=nf.Get('limit');nullrows=[]
 for e in tree:
  if abs(float(e.r_ttH))<1e-6:nullrows.append(dict(deltaNLL=float(e.deltaNLL),strengths={n:float(getattr(e,n)) for n in profiles}))
 nf.Close();assert len(nullrows)==1,(case,nullrows);np=nullrows[0];assert np['deltaNLL']>=-1e-4
 for name,v in np['strengths'].items():
  lo,hi=BOUNDS[name];assert lo+1e-3<v<hi-1e-3,('profile hit boundary',case,name,v,lo,hi)
 nstatuses=statuses(null);(null/'validation.json').write_text(json.dumps(dict(point=np,logged_status_counts=nstatuses),indent=2)+'\n')
 sig=out/'significance';run(sig,['combine','-M','Significance']+common+['--redefineSignalPOIs','r_ttH','--floatParameters',','.join(profiles),'--saveWorkspace','--saveToys','-v','3','-n','_Expected'])
 outputs=list(sig.glob('higgsCombine_Expected.Significance*.root'));assert len(outputs)==1;of=ROOT.TFile.Open(str(outputs[0]));tree=of.Get('limit');assert tree and tree.GetEntries()==1;tree.GetEntry(0);z=float(tree.limit);of.Close();assert math.isfinite(z) and z>=0
 status=statuses(sig);nullZ=math.sqrt(max(2*np['deltaNLL'],0));assert abs(nullZ-z)<.01,(case,'conditional and significance differ',nullZ,z)
 result=dict(complete=True,model='DCB',case=case,expected_local_Z=z,q0=z*z,approx_Z_at_137fb=z*math.sqrt(137/62.4),scaling_qualification='sqrt(luminosity) approximation only; not a 13 TeV prediction',dataset_sha256=dh.hexdigest(),dataset=str(TOYS),source_snapshot=str(SOURCE),profiled_groups=profiles,dependency_counts=counts,closure=fit,null_point=np,null_check_Z=nullZ,logged_status_counts=status,input_audit=str(out/'inputs.json'))
 RESULTS[key]=result;save();(out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print('RESULT',key,json.dumps(result),flush=True)
sf.Close();print('REQUESTED THREE DCB SIGNIFICANCE TESTS COMPLETE',flush=True)
