import pandas as pd
import pickle
import ROOT
import re
import sys
from optparse import OptionParser

def get_options():
  parser = OptionParser()
  parser.add_option("-i", "--inputWS", dest="inputWS", default = "", help="Input RooWorkspace")
  return parser.parse_args()
(opt,args) = get_options()

def rooiter(x):
  iter = x.iterator()
  ret = iter.Next()
  while ret:
    yield ret
    ret = iter.Next()

def procToProcS0(p):
  p = p.lower()
  # Specific matches for tHq to avoid merging
  if "thqhad" in p: return "thqhad_incl"
  elif "thqlep" in p: return "thqlep_incl"
  
  # Matches for the other 6 processes
  elif "ggh" in p: return "ggh_incl"
  elif "vbf" in p: return "vbf_incl"
  elif "bbh" in p: return "bbh_incl"
  elif "tth" in p: return "tth_incl"
  elif "thw" in p: return "thw_incl"
  elif "vh" in p: return "vh_incl"

  else: 
    print(" --> [ERROR] proc s0 not realised for process %s. Leaving"%p)
    exit(0)

# Extract normalisations from workspace
f = ROOT.TFile(opt.inputWS)
ws = f.Get("w")
allNorms = ws.allFunctions().selectByName("n_exp_final*")

# Initialise dataFrame: proc, cat, yield
columns_data = ['proc','proc_s0','cat','total_yield']
data = pd.DataFrame( columns=columns_data )

# Loop over norms and fill dataframe with signal entries
for _func in rooiter(allNorms):
  print("\n--- New Function ---")
  full_name = _func.GetName()
  print("Full function name:", full_name)
  _proc =  _func.GetName().split("_proc_")[-1]
  print("Extracted process:", _proc)
  if "bkg_mass" in _proc:
      print("Skipping background process")
      continue
  _proc_s0 = procToProcS0(_proc)
  print("Simplified process (proc_s0):", _proc_s0)
  _cat = cat = (_func.GetName().split("_proc_")[0]).split("bin")[-1]
  print("Extracted category:", _cat)
  # Extract the total expected events (Rate * XS * BR * Eff * Acc)
  total_yield = _func.getVal()
  print("total yield:", total_yield)
  data.loc[len(data)] = [_proc,_proc_s0,_cat,total_yield]
  print("Row added to dataframe")
# Save dataframe
outputFrame = re.sub(".root","_yields.pkl",opt.inputWS)
with open( outputFrame, "wb" ) as fD: pickle.dump(data,fD) 
