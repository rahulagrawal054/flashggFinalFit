import pandas as pd
import ROOT
import re
import sys
from optparse import OptionParser

def get_options():
    parser = OptionParser()
    parser.add_option("-i", "--inputWS", dest="inputWS", default="", help="Input RooWorkspace")
    return parser.parse_args()

(opt, args) = get_options()

def rooiter(x):
    iter = x.iterator()
    ret = iter.Next()
    while ret:
        yield ret
        ret = iter.Next()

# Extract normalisations from workspace
f = ROOT.TFile(opt.inputWS)
ws = f.Get("w")
allNorms = ws.allFunctions().selectByName("n_exp_final*")

# Initialise dataFrame with enhanced process breakdown
columns_data = ['proc', 'proc_s0', 'base_proc', 'fiducial', 'cat', 'nominal_yield']
data = pd.DataFrame(columns=columns_data)

print("--- Extracting Processes from Workspace ---")

for _func in rooiter(allNorms):
    _proc = _func.GetName().split("_proc_")[-1]
    if "bkg_mass" in _proc: 
        continue

    _proc_s0 = _proc
    _cat = (_func.GetName().split("_proc_")[0]).split("bin")[-1]
    _nominal_yield = _func.getVal()

    # Determine fiducial status (in vs out)
    if "_in_" in _proc:
        fiducial = "in"
    elif "_out_" in _proc:
        fiducial = "out"
    else:
        fiducial = "inclusive"

    # Extract base physics process (e.g., 'ggh_in_2022' -> 'ggh')
    base_proc = _proc.split('_')[0] if '_' in _proc else _proc

    data.loc[len(data)] = [_proc, _proc_s0, base_proc, fiducial, _cat, _nominal_yield]

print(f"Extracted {len(data)} process entries across categories.")
print("------------------------------------------")

# Save directly to CSV format
outputCSV = re.sub(r"\.root$", "_yields.csv", opt.inputWS)
if outputCSV == opt.inputWS:
    outputCSV += "_yields.csv"

data.to_csv(outputCSV, index=False)
print("Yields saved successfully to CSV: %s" % outputCSV)
