import sys
import ROOT
import pandas as pd
import argparse

# --- Argument Parsing ---
parser = argparse.ArgumentParser()
parser.add_argument("--inputFile", required=True, help="Input ROOT file")
parser.add_argument("--expected", required=True, type=float, help="Expected signal")
parser.add_argument("--poi", required=True, help="Parameter of interest")

args = parser.parse_args()

input_file = args.inputFile
expectSignal = args.expected
poi = args.poi

# --- Open File ---
f = ROOT.TFile.Open(input_file)
tree = f.Get("limit")

n_entries = tree.GetEntries()
nToys = n_entries // 3

results = []

print(f"Processing {nToys} toys with Expected Signal: {expectSignal}")

for itoy in range(nToys):

    # Best fit
    tree.GetEntry(3 * itoy)
    if tree.quantileExpected != -1:
        continue
    bf = getattr(tree, poi)

    # -1 sigma
    tree.GetEntry(3 * itoy + 1)
    if abs(tree.quantileExpected - (-0.32)) >= 0.001:
        continue
    lo = getattr(tree, poi)

    # +1 sigma
    tree.GetEntry(3 * itoy + 2)
    if abs(tree.quantileExpected - 0.32) >= 0.001:
        continue
    hi = getattr(tree, poi)

    # Calculations
    unc = 0.5 * (hi - lo)
    diff = bf - expectSignal

    if unc > 0:
        pull = diff / unc
    else:
        pull = None

    results.append({
        "toy": itoy,
        "bf": bf,
        "expected": expectSignal,
        "+1sigma": hi,
        "-1sigma": lo,
        "unc": unc,
        "diff": diff,
        "pull": pull
    })

# --- DataFrame ---
df = pd.DataFrame(results)

print(df[["toy", "bf", "expected", "+1sigma", "-1sigma", "unc", "diff", "pull"]])

import matplotlib.pyplot as plt

fig, ax = plt.subplots(3,3, figsize=(14,12))

cols = ["bf", "+1sigma", "-1sigma", "unc", "diff", "pull"]

# Histograms
for i, c in enumerate(cols):
    r = i // 3
    cpos = i % 3
    ax[r, cpos].hist(df[c].dropna(), bins=40)
    ax[r, cpos].set_title(c)
    ax[r, cpos].set_xlabel(c)
    ax[r, cpos].set_ylabel("Toys")

# Pull vs toy
ax[2,1].scatter(df["toy"], df["pull"], s=8)
ax[2,1].set_title("Pull vs Toy")
ax[2,1].set_xlabel("Toy")
ax[2,1].set_ylabel("Pull")

# Best fit vs toy
ax[2,2].scatter(df["toy"], df["bf"], s=8)
ax[2,2].set_title("Best Fit vs Toy")
ax[2,2].set_xlabel("Toy")
ax[2,2].set_ylabel("bf")

plt.tight_layout()

# Save figure
plt.savefig("bias_study_summary.png", dpi=300)

plt.show()
