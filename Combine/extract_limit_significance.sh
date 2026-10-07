#!/bin/bash

# Exit if no folders are passed
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <folder1> [folder2 ...]"
    echo "Example: $0 dir1 dir2 dir3"
    echo "Example: $0 /path/to/folders/*"
    exit 1
fi

LIMIT_FILE="higgsCombine_limit_r_tHq.AsymptoticLimits.mH125.08.root"
SIG_FILE="higgsCombine_significance_r_ttH.Significance.mH125.08.root"
OUT_FILE="results_summary.txt"

for DIR in "$@"; do
    if [ ! -d "$DIR" ]; then
        echo "Warning: Directory '$DIR' does not exist. Skipping..."
        continue
    fi

    echo "=================================================="
    echo " Processing folder: $DIR"
    echo "=================================================="

    # Run embedded Python script using PyROOT
    python3 - "$DIR" "$LIMIT_FILE" "$SIG_FILE" "$OUT_FILE" << 'EOF'
import sys
import os
import ROOT

# Suppress ROOT info messages
ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

dir_path = sys.argv[1]
limit_fname = sys.argv[2]
sig_fname = sys.argv[3]
out_fname = sys.argv[4]

limit_path = os.path.join(dir_path, limit_fname)
sig_path = os.path.join(dir_path, sig_fname)
out_path = os.path.join(dir_path, out_fname)

results = []
results.append(f"Results Summary for: {dir_path}")
results.append("="*45)

# --- Extract Asymptotic Limits ---
results.append(f"\n[ Asymptotic Limits: {limit_fname} ]")
if os.path.exists(limit_path):
    f_lim = ROOT.TFile.Open(limit_path)
    if f_lim and not f_lim.IsZombie():
        t_lim = f_lim.Get("limit")
        if t_lim:
            limits = {}
            for entry in t_lim:
                q = round(entry.quantileExpected, 3)
                val = entry.limit
                if q == -1.0: limits["Observed"] = val
                elif q == 0.025: limits["Expected -2s"] = val
                elif q == 0.160: limits["Expected -1s"] = val
                elif q == 0.500: limits["Expected Median"] = val
                elif q == 0.840: limits["Expected +1s"] = val
                elif q == 0.975: limits["Expected +2s"] = val

            for k in ["Observed", "Expected -2s", "Expected -1s", "Expected Median", "Expected +1s", "Expected +2s"]:
                if k in limits:
                    results.append(f"  {k:<18}: {limits[k]:.4f}")
        else:
            results.append("  Error: 'limit' TTree not found in file.")
        f_lim.Close()
    else:
        results.append("  Error: Unable to open ROOT file.")
else:
    results.append("  File not found.")

# --- Extract Significance ---
results.append(f"\n[ Significance: {sig_fname} ]")
if os.path.exists(sig_path):
    f_sig = ROOT.TFile.Open(sig_path)
    if f_sig and not f_sig.IsZombie():
        t_sig = f_sig.Get("limit")
        if t_sig:
            sig_val = None
            for entry in t_sig:
                sig_val = entry.limit
                break
            if sig_val is not None:
                results.append(f"  Significance      : {sig_val:.4f} sigma")
            else:
                results.append("  Error: Empty limit TTree.")
        else:
            results.append("  Error: 'limit' TTree not found in file.")
        f_sig.Close()
    else:
        results.append("  Error: Unable to open ROOT file.")
else:
    results.append("  File not found.")

summary_text = "\n".join(results)

# Output to console
print(summary_text)

# Save to file in the directory
with open(out_path, "w") as f_out:
    f_out.write(summary_text + "\n")

print(f"\n[+] Saved summary to: {out_path}\n")

EOF

done
