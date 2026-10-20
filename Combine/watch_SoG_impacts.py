#!/usr/bin/env python3
"""Local delayed watcher; collect/plot completed SoG impacts without running fits."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import shlex
import subprocess
import time

BASE = Path(__file__).resolve().parent


def status(run):
    report = run/'impacts/validation/fit.json'
    if not report.exists():
        return {'state': 'waiting', 'reason': 'impact report not available'}
    d = json.loads(report.read_text())
    accepted = [c for c in d['checks'] if c.get('structurally_complete')
                and c.get('exit_status') == 0 and c.get('last_logged_status') == '0']
    result = dict(accepted=len(accepted), expected=d['expected_nuisances'])
    if any((run/x).exists() for x in ('.runner.lock', '.continuation.lock')):
        return dict(result, state='waiting', reason='continuation or fit stage still active')
    exitfile = run/'continuation_exit_status.txt'
    if not exitfile.exists() or exitfile.read_text().strip() != '0':
        return dict(result, state='blocked', reason='continuation did not finish successfully')
    if not d['structurally_complete'] or len(accepted) != d['expected_nuisances']:
        return dict(result, state='blocked', reason='missing or failed impact fits')
    return dict(result, state='ready')


def collect(run):
    import uproot
    import numpy as np
    stage = run/'impacts'
    meta = json.loads((stage/'manifest.json').read_text())
    initial = json.loads((stage/'validation/initial.json').read_text())
    report = json.loads((stage/'validation/fit.json').read_text())
    names = meta['nuisances']
    assert len(names) == len(set(names))
    assert {c['nuisance'] for c in report['checks']} == set(names)
    assert initial['structurally_complete'] and all(c['last_logged_status']=='0' for c in initial['checks'])
    snapshot = Path(meta['input_snapshot'])
    assert hashlib.sha256(snapshot.read_bytes()).hexdigest() == meta['input_sha256'], 'Snapshot changed'
    for c in report['checks']:
        assert c['structurally_complete'] and c['exit_status']==0 and c['last_logged_status']=='0'
        with uproot.open(c['file']) as f:
            t=f['limit']
            assert t.num_entries == 3
            for field in ('r_ttH','r_tHq',c['nuisance']):
                assert np.isfinite(t[field].array(library='np')).all()
    out = stage/'collected_auto'
    if out.exists():
        if (out/'completed.json').exists():
            print('Plots already complete:',out,flush=True); return
        raise RuntimeError('Incomplete collection folder exists; inspect it before retrying')
    out.mkdir()
    commands=[]
    def execute(cmd,cwd,log):
        commands.append({'command':cmd,'cwd':str(cwd)})
        print(shlex.join(cmd),flush=True)
        with (out/log).open('w') as stream:
            subprocess.run(cmd,cwd=str(cwd),stdout=stream,stderr=subprocess.STDOUT,check=True)
    mh=f"{meta['mass']:g}"
    execute(['combineTool.py','-M','Impacts','-d',str(snapshot),'-m',mh,
             '--name','FiducialImpacts','--redefineSignalPOIs','r_ttH,r_tHq',
             '--splitInitial','--named',','.join(names),'-o',str(out/'impacts.json')],stage,'collect.log')
    data=json.loads((out/'impacts.json').read_text())
    assert len(data['params'])==len(names) and {p['name'] for p in data['params']}==set(names)
    assert {p['name'] for p in data['POIs']}=={'r_ttH','r_tHq'}
    for p in data['params']:
        for key in ('fit','r_ttH','r_tHq'):
            assert len(p[key])==3 and all(math.isfinite(x) for x in p[key])
    plotter=BASE.parent.parent/'CombineHarvester/CombineTools/scripts/plotImpacts.py'
    assert plotter.is_file()
    pages=out/'pages';pages.mkdir()
    for poi in ('r_ttH','r_tHq'):
        execute(['python3','-B',str(plotter),'-i',str(out/'impacts.json'),'-o','impacts_'+poi,
                 '--POI',poi,'--per-page','30','--height','900','--left-margin','0.48',
                 '--cms-label','Private work'],out,'plot_'+poi+'.log')
        pdf=out/('impacts_'+poi+'.pdf');assert pdf.is_file() and pdf.stat().st_size>0
        for fmt in ('png','jpeg'):
            execute(['pdftoppm','-'+fmt,'-r','120',str(pdf),str(pages/('impacts_'+poi))],out,'export_'+poi+'_'+fmt+'.log')
    (out/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    (out/'completed.json').write_text(json.dumps(dict(nuisances=len(names),POIs=['r_ttH','r_tHq'],
        source_validation=str(stage/'validation/fit.json'),snapshot_validation=json.loads((run/'snapshot/validation.json').read_text()),
        qualification='Diagnostic collection only. No recentering or nuisance removal. Snapshot status/covariance, internal fit warnings and separate-model Asimov qualifications remain.'),indent=2)+'\n')
    print('COMPLETE: impacts JSON, PDFs and every page as PNG/JPG:',out,flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run-dir',default=str(BASE/'SoG'))
    p.add_argument('--delay-hours',type=float,default=3.5)
    p.add_argument('--poll-seconds',type=float,default=600)
    p.add_argument('--timeout-hours',type=float,default=48)
    p.add_argument('--check-only',action='store_true')
    a=p.parse_args();run=Path(a.run_dir).resolve()
    if a.check_only:
        print(json.dumps(status(run),indent=2));return
    assert a.delay_hours>=0 and a.poll_seconds>0 and a.timeout_hours>a.delay_hours
    lock=run/'.autoplot.lock';lock.mkdir()
    try:
        started=time.time();deadline=started+3600*a.timeout_hours
        print('Watcher started. First check after hours:',a.delay_hours,flush=True)
        time.sleep(3600*a.delay_hours)
        while time.time()<deadline:
            s=status(run);print(time.strftime('%Y-%m-%d %H:%M:%S'),json.dumps(s),flush=True)
            if s['state']=='ready':collect(run);return
            if s['state']=='blocked':raise RuntimeError(s['reason']+'; preserving outputs, no fit changes')
            time.sleep(a.poll_seconds)
        raise RuntimeError('Timed out waiting; no fit changes')
    finally:
        lock.rmdir()


if __name__=='__main__':main()
