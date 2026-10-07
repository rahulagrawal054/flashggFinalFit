#!/usr/bin/env python3

import os
import re
import math
import argparse

import numpy as np
import uproot
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

plt.rcParams["figure.figsize"] = (12.5, 10)


# ============================================================
# Arguments
# ============================================================

parser = argparse.ArgumentParser(
    description="Bias in significance: fixed vs envelope"
)

parser.add_argument(
    "-i", "--inputDir",
    required=True,
    help="Input directory containing Significance ROOT files"
)

parser.add_argument(
    "--use-mplhep",
    action="store_true"
)

parser.add_argument(
    "--expectedToys",
    type=int,
    default=None,
    help="Expected total toy count (e.g. 20000), used to flag categories where "
         "condor jobs produced fewer toys than intended"
)

parser.add_argument(
    "--summaryFile",
    default=None,
    help="If given, append one CSV row per mode/POI combination to this file "
         "(category,poi_test,poi_profile,mode,raw_toys,expected_toys,"
         "pct_of_expected,dropped_by_zcut,used_in_plot). Header is written "
         "once if the file doesn't already exist."
)

args = parser.parse_args()

if args.summaryFile and not os.path.exists(args.summaryFile):
    with open(args.summaryFile, "w") as sf:
        sf.write(
            "category,poi_test,poi_profile,mode,raw_toys,expected_toys,"
            "missing_toys,pct_of_expected,dropped_by_zcut,used_in_plot\n"
        )


if args.use_mplhep:
    import mplhep
    mplhep.style.use("CMS")


INPUT_DIR = os.path.abspath(args.inputDir)
PLOT_DIR = os.path.join(INPUT_DIR, "plots")

os.makedirs(PLOT_DIR, exist_ok=True)


# ============================================================
# Category
# Example:
# ttH_had_1_5000toys --> ttH_had_1
# ============================================================

folder_name = os.path.basename(INPUT_DIR.rstrip("/"))
category = re.sub(r"_\d+toys$", "", folder_name)


print("==============================================")
print("Bias in Significance")
print("Input directory :", INPUT_DIR)
print("Category        :", category)
print("==============================================")


# ============================================================
# Find ROOT files automatically
# ============================================================

root_files = {}

for filename in os.listdir(INPUT_DIR):

    if not filename.endswith(".root"):
        continue

    # Fixed
    match = re.match(
        r"higgsCombine_fixed_(r_\w+)_test_(r_\w+)_profile_.*\.Significance\..*\.root",
        filename
    )

    if match:

        poi_test = match.group(1)
        poi_profile = match.group(2)

        root_files[
            ("fixed", poi_test, poi_profile)
        ] = os.path.join(INPUT_DIR, filename)

        continue

    # Envelope
    match = re.match(
        r"higgsCombine_envelope_(r_\w+)_test_(r_\w+)_profile_.*\.Significance\..*\.root",
        filename
    )

    if match:

        poi_test = match.group(1)
        poi_profile = match.group(2)

        root_files[
            ("envelope", poi_test, poi_profile)
        ] = os.path.join(INPUT_DIR, filename)


print("\nFound files:")

for key, filename in sorted(root_files.items()):
    print(
        " ",
        key,
        "->",
        os.path.basename(filename)
    )


# ============================================================
# Z points
# ============================================================

Z_points = np.linspace(0, 3.5, 100)

p_gaus = np.array([
    (1 - math.erf(Z / math.sqrt(2))) / 2
    for Z in Z_points
])

z_thr = 4


# ============================================================
# Read ROOT file
# ============================================================

def read_significance(filename, label="", cat=None, poi_test=None, poi_profile=None):

    f = uproot.open(filename)

    z_raw = np.array(
        f["limit"].arrays("limit")["limit"]
    )
    raw_N = len(z_raw)

    # Remove failed fits
    z = z_raw[z_raw < z_thr]
    dropped_by_cut = raw_N - len(z)

    pct = None
    missing = None
    msg = f"{label}: {raw_N} toys found"
    if args.expectedToys is not None:
        missing = args.expectedToys - raw_N
        pct = 100.0 * raw_N / args.expectedToys
        msg += f" ({pct:.1f}% of expected {args.expectedToys}, {missing} missing)"
        if pct < 90:
            msg += "  <-- SHORTFALL, check for failed/missing condor jobs"
    msg += f"; {dropped_by_cut} removed by z<{z_thr} cut -> {len(z)} used in plot"

    print(msg)

    if args.summaryFile:
        with open(args.summaryFile, "a") as sf:
            sf.write(
                f"{cat},{poi_test},{poi_profile},{label},{raw_N},"
                f"{args.expectedToys if args.expectedToys is not None else ''},"
                f"{missing if missing is not None else ''},"
                f"{f'{pct:.1f}' if pct is not None else ''},"
                f"{dropped_by_cut},{len(z)}\n"
            )

    return z


# ============================================================
# Calculate p-value curve and uncertainty
# ============================================================

def calculate_p(z):

    N = len(z)

    p = []
    err = []

    for Z in Z_points:

        k = np.sum(z > Z, dtype=float)

        p.append(k / N)

        # Bayesian binomial uncertainty
        variance = (
            ((k + 1) * (k + 2))
            / ((N + 2) * (N + 3))
            -
            ((k + 1) * (k + 1))
            / ((N + 2) * (N + 2))
        )

        err.append(np.sqrt(variance))

    return np.array(p), np.array(err), N


# ============================================================
# Make one plot
# ============================================================

def make_plot(poi_test, poi_profile):

    fixed_key = (
        "fixed",
        poi_test,
        poi_profile
    )

    envelope_key = (
        "envelope",
        poi_test,
        poi_profile
    )

    if fixed_key not in root_files:
        print(
            "\nMissing fixed file:",
            poi_test,
            poi_profile
        )
        return

    if envelope_key not in root_files:
        print(
            "\nMissing envelope file:",
            poi_test,
            poi_profile
        )
        return

    fixed_file = root_files[fixed_key]
    envelope_file = root_files[envelope_key]

    print("\n----------------------------------------------")
    print("Making plot")
    print("Category    :", category)
    print("Test POI    :", poi_test)
    print("Profile POI :", poi_profile)
    print("----------------------------------------------")

    # --------------------------------------------------------
    # Read toys
    # --------------------------------------------------------

    z_fixed = read_significance(fixed_file, label="fixed", cat=category, poi_test=poi_test, poi_profile=poi_profile)
    z_envelope = read_significance(envelope_file, label="envelope", cat=category, poi_test=poi_test, poi_profile=poi_profile)

    p_fixed, err_fixed, N_fixed = calculate_p(z_fixed)
    p_envelope, err_envelope, N_envelope = calculate_p(z_envelope)

    # --------------------------------------------------------
    # Figure
    # --------------------------------------------------------
    #
    # Layout, matching the original single-POI script exactly:
    #
    # axs[0] = Bottom  (y=0.10-0.28, small)  -> Ratio to fixed
    #                                           (has the shared x-axis label)
    # axs[1] = Middle  (y=0.32-0.50, small)  -> Ratio to Gaussian
    # axs[2] = Top     (y=0.55-0.95, tall)   -> Type-1 error rate
    #                                           (main legend lives here)

    fig = plt.figure(figsize=(12, 12))

    left = 0.08
    width = 0.82

    axs = []

    # Bottom
    axs.append(
        fig.add_axes(
            [left, 0.10, width, 0.18]
        )
    )

    # Middle
    axs.append(
        fig.add_axes(
            [left, 0.32, width, 0.18]
        )
    )

    # TOP
    axs.append(
        fig.add_axes(
            [left, 0.55, width, 0.40]
        )
    )

    # ========================================================
    # BOTTOM PANEL (axs[0])
    # Ratio to fixed
    # ========================================================

    axs[0].plot(
        Z_points, p_fixed / p_fixed,
        ls="-", color="red", linewidth=2
    )
    axs[0].fill_between(
        Z_points,
        (p_fixed - err_fixed) / p_fixed,
        (p_fixed + err_fixed) / p_fixed,
        color="salmon", alpha=0.2
    )

    axs[0].plot(
        Z_points, p_envelope / p_fixed,
        ls="-", color="mediumblue", linewidth=2
    )
    axs[0].fill_between(
        Z_points,
        (p_envelope - err_envelope) / p_fixed,
        (p_envelope + err_envelope) / p_fixed,
        color="cornflowerblue", alpha=0.2
    )

    axs[0].fill_between(Z_points, 0.8, 0.9, color="orange", alpha=0.2)
    axs[0].fill_between(Z_points, 0.9, 1.1, color="limegreen", alpha=0.2, label="$<10$%")
    axs[0].fill_between(Z_points, 1.1, 1.2, color="orange", alpha=0.2, label="$<20$%")
    axs[0].legend(loc="upper left", fontsize=12, frameon=True)

    axs[0].set_ylim(0.5, 1.5)
    axs[0].set_xlim(0, 2.5)
    axs[0].set_ylabel("Ratio to fixed", fontsize=16)
    axs[0].set_xlabel("Z-score", fontsize=20)

    # ========================================================
    # MIDDLE PANEL (axs[1])
    # Ratio to Gaussian
    # ========================================================

    axs[1].plot(
        Z_points, p_fixed / p_gaus,
        ls="-", color="red", linewidth=2
    )
    axs[1].fill_between(
        Z_points,
        (p_fixed - err_fixed) / p_gaus,
        (p_fixed + err_fixed) / p_gaus,
        color="salmon", alpha=0.2
    )

    axs[1].plot(
        Z_points, p_envelope / p_gaus,
        ls="-", color="mediumblue", linewidth=2
    )
    axs[1].fill_between(
        Z_points,
        (p_envelope - err_envelope) / p_gaus,
        (p_envelope + err_envelope) / p_gaus,
        color="cornflowerblue", alpha=0.2
    )

    axs[1].plot(Z_points, p_gaus / p_gaus, ls="--", color="black", linewidth=2)

    axs[1].fill_between(Z_points, 0.8, 0.9, color="orange", alpha=0.2)
    axs[1].fill_between(Z_points, 0.9, 1.1, color="limegreen", alpha=0.2, label="$<10$%")
    axs[1].fill_between(Z_points, 1.1, 1.2, color="orange", alpha=0.2, label="$<20$%")
    axs[1].legend(loc="upper left", fontsize=12, frameon=True)

    axs[1].set_ylim(0.5, 1.5)
    axs[1].set_xlim(0, 2.5)
    axs[1].set_ylabel("Ratio to Gaussian", fontsize=16)
    axs[1].set_xticklabels(labels=[], fontsize=0)

    # ========================================================
    # TOP PANEL (axs[2])
    # Type-1 error rate - main legend, incl. which POI was tested/profiled
    # ========================================================

    axs[2].plot(
        Z_points, 100 * p_fixed,
        ls="-", color="red", linewidth=2,
        label="Toys (fixed)"
    )
    axs[2].fill_between(
        Z_points,
        100 * (p_fixed - err_fixed),
        100 * (p_fixed + err_fixed),
        color="salmon", alpha=0.2
    )

    axs[2].plot(
        Z_points, 100 * p_envelope,
        ls="-", color="mediumblue", linewidth=2,
        label="Toys (envelope)"
    )
    axs[2].fill_between(
        Z_points,
        100 * (p_envelope - err_envelope),
        100 * (p_envelope + err_envelope),
        color="cornflowerblue", alpha=0.2
    )

    axs[2].plot(
        Z_points, 100 * p_gaus,
        ls="--", color="black", linewidth=2, alpha=0.8,
        label="Gaussian"
    )

    axs[2].set_ylim(0.1, 100)
    axs[2].set_xlim(0, 2.5)
    axs[2].set_yscale("log")
    axs[2].set_ylabel("Type-1 error rate [%]", fontsize=20)

    poi_handles = [
        Line2D([0], [0], color="none", label=f"Test POI: {poi_test}"),
        Line2D([0], [0], color="none", label=f"Profile POI: {poi_profile}"),
    ]
    handles, labels = axs[2].get_legend_handles_labels()
    axs[2].legend(
        handles=handles + poi_handles,
        loc="best", fontsize=16, frameon=True
    )

    fig.suptitle(category, fontsize=18, y=0.97)

    # ========================================================
    # Save
    # ========================================================

    output_base = (
        f"summary_significance_{category}_"
        f"test_{poi_test}_profile_{poi_profile}"
    )

    pdf_file = os.path.join(PLOT_DIR, output_base + ".pdf")
    png_file = os.path.join(PLOT_DIR, output_base + ".png")

    fig.savefig(pdf_file, bbox_inches="tight")
    fig.savefig(png_file, bbox_inches="tight", dpi=150)

    plt.close(fig)

    print("Saved:", pdf_file)
    print("Saved:", png_file)


# ============================================================
# EXACTLY TWO PLOTS
# ============================================================

make_plot("r_ttH", "r_tHq")
make_plot("r_tHq", "r_ttH")


print("\n==============================================")
print("DONE")
print("==============================================")
