#!/usr/bin/env python
"""
Single-POI (r_ttH) nominal bias study, for workspaces built with the
r_1D_ttH_fixedtHq physics model (r_tHq fixed to 1 in the model itself,
not a fittable parameter). Intended for "Group A" categories where tHq
acceptance is negligible (e.g. ttH_had_1: ~0.01 expected tHq events).

Same three stages as the original RunBiasStudy.py (--toys / --fits / --plots),
extended with:
  - --grid: scan a list of truth values for r_ttH (default matches the
    slide's recommendation: 0, 1 - add the expected limit later once known)
  - reproducible seeds: if --seed -1, a seed is generated once up front,
    logged, and reused consistently for every combine call in this run,
    so the whole run can be repeated exactly later
  - every combine command's full stdout/stderr is captured to a per-call
    log file under BiasLogs/, in addition to the console, for debugging
  - --plots writes one PNG/PDF per (function, truth point) AND one
    combined BiasResults.json with, per point: how many toys were thrown,
    how many fits succeeded vs failed, the histogram's raw mean/RMS, the
    Gaussian fit's bias/sigma (+ their fit errors and chi2/ndf), the seed
    used, and whether it passes the 0.14 / 0.2 thresholds.
"""

import os
import sys
import json
import random
import subprocess
from os import path
from optparse import OptionParser
from time import sleep

from biasUtils import rooArgSetToList, raiseMultiError, shortName

PASS_THRESHOLD = 0.14
WARN_THRESHOLD = 0.20

parser = OptionParser()
parser.add_option("-d", "--datacard", default="Datacard.root",
                   help="Workspace built with the r_1D_ttH_fixedtHq model (r_ttH is the ONLY POI)")
parser.add_option("-w", "--workspace", default="w")
parser.add_option("--toys", action="store_true", default=False)
parser.add_option("-n", "--nToys", default=1000, type="int")
parser.add_option("--fits", action="store_true", default=False)
parser.add_option("--plots", action="store_true", default=False)
parser.add_option("--grid", default="0,1",
                   help="Comma-separated truth values for r_ttH (default: %default). "
                        "Add the category's expected limit here once computed, e.g. 0,1,2.1")
parser.add_option("-m", "--mH", default=125.08, type="float")
parser.add_option("-c", "--combineOptions",
                   default="--cminDefaultMinimizerStrategy 0 "
                           "--X-rtd MINIMIZER_freezeDisassociatedParams "
                           "--X-rtd MINIMIZER_multiMin_hideConstants "
                           "--X-rtd MINIMIZER_multiMin_maskConstraints "
                           "--X-rtd MINIMIZER_multiMin_maskChannels=2 "
                           "--freezeParameters MH",
                   help="Extra combine options for the FIT step (default includes the usual "
                        "minimizer settings + freezing MH; override with your own string if needed)")
parser.add_option("-s", "--seed", default=-1, type="int",
                   help="Fixed seed for reproducibility. -1 (default): generate one now, "
                        "log it, and reuse it for every call in this run.")
parser.add_option("--dryRun", action="store_true", default=False)
parser.add_option("--rMin", default=-1., type="float", help="r_ttH fit range min (default: %default)")
parser.add_option("--rMax", default=3., type="float", help="r_ttH fit range max (default: %default)")
parser.add_option("--selectFunction", default=None,
                   help="Only run functions whose pdf name contains this string "
                        "(e.g. 'bern', 'exp1'). Default: all functions in the envelope.")
parser.add_option("--gaussianFit", action="store_true", default=True)
(opts, args) = parser.parse_args()

# --- reproducible seed, fixed once for the whole run, logged either way ---
if opts.seed == -1:
    opts.seed = random.randint(1, 2**31 - 1)
    print("No --seed given: generated seed %d for this run. "
          "Pass -s %d next time to reproduce it exactly." % (opts.seed, opts.seed))
else:
    print("Using fixed seed %d" % opts.seed)
print()

gridVals = [float(v) for v in opts.grid.split(",")]
print("Truth grid for r_ttH (%d points): %s" % (len(gridVals), gridVals))
print()

for d in ("BiasToys", "BiasFits", "BiasPlots", "BiasLogs"):
    if not path.isdir(d):
        os.system("mkdir -p %s" % d)


def run(cmd, tag, dry=False):
    """Print + log a command. Captures full stdout/stderr to BiasLogs/<tag>.log
    regardless of dryRun (so the exact command attempted is always on record),
    and also echoes to the console as it runs."""
    logFile = "BiasLogs/%s.log" % tag
    print("[%s] %s" % (tag, cmd))
    with open(logFile, "w") as lf:
        lf.write(cmd + "\n\n")
        if dry:
            lf.write("(dry run - not executed)\n")
            return True
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, universal_newlines=True)
        for line in proc.stdout:
            sys.stdout.write(line)
            lf.write(line)
        proc.wait()
        if proc.returncode != 0:
            lf.write("\n[FAILED] exit code %d\n" % proc.returncode)
            print("[%s] FAILED (exit code %d) - see %s" % (tag, proc.returncode, logFile))
            return False
    return True


def toyName(name, truth):
    return "BiasToys/biasStudy_%s_ttH%g_toys.root" % (name, truth)


def fitName(name, truth):
    return "BiasFits/biasStudy_%s_ttH%g_fits.root" % (name, truth)


def plotName(name, truth):
    return "BiasPlots/biasStudy_%s_ttH%g_pulls" % (name, truth)


import ROOT as r
r.gROOT.SetBatch(True)
r.gStyle.SetOptStat(2211)

ws = r.TFile(opts.datacard).Get(opts.workspace)

pdfs = rooArgSetToList(ws.allPdfs())
multipdfName = None
for pdf in pdfs:
    if pdf.InheritsFrom("RooMultiPdf"):
        if multipdfName is not None: raiseMultiError()
        multipdfName = pdf.GetName()
        print('Conduct bias study for multipdf called %s' % multipdfName)
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

from collections import OrderedDict as od
indexNameMap = od()
for ipdf in range(multipdf.getNumPdfs()):
    if opts.selectFunction is not None:
        if not multipdf.getPdf(ipdf).GetName().count(opts.selectFunction): continue
    indexNameMap[ipdf] = multipdf.getPdf(ipdf).GetName()
print("Functions in envelope: %s" % {ip: shortName(n) for ip, n in indexNameMap.items()})
print()

# ---------------------------------------------------------------- toys ----
if opts.toys:
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for truth in gridVals:
            tag = "toys_%s_ttH%g" % (name, truth)
            toyCmd = (
                "combine -m %.4f -d %s -M GenerateOnly -s %d --saveToys --toysNoSystematics "
                "-t %d -n _%s_ttH%g "
                "--setParameterRanges r_ttH=%g,%g "
                "--setParameters %s=%d,r_ttH=%g --freezeParameters %s"
                % (opts.mH, opts.datacard, opts.seed, opts.nToys, name, truth,
                   opts.rMin, opts.rMax, indexName, ipdf, truth, indexName)
            )
            ok = run(toyCmd, tag, dry=opts.dryRun)
            if not opts.dryRun and ok:
                os.system("mv higgsCombine_%s_ttH%g* %s" % (name, truth, toyName(name, truth)))
            sleep(0.2)
print()

# ---------------------------------------------------------------- fits ----
if opts.fits:
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for truth in gridVals:
            tag = "fits_%s_ttH%g" % (name, truth)
            tfile = toyName(name, truth)
            if not opts.dryRun and not path.exists(tfile):
                print("WARNING: toy file %s not found - run --toys first. Skipping." % tfile)
                continue
            fitCmd = (
                "combine -m %.4f -d %s -M MultiDimFit -P r_ttH --algo singles "
                "--setParameterRanges r_ttH=%g,%g %s "
                "-t %d -n _%s_ttH%g_fit --toysFile=%s -s %d"
                % (opts.mH, opts.datacard, opts.rMin, opts.rMax, opts.combineOptions,
                   opts.nToys, name, truth, tfile, opts.seed)
            )
            ok = run(fitCmd, tag, dry=opts.dryRun)
            if not opts.dryRun and ok:
                os.system("mv higgsCombine_%s_ttH%g_fit* %s" % (name, truth, fitName(name, truth)))
            sleep(0.2)
print()

# --------------------------------------------------------------- plots ----
if opts.plots:
    allResults = {}
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for truth in gridVals:
            key = "%s_ttH%g" % (name, truth)
            ffile = fitName(name, truth)
            if not path.exists(ffile):
                print("WARNING: fit file %s not found - run --fits first. Skipping." % ffile)
                continue
            tfile = r.TFile(ffile)
            tree = tfile.Get('limit')

            pullHist = r.TH1F('pulls_%s' % key,
                               'Pull of r_ttH, truth function=%s, r_ttH_truth=%g;Pull;Toys' % (name, truth),
                               80, -4., 4.)

            pullEntries, failedToys = 0, 0
            for itoy in range(opts.nToys):
                if tree.GetEntry(3 * itoy) <= 0:
                    failedToys += 1; continue
                if not getattr(tree, 'quantileExpected') == -1:
                    failedToys += 1; continue
                bf = getattr(tree, 'r_ttH')

                if tree.GetEntry(3 * itoy + 1) <= 0:
                    failedToys += 1; continue
                if not abs(getattr(tree, 'quantileExpected') - (-0.32)) < 0.001:
                    failedToys += 1; continue
                lo = getattr(tree, 'r_ttH')

                if tree.GetEntry(3 * itoy + 2) <= 0:
                    failedToys += 1; continue
                if not abs(getattr(tree, 'quantileExpected') - 0.32) < 0.001:
                    failedToys += 1; continue
                hi = getattr(tree, 'r_ttH')

                unc = 0.5 * (hi - lo)
                if unc > 0.:
                    pullHist.Fill((bf - truth) / unc)
                    pullEntries += 1
                else:
                    failedToys += 1

            canv = r.TCanvas()
            pullHist.Draw()
            mean, meanErr, sigma, sigmaErr, chi2ndf = -999., -999., -999., -999., -999.
            if opts.gaussianFit and pullHist.GetEntries() > 10:
                r.gStyle.SetOptFit(111)
                pullHist.Fit('gaus', 'Q')
                fitFunc = pullHist.GetFunction('gaus')
                if fitFunc:
                    mean, meanErr = fitFunc.GetParameter(1), fitFunc.GetParError(1)
                    sigma, sigmaErr = fitFunc.GetParameter(2), fitFunc.GetParError(2)
                    ndf = fitFunc.GetNDF()
                    chi2ndf = fitFunc.GetChisquare() / ndf if ndf > 0 else -999.
            canv.SaveAs('%s.pdf' % plotName(name, truth))
            canv.SaveAs('%s.png' % plotName(name, truth))

            status = "PASS" if abs(mean) < PASS_THRESHOLD else (
                     "WARN" if abs(mean) < WARN_THRESHOLD else "FAIL")

            allResults[key] = {
                "function": name,
                "pdfindex": ipdf,
                "poi": "r_ttH",
                "truth_r_ttH": truth,
                "seed": opts.seed,
                "nToysRequested": opts.nToys,
                "nToysSucceeded": int(pullEntries),
                "nToysFailed": int(failedToys),
                "histEntries": int(pullHist.GetEntries()),
                "histMeanPull": pullHist.GetMean(),
                "histRmsPull": pullHist.GetRMS(),
                "gaussianBias": mean,
                "gaussianBiasErr": meanErr,
                "gaussianSigma": sigma,
                "gaussianSigmaErr": sigmaErr,
                "gaussianChi2PerNdf": chi2ndf,
                "status_0p14": status,
                "plotPdf": "%s.pdf" % plotName(name, truth),
                "plotPng": "%s.png" % plotName(name, truth),
            }
            print("%-30s bias=%+.4f +/- %.4f  sigma=%.3f  succeeded=%d/%d  -> %s"
                  % (key, mean, meanErr, sigma, pullEntries, opts.nToys, status))

    outJson = 'BiasPlots/BiasResults_r_ttH_seed%d.json' % opts.seed
    with open(outJson, 'w') as f:
        json.dump(allResults, f, indent=2)
    print()
    print('Wrote %s' % outJson)
