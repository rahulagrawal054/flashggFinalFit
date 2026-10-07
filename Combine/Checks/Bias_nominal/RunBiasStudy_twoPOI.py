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
from biasUtils import rooArgSetToList, raiseMultiError, raiseFailError, shortName, run
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
parser.add_option("--poi", default=None, choices=POIS,
                   help="POI to fit/plot in this call: one of %s. Required for --fits "
                        "and --plots; run the script twice to cover both POIs." % POIS)
parser.add_option("-m", "--mH", default=125.08, type="float")
parser.add_option("-c", "--combineOptions", default="")
parser.add_option("-s", "--seed", default=-1, type="int")
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

if opts.split is not None and opts.nToys > opts.split and not opts.nToys % opts.split == 0:
    raise RuntimeError('nToys %g needs to be smaller than or divisible by split %g' % (opts.nToys, opts.split))
if (opts.fits or opts.plots) and opts.poi is None:
    raise SystemExit("--poi is required for --fits and --plots (choose one of %s); "
                      "run the script twice to cover both POIs." % POIS)

gridVals = [float(v) for v in opts.grid.split(",")]
gridPoints = [(ttH, tHq) for ttH in gridVals for tHq in gridVals]
rRanges = "r_ttH=%g,%g:r_tHq=%g,%g" % (opts.rMinTtH, opts.rMaxTtH, opts.rMinTHq, opts.rMaxTHq)

print()
print("Truth grid (%d points): %s" % (len(gridPoints), gridPoints))
print()

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


def gridTag(ttH, tHq):
    return 'ttH%g_tHq%g' % (ttH, tHq)


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
    if not path.isdir('BiasToys'): system('mkdir -p BiasToys')
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for (ttH, tHq) in gridPoints:
            toyCmdBase = ('combine -m %.4f -d %s -M GenerateOnly -s %g --saveToys %s --toysNoSystematics'
                          % (opts.mH, opts.datacard, opts.seed, opts.combineOptions))
            setParams = '%s=%g,r_ttH=%g,r_tHq=%g' % (indexName, ipdf, ttH, tHq)
            if opts.split is not None and opts.nToys > opts.split:
                for isplit in range(opts.nToys // opts.split):
                    toyCmd = toyCmdBase + (' -t %g -n _%s_%s_split%g --setParameters %s --freezeParameters %s'
                                           % (opts.split, name, gridTag(ttH, tHq), isplit, setParams, indexName))
                    run(toyCmd, dry=opts.dryRun)
                    sleep(1)
                    system('mv higgsCombine_%s_%s* %s' % (name, gridTag(ttH, tHq), toyName(name, ttH, tHq, split=isplit)))
            else:
                toyCmd = toyCmdBase + (' -t %g -n _%s_%s --setParameters %s --freezeParameters %s'
                                       % (opts.nToys, name, gridTag(ttH, tHq), setParams, indexName))
                run(toyCmd, dry=opts.dryRun)
                system('mv higgsCombine_%s_%s* %s' % (name, gridTag(ttH, tHq), toyName(name, ttH, tHq)))
print()

if opts.fits:
    if not path.isdir('BiasFits'): system('mkdir -p BiasFits')
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for (ttH, tHq) in gridPoints:
            fitCmdBase = ('combine -m %.4f -d %s -M MultiDimFit -P %s --algo singles '
                         '--setParameterRanges %s %s'
                         % (opts.mH, opts.datacard, opts.poi, rRanges, opts.combineOptions))
            if opts.split is not None and opts.nToys > opts.split:
                for isplit in range(opts.nToys // opts.split):
                    fitCmd = fitCmdBase + (' -t %g -n _%s_%s_%s_split%g --toysFile=%s'
                                           % (opts.split, name, gridTag(ttH, tHq), opts.poi, isplit,
                                              toyName(name, ttH, tHq, split=isplit)))
                    run(fitCmd, dry=opts.dryRun)
                    sleep(1)
                    system('mv higgsCombine_%s_%s_%s* %s'
                          % (name, gridTag(ttH, tHq), opts.poi, fitName(name, ttH, tHq, opts.poi, split=isplit)))
                run('hadd %s BiasFits/*%s_%s_%s*split*.root'
                    % (fitName(name, ttH, tHq, opts.poi), name, gridTag(ttH, tHq), opts.poi), dry=opts.dryRun)
            else:
                fitCmd = fitCmdBase + (' -t %g -n _%s_%s_%s --toysFile=%s'
                                       % (opts.nToys, name, gridTag(ttH, tHq), opts.poi,
                                          toyName(name, ttH, tHq)))
                run(fitCmd, dry=opts.dryRun)
                system('mv higgsCombine_%s_%s_%s* %s'
                      % (name, gridTag(ttH, tHq), opts.poi, fitName(name, ttH, tHq, opts.poi)))
print()

if opts.plots:
    if not path.isdir('BiasPlots'): system('mkdir -p BiasPlots')
    biasResults = {}
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        for (ttH, tHq) in gridPoints:
            truth = ttH if opts.poi == 'r_ttH' else tHq
            tfile = r.TFile(fitName(name, ttH, tHq, opts.poi))
            tree = tfile.Get('limit')
            pullHist = r.TH1F('pulls_%s_%s_%s' % (name, gridTag(ttH, tHq), opts.poi),
                              'Pull of %s using envelope, truth %s, %s=%g' % (opts.poi, name, opts.poi, truth),
                              80, -4., 4.)
            pullHist.GetXaxis().SetTitle('Pull')
            pullHist.GetYaxis().SetTitle('Entries')

            pullEntries = 0
            for itoy in range(opts.nToys):
                tree.GetEntry(3 * itoy)
                if not getattr(tree, 'quantileExpected') == -1:
                    raiseFailError(itoy, True)
                    continue
                bf = getattr(tree, opts.poi)

                tree.GetEntry(3 * itoy + 1)
                if not abs(getattr(tree, 'quantileExpected') - (-0.32)) < 0.001:
                    raiseFailError(itoy, True)
                    continue
                lo = getattr(tree, opts.poi)

                tree.GetEntry(3 * itoy + 2)
                if not abs(getattr(tree, 'quantileExpected') - 0.32) < 0.001:
                    raiseFailError(itoy, True)
                    continue
                hi = getattr(tree, opts.poi)

                diff = bf - truth
                unc = 0.5 * (hi - lo)
                if unc > 0.:
                    pullHist.Fill(diff / unc)
                    pullEntries += 1

            canv = r.TCanvas()
            pullHist.Draw()
            mean, sigma = -999.0, -999.0
            if opts.gaussianFit:
                r.gStyle.SetOptFit(111)
                pullHist.Fit('gaus')
                fitFunc = pullHist.GetFunction('gaus')
                if fitFunc:
                    mean = fitFunc.GetParameter(1)
                    sigma = fitFunc.GetParameter(2)

            biasResults['%s_%s_%s' % (name, gridTag(ttH, tHq), opts.poi)] = {
                "function": name, "poi": opts.poi,
                "truth_r_ttH": ttH, "truth_r_tHq": tHq,
                "bias": mean, "sigma": sigma,
                "pullEntries": int(pullEntries),
                "failedToys": int(opts.nToys - pullEntries),
                "meanPull": pullHist.GetMean(), "rmsPull": pullHist.GetRMS(),
            }
            canv.SaveAs('%s.pdf' % plotName(name, ttH, tHq, opts.poi))
            canv.SaveAs('%s.png' % plotName(name, ttH, tHq, opts.poi))

    import json
    outJson = 'BiasPlots/BiasResults_%s.json' % opts.poi
    with open(outJson, 'w') as f:
        json.dump(biasResults, f, indent=2)
    print('Wrote %s' % outJson)
