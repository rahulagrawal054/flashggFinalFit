#!/usr/bin/env python3
"""
plot_fitresult.py -- visualize a Combine RooFitResult (e.g. multidimfit_*.root)
as three grouped, readable plots instead of one giant text dump.

Usage (on lxplus, inside your CMSSW/combine environment):
  python3 plot_fitresult.py --inputFile multidimfit_AsimovPostfit.root --fitResultName fit_mdf

Produces, in ./FitResultPlots/:
  - nuisance_pulls.png/.pdf   : constrained nuisances, sorted by |pull|=value/error,
                                 with +-1sigma/+-2sigma shaded bands (the standard
                                 "pull plot" used to sanity-check a postfit result)
  - poi_values.png/.pdf       : your POIs (r_tHq, r_ttH, ...) with error bars
  - bkg_norms.png/.pdf        : per-category background normalizations (log scale,
                                 since these span 4+ orders of magnitude)

Parameters are classified by name pattern:
  - POI            : starts with "r_" (edit POI_PREFIXES below if your POIs differ)
  - background norm: contains "__norm"
  - shape envelope : starts with "env_pdf" (skipped -- these are the discrete
                      background function coefficients, not independently meaningful
                      unless you know which pdfindex is currently active)
  - nuisance       : everything else
"""

import argparse
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

POI_PREFIXES = ("r_",)


def classify(name):
    if name.startswith("env_pdf"):
        return "shape_envelope"
    if "__norm" in name:
        return "bkg_norm"
    if any(name.startswith(p) for p in POI_PREFIXES):
        return "poi"
    return "nuisance"


def read_fitresult_root(input_file, fitresult_name):
    """Read a RooFitResult from a ROOT file via PyROOT. Returns list of (name, value, error)."""
    import ROOT
    f = ROOT.TFile(input_file)
    fr = f.Get(fitresult_name)
    if not fr:
        raise RuntimeError("Could not find RooFitResult '%s' in %s" % (fitresult_name, input_file))
    params = []
    for p in fr.floatParsFinal():
        params.append((p.GetName(), p.getVal(), p.getError()))
    f.Close()
    return params


def read_fitresult_text(text_block):
    """Fallback: parse a pasted RooFitResult::Print() text block instead of reading ROOT directly.
    Matches lines like: '  paramName   1.2345e+00 +/-  6.78e-01'
    """
    pattern = re.compile(r"^\s*(\S+)\s+([\-+0-9.eE]+)\s*\+/-\s*([\-+0-9.eE]+)\s*$")
    params = []
    for line in text_block.splitlines():
        m = pattern.match(line)
        if m:
            name, val, err = m.groups()
            try:
                params.append((name, float(val), float(err)))
            except ValueError:
                continue
    return params


def make_pull_plot(params, out_dir):
    """Standard nuisance pull plot: pull = value/error, sorted by |pull|, with 1/2 sigma bands."""
    entries = [(n, v, e) for n, v, e in params if classify(n) == "nuisance" and e > 0]
    if not entries:
        print(" --> No constrained nuisances with nonzero error found, skipping pull plot.")
        return
    entries.sort(key=lambda t: abs(t[1] / t[2]))
    names = [n for n, v, e in entries]
    pulls = [v / e for n, v, e in entries]

    fig_h = max(4, 0.22 * len(entries))
    fig, ax = plt.subplots(figsize=(8, fig_h))

    ax.axvspan(-2, -1, color="gold", alpha=0.3)
    ax.axvspan(1, 2, color="gold", alpha=0.3)
    ax.axvspan(-1, 1, color="mediumseagreen", alpha=0.3)
    ax.axvline(0, color="black", linewidth=1)

    y = np.arange(len(entries))
    ax.errorbar(pulls, y, xerr=1.0, fmt="o", color="black", markersize=4, capsize=2, linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel(r"Pull: $(\hat{\theta} - \theta_0)/\sigma_\theta$")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, len(entries))
    ax.set_title("Postfit nuisance pulls (%d constrained parameters)" % len(entries))
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(out_dir, "nuisance_pulls.%s" % ext), dpi=150)
    plt.close(fig)
    print(" --> Saved nuisance_pulls.png/.pdf (%d parameters)" % len(entries))


def make_poi_plot(params, out_dir):
    entries = [(n, v, e) for n, v, e in params if classify(n) == "poi"]
    if not entries:
        print(" --> No POIs found (looked for names starting with %s), skipping." % (POI_PREFIXES,))
        return
    names = [n for n, v, e in entries]
    vals = [v for n, v, e in entries]
    errs = [e for n, v, e in entries]

    fig, ax = plt.subplots(figsize=(6, 1.2 * len(entries) + 1))
    y = np.arange(len(entries))
    ax.errorbar(vals, y, xerr=errs, fmt="o", color="crimson", markersize=8, capsize=4, linewidth=2)
    ax.axvline(1.0, color="gray", linestyle="--", linewidth=1, label="SM (r=1)")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=11)
    ax.set_xlabel("Best-fit value")
    ax.set_ylim(-1, len(entries))
    ax.legend(loc="best", fontsize=9)
    ax.set_title("Parameters of interest")
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(out_dir, "poi_values.%s" % ext), dpi=150)
    plt.close(fig)
    print(" --> Saved poi_values.png/.pdf (%d POIs)" % len(entries))
    for n, v, e in entries:
        print("     %s = %.4f +/- %.4f" % (n, v, e))


def make_bkg_norm_plot(params, out_dir):
    entries = [(n, v, e) for n, v, e in params if classify(n) == "bkg_norm"]
    if not entries:
        print(" --> No background normalizations found, skipping.")
        return
    entries.sort(key=lambda t: t[1])
    names = [n.replace("shapeBkg_bkg_mass_", "").replace("__norm", "") for n, v, e in entries]
    vals = [v for n, v, e in entries]
    errs = [e for n, v, e in entries]

    fig, ax = plt.subplots(figsize=(8, max(4, 0.35 * len(entries))))
    y = np.arange(len(entries))
    ax.errorbar(vals, y, xerr=errs, fmt="s", color="steelblue", markersize=6, capsize=3, linewidth=1.5)
    ax.set_xscale("log")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlabel("Fitted background yield (events, log scale)")
    ax.set_ylim(-1, len(entries))
    ax.set_title("Per-category background normalization")
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(out_dir, "bkg_norms.%s" % ext), dpi=150)
    plt.close(fig)
    print(" --> Saved bkg_norms.png/.pdf (%d categories)" % len(entries))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputFile", help="ROOT file containing the RooFitResult (e.g. multidimfit_AsimovPostfit.root)")
    parser.add_argument("--fitResultName", default="fit_mdf", help="Name of the RooFitResult object inside the file")
    parser.add_argument("--textFile", help="Fallback: a text file containing a pasted RooFitResult::Print() block, "
                                            "used instead of --inputFile if PyROOT/ROOT isn't available")
    parser.add_argument("--outDir", default="./FitResultPlots", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.outDir, exist_ok=True)

    if args.inputFile:
        params = read_fitresult_root(args.inputFile, args.fitResultName)
    elif args.textFile:
        with open(args.textFile) as f:
            params = read_fitresult_text(f.read())
    else:
        print("Provide --inputFile <root file> (needs PyROOT) or --textFile <pasted text>.", file=sys.stderr)
        sys.exit(1)

    print(" --> Parsed %d floating parameters" % len(params))
    make_pull_plot(params, args.outDir)
    make_poi_plot(params, args.outDir)
    make_bkg_norm_plot(params, args.outDir)


if __name__ == "__main__":
    main()
