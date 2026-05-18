#!/usr/bin/env python
import os
import json
from os import system, path
from biasUtils import *
from optparse import OptionParser
from time import sleep
parser = OptionParser()
parser.add_option("-d","--datacard",default="Datacard.root")
parser.add_option("-w","--workspace",default="w")
parser.add_option("--toys",action="store_true", default=False)
parser.add_option("-n","--nToys",default=1000,type="int")
parser.add_option("-f","--fits",action="store_true", default=False)
parser.add_option("-p","--plots",action="store_true", default=False)
parser.add_option("-e","--expectSignal",default=1.,type="float")
parser.add_option("-m","--mH",default=125.38,type="float")
parser.add_option("-c","--combineOptions",default="")
parser.add_option("-s","--seed",default=-1,type="int")
parser.add_option("--dryRun",action="store_true", default=False)
parser.add_option("--poi",default="r_ttH")
parser.add_option("--split",default=500,type="int")
parser.add_option("--selectFunction",default=None)
parser.add_option("--gaussianFit",action="store_true", default=False)
(opts,args) = parser.parse_args()
print()
if opts.nToys>opts.split and not opts.nToys%opts.split==0: raise RuntimeError('The number of toys %g needs to be smaller than or divisible by the split number %g'%(opts.nToys, opts.split))

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
        print('Conduct bias study for multipdf called %s'%multipdfName)
multipdf = ws.pdf(multipdfName)
print()

varlist = rooArgSetToList(ws.allCats())
indexName = None
for var in varlist:
    if var.GetName().startswith('pdfindex'):
        if indexName is not None: raiseMultiError()
        indexName = var.GetName()
        print('Found index called %s'%indexName)
print()

from collections import OrderedDict as od
indexNameMap = od()
for ipdf in range(multipdf.getNumPdfs()):
    if opts.selectFunction is not None:
        if not multipdf.getPdf(ipdf).GetName().count(opts.selectFunction): continue
    indexNameMap[ipdf] = multipdf.getPdf(ipdf).GetName()

if opts.toys:
    if not path.isdir(f'BiasToys_Expected.{opts.expectSignal}'): os.system(f'mkdir -p BiasToys_Expected.{opts.expectSignal}')
    toyCmdBase = 'combine -m %.4f -d %s -M GenerateOnly -s %g --saveToys %s --toysNoSystematics'%(opts.mH, opts.datacard, opts.seed, opts.combineOptions)
    for ipdf,pdfName in indexNameMap.items():
        name = shortName(pdfName)
        if opts.nToys > opts.split:
            for isplit in range(opts.nToys//opts.split):
                toyCmd = toyCmdBase + ' -t %g -n _%s_split%g --setParameters %s=%g,%s=%.4f --freezeParameters %s'%(opts.split, name, isplit, indexName, ipdf, opts.poi, opts.expectSignal, indexName)
                run(toyCmd, dry=opts.dryRun)
                sleep(1)
                #toyname = toyName(name, opts.expectSignal, split=isplit)
                #print("toyname",toyname)
                #system('echo mv higgsCombine_%s* %s' % (name, toyName(name, opts.expectSignal, split=isplit)))
                system('mv higgsCombine_%s* %s' % (name, toyName(name, opts.expectSignal, split=isplit)))
        else: 
            toyCmd = toyCmdBase + ' -t %g -n _%s --setParameters %s=%g,%s=%.4f --freezeParameters %s'%(opts.nToys, name, indexName, ipdf, opts.poi, opts.expectSignal, indexName)
            run(toyCmd, dry=opts.dryRun)
            #toyname = toyName(name, opts.expectSignal)
            #print("toyname",toyname)
            #system(' echo mv higgsCombine_%s* %s'%(name, toyName(name, opts.expectSignal)))
            system('mv higgsCombine_%s* %s'%(name, toyName(name, opts.expectSignal)))
print()

if opts.fits:
    if not path.isdir(f'BiasFits_Expected.{opts.expectSignal}'): system(f'mkdir -p BiasFits_Expected.{opts.expectSignal}')
    fitCmdBase = 'combine -m %.4f -d %s -M MultiDimFit --algo singles --freezeParameters allConstrainedNuisances,MH %s'%(opts.mH, opts.datacard, opts.combineOptions)
    for ipdf,pdfName in indexNameMap.items():
        name = shortName(pdfName)
        if opts.nToys > opts.split:
            for isplit in range(opts.nToys//opts.split):
                fitCmd = fitCmdBase + ' --setParameters %s=%.4f -t %g -n _%s_split%g --toysFile=%s' % (opts.poi, opts.expectSignal, opts.split, name, isplit, toyName(name, opts.expectSignal, split=isplit))
                run(fitCmd, dry=opts.dryRun)
                sleep(1)
                system(' mv higgsCombine_%s* %s'%(name, fitName(name, opts.expectSignal, split=isplit)))
                sleep(1)
            # The [3011] error is a non-fatal EOS metadata warning.
            # It happens because the internal 'parent' path was moved/renamed.
            run(f'hadd {fitName(name, opts.expectSignal)} BiasFits_Expected.{opts.expectSignal}/*{name}*split*.root', dry=opts.dryRun)
        else:
            fitCmd = fitCmdBase + ' --setParameters %s=%.4f -t %g -n _%s --toysFile=%s' % (opts.poi, opts.expectSignal, opts.nToys, name, toyName(name, opts.expectSignal))
            run(fitCmd, dry=opts.dryRun)
            system('mv higgsCombine_%s* %s'%(name, fitName(name, opts.expectSignal)))

if opts.plots:
    if not path.isdir(f'BiasPlots_Expected.{opts.expectSignal}'): 
        system(f'mkdir -p BiasPlots_Expected.{opts.expectSignal}')
    
    biasResults = {}
    for ipdf, pdfName in indexNameMap.items():
        name = shortName(pdfName)
        fileName = fitName(name, opts.expectSignal)
        
        # IMPROVEMENT 1: Check if file exists and is healthy
        tfile = r.TFile(fileName)
        if not tfile or tfile.IsZombie():
            print(f"[ERROR] Could not open {fileName}. Skipping...")
            continue
            
        tree = tfile.Get('limit')
        if not tree:
            print(f"[ERROR] No 'limit' tree found in {fileName}. Skipping...")
            continue

        pullHist = r.TH1F('pullsForTruth_%s'%name, 'Pull distribution using the envelope to fit %s'%name, 80, -4., 4.)
        pullHist.GetXaxis().SetTitle('Pull')
        pullHist.GetYaxis().SetTitle('Entries')
        
        # Explicit counters for debugging
        boundaryHits = 0
        pullEntries  = 0
        failedToys   = 0  # IMPROVEMENT 2: Explicit counter for failures
        badErrors    = 0  # IMPROVEMENT 3: Track toys with invalid uncertainties

        # IMPROVEMENT 4: Ensure we don't read past the end of a broken tree
        maxEntries = tree.GetEntries()

        for itoy in range(opts.nToys):
            if (3*itoy + 2) >= maxEntries:
                print(f"[WARNING] Tree ends early. Missing toys starting at {itoy}")
                failedToys += (opts.nToys - itoy)
                break # Stop the loop, tree is out of entries

            tree.GetEntry(3*itoy)
            if getattr(tree, 'quantileExpected') != -1:
                raiseFailError(itoy, True)
                failedToys += 1
                continue
            bf = getattr(tree, opts.poi)

            tree.GetEntry(3*itoy+1)
            if abs(getattr(tree, 'quantileExpected') - (-0.32)) > 0.001:
                raiseFailError(itoy, True)
                failedToys += 1
                continue
            lo = getattr(tree, opts.poi)

            tree.GetEntry(3*itoy+2)
            if abs(getattr(tree, 'quantileExpected') - 0.32) > 0.001:
                raiseFailError(itoy, True)
                failedToys += 1
                continue
            hi = getattr(tree, opts.poi)

            # Boundary check (WITH the continue statement)
            if abs(bf) >= 49.9 or abs(lo) >= 49.9 or abs(hi) >= 49.9:
                boundaryHits += 1
                continue 

            diff = bf - opts.expectSignal
            unc = 0.5 * (hi-lo)
            
            # Check for valid uncertainties
            if unc > 0.:
                pullHist.Fill(diff/unc)
                pullEntries += 1
            else:
                badErrors += 1

        canv = r.TCanvas()
        pullHist.Draw()
        
        # IMPROVEMENT 5: Default values in case the fit fails
        mean = -999.0
        sigma = -999.0

        if opts.gaussianFit and pullEntries > 0:
           r.gStyle.SetOptFit(111)
           pullHist.Fit('gaus', 'Q') # 'Q' makes the fit output quiet in terminal
           fitFunc = pullHist.GetFunction('gaus')
           if fitFunc:
               mean  = fitFunc.GetParameter(1)   # bias
               sigma = fitFunc.GetParameter(2)
           else:
               print(f"[WARNING] Gaussian fit failed for {name}!")

        biasResults[name] = {
               "expectSignal": opts.expectSignal,
               "bias": mean,
               "sigma": sigma,
               "pullEntries": int(pullEntries),
               "failedToys": int(failedToys),
               "boundaryHits": int(boundaryHits),
               "badErrors": int(badErrors),
               "meanPull": pullHist.GetMean(),
               "rmsPull":  pullHist.GetRMS()
            }
            
        # Print a helpful summary to the terminal
        print(f"--- Summary for {name} ---")
        print(f"  Total Toys   : {opts.nToys}")
        print(f"  Good Fits    : {pullEntries}")
        print(f"  Boundary Hits: {boundaryHits}")
        print(f"  Failures     : {failedToys} (Crashes) + {badErrors} (Bad Errors)")
        print(f"  Calculated Bias: {mean:.3f}")

        canv.SaveAs(f'{plotName(name, opts.expectSignal)}.pdf')
        canv.SaveAs(f'{plotName(name, opts.expectSignal)}.png')

    outJson = f'BiasPlots_Expected.{opts.expectSignal}/BiasResults.json'
    with open(outJson, 'w') as f:
        json.dump(biasResults, f, indent=2)
