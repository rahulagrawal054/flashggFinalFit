#!/usr/bin/env python3

import json
import glob
import re
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
try:
    import mplhep as hep
    hep.style.use(hep.styles.CMS) # Use official CMS style
    hep_available = True
except ImportError:
    hep_available = False
from collections import defaultdict

# -----------------------
# configuration
# -----------------------
categories = [
    "ttH_had_1", "ttH_had_2", "ttH_lep_1", "ttH_lep_2",
    "tH_had_1", "tH_had_2", "tH_lep_1", "tH_lep_2"
]

def plot_paper_bias(cat_name):
    poi = "r_{ttH}" if "ttH" in cat_name else "r_{tH}"
    data = defaultdict(list)

    # File searching
    search_path = os.path.join(f"{cat_name}_mu*", "BiasPlots_Expected.*", "BiasResults.json")
    json_files = glob.glob(search_path)
    if not json_files: return

    for jf in json_files:
        m = re.search(r"_mu([0-9.]+)", jf)
        if not m: continue
        mu_val = float(m.group(1))
        try:
            with open(jf, 'r') as f:
                content = json.load(f)
            for func, res in content.items():
                if "bias" in res:
                    data[func].append((mu_val, res["bias"]))
        except: continue

    # --- Plotting ---
    fig, ax = plt.subplots(figsize=(10, 9))

    # 1. CMS Labels (Preliminary in italics)
    if hep_available:
        # loc=0: top left, data=True: 'Simulation' or 'Data' context
        # Standard: CMS is Bold, Preliminary is Italics
        #hep.cms.label("Preliminary", data=True, ax=ax, loc=0, fontsize=24)
        # 2. Lumi and Energy
        #hep.cms.lumitext("61.9 fb$^{-1}$ (13.6 TeV)", ax=ax, fontsize=20)
        hep.cms.label("Preliminary", data=True, lumi=61.9, com=13.6, loc=0, ax=ax)
    else:
        ax.text(0, 1.01, "CMS", fontweight='bold', fontsize=24, transform=ax.transAxes)
        ax.text(0.12, 1.01, "Preliminary Simulation", fontstyle='italic', fontsize=20, transform=ax.transAxes)
        ax.text(1, 1.01, "61.9 fb$^{-1}$ (13.6 TeV)", ha='right', fontsize=20, transform=ax.transAxes)

    # 3. Dynamic Y-Axis Limits
    all_biases = [pt[1] for func in data for pt in data[func]]
    if all_biases:
        max_bias = max(max([abs(b) for b in all_biases]), 0.3) # Minimum window of 0.3
        y_limit = max_bias * 1.5 # Add 50% headroom for legend
    else:
        y_limit = 0.5

    # 4. Pull Bands
    ax.axhspan(-0.1, 0.1, color='green', alpha=0.15, label=r'$\pm 10\% \ \Delta\mu/\sigma$')
    ax.axhspan(-0.2, 0.2, color='yellow', alpha=0.15, label=r'$\pm 20\% \ \Delta\mu/\sigma$')
    ax.axhline(0, color='black', linestyle='-', linewidth=1, alpha=0.5)

    # 5. Data Lines (Solid with markers - Best for Papers)
    colors = plt.cm.Set1(np.linspace(0, 1, len(data)))
    for i, func in enumerate(sorted(data.keys())):
        points = sorted(data[func], key=lambda x: x[0])
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        
        # Using solid lines with markers for clear visualization
        ax.plot(x, y, marker='o', markersize=7, linewidth=2, 
                color=colors[i], label=func.replace("_", " "))

    # 6. Fine Grid
    ax.grid(True, which='major', linestyle='-', alpha=0.3)
    ax.grid(True, which='minor', linestyle=':', alpha=0.2)
    ax.minorticks_on()
    
    # 7. Axes Labels and Limits
    ax.set_xlabel(f"Expected Signal Strength ${poi}$", fontsize=22)
    ax.set_ylabel(r"Bias $(\hat{\mu} - \mu_{true})/\sigma_{\mu}$", fontsize=22)
    ax.set_ylim(-y_limit, y_limit)
    ax.set_xlim(0, 10)

    # Legend & Category Box
    ax.legend(loc='upper right', ncol=2, frameon=True, fontsize=14, edgecolor='none', facecolor='white', framealpha=0.8)
    ax.text(0.05, 0.05, f"Category: {cat_name.replace('_',' ')}", transform=ax.transAxes, 
            fontsize=16, fontweight='bold', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

    plt.tight_layout()
    
    # Save as PDF (Vector format for papers) and PNG
    plt.savefig(f"Bias_Study_{cat_name}.pdf", bbox_inches='tight')
    plt.savefig(f"Bias_Study_{cat_name}.png", bbox_inches='tight')
    print(f"Generated paper-quality plot for {cat_name}")
    plt.close()

if __name__ == "__main__":
    for cat in categories:
        plot_paper_bias(cat)
