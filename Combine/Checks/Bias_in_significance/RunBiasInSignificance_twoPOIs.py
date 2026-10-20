"""Conditional significance calibration: fixed background index versus envelope.

The tested strength is zero in generation. --otherValue defines the other
strength's generating truth; --otherMode controls whether it is fixed or
profiled in significance fits. Fixed Higgs processes in the physics model remain.
"""
import argparse
import json
import logging
import math
from pathlib import Path
import shlex
import subprocess
import ROOT

POIS = ('r_ttH', 'r_tHq')


def get_options():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputWSFile', required=True)
    p.add_argument('--MH', type=float, default=125.09)
    p.add_argument('--seed', type=int, default=12345)
    p.add_argument('--nToys', type=int, default=1000)
    p.add_argument('--POI', choices=POIS, required=True, help='Required for every stage')
    p.add_argument('--otherMode', choices=('fixed', 'profiled'), required=True)
    p.add_argument('--otherValue', type=float, required=True,
                   help='Generating truth of other strength; also its fixed fit value in fixed mode')
    p.add_argument('--initial-fit-param', default=None,
                   help='Free nuisance for initial MultiDimFit; default: first free background normalization')
    p.add_argument('--dataset', required=True,
                   help='Dataset in input workspace for setup; choose explicitly (data_obs may be unblinded)')
    p.add_argument('--rMinTtH', type=float, default=0.)
    p.add_argument('--rMaxTtH', type=float, default=15.)
    p.add_argument('--rMinTHq', type=float, default=0.)
    p.add_argument('--rMaxTHq', type=float, default=25.)
    p.add_argument('--label', default='allCats')
    p.add_argument('--outDir', default='.')
    p.add_argument('--mode', choices=('setup', 'generate', 'fixed', 'envelope'), default='setup')
    p.add_argument('--dryRun', action='store_true')
    o = p.parse_args()
    if o.nToys <= 0 or o.seed <= 0 or not math.isfinite(o.MH):
        p.error('Need positive nToys/seed and finite MH')
    other = next(x for x in POIS if x != o.POI)
    for poi, lo, hi in [('r_ttH', o.rMinTtH, o.rMaxTtH), ('r_tHq', o.rMinTHq, o.rMaxTHq)]:
        if not all(math.isfinite(x) for x in (lo, hi)) or not lo < hi:
            p.error('Invalid range for '+poi)
        truth = o.otherValue if poi == other else 0.
        if not math.isfinite(truth) or not lo <= truth <= hi:
            p.error('Null-model truth outside range for '+poi)
    if not o.label or Path(o.label).name != o.label or o.label in ('.', '..'):
        p.error('label must be one folder name')
    return o


class BiasRunner:
    def __init__(self, opt):
        self.o = opt
        self.other = next(x for x in POIS if x != opt.POI)
        self.folder = (Path(opt.outDir).resolve() /
                       f'{opt.label}_{opt.POI}_{self.other}_{opt.otherMode}{opt.otherValue:g}_{opt.nToys}toys')
        self.ws = Path(opt.inputWSFile).resolve()
        if not self.ws.is_file():
            raise RuntimeError(f'Input not found: {self.ws}')
        self.mh = f'{opt.MH:g}'
        self.initial = self.folder / f'higgsCombine_initial.MultiDimFit.mH{self.mh}.root'
        self.toys = self.folder / f'higgsCombine_toy_{opt.nToys}.GenerateOnly.mH{self.mh}.{opt.seed}.root'
        self.common = ['--cminDefaultMinimizerStrategy', '0']
        for flag in ('MINIMIZER_freezeDisassociatedParams', 'MINIMIZER_multiMin_hideConstants',
                     'MINIMIZER_multiMin_maskConstraints', 'MINIMIZER_multiMin_maskChannels=2'):
            self.common += ['--X-rtd', flag]
        self.ranges = f'r_ttH={opt.rMinTtH:g},{opt.rMaxTtH:g}:r_tHq={opt.rMinTHq:g},{opt.rMaxTHq:g}'
        self.truth = f'MH={self.mh},{opt.POI}=0,{self.other}={opt.otherValue:g}'
        self.settings = dict(workspace=str(self.ws), mass=opt.MH, poi=opt.POI,
                             otherMode=opt.otherMode, otherValue=opt.otherValue,
                             ranges=self.ranges, dataset=opt.dataset, nToys=opt.nToys,
                             initialFitParam=opt.initial_fit_param)
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        if not opt.dryRun:
            self.folder.mkdir(parents=True, exist_ok=True)
            manifest = self.folder / 'settings.json'
            if manifest.exists() and json.loads(manifest.read_text()) != self.settings:
                raise RuntimeError('Run settings differ from existing settings.json; use another label')
            if not manifest.exists():
                if opt.mode != 'setup':
                    raise RuntimeError('Run setup first')
                manifest.write_text(json.dumps(self.settings, indent=2)+'\n')

    def run(self, args):
        cmd = ['combine', '-m', self.mh, *args]
        print(shlex.join(cmd), flush=True)
        if self.o.dryRun:
            return
        log = self.folder / f'{self.o.mode}_seed{self.o.seed}.log'
        with log.open('a') as out:
            out.write(shlex.join(cmd)+'\n'); out.flush()
            process = subprocess.Popen(cmd, cwd=str(self.folder), stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(line, end='', flush=True); out.write(line)
            if process.wait():
                raise RuntimeError(f'Combine failed; inspect {log}')

    def setup(self):
        f = ROOT.TFile.Open(str(self.ws))
        if not f or f.IsZombie():
            raise RuntimeError('Cannot open input workspace')
        w = f.Get('w')
        if not w or not w.data(self.o.dataset):
            raise RuntimeError('Workspace w or requested setup dataset missing')
        mc = w.obj('ModelConfig')
        if not mc or any(not w.var(x) for x in POIS):
            raise RuntimeError('Expected ModelConfig and both signal strengths')
        indices = [x.GetName() for x in w.allCats() if x.GetName().startswith('pdfindex')]
        if not indices:
            raise RuntimeError('No background PDF indices found')
        # Register the other strength as a nuisance so the significance likelihood
        # explicitly profiles it. The source workspace is never overwritten.
        nuisance = ROOT.RooArgSet(mc.GetNuisanceParameters())
        nuisance.remove(ROOT.RooArgSet(w.var(self.o.POI)), True, True)
        nuisance.add(w.var(self.other), True)
        mc.SetNuisanceParameters(nuisance)
        mc.SetParametersOfInterest(ROOT.RooArgSet(w.var(self.o.POI)))
        for x in POIS:
            w.var(x).setRange(getattr(self.o, 'rMinTtH' if x == 'r_ttH' else 'rMinTHq'),
                              getattr(self.o, 'rMaxTtH' if x == 'r_ttH' else 'rMaxTHq'))
        param = self.o.initial_fit_param
        if param is None:
            candidates = [x.GetName() for x in w.allVars() if x.InheritsFrom('RooRealVar')
                          and not x.isConstant() and 'bkg' in x.GetName().lower()
                          and 'norm' in x.GetName().lower() and mc.GetPdf().dependsOn(x)]
            if not candidates:
                raise RuntimeError('Specify --initial-fit-param: no free background normalization found')
            param = sorted(candidates)[0]
        var = w.var(param)
        if not var or var.isConstant() or param in (*POIS, 'MH') or not mc.GetPdf().dependsOn(var):
            raise RuntimeError('initial-fit-param must be a free nuisance other than MH/strengths')
        prepared = self.folder / 'study_input.root'
        if not self.o.dryRun:
            w.writeToFile(str(prepared))
        self.run(['-d', str(prepared), '-D', self.o.dataset, '-M', 'MultiDimFit',
                  *self.common, '-P', param, '--floatOtherPOIs', '0',
                  '--setParameters', self.truth, '--freezeParameters', 'MH,'+','.join(POIS),
                  '-n', '_initial', '--saveWorkspace', '--saveFitResult',
                  '--saveSpecifiedIndex', ','.join(indices)])
        f.Close()
        if self.o.dryRun:
            return
        result = ROOT.TFile.Open(str(self.initial), 'UPDATE')
        if not result or result.IsZombie():
            raise RuntimeError('Missing setup output')
        tree = result.Get('limit')
        fit_file = ROOT.TFile.Open(str(self.folder / 'multidimfit_initial.root'))
        fit = fit_file.Get('fit_mdf') if fit_file and not fit_file.IsZombie() else None
        if not tree or not tree.GetEntries() or not fit or fit.status() != 0:
            raise RuntimeError('Setup fit missing or nonzero fit status; inspect before continuing')
        tree.GetEntry(0)
        (self.folder / 'pdfindex.json').write_text(json.dumps(
            {x: int(getattr(tree, x)) for x in indices}, indent=2)+'\n')
        # Combine strips frozen nuisances during setup. Restore the other
        # strength's registration in the saved model for later profiled fits.
        saved = result.Get('w')
        if not saved:
            raise RuntimeError('Missing saved workspace')
        saved_mc = saved.obj('ModelConfig')
        if self.o.otherMode == 'profiled':
            saved_nuis = ROOT.RooArgSet(saved_mc.GetNuisanceParameters())
            saved_nuis.add(saved.var(self.other), True)
            saved_mc.SetNuisanceParameters(saved_nuis)
            result.cd()
            saved.Write('w', ROOT.TObject.kOverwrite)
        result.Close()
        fit_file.Close()

    def generate(self):
        self.run(['-d', str(self.initial), '-M', 'GenerateOnly', '--snapshotName', 'MultiDimFit',
                  '--setParameters', self.truth, '--freezeParameters', 'MH,'+','.join(POIS),
                  '--setParameterRanges', self.ranges, '--toysNoSystematics', '--saveToys',
                  '-n', f'_toy_{self.o.nToys}', '-t', str(self.o.nToys), '-s', str(self.o.seed)])

    def significance(self):
        if not self.o.dryRun and not self.toys.is_file():
            raise RuntimeError('Toys missing; run generate first')
        freeze = ['MH']; sets = [self.truth]
        extra = []
        if self.o.otherMode == 'fixed':
            freeze.append(self.other)
        else:
            extra += ['--floatParameters', self.other]
        if self.o.mode == 'fixed':
            if self.o.dryRun and not (self.folder / 'pdfindex.json').exists():
                f = ROOT.TFile.Open(str(self.ws))
                w = f.Get('w')
                indices = {x.GetName(): x.getIndex() for x in w.allCats() if x.GetName().startswith('pdfindex')}
                f.Close()
                print('Preview indices below use input values; real fixed fits use setup best-fit indices.')
            else:
                with (self.folder / 'pdfindex.json').open() as f:
                    indices = json.load(f)
            freeze += list(indices)
            sets += [f'{k}={v}' for k,v in indices.items()]
        self.run(['-d', str(self.initial), '-M', 'Significance', '--snapshotName', 'MultiDimFit',
                  *self.common, '--redefineSignalPOIs', self.o.POI, *extra,
                  '--setParameterRanges', self.ranges, '--setParameters', ','.join(sets),
                  '--freezeParameters', ','.join(freeze), '-t', str(self.o.nToys),
                  '--toysFile', str(self.toys), '-n',
                  f'_{self.o.mode}_{self.o.POI}_test_{self.other}_{self.o.otherMode}_{self.o.nToys}_seed{self.o.seed}',
                  '--X-rtd', 'ADDNLL_RECURSIVE=1'])


if __name__ == '__main__':
    options = get_options()
    runner = BiasRunner(options)
    print('Study folder:', runner.folder, flush=True)
    if options.mode == 'setup': runner.setup()
    elif options.mode == 'generate': runner.generate()
    else: runner.significance()
