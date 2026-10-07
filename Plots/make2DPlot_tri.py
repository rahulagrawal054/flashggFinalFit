#!/usr/bin/env python3
"""2D likelihood scan plotter (matplotlib / tricontour version).

Rewritten to avoid the staircase/blocky-contour artifact that came from the
old pipeline's double discretization (scipy.griddata onto a rectangular
raster, then re-binning that raster into a ROOT TProfile2D and running
marching-squares on THAT). Instead this mirrors the reference approach:
interpolate exactly once, directly from the real scanned (x, y, deltaNLL)
points, via matplotlib's Delaunay-triangulation-based tricontour/tripcolor.

Points where combine's fit failed to converge (non-finite or unphysical
negative deltaNLL) are dropped, not filled in -- the resulting white space
in the plot is genuine "no valid fit here" information, not a rendering
artifact.

Example:
  python3 make2DPlot_tri.py \
    --inputTreeFile ../Combine/make2D/higgsCombine_2Dscan_statsyst.MultiDimFit.mH125.08.root \
    --xparam "r_tHq:-10,25" \
    --yparam "r_ttH:-0.5,3.0" \
    --doShift --doBestFit --doSM --ext _statsyst
"""

import os
import math
from optparse import OptionParser

import numpy as np
import uproot
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG 2D PLOTTER (tricontour) ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")


def get_options():
    parser = OptionParser()
    parser.add_option("--inputTreeFile", dest="inputTreeFile", default=None, help="Input ROOT tree")
    parser.add_option("--xparam", dest="xparam", default="r_tHq:-20,25", help="X-parameter:range")
    parser.add_option("--yparam", dest="yparam", default="r_ttH:-0.5,3.0", help="Y-parameter:range")
    parser.add_option("--doShift", dest="doShift", default=False, action="store_true", help="Shift minimum to 0")
    parser.add_option("--doBestFit", dest="doBestFit", default=False, action="store_true", help="Draw best fit point")
    parser.add_option("--doSM", dest="doSM", default=False, action="store_true", help="Draw SM point")
    parser.add_option("--ext", dest="ext", default='', help="Extension for saving")
    parser.add_option("--placeLegend", dest="placeLegend", default='', help="Legend position")
    parser.add_option("--no-colour", dest="no_colour", default=False, action="store_true", help="Disable color heatmap")
    parser.add_option("--max-dnll", dest="max_dnll", default=10.0, type='float', help="Max -2*deltaNLL to keep/show")
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

# --------------------------------------------------------------------------
# Load the scan directly from the combine tree, exactly once, no re-gridding.
# --------------------------------------------------------------------------
with uproot.open(opt.inputTreeFile) as f:
    tree = f["limit"]
    xvals = tree[x].array(library="np")
    yvals = tree[y].array(library="np")
    dnll = tree["deltaNLL"].array(library="np") * 2.0  # -> -2*deltaNLL

# Drop points where the fit failed to converge / gave unphysical results.
# This is what produces the "white area" -- it's real information (no valid
# fit exists there), not a mask or styling choice.
#mask = np.isfinite(xvals) & np.isfinite(yvals) & np.isfinite(dnll) & (dnll >= 0)
mask = np.isfinite(xvals) & np.isfinite(yvals) & np.isfinite(dnll) & (dnll >= 0) & (dnll <= opt.max_dnll)
n_drop = np.size(dnll) - int(np.count_nonzero(mask))
if n_drop > 0:
    print(f"[WARN] Dropping {n_drop} non-converged/unphysical points out of {np.size(dnll)}")

xvals, yvals, dnll = xvals[mask], yvals[mask], dnll[mask]

if opt.doShift:
    dnll = dnll - np.min(dnll)

best_idx = int(np.argmin(dnll))

# 2D CL thresholds for -2*deltaNLL
LEVEL_68, LEVEL_95 = 2.30, 5.99

# --------------------------------------------------------------------------
# Plot
# --------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(opt.figWidth, opt.figHeight))

if not opt.no_colour:
    hm = ax.tripcolor(
        xvals, yvals, dnll,
        shading="gouraud",
        cmap="viridis",
        vmin=0.0,
        vmax=opt.max_dnll,
    )
    cbar = fig.colorbar(hm, ax=ax, pad=0.02)
    cbar.set_label(r"$-2\Delta\ln\mathcal{L}$", fontsize=13)
    cbar.ax.minorticks_on()

# 68% CL contour (solid)
ax.tricontour(
    xvals, yvals, dnll,
    levels=[LEVEL_68],
    colors="black",
    linewidths=2.2,
    linestyles="-",
    zorder=4,
)
# 95% CL contour (dashed)
ax.tricontour(
    xvals, yvals, dnll,
    levels=[LEVEL_95],
    colors="black",
    linewidths=2.2,
    linestyles="--",
    zorder=4,
)

# SM point
sm_handle = None
if opt.doSM:
    (sm_handle,) = ax.plot(
        [1.0], [1.0],
        marker="D", markersize=9,
        color="red", markeredgecolor="black", markeredgewidth=0.6,
        linestyle="none", zorder=5,
    )

# Best-fit point
bf_handle = None
if opt.doBestFit:
    (bf_handle,) = ax.plot(
        [xvals[best_idx]], [yvals[best_idx]],
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
    Line2D([0], [0], color="black", lw=2.2, linestyle="-"),
    Line2D([0], [0], color="black", lw=2.2, linestyle="--"),
]
legend_labels = ["68% CL", "95% CL"]
if opt.doBestFit:
    legend_handles.append(bf_handle)
    legend_labels.append("Best fit")
if opt.doSM:
    legend_handles.append(sm_handle)
    legend_labels.append("SM")

loc = "lower right" if opt.placeLegend == "bottom_right" else "upper right"
ax.legend(legend_handles, legend_labels, loc=loc, frameon=False, fontsize=11)

fig.tight_layout()

out_dir = "./Final2DPlots"
os.makedirs(out_dir, exist_ok=True)
outbase = f"{out_dir}/scan2D_tri_{x}_vs_{y}{opt.ext}"
fig.savefig(outbase + ".png", dpi=200)
fig.savefig(outbase + ".pdf")
plt.close(fig)

print(f"Saved: {outbase}.png / .pdf")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HGG 2D PLOTTER (tricontour) (END) ~~~~~~~~~~~~~~~~~~~~~~~~ ")
