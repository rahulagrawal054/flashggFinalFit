#!/usr/bin/env python
"""
Two-POI nominal bias study (r_ttH, r_tHq), per-category.

Same three stages as the original RunBiasStudy.py (--toys / --fits / --plots),
extended to:
  - inject BOTH r_ttH and r_tHq together when throwing toys
  - scan a full grid of truth values for both POIs (--grid, applied to both)
  - fit ONE POI per script call (--poi), profiling the other, matching the
    real analysis's significance/limit commands. Run the script twice
    (--poi r_ttH, then --poi r_tHq) to cover both.

Requires a per-category workspace: one multipdf, one pdfindex, as described
in README.md ("combineCards.py Datacard.txt --ic cat_name" + text2workspace).
"""

import os
from os import system, path
import glob
import json
import hashlib
import datetime
import socket
import sys
from collections import Counter
from pathlib import Path
import math
import shlex
import shutil
import subprocess
from biasUtils import rooArgSetToList, raiseMultiError, raiseFailError, shortName
from optparse import OptionParser
from time import sleep

POIS = ['r_ttH', 'r_tHq']

parser = OptionParser()
parser.add_option("-d", "--datacard", default="Datacard.root")
parser.add_option("-w", "--workspace", default="w")
parser.add_option("--toys", action="store_true", default=False)
parser.add_option("-n", "--nToys", default=1000, type="int")
parser.add_option("--fits", action="store_true", default=False)
parser.add_option("--plots", action="store_true", default=False)
parser.add_option("--grid", default="0,1,2",
                   help="Comma-separated truth values applied to BOTH r_ttH and r_tHq; "
                        "the full grid x grid is scanned (default: %default)")
parser.add_option("--gridTtH", default=None, help="Independent injected r_ttH grid; overrides --grid for r_ttH")
parser.add_option("--gridTHq", default=None, help="Independent injected r_tHq grid; overrides --grid for r_tHq")
parser.add_option("--poi", default=None, choices=POIS,
                   help="POI to fit/plot in this call: one of %s. Required for --fits "
                        "and --plots; run the script twice to cover both POIs." % POIS)
parser.add_option("--floatOtherPOIs", default=1, type="int",
                  help="1 profiles the other POI; 0 fixes it to its injected value (default: %default)")
parser.add_option("-m", "--mH", default=125.08, type="float")
parser.add_option("-c", "--combineOptions",
                  default="--cminDefaultMinimizerStrategy 0 "
                          "--X-rtd MINIMIZER_freezeDisassociatedParams "
                          "--X-rtd MINIMIZER_multiMin_hideConstants "
                          "--X-rtd MINIMIZER_multiMin_maskConstraints "
                          "--X-rtd MINIMIZER_multiMin_maskChannels=2 "
                          "--freezeParameters MH",
                  help="Fit-only options; defaults match the repository envelope minimizer settings")
parser.add_option("-s", "--seed", default=12345, type="int")
parser.add_option("--dryRun", action="store_true", default=False)
parser.add_option("--rMinTtH", default=-5., type="float")
parser.add_option("--rMaxTtH", default=15., type="float")
parser.add_option("--rMinTHq", default=-25., type="float")
parser.add_option("--rMaxTHq", default=25., type="float")
parser.add_option("--split", default=None, type="int",
                   help="Split toys/fits into chunks of this size (condor walltime/memory). "
                        "Default: no splitting, run --nToys in one combine call.")
parser.add_option("--selectFunction", default=None,
                   help="Only run functions whose pdf name contains this string "
                        "(e.g. 'bern', 'exp1'). Default: all functions in the envelope.")
parser.add_option("--gaussianFit", action="store_true", default=False)
(opts, args) = parser.parse_args()
if not (opts.toys or opts.fits or opts.plots):
    parser.error("Choose --toys, --fits, and/or --plots")
if opts.nToys <= 0 or (opts.split is not None and opts.split <= 0):
    parser.error("nToys and split must be positive")
if opts.seed < 0:
    parser.error("Use an explicit nonnegative seed, identical for all stages")
if opts.floatOtherPOIs not in (0, 1):
    parser.error("floatOtherPOIs must be 0 or 1")
if opts.rMinTtH >= opts.rMaxTtH or opts.rMinTHq >= opts.rMaxTHq:
    parser.error("Each fit range minimum must be below its maximum")


def run(cmd, dry=False):
    print(cmd, flush=True)
    if not dry:
        Path("BiasLogs").mkdir(exist_ok=True)
        tokens = shlex.split(cmd)
        tag = tokens[tokens.index("-n") + 1] if "-n" in tokens else "merge"
        logPath = Path("BiasLogs") / (tag + ".log")
        started = datetime.datetime.now(datetime.timezone.utc)
        with open(logPath, "w") as log:
            proc = subprocess.run(tokens, stdout=log, stderr=subprocess.STDOUT)
        record = {"command": tokens, "returnCode": proc.returncode,
                  "startedUTC": started.isoformat(),
                  "finishedUTC": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  "elapsedSeconds": (datetime.datetime.now(datetime.timezone.utc) - started).total_seconds(),
                  "host": socket.gethostname(), "log": str(logPath.resolve())}
        logPath.with_suffix(".command.json").write_text(json.dumps(record, indent=2))
        proc.check_returncode()


def move_output(pattern, destination):
    if opts.dryRun:
        print("Move %s -> %s" % (pattern, destination))
        return
    matches = glob.glob(pattern)
    if len(matches) != 1:
        raise RuntimeError("Expected exactly one output for %s, found %s" % (pattern, matches))
    shutil.move(matches[0], destination)


def validate_plot_fit_settings(logs, options):
    """Reject mislabeled plotting settings when original commands are available."""
    verified = 0
    expected_ranges = {"r_ttH": [options.rMinTtH, options.rMaxTtH],
                       "r_tHq": [options.rMinTHq, options.rMaxTHq]}
    for log in logs:
        sidecar = log.with_suffix('.command.json')
        if not sidecar.exists():
            print("[WARNING] Missing fit command sidecar: %s; plot settings are unverified" % sidecar)
            continue
        command = json.loads(sidecar.read_text())["command"]
        def value(flag):
            for i, token in enumerate(command):
                if token == flag:
                    return command[i + 1]
                if token.startswith(flag + '='):
                    return token.split('=', 1)[1]
            raise RuntimeError("Missing %s in %s; cannot verify plot settings" % (flag, sidecar))
        ranges = {}
        for item in value('--setParameterRanges').split(':'):
            name, bounds = item.split('=', 1)
            ranges[name] = [float(x) for x in bounds.split(',')]
        for poi, bounds in expected_ranges.items():
            if ranges.get(poi) != bounds:
                raise RuntimeError("Plot range for %s %s differs from saved fit range %s in %s; repeat the fit range options" %
                                   (poi, bounds, ranges.get(poi), sidecar))
        mode = int(value('--floatOtherPOIs'))
        if mode != options.floatOtherPOIs:
            raise RuntimeError("Plot --floatOtherPOIs %s differs from saved fit value %s in %s; repeat the fit option" %
                               (options.floatOtherPOIs, mode, sidecar))
        verified += 1
    return verified == len(logs)


if opts.split is not None and opts.nToys > opts.split and not opts.nToys % opts.split == 0:
    raise RuntimeError('nToys %g needs to be smaller than or divisible by split %g' % (opts.nToys, opts.split))
if (opts.fits or opts.plots) and opts.poi is None:
    raise SystemExit("--poi is required for --fits and --plots (choose one of %s); "
                      "run the script twice to cover both POIs." % POIS)

gridVals = [float(v) for v in opts.grid.split(",")]
if not gridVals or len(set(gridVals)) != len(gridVals) or not all(math.isfinite(v) for v in gridVals):
    parser.error("Grid must contain unique finite values")
def injection_grid(value):
    values = [float(v) for v in value.split(",")]
    if not values or len(set(values)) != len(values) or not all(math.isfinite(v) for v in values):
        parser.error("Injection grids must contain unique finite values")
    return values

gridTtH = injection_grid(opts.gridTtH) if opts.gridTtH is not None else gridVals
gridTHq = injection_grid(opts.gridTHq) if opts.gridTHq is not None else gridVals
gridPoints = [(ttH, tHq) for ttH in gridTtH for tHq in gridTHq]
for poi, values, lo, hi in [('r_ttH', gridTtH, opts.rMinTtH, opts.rMaxTtH),
                            ('r_tHq', gridTHq, opts.rMinTHq, opts.rMaxTHq)]:
    if not all(math.isfinite(v) for v in [lo, hi]):
        parser.error("%s range must have finite endpoints" % poi)
    for value in values:
        if not lo <= value <= hi:
            parser.error("Injected %s=%g is outside [%g,%g]; refusing silent clipping" % (poi, value, lo, hi))
rRanges = "r_ttH=%g,%g:r_tHq=%g,%g" % (opts.rMinTtH, opts.rMaxTtH, opts.rMinTHq, opts.rMaxTHq)

print()
print("Truth grid (%d points): %s" % (len(gridPoints), gridPoints))
print()

import ROOT as r
r.gROOT.SetBatch(True)
r.gStyle.SetOptStat(2211)

inputFile = r.TFile.Open(opts.datacard)
if not inputFile or inputFile.IsZombie():
    raise RuntimeError("Cannot open workspace file: " + opts.datacard)
ws = inputFile.Get(opts.workspace)
if not ws:
    raise RuntimeError("Workspace not found: " + opts.workspace)
model = ws.obj("ModelConfig")
if not model or not all(model.GetParametersOfInterest().find(poi) for poi in POIS):
    raise RuntimeError("ModelConfig must define both r_ttH and r_tHq as POIs")

pdfs = rooArgSetToList(ws.allPdfs())
multipdfName = None
for pdf in pdfs:
    if pdf.InheritsFrom("RooMultiPdf"):
        if multipdfName is not None: raiseMultiError()
        multipdfName = pdf.GetName()
        print('Conduct bias study for multipdf called %s' % multipdfName)
if multipdfName is None:
    raise RuntimeError("Workspace must contain exactly one RooMultiPdf")
multipdf = ws.pdf(multipdfName)
print()

varlist = rooArgSetToList(ws.allCats())
indexName = None
for var in varlist:
    if var.GetName().startswith('pdfindex'):
        if indexName is not None: raiseMultiError()
        indexName = var.GetName()
        print('Found index called %s' % indexName)
print()

if indexName is None:
    raise RuntimeError("Workspace must contain one pdfindex category")
from collections import OrderedDict as od
indexNameMap = od()
for ipdf in range(multipdf.getNumPdfs()):
    if opts.selectFunction is not None:
        if not multipdf.getPdf(ipdf).GetName().count(opts.selectFunction): continue
    indexNameMap[ipdf] = multipdf.getPdf(ipdf).GetName()


if not indexNameMap:
    raise RuntimeError("No background functions matched --selectFunction")


def gridTag(ttH, tHq):
    return 'ttH%s_tHq%s_seed%d' % (repr(ttH), repr(tHq), opts.seed)


def toyName(name, ttH, tHq, split=None):
    retval = 'BiasToys/biasStudy_%s_%s_toys.root' % (name, gridTag(ttH, tHq))
    if split is not None:
        retval = retval.replace('_toys.root', '_split%g_toys.root' % int(split))
    return retval


def fitName(name, ttH, tHq, poi, split=None):
    retval = 'BiasFits/biasStudy_%s_%s_%s_fits.root' % (name, gridTag(ttH, tHq), poi)
    if split is not None:
        retval = retval.replace('_fits.root', '_split%g_fits.root' % int(split))
    return retval


def plotName(name, ttH, tHq, poi):
    return 'BiasPlots/biasStudy_%s_%s_%s_pulls' % (name, gridTag(ttH, tHq), poi)


if opts.toys:
    if not opts.dryRun and not path.isdir('BiasToys'): system('mkdir -p BiasToys')
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for (ttH, tHq) in gridPoints:
            toyCmdBase = ('combine -m %.4f -d %s -M GenerateOnly -s %g --saveToys %s --toysNoSystematics'
                          % (opts.mH, shlex.quote(opts.datacard), opts.seed, '--setParameterRanges '+rRanges))
            setParams = '%s=%g,r_ttH=%g,r_tHq=%g' % (indexName, ipdf, ttH, tHq)
            if opts.split is not None and opts.nToys > opts.split:
                for isplit in range(opts.nToys // opts.split):
                    toyCmd = toyCmdBase + (' -t %g -n _%s_%s_split%g --setParameters %s --freezeParameters %s'
                                           % (opts.split, name, gridTag(ttH, tHq), isplit, setParams, indexName))
                    toyCmd = toyCmd.replace('-s %g' % opts.seed, '-s %g' % (opts.seed + isplit), 1)
                    run(toyCmd, dry=opts.dryRun)
                    # Output is moved only after Combine returns successfully.
                    move_output('higgsCombine_%s_%s_split%d.GenerateOnly.*.%d.root' % (name, gridTag(ttH, tHq), isplit, opts.seed + isplit), toyName(name, ttH, tHq, split=isplit))
            else:
                toyCmd = toyCmdBase + (' -t %g -n _%s_%s --setParameters %s --freezeParameters %s'
                                       % (opts.nToys, name, gridTag(ttH, tHq), setParams, indexName))
                run(toyCmd, dry=opts.dryRun)
                move_output('higgsCombine_%s_%s.GenerateOnly.*.%d.root' % (name, gridTag(ttH, tHq), opts.seed), toyName(name, ttH, tHq))
print()

if opts.fits:
    if not opts.dryRun and not path.isdir('BiasFits'): system('mkdir -p BiasFits')
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for (ttH, tHq) in gridPoints:
            fitCmdBase = ('combine -m %.4f -d %s -M MultiDimFit -P %s --algo singles '
                         '--floatOtherPOIs %d --saveInactivePOI 1 --setParameters r_ttH=%g,r_tHq=%g --setParameterRanges %s %s'
                         % (opts.mH, shlex.quote(opts.datacard), opts.poi, opts.floatOtherPOIs, ttH, tHq, rRanges, opts.combineOptions))
            if opts.split is not None and opts.nToys > opts.split:
                for isplit in range(opts.nToys // opts.split):
                    fitCmd = fitCmdBase + (' -t %g -n _%s_%s_%s_split%g --toysFile=%s'
                                           % (opts.split, name, gridTag(ttH, tHq), opts.poi, isplit,
                                              toyName(name, ttH, tHq, split=isplit)))
                    run(fitCmd, dry=opts.dryRun)
                    # Output is moved only after Combine returns successfully.
                    move_output('higgsCombine_%s_%s_%s_split%d.MultiDimFit.*.root' % (name, gridTag(ttH, tHq), opts.poi, isplit), fitName(name, ttH, tHq, opts.poi, split=isplit))
                run('hadd -f %s %s' % (fitName(name, ttH, tHq, opts.poi), ' '.join(fitName(name, ttH, tHq, opts.poi, split=i) for i in range(opts.nToys // opts.split))), dry=opts.dryRun)
            else:
                fitCmd = fitCmdBase + (' -t %g -n _%s_%s_%s --toysFile=%s'
                                       % (opts.nToys, name, gridTag(ttH, tHq), opts.poi,
                                          toyName(name, ttH, tHq)))
                run(fitCmd, dry=opts.dryRun)
                move_output('higgsCombine_%s_%s_%s.MultiDimFit.*.root' % (name, gridTag(ttH, tHq), opts.poi), fitName(name, ttH, tHq, opts.poi))
print()

if opts.plots and not opts.dryRun:
    if not path.isdir('BiasPlots'): system('mkdir -p BiasPlots')
    biasResults = {}
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for (ttH, tHq) in gridPoints:
            truth = ttH if opts.poi == 'r_ttH' else tHq
            prefix = '_%s_%s_%s' % (name, gridTag(ttH, tHq), opts.poi)
            logs = [Path('BiasLogs') / (prefix + '.log')]
            if opts.split is not None and opts.nToys > opts.split:
                logs = [Path('BiasLogs') / (prefix + '_split%d.log' % i)
                        for i in range(opts.nToys // opts.split)]
            plotSettingsVerified = validate_plot_fit_settings(logs, opts)
            tfile = r.TFile(fitName(name, ttH, tHq, opts.poi))
            if not tfile or tfile.IsZombie():
                raise RuntimeError('Cannot open fit file')
            tree = tfile.Get('limit')
            if not tree or not tree.GetBranch(opts.poi):
                raise RuntimeError('Missing limit tree or POI branch')
            pullHist = r.TH1F('pulls_%s_%s_%s' % (name, gridTag(ttH, tHq), opts.poi),
                              'Pull of %s using envelope, truth %s, %s=%g' % (opts.poi, name, opts.poi, truth),
                              80, -4., 4.)
            pullHist.GetXaxis().SetTitle('Pull')
            pullHist.GetYaxis().SetTitle('Entries')

            pullEntries = 0
            failures = Counter()
            toyDiagnostics = []
            boundaryCount = 0
            bounds = (opts.rMinTtH, opts.rMaxTtH) if opts.poi == 'r_ttH' else (opts.rMinTHq, opts.rMaxTHq)
            boundaryTolerance = 1.e-4 * max(1., bounds[1] - bounds[0])
            entries = int(tree.GetEntries())
            for offset in range(0, entries, 3):
                detail = {"treeEntry": offset, "toyId": None}
                if offset + 2 >= entries:
                    detail["reason"] = "incomplete_triplet"
                    failures[detail["reason"]] += 1
                    toyDiagnostics.append(detail)
                    continue
                values, quantiles, otherValues = [], [], []
                otherPoi = 'r_tHq' if opts.poi == 'r_ttH' else 'r_ttH'
                for j in range(3):
                    tree.GetEntry(offset + j)
                    if j == 0 and tree.GetBranch('iToy'):
                        detail['toyId'] = int(tree.iToy)
                    values.append(float(getattr(tree, opts.poi)))
                    quantiles.append(float(tree.quantileExpected))
                    if tree.GetBranch(otherPoi):
                        otherValues.append(float(getattr(tree, otherPoi)))
                detail['quantiles'] = quantiles
                detail['values'] = dict(zip(['bestFit', 'lower', 'upper'], values))
                detail['otherPoiValues'] = otherValues
                bf, lo, hi = values
                boundary = any(abs(v - edge) <= boundaryTolerance for v in values for edge in bounds)
                detail['boundaryHit'] = boundary
                boundaryCount += int(boundary)
                reason = None
                if not all(math.isfinite(v) for v in values + quantiles):
                    reason = 'nonfinite_value'
                elif not all(abs(q - expected) < .001 for q, expected in zip(quantiles, [-1., -.32, .32])):
                    reason = 'unexpected_quantiles'
                elif hi <= lo:
                    reason = 'nonpositive_uncertainty'
                else:
                    pull = (bf - truth) / (0.5 * (hi - lo))
                    if not math.isfinite(pull):
                        reason = 'nonfinite_pull'
                    else:
                        pullHist.Fill(pull)
                        pullEntries += 1
                        detail['pull'] = pull
                detail['accepted'] = reason is None
                detail['reason'] = reason
                if reason:
                    failures[reason] += 1
                toyDiagnostics.append(detail)

            # Failed Combine fits can be omitted from the tree. Do not invent IDs.
            missing = max(0, opts.nToys - entries // 3)
            logRecords, warningCounts = [], Counter()
            version = None
            for logPath in logs:
                record = {"log": str(logPath.resolve()), "exists": logPath.exists()}
                sidecar = logPath.with_suffix('.command.json')
                if sidecar.exists():
                    record.update(json.loads(sidecar.read_text()))
                if logPath.exists():
                    with logPath.open(errors='replace') as log:
                        for line in log:
                            if '<<< v' in line:
                                version = line.strip()
                            for label, text in [('multiDimFitFailed', 'MultiDimFit failed'),
                                                ('negativeEvents', 'Number of events is negative'),
                                                ('nanMessages', 'function value is NAN'),
                                                ('boundaryMessages', 'boundary')]:
                                if text.lower() in line.lower():
                                    warningCounts[label] += 1
                logRecords.append(record)

            canv = r.TCanvas()
            pullHist.Draw()
            mean, sigma = None, None
            fitStatus = None
            gaussianDetails = {"requested": opts.gaussianFit, "status": None,
                               "biasError": None, "sigmaError": None, "chi2": None, "ndf": None}
            if opts.gaussianFit and pullHist.Integral() >= 3:
                r.gStyle.SetOptFit(111)
                fitStatus = int(pullHist.Fit('gaus', 'QS'))
                gaussianDetails["status"] = fitStatus
                fitFunc = pullHist.GetFunction('gaus')
                if fitFunc and fitStatus == 0:
                    mean = fitFunc.GetParameter(1)
                    sigma = fitFunc.GetParameter(2)
                    gaussianDetails.update(biasError=fitFunc.GetParError(1),
                                           sigmaError=fitFunc.GetParError(2),
                                           chi2=fitFunc.GetChisquare(), ndf=fitFunc.GetNDF())

            biasResults['%s_%s_%s' % (name, gridTag(ttH, tHq), opts.poi)] = {
                "function": name, "poi": opts.poi, "seed": opts.seed,
                "schemaVersion": 2,
                "metadata": {"createdUTC": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                             "host": socket.gethostname(), "workingDirectory": str(Path.cwd()),
                             "invocation": sys.argv, "pythonVersion": sys.version,
                             "rootVersion": r.gROOT.GetVersion(), "combineVersionFromLog": version,
                             "workspace": str(Path(opts.datacard).resolve()), "workspaceName": opts.workspace,
                             "workspaceSizeBytes": Path(opts.datacard).stat().st_size,
                             "scriptSHA256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                             "pdfName": pdfName, "pdfIndex": ipdf, "pdfIndexName": indexName,
                             "mass": opts.mH, "fitOptions": opts.combineOptions,
                             "fitRanges": {"r_ttH": [opts.rMinTtH, opts.rMaxTtH],
                                           "r_tHq": [opts.rMinTHq, opts.rMaxTHq]},
                             "otherPoiProfiled": bool(opts.floatOtherPOIs),
                             "floatOtherPOIs": opts.floatOtherPOIs,
                             "fitSettingsVerified": plotSettingsVerified, "toysNoSystematics": True,
                             "nToysRequested": opts.nToys, "split": opts.split,
                             "settingsSource": "plot invocation; command sidecars are authoritative when present"},
                "fitFile": str(Path(fitName(name, ttH, tHq, opts.poi)).resolve()),
                "fitLogs": logRecords, "warningCounts": dict(warningCounts),
                "treeEntries": entries, "completeTriplets": entries // 3,
                "missingToyResults": missing, "rejectionReasons": dict(failures),
                "boundaryHits": boundaryCount, "boundaryTolerance": boundaryTolerance,
                "boundaryPolicy": "flagged, not excluded", "toyDiagnostics": toyDiagnostics,
                "toyIdNote": "iToy is used when available; missing fits have no inferred toy ID",
                "gaussianFit": gaussianDetails,
                "histogram": {"bins": 80, "range": [-4., 4.],
                              "underflow": pullHist.GetBinContent(0),
                              "overflow": pullHist.GetBinContent(81)},
                "truth_r_ttH": ttH, "truth_r_tHq": tHq,
                "bias": mean, "sigma": sigma,
                "pullEntries": int(pullEntries),
                "failedToys": int(opts.nToys - pullEntries),
                "meanPull": pullHist.GetMean(), "rmsPull": pullHist.GetRMS(),
            }
            canv.SaveAs('%s.pdf' % plotName(name, ttH, tHq, opts.poi))
            canv.SaveAs('%s.png' % plotName(name, ttH, tHq, opts.poi))

    import json
    outJson = 'BiasPlots/BiasResults_%s_seed%d.json' % (opts.poi, opts.seed)
    with open(outJson, 'w') as f:
        def clean(value):
            if isinstance(value, float) and not math.isfinite(value):
                return None
            if isinstance(value, dict):
                return {k: clean(v) for k, v in value.items()}
            if isinstance(value, list):
                return [clean(v) for v in value]
            return value
        json.dump(clean(biasResults), f, indent=2, allow_nan=False)
    print('Wrote %s' % outJson)
