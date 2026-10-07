#!/usr/bin/env python3
"""2D likelihood scan plotter -- overlay Stat.+syst. vs Stat.-only.

Same single-interpolation-from-real-points method as make2DPlot_tri.py
(matplotlib tricontour/tripcolor, no rasterization -> no staircase
artifact), but takes TWO input scan files and overlays their 68%/95% CL
contours on one plot: black = Stat.+syst., orange (C1) = Stat.-only.
The color heatmap is drawn from the Stat.+syst. scan (the primary result).

Example:
  python3 make2DPlot_tri_overlay.py \
    --scanStatSyst higgsCombine_2Dscan_statsyst.MultiDimFit.mH125.08.root \
    --scanStatOnly higgsCombine_2Dscan_statonly.MultiDimFit.mH125.08.root \
    --xparam "r_tHq:-10,25" \
    --yparam "r_ttH:-0.5,3.0" \
    --doShift --doBestFit --doSM --ext _stat_vs_syst
"""

import os
from optparse import OptionParser

import numpy as np
import uproot
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG 2D PLOTTER (tricontour, overlay) ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")


def get_options():
    parser = OptionParser()
    parser.add_option("--scanStatSyst", dest="scanStatSyst", default=None, help="Stat.+syst. scan ROOT file")
    parser.add_option("--scanStatOnly", dest="scanStatOnly", default=None, help="Stat.-only scan ROOT file")
    parser.add_option("--xparam", dest="xparam", default="r_tHq:-20,25", help="X-parameter:range")
    parser.add_option("--yparam", dest="yparam", default="r_ttH:-0.5,3.0", help="Y-parameter:range")
    parser.add_option("--doShift", dest="doShift", default=False, action="store_true", help="Shift minimum to 0 (each scan shifted to its own minimum)")
    parser.add_option("--doBestFit", dest="doBestFit", default=False, action="store_true", help="Draw best fit point (from Stat.+syst.)")
    parser.add_option("--doSM", dest="doSM", default=False, action="store_true", help="Draw SM point")
    parser.add_option("--ext", dest="ext", default='', help="Extension for saving")
    parser.add_option("--placeLegend", dest="placeLegend", default='', help="Legend position")
    parser.add_option("--max-dnll", dest="max_dnll", default=8.0, type='float', help="Max -2*deltaNLL to keep/show")
    parser.add_option("--figWidth", dest="figWidth", default=6.0, type='float', help="Figure width (inches)")
    parser.add_option("--figHeight", dest="figHeight", default=6.0, type='float', help="Figure height (inches)")
    return parser.parse_args()


(opt, args) = get_options()

translatePOIs = {
    "r_ttH": r"$\mu_{ttH}$",
    "r_tHq": r"$\mu_{tHq}$",
}


def Translate(name, ndict):
    return ndict[name] if name in ndict else name


x, x_range = opt.xparam.split(":")[0], [float(p) for p in opt.xparam.split(":")[1].split(",")]
y, y_range = opt.yparam.split(":")[0], [float(p) for p in opt.yparam.split(":")[1].split(",")]

LEVEL_68, LEVEL_95 = 2.30, 5.99


def load_scan(root_path, doShift, max_dnll):
    """Load one scan directly from the combine tree -- single interpolation,
    no re-gridding. Drops non-converged/unphysical/far-from-best-fit points."""
    with uproot.open(root_path) as f:
        tree = f["limit"]
        xvals = tree[x].array(library="np")
        yvals = tree[y].array(library="np")
        dnll = tree["deltaNLL"].array(library="np") * 2.0  # -> -2*deltaNLL

    mask = np.isfinite(xvals) & np.isfinite(yvals) & np.isfinite(dnll) & (dnll >= 0)
    if doShift:
        # shift is applied after masking to non-negative finite points only
        pass
    xvals, yvals, dnll = xvals[mask], yvals[mask], dnll[mask]

    if doShift:
        dnll = dnll - np.min(dnll)

    # display cut: drop points far beyond what's informative (matches
    # reference script's max_dnll cut -- keeps the white "excluded" region
    # white instead of solid-color)
    mask2 = dnll <= max_dnll
    n_drop = np.size(dnll) - int(np.count_nonzero(mask2))
    if n_drop > 0:
        print(f"[INFO] {root_path}: dropping {n_drop} points with -2dNLL > {max_dnll}")

    return xvals[mask2], yvals[mask2], dnll[mask2]


# --------------------------------------------------------------------------
# Load both scans (each interpolated once, directly from its own real
# scanned points -- no rasterization, no cross-contamination between scans)
# --------------------------------------------------------------------------
xs, ys, dnll_s = load_scan(opt.scanStatSyst, opt.doShift, opt.max_dnll)
xo, yo, dnll_o = load_scan(opt.scanStatOnly, opt.doShift, opt.max_dnll)

best_idx = int(np.argmin(dnll_s))  # best fit taken from Stat.+syst.

# --------------------------------------------------------------------------
# Plot
# --------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(opt.figWidth, opt.figHeight))

# Heatmap from Stat.+syst. (the primary result)
hm = ax.tripcolor(
    xs, ys, dnll_s,
    shading="gouraud",
    cmap="viridis",
    vmin=0.0,
    vmax=opt.max_dnll,
)
cbar = fig.colorbar(hm, ax=ax, pad=0.02)
cbar.set_label(r"$-2\Delta\ln\mathcal{L}$", fontsize=13)
cbar.ax.minorticks_on()

# Stat.-only contours (orange), drawn first
ax.tricontour(xo, yo, dnll_o, levels=[LEVEL_68], colors="C1", linewidths=2.2, linestyles="-", zorder=3)
ax.tricontour(xo, yo, dnll_o, levels=[LEVEL_95], colors="C1", linewidths=2.2, linestyles="--", zorder=3)

# Stat.+syst. contours (black), drawn on top
ax.tricontour(xs, ys, dnll_s, levels=[LEVEL_68], colors="black", linewidths=2.2, linestyles="-", zorder=4)
ax.tricontour(xs, ys, dnll_s, levels=[LEVEL_95], colors="black", linewidths=2.2, linestyles="--", zorder=4)

# SM point
sm_handle = None
if opt.doSM:
    (sm_handle,) = ax.plot(
        [1.0], [1.0],
        marker="D", markersize=9,
        color="red", markeredgecolor="black", markeredgewidth=0.6,
        linestyle="none", zorder=5,
    )

# Best-fit point (from Stat.+syst.)
bf_handle = None
if opt.doBestFit:
    (bf_handle,) = ax.plot(
        [xs[best_idx]], [ys[best_idx]],
        marker="x", markersize=9, markeredgewidth=1.6,
        color="black", linestyle="none", zorder=6,
    )

# Axis labels / ranges
ax.set_xlabel(Translate(x, translatePOIs), fontsize=15)
ax.set_ylabel(Translate(y, translatePOIs), fontsize=15)
ax.set_xlim(x_range[0], x_range[1])
ax.set_ylim(y_range[0], y_range[1])
ax.tick_params(direction="in", which="both", top=True, right=True, labelsize=12)
ax.minorticks_on()

# CMS label
ax.text(0.0, 1.02, r"$\bf{CMS}$ $\it{Preliminary}$", transform=ax.transAxes,
        fontsize=15, ha="left", va="bottom")
ax.text(1.0, 1.02, r"62.4 fb$^{-1}$ (13.6 TeV)", transform=ax.transAxes,
        fontsize=13, ha="right", va="bottom")

# Legend
legend_handles = [
    Line2D([0], [0], color="C1", lw=2.2, linestyle="-"),
    Line2D([0], [0], color="black", lw=2.2, linestyle="-"),
    Line2D([0], [0], color="C1", lw=2.2, linestyle="--"),
    Line2D([0], [0], color="black", lw=2.2, linestyle="--"),
]
legend_labels = [
    "Stat.-only, 68% CL",
    "Stat.+syst., 68% CL",
    "Stat.-only, 95% CL",
    "Stat.+syst., 95% CL",
]
if opt.doBestFit:
    legend_handles.append(bf_handle)
    legend_labels.append("Stat.+syst., best-fit")
if opt.doSM:
    legend_handles.append(sm_handle)
    legend_labels.append("SM")

loc = "lower right" if opt.placeLegend == "bottom_right" else "upper right"
ax.legend(legend_handles, legend_labels, loc=loc, frameon=False, fontsize=10, ncol=2,
          labelspacing=0.4, columnspacing=0.8, handletextpad=0.4)

fig.tight_layout()

out_dir = "./Final2DPlots"
os.makedirs(out_dir, exist_ok=True)
outbase = f"{out_dir}/scan2D_{x}_vs_{y}{opt.ext}"
fig.savefig(outbase + ".png", dpi=200)
fig.savefig(outbase + ".pdf")
plt.close(fig)

print(f"Saved: {outbase}.png / .pdf")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG 2D PLOTTER (tricontour, overlay) (END) ~~~~~~~~~~~~~~~~~~~~~~~~ ")
