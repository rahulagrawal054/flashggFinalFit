#!/usr/bin/env python3
"""Validate a hybrid production and optionally write configs/commands; never run fits."""
import argparse
import json
import math
from pathlib import Path
import pprint
import re
import shlex

ROOT = Path(__file__).resolve().parent
ANALYSIS = 'tth_th_analysis_hybrid_fiducial'


def validate(c):
    def require(ok, message):
        if not ok:
            raise ValueError(message)
    require(re.fullmatch(r'[A-Za-z0-9_]+', c['tag']), 'Use letters, digits and underscores in tag')
    eras = c['lumi_fb']
    require({'2022preEE', '2022postEE', '2023preBPix', '2023postBPix'} <= set(eras),
            'Include the four existing eras')
    require(any(e.startswith('2024') for e in eras), 'Specify approved 2024 era(s)')
    for era, lumi in eras.items():
        require(re.fullmatch(r'202[234][A-Za-z0-9]*', era), 'Invalid era: '+era)
        require(isinstance(lumi, (int, float)) and not isinstance(lumi, bool) and
                math.isfinite(lumi) and lumi > 0, 'Fill approved lumi_fb for '+era)
        for kind in ('data', 'mc'):
            width = c['beamspot_cm'].get(era, {}).get(kind)
            require(isinstance(width, (int, float)) and not isinstance(width, bool) and
                    math.isfinite(width) and width > 0, 'Fill beamspot_cm '+era+' '+kind)
    cats = c['categories']
    require(cats and len(set(cats)) == len(cats) and
            all(re.fullmatch(r'[A-Za-z0-9_]+', k) for k in cats),
            'Fill unique actual hybrid category names')
    require(set(c['donors']) == set(cats), 'Specify one reviewed donor per category')
    procs = {'tth', 'tHW', 'tHqHad', 'tHqLep', 'ggh', 'vbf', 'vh', 'bbh'}
    allowed = {p+'_'+region for p in procs for region in ('in', 'out')}
    for donor in [*c['donors'].values(), c['wv_donor']]:
        require(donor['process'] in allowed and donor['category'] in cats,
                'Donor must use a supported in/out process and a configured category')
    for key in ('ws_base', 'data_workspace'):
        require(isinstance(c[key], str) and Path(c[key]).is_absolute() and
                not re.search(r'\s', c[key]), 'Fill absolute '+key+' without whitespace')
    require(Path(c['data_workspace']).is_file(), 'Missing new combined data workspace')
    for era in eras:
        folder = Path(c['ws_base'])/era/'ws_signal'
        require(folder.is_dir() and any(folder.glob('*.root')), 'Missing MC workspaces: '+str(folder))
    return c


def prepare(c, out, with_systematics=False):
    if out.exists():
        raise ValueError('Output already exists: '+str(out))
    if re.search(r'\s', str(out)):
        raise ValueError('Output path must not contain whitespace (legacy job writers)')
    if with_systematics and c.get('systematics_reviewed') is not True:
        raise ValueError('Review 2024 nuisances/correlations and set systematics_reviewed=true first')
    out.mkdir(parents=True)
    config = out/'run_config.json'
    config.write_text(json.dumps(c, indent=2)+'\n')
    years = ','.join(c['lumi_fb'])
    cats = ','.join(c['categories'])
    q = shlex.quote
    setup = ('#!/usr/bin/env bash\nset -eo pipefail\n'
             'export PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1\n'
             f'export FINALFIT_RUN_CONFIG={q(str(config))}\n'
             f'export ANALYSIS_PATH={q(str(ROOT))}\n'
             f'export PYTHONPATH={q(str(ROOT/"commonTools"))}:${{PYTHONPATH:-}}\n'
             f'source {q(str(ROOT/"setup.sh"))}\n')
    def shell(name, directory, commands):
        path = out/(name+'.sh')
        log = out/(name+'.log')
        body = setup+f'cd {q(str(directory))}\n'
        body += f'[[ ! -e {q(str(out/(name+".done")))} ]] || {{ echo "Stage already completed"; exit 1; }}\n'
        body += f'exec > >(tee -a {q(str(log))}) 2>&1\n'
        body += commands+'\n'+f'touch {q(str(out/(name+".done")))}\n'
        path.write_text(body)
    tree_cfg = out/'trees2ws_config.py'
    tree_cfg.write_text((ROOT/'Trees2WS/config/config_ttH_tH_2022_2023.py').read_text())
    background = dict(inputWS=c['data_workspace'], cats=cats, catOffset=0,
                      ext=c['tag'], lumi=sum(c['lumi_fb'].values()), sqrts=13.6,
                      year='combined', batch='local', queue='microcentury')
    bg_cfg = out/'background_config.py'
    bg_cfg.write_text('backgroundScriptCfg = '+pprint.pformat(background)+'\n')
    # Background uses a different job layout; leave its official launch explicit.
    (out/'background_command.sh').write_text(setup+f'cd {q(str(ROOT/"Background"))}\n'+
        shlex.join(['python3','-B','RunBackgroundScripts.py','--inputConfig',str(bg_cfg),'--mode','fTestParallel','--printOnly'])+'\n')
    for model in ('DCB', 'SoG'):
        exts = []
        for era in c['lumi_fb']:
            ext = c['tag']+'_'+era+'_'+model
            exts.append(ext)
            cfg = dict(inputWSDir=str(Path(c['ws_base'])/era/'ws_signal'), procs='auto',
                       cats=cats, ext=ext, analysis=ANALYSIS, year=era, massPoints='125',
                       scales='', scalesCorr='FNUF,Material,ScaleEB,ScaleEE' if with_systematics else '',
                       scalesGlobal='', smears='', smearsCorr='Smearing' if with_systematics else '',
                       batch='local', queue='microcentury', jobOpts='')
            cfg_path = out/('config_'+era+'_'+model+'.py')
            cfg_path.write_text('signalScriptCfg = '+pprint.pformat(cfg)+'\n')
            modes = [('fTest','--doPlots --skipWV')] if model == 'SoG' else []
            if with_systematics:
                modes.append(('calcPhotonSyst',''))
            width = c['beamspot_cm'][era]
            flags = '--skipVertexScenarioSplit --MHPolyOrder 0 --doPlots'
            flags += f" --beamspotWidthData {width['data']} --beamspotWidthMC {width['mc']}"
            if not with_systematics: flags += ' --skipSystematics'
            if model == 'DCB': flags += ' --useDCB'
            modes.append(('signalFit', flags))
            commands = f'[[ ! -e outdir_{ext} ]] || {{ echo "Output exists"; exit 1; }}\n'
            for mode, flags in modes:
                cmd = ['python3','-B','-u','RunSignalScripts.py','--inputConfig',str(cfg_path),
                       '--mode',mode,'--printOnly','--modeOpts',flags]
                if mode == 'signalFit': cmd.append('--groupSignalFitJobsByCat')
                commands += shlex.join(cmd)+'\n'
                commands += f'for job in outdir_{ext}/{mode}/jobs/*.sh; do bash "$job"; done\n'
            shell('signal_'+model+'_'+era, ROOT/'Signal', commands)
        packages = out/'packages'/model
        commands = f'[[ ! -e {q(str(packages))} ]] || {{ echo "Packages already exist"; exit 1; }}\n'
        for cat in c['categories']:
            commands += shlex.join(['python3','-B','scripts/packageSignal.py','--cat',cat,
                '--exts',','.join(exts),'--outputExt',model,'--inputDir',str(ROOT/'Signal'),
                '--outputDir',str(packages),'--massPoints','125','--mergeYears'])+'\n'
        shell('package_'+model, ROOT/'Signal', commands)
        yields = out/('yields_'+model)
        cards = out/('card_'+model)
        mode_flags = [] if with_systematics else ['--stat-only']
        cmd = ['bash',str(ROOT/'Datacard/run_makeYields.sh'),'--model',model,'--outdir',str(yields),
               '--years',years,'--ws-base',c['ws_base'],'--signal-dir',str(packages),
               '--background-dir',str(ROOT/'Background'/('outdir_'+c['tag']))]+mode_flags
        shell('yields_'+model, ROOT/'Datacard', shlex.join(cmd))
        cmd = ['bash',str(ROOT/'Datacard/run_makeDatacard.sh'),'--model',model,'--yields',str(yields),
               '--outdir',str(cards),'--years',years,'--analysis',ANALYSIS]+mode_flags
        shell('datacard_'+model, ROOT/'Datacard', shlex.join(cmd))
        cmd = ['python3','-B',str(ROOT/'Combine/build_model_workspace.py'),'--datacard',
               str(cards/('Datacard_'+model+'.txt')),'--model','r_2D_fiducial',
               '--outdir',str(out/('Combine_'+model))]
        (out/('workspace_'+model+'.sh')).write_text(setup+shlex.join(cmd)+'\n')
        commands = ''
        for cat in c['categories']:
            commands += shlex.join(['python3','-B','RunPlotter.py','--inputDir',str(packages),
                '--outputDir',str(out/'plots'/model),'--ext','packaged_'+model,'--cats',cat,
                '--years',years,'--mass','125','--MH','125.09'])+'\n'
        shell('plot_'+model, ROOT/'Signal', commands)
    print('Prepared:',out)
    print('No fits/jobs were launched. Follow HYBRID_2022_2024.md one stage at a time.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',required=True,type=Path)
    p.add_argument('--outdir',type=Path)
    p.add_argument('--write',action='store_true',help='Write new configs and runners; never execute them')
    p.add_argument('--with-systematics',action='store_true',help='Requires systematics_reviewed=true')
    args = p.parse_args()
    try:
        c = validate(json.loads(args.config.read_text()))
        out = (args.outdir or ROOT/'hybrid_runs'/c['tag']).resolve()
        print('Validated:',c['tag'],'eras:',','.join(c['lumi_fb']), 'categories:',len(c['categories']))
        if args.write:
            prepare(c,out,args.with_systematics)
        else:
            print('Validation only; no files written. Add --write to prepare:',out)
    except (ValueError, KeyError, TypeError, OSError) as error:
        p.error(str(error))


if __name__ == '__main__':
    main()
