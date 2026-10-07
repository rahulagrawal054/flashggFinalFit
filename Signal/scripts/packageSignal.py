# Script to package individual signal models for a single category in one ROOT file
# Option to merge different extensions (years)

import os, re, sys
import glob
import ROOT
from optparse import OptionParser
from commonObjects import *

def get_options():
  parser = OptionParser()
  parser.add_option("--cat", dest='cat', default='RECO_0J_PTH_0_10_Tag0', help="RECO category to package")
  parser.add_option("--exts", dest='exts', default='', help="Comma separate list of extensions")
  parser.add_option("--outputExt", dest='outputExt', default='packaged', help="Output extension")
  parser.add_option("--inputDir", dest='inputDir', default=swd__, help="Input directory containing outdir_<ext>/signalFit/output")
  parser.add_option("--outputDir", dest='outputDir', default=swd__, help="Output directory")
  parser.add_option("--massPoints", dest='massPoints', default='120,125,130', help="Comma separated list of mass points")
  parser.add_option("--mergeYears", dest='mergeYears', default=False, action="store_true", help="Merge specified categories across years")
  parser.add_option("--year", dest="year", default="2016", help="If not merging, then specify year for output file name")
  return parser.parse_args()
(opt,args) = get_options()

def rooiter(x):
  iter = x.iterator()
  ret = iter.Next()
  while ret:
    yield ret
    ret = iter.Next()

# Extract all files to be merged
fNames = {}
input_base = opt.inputDir or swd__
for ext in opt.exts.split(","):
  fNames[ext] = glob.glob("%s/outdir_%s/signalFit/output/CMS-HGG_sigfit_%s_*_%s.root"%(input_base,ext,ext,opt.cat))
  if len(fNames[ext]) == 0:
    print(" --> [ERROR] No signalFit inputs found for ext=%s cat=%s under %s/outdir_%s/signalFit/output"%(
      ext, opt.cat, input_base, ext))
    exit(1)

# Define ouput packaged workspace
print(" --> Packaging output workspaces")
packagedWS = ROOT.RooWorkspace("wsig_13TeV","wsig_13TeV")
packagedWS.imp = getattr(packagedWS,"import")

# ==============================================================================
# NOTE ON bkg_had:
# We skip creating a single merged dataset (sig_mass_m125_bkg_had) for the bkg_had 
# category because it contains too many events across all processes. Merging them into 
# one object exceeds ROOT's 1 GB TBuffer limit and causes a crash. All individual 
# process datasets (ggH, VBF, ttH, bbH, etc.) remain 100% intact and saved, which is 
# all CMS Combine requires.
# ==============================================================================

# Define the merged dataset names for this category so we can exclude them from input loops
merged_dataset_names = ["sig_mass_m%s_%s" % (mp, opt.cat) for mp in opt.massPoints.split(",")]

data_merged = {}
skip_merged = (opt.cat == "bkg_had")

if not skip_merged:
    print(" --> Action: Merging datasets together for category %s..." % opt.cat)
    # Initialize empty clones for merging
    for mp in opt.massPoints.split(","):
        ds_name = "sig_mass_m%s_%s" % (mp, opt.cat)
        first_file = ROOT.TFile(fNames[opt.exts.split(",")[0]][0])
        first_ws = first_file.Get("wsig_13TeV")
        if first_ws and first_ws.data(ds_name):
            data_merged["m%s" % mp] = first_ws.data(ds_name).emptyClone(ds_name)

    # Accumulate events across all files
    for ext, fNames_by_ext in fNames.items():
        for fName in fNames_by_ext:
            fin = ROOT.TFile(fName)
            wsin = fin.Get("wsig_13TeV")
            if not wsin: continue
            for mp in opt.massPoints.split(","):
                d = wsin.data("sig_mass_m%s_%s" % (mp, opt.cat))
                if not d: continue
                for i in range(d.numEntries()):
                    data_merged["m%s" % mp].add(d.get(i), d.weight())

    # Import merged dataset ONCE into output workspace
    for _data in data_merged.values():
        packagedWS.imp(_data)
else:
    print(" --> Action: Skipping merged dataset creation for %s to avoid 1GB ROOT buffer limit." % opt.cat)

# Loop over input signal fit workspaces and import individual process datasets
for ext, fNames_by_ext in fNames.items():
    for fName in fNames_by_ext:
        fin = ROOT.TFile(fName)
        wsin = fin.Get("wsig_13TeV")
        if not wsin: continue
        
        allVars, allFunctions, allPdfs = {}, {}, {}
        for _var in rooiter(wsin.allVars()): allVars[_var.GetName()] = _var
        for _func in rooiter(wsin.allFunctions()): allFunctions[_func.GetName()] = _func
        for _pdf in rooiter(wsin.allPdfs()): allPdfs[_pdf.GetName()] = _pdf
        allData = wsin.allData()

        # Import objects into output workspace
        for _varName, _var in allVars.items(): packagedWS.imp(_var, ROOT.RooFit.RecycleConflictNodes(), ROOT.RooFit.Silence())
        for _funcName, _func in allFunctions.items(): packagedWS.imp(_func, ROOT.RooFit.RecycleConflictNodes(), ROOT.RooFit.Silence())
        for _pdfName, _pdf in allPdfs.items(): packagedWS.imp(_pdf, ROOT.RooFit.RecycleConflictNodes(), ROOT.RooFit.Silence())

        for _data in allData:
            # EXCLUDE merged dataset names from input files so they don't get imported multiple times
            if _data.GetName() in merged_dataset_names:
                continue
            else:
                packagedWS.imp(_data)
# Save to file
if opt.outputDir == swd__:
  if not os.path.isdir("outdir_%s"%opt.outputExt): os.system("mkdir outdir_%s"%opt.outputExt)
  if opt.mergeYears:
    print(" --> Writing to: ./outdir_%s/CMS-HGG_sigfit_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat))
    f = ROOT.TFile("./outdir_%s/CMS-HGG_sigfit_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat),"RECREATE")
  else:
    print(" --> Writing to: ./outdir_%s/CMS-HGG_sigfit_%s_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat,opt.year))
    f = ROOT.TFile("./outdir_%s/CMS-HGG_sigfit_%s_%s_%s.root"%(opt.outputExt,opt.outputExt,opt.cat,opt.year),"RECREATE")
else:
  if not os.path.isdir(opt.outputDir): os.system("mkdir -p %s"%opt.outputDir)
  packaged_suffix = opt.outputExt if opt.outputExt else ""
  if opt.outputExt == "packaged":
    packaged_suffix = ""
  elif packaged_suffix and not packaged_suffix.startswith("_"):
    packaged_suffix = "_%s"%packaged_suffix
  if opt.mergeYears:
    print(" --> Writing to: %s/CMS-HGG_sigfit_packaged%s_%s.root"%(opt.outputDir,packaged_suffix,opt.cat))
    f = ROOT.TFile("%s/CMS-HGG_sigfit_packaged%s_%s.root"%(opt.outputDir,packaged_suffix,opt.cat),"RECREATE")
  else:
    print(" --> Writing to: %s/CMS-HGG_sigfit_packaged%s_%s_%s.root"%(opt.outputDir,packaged_suffix,opt.cat,opt.year))
    f = ROOT.TFile("%s/CMS-HGG_sigfit_packaged%s_%s_%s.root"%(opt.outputDir,packaged_suffix,opt.cat,opt.year),"RECREATE")

packagedWS.Write()
f.Close()
