#!/usr/bin/env python3
"""
plot_fitresult.py -- visualize a Combine RooFitResult (e.g. multidimfit_*.root)
as readable, paginated plots instead of one giant text dump.

Usage (on lxplus, inside your CMSSW/combine environment):
  python3 plot_fitresult.py --inputFile multidimfit_AsimovPostfit.root --fitResultName fit_mdf

Produces, in ./FitResultPlots/:
  - nuisance_pulls_pageN.png/.pdf : constrained nuisances, PAGINATED (--perPage, default 15),
                                     sorted by |pull| across the whole set before paging
  - poi_values.png/.pdf           : your POIs (r_tHq, r_ttH, ...) with error bars
  - bkg_norms.png/.pdf            : per-category background normalizations (log scale)
  - shape_envelope_pageN.png/.pdf : the env_pdf_* background-shape coefficients (UNCONSTRAINED --
                                     no prior, so these are NOT pulls; plotted as raw postfit
                                     value +/- error instead)

============================================================================
WHAT "PULL" MEANS HERE, AND WHERE THE PREFIT VALUE/SIGMA COME FROM
============================================================================
A pull is defined as:
    pull = (postfit_value - prefit_central) / prefit_sigma

For every nuisance in this datacard, prefit_central = 0 by construction --
that's how RooFit/Combine build BOTH lnN and "param" type nuisances: as a
parameter centered at 0 pre-fit, with a Gaussian constraint pulling it back
toward 0 (the constraint IS the prior).

prefit_sigma is NOT always 1, and this script does not assume it is:
  - For "lnN" datacard entries (the vast majority here), Combine internally
    ALWAYS builds the nuisance parameter itself as a standard N(0,1) --
    the actual asymmetric % magnitude you wrote in the datacard (e.g.
    0.998/1.002) is applied separately, as a multiplicative rate function
    of that N(0,1) parameter. So prefit_sigma = 1.0 for these.
  - For "param" type entries, the datacard line format is
        <name> param <prefit_central> <prefit_sigma>
    and the SECOND number IS the prefit sigma directly. From your actual
    datacard: ScaleEB=2.0, ScaleEE=2.0, Smearing=1.0, Material=1.0, FNUF=1.0.
    These are hardcoded in PARAM_PREFIT_SIGMA below, taken directly from
    your uploaded datacard text -- if your real datacard has more "param"
    lines, or different widths, EDIT that dict (or pass --paramWidths a
    JSON file of {name: sigma} to override/extend it without editing code).

The postfit error you see in the fit result (e.g. 5.26e-01) is a SEPARATE
number from prefit_sigma -- it tells you how much the DATA constrained that
parameter beyond the prior alone. This script plots that as the horizontal
error bar, expressed as postfit_sigma / prefit_sigma (so 1.0 = data added no
extra constraining power beyond the prior; < 1.0 = the fit constrained it
further than the prior alone did).
============================================================================
"""

import argparse
import json
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

POI_PREFIXES = ("r_",)

# Prefit sigma for "param"-type nuisances, taken directly from the datacard
# lines: "<name> param <center> <sigma>". Default for everything else
# (i.e. every "lnN" nuisance) is 1.0 -- see the module docstring above for why.
PARAM_PREFIT_SIGMA = {
    "CMS_hgg_nuisance_ScaleEB": 2.0,
    "CMS_hgg_nuisance_ScaleEE": 2.0,
    "CMS_hgg_nuisance_Smearing": 1.0,
    "CMS_hgg_nuisance_Material": 1.0,
    "CMS_hgg_nuisance_FNUF": 1.0,
}


def classify(name):
    if name.startswith("env_pdf"):
        return "shape_envelope"
    if "__norm" in name:
        return "bkg_norm"
    if any(name.startswith(p) for p in POI_PREFIXES):
        return "poi"
    return "nuisance"


def prefit_sigma_for(name, overrides):
    if name in overrides:
        return overrides[name]
    return 1.0


def read_fitresult_root(input_file, fitresult_name):
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


def paginate(entries, per_page):
    for i in range(0, len(entries), per_page):
        yield entries[i:i + per_page]


def make_pull_plots(params, out_dir, per_page, sigma_overrides):
    """Paginated pull plot: pull = value/prefit_sigma, xerr = postfit_sigma/prefit_sigma."""
    entries = [(n, v, e) for n, v, e in params if classify(n) == "nuisance" and e > 0]
    if not entries:
        print(" --> No constrained nuisances with nonzero error found, skipping pull plots.")
        return

    scored = []
    for n, v, e in entries:
        prefit_sigma = prefit_sigma_for(n, sigma_overrides)
        pull = v / prefit_sigma
        ratio = e / prefit_sigma
        scored.append((n, pull, ratio, prefit_sigma))
    scored.sort(key=lambda t: abs(t[1]))

    n_pages = (len(scored) + per_page - 1) // per_page
    for page_idx, page in enumerate(paginate(scored, per_page), start=1):
        names = [n for n, p, r, s in page]
        pulls = [p for n, p, r, s in page]
        ratios = [r for n, p, r, s in page]

        fig, ax = plt.subplots(figsize=(8, max(3, 0.5 * len(page) + 1)))
        ax.axvspan(-2, -1, color="gold", alpha=0.3)
        ax.axvspan(1, 2, color="gold", alpha=0.3)
        ax.axvspan(-1, 1, color="mediumseagreen", alpha=0.3)
        ax.axvline(0, color="black", linewidth=1)

        y = np.arange(len(page))
        ax.errorbar(pulls, y, xerr=ratios, fmt="o", color="black", markersize=5, capsize=3, linewidth=1.3)
        ax.set_yticks(y)
        ax.set_yticklabels(names, fontsize=9)
        ax.set_xlabel(r"Pull: $\hat{\theta}/\sigma_{\rm prefit}$   (error bar = $\sigma_{\rm postfit}/\sigma_{\rm prefit}$)")
        ax.set_xlim(-3, 3)
        ax.set_ylim(-1, len(page))
        ax.set_title("Postfit nuisance pulls -- page %d/%d (params %d-%d of %d)" %
                      (page_idx, n_pages, (page_idx - 1) * per_page + 1,
                       (page_idx - 1) * per_page + len(page), len(scored)))
        fig.tight_layout()
        for ext in ("png", "pdf"):
            fig.savefig(os.path.join(out_dir, "nuisance_pulls_page%d.%s" % (page_idx, ext)), dpi=150)
        plt.close(fig)

    print(" --> Saved %d nuisance pull page(s) (.png + .pdf), %d params/page, %d total" %
          (n_pages, per_page, len(scored)))


def make_shape_envelope_plots(params, out_dir, per_page):
    """Separate plot(s) for env_pdf_* -- these are UNCONSTRAINED (no prior), so plotted as
    raw postfit value +/- error, not as a pull. Entries with error==0 (not the currently
    active pdfindex choice for their category) are shown grayed out for context."""
    entries = [(n, v, e) for n, v, e in params if classify(n) == "shape_envelope"]
    if not entries:
        print(" --> No env_pdf_* shape-envelope parameters found, skipping.")
        return

    entries.sort(key=lambda t: t[0])
    n_pages = (len(entries) + per_page - 1) // per_page
    for page_idx, page in enumerate(paginate(entries, per_page), start=1):
        names = [n for n, v, e in page]
        vals = [v for n, v, e in page]
        errs = [e for n, v, e in page]
        colors = ["steelblue" if e > 0 else "lightgray" for n, v, e in page]

        fig, ax = plt.subplots(figsize=(8, max(3, 0.5 * len(page) + 1)))
        y = np.arange(len(page))
        for yi, (val, err, col) in enumerate(zip(vals, errs, colors)):
            ax.errorbar([val], [yi], xerr=[err] if err > 0 else None, fmt="o",
                        color=col, markersize=6, capsize=3, linewidth=1.3)
        ax.axvline(0, color="black", linewidth=0.8, linestyle=":")
        ax.set_yticks(y)
        ax.set_yticklabels(names, fontsize=9)
        ax.set_xlabel("Postfit value (raw -- UNCONSTRAINED, not a pull; see note below)")
        ax.set_ylim(-1, len(page))
        ax.set_title("Background shape envelope (env_pdf_*) -- page %d/%d\n"
                      "blue = active pdfindex (real error)   gray = inactive candidate (error=0)" %
                      (page_idx, n_pages), fontsize=9)
        fig.tight_layout()
        for ext in ("png", "pdf"):
            fig.savefig(os.path.join(out_dir, "shape_envelope_page%d.%s" % (page_idx, ext)), dpi=150)
        plt.close(fig)

    n_active = sum(1 for n, v, e in entries if e > 0)
    print(" --> Saved %d shape-envelope page(s) (.png + .pdf), %d params/page, %d total (%d active, %d inactive)" %
          (n_pages, per_page, len(entries), n_active, len(entries) - n_active))


def make_poi_plot(params, out_dir):
    entries = [(n, v, e) for n, v, e in params if classify(n) == "poi"]
    if not entries:
        print(" --> No POIs found, skipping.")
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
    parser.add_argument("--inputFile", help="ROOT file containing the RooFitResult")
    parser.add_argument("--fitResultName", default="fit_mdf")
    parser.add_argument("--textFile", help="Fallback: pasted RooFitResult::Print() text block")
    parser.add_argument("--outDir", default="./FitResultPlots")
    parser.add_argument("--perPage", type=int, default=15, help="Max parameters per page (default 15)")
    parser.add_argument("--paramWidths", default=None,
                         help="Optional JSON file {name: prefit_sigma} to override/extend PARAM_PREFIT_SIGMA")
    args = parser.parse_args()

    os.makedirs(args.outDir, exist_ok=True)

    sigma_overrides = dict(PARAM_PREFIT_SIGMA)
    if args.paramWidths:
        with open(args.paramWidths) as f:
            sigma_overrides.update(json.load(f))

    if args.inputFile:
        params = read_fitresult_root(args.inputFile, args.fitResultName)
    elif args.textFile:
        with open(args.textFile) as f:
            params = read_fitresult_text(f.read())
    else:
        print("Provide --inputFile <root file> (needs PyROOT) or --textFile <pasted text>.", file=sys.stderr)
        sys.exit(1)

    print(" --> Parsed %d floating parameters" % len(params))
    make_pull_plots(params, args.outDir, args.perPage, sigma_overrides)
    make_shape_envelope_plots(params, args.outDir, args.perPage)
    make_poi_plot(params, args.outDir)
    make_bkg_norm_plot(params, args.outDir)


if __name__ == "__main__":
    main()
