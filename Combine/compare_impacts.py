#!/usr/bin/env python3

"""
Compare two Combine impacts JSON files: SoG vs DCB.

Usage:

    python3 compare_impacts.py SOG.json DCB.json

Optional output directory:

    python3 compare_impacts.py SOG.json DCB.json output_directory

The default output directory is created next to the SoG JSON:

    <directory_of_SoG_JSON>/NP_DCB_vs_SoG/

Output:
    01_summary.pdf/png
    02_all_NP_impacts.pdf/png
    03_top15_impacts.pdf/png
    04_rank_comparison.pdf/png
    05_largest_relative_differences.pdf/png
    06_DCB_over_SoG_ratio.pdf/png

    NP_DCB_vs_SoG_comparison.csv
    rank_comparison.csv
    summary.txt
    README.txt
"""

import sys
import json
import csv
import math
from pathlib import Path

import numpy as np

# IMPORTANT for LXPLUS / batch mode
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


# ============================================================
# Configuration
# ============================================================

SOG_LABEL = "SoG"
DCB_LABEL = "DCB"

# 16:9 PowerPoint slide size
FIGSIZE = (13.333, 7.5)

DPI = 180

SOG_COLOR = "tab:blue"
DCB_COLOR = "tab:red"


# ============================================================
# JSON helpers
# ============================================================

def load_json(path):

    with open(path, "r") as f:
        return json.load(f)


def get_params(data):

    return {
        p["name"]: p
        for p in data["params"]
    }


def get_impact(p):

    value = p.get("impact_r_ttH", 0.0)

    if value is None:
        return 0.0

    return abs(float(value))


def relative_difference(a, b):

    denominator = (abs(a) + abs(b)) / 2.0

    if denominator == 0:
        return 0.0

    return abs(a - b) / denominator * 100.0


def rank_dict(impact_dict):

    ordered = sorted(
        impact_dict.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return {
        name: i + 1
        for i, (name, _) in enumerate(ordered)
    }


def save_fig(fig, outdir, name):

    png = outdir / f"{name}.png"
    pdf = outdir / f"{name}.pdf"

    fig.savefig(
        png,
        dpi=DPI,
        bbox_inches="tight"
    )

    fig.savefig(
        pdf,
        bbox_inches="tight"
    )

    plt.close(fig)


def write_csv(path, rows, fieldnames):

    with open(path, "w", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)


# ============================================================
# Plot 1
# Summary slide
# ============================================================

def plot_summary(outdir, summary):

    fig = plt.figure(figsize=FIGSIZE)

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")

    fig.text(
        0.06,
        0.91,
        "Nuisance-parameter comparison: SoG vs DCB",
        fontsize=25,
        fontweight="bold"
    )

    fig.text(
        0.06,
        0.84,
        "The NP set is identical; the difference is in impact size and ordering.",
        fontsize=16
    )

    boxes = [

        (
            "Total NPs",
            f"{summary['n_total_sog']}",
            f"SoG / {summary['n_total_dcb']} DCB"
        ),

        (
            "Common NPs",
            f"{summary['n_common']}",
            "100%"
        ),

        (
            "SoG-only",
            f"{summary['n_sog_only']}",
            ""
        ),

        (
            "DCB-only",
            f"{summary['n_dcb_only']}",
            ""
        ),

        (
            "Within 10%",
            f"{summary['within10']}",
            f"{summary['within10_pct']:.1f}%"
        ),

        (
            "> 10% change",
            f"{summary['over10']}",
            f"{summary['over10_pct']:.1f}%"
        ),

        (
            "Within 20%",
            f"{summary['within20']}",
            f"{summary['within20_pct']:.1f}%"
        ),

        (
            "> 20% change",
            f"{summary['over20']}",
            f"{summary['over20_pct']:.1f}%"
        )
    ]

    x0 = 0.06
    y0 = 0.60

    w = 0.20
    h = 0.12

    dx = 0.225
    dy = 0.16

    for i, (title, value1, value2) in enumerate(boxes):

        row = i // 4
        col = i % 4

        x = x0 + col * dx
        y = y0 - row * dy

        rect = plt.Rectangle(
            (x, y),
            w,
            h,
            transform=fig.transFigure,
            fill=False,
            linewidth=1.5
        )

        fig.patches.append(rect)

        fig.text(
            x + 0.015,
            y + 0.075,
            title,
            fontsize=13
        )

        fig.text(
            x + 0.015,
            y + 0.030,
            value1,
            fontsize=24,
            fontweight="bold"
        )

        if value2:

            fig.text(
                x + 0.115,
                y + 0.035,
                value2,
                fontsize=11
            )

    fig.text(
        0.06,
        0.25,
        "Largest ordering change:",
        fontsize=15,
        fontweight="bold"
    )

    fig.text(
        0.06,
        0.20,
        "CMS_hgg_nuisance_Smearing",
        fontsize=19,
        fontweight="bold"
    )

    fig.text(
        0.06,
        0.15,
        (
            f"SoG rank #{summary['smearing_sog_rank']}  →  "
            f"DCB rank #{summary['smearing_dcb_rank']}    |    "
            f"{summary['smearing_sog']:.5f}  →  "
            f"{summary['smearing_dcb']:.5f}    |    "
            f"{summary['smearing_rel']:.1f}% relative difference"
        ),
        fontsize=14
    )

    fig.text(
        0.06,
        0.07,
        (
            "Within X% = symmetric relative difference between "
            "the two absolute NP impacts is ≤ X%."
        ),
        fontsize=11,
        color="0.55"
    )

    save_fig(
        fig,
        outdir,
        "01_summary"
    )


# ============================================================
# Plot 2
# All NP impacts
# ============================================================

def plot_all_impacts(
    outdir,
    common_names,
    sog_imp,
    dcb_imp
):

    order = sorted(
        common_names,
        key=lambda n: max(
            sog_imp[n],
            dcb_imp[n]
        ),
        reverse=True
    )

    x = np.arange(len(order))

    fig, ax = plt.subplots(
        figsize=FIGSIZE
    )

    for i, name in enumerate(order):

        ax.plot(
            [i, i],
            [
                sog_imp[name],
                dcb_imp[name]
            ],
            color="0.75",
            linewidth=0.8,
            zorder=1
        )

    ax.scatter(
        x,
        [sog_imp[n] for n in order],
        s=30,
        color=SOG_COLOR,
        label=SOG_LABEL,
        zorder=3
    )

    ax.scatter(
        x,
        [dcb_imp[n] for n in order],
        s=30,
        color=DCB_COLOR,
        label=DCB_LABEL,
        zorder=3
    )

    ax.set_yscale("log")

    ax.set_xlabel(
        "NPs, ordered by maximum impact",
        fontsize=13
    )

    ax.set_ylabel(
        r"|Impact on $r_{ttH}$|",
        fontsize=13
    )

    ax.set_title(
        "All nuisance-parameter impacts: SoG vs DCB",
        fontsize=18,
        fontweight="bold"
    )

    ax.legend(
        fontsize=12,
        loc="upper right"
    )

    ax.grid(
        True,
        which="both",
        axis="y",
        alpha=0.25
    )

    ax.set_xticks([])

    ax.text(
        0.01,
        0.02,
        f"N = {len(order)} common NPs",
        transform=ax.transAxes,
        fontsize=11
    )

    save_fig(
        fig,
        outdir,
        "02_all_NP_impacts"
    )


# ============================================================
# Plot 3
# Top 15
# ============================================================

def plot_top15(
    outdir,
    common_names,
    sog_imp,
    dcb_imp
):

    order = sorted(
        common_names,
        key=lambda n: max(
            sog_imp[n],
            dcb_imp[n]
        ),
        reverse=True
    )[:15]

    names = order[::-1]

    y = np.arange(len(names))

    h = 0.36

    fig, ax = plt.subplots(
        figsize=FIGSIZE
    )

    ax.barh(
        y + h / 2,
        [sog_imp[n] for n in names],
        height=h,
        color=SOG_COLOR,
        label=SOG_LABEL
    )

    ax.barh(
        y - h / 2,
        [dcb_imp[n] for n in names],
        height=h,
        color=DCB_COLOR,
        label=DCB_LABEL
    )

    ax.set_yticks(y)

    ax.set_yticklabels(
        names,
        fontsize=10
    )

    ax.set_xlabel(
        r"|Impact on $r_{ttH}$|",
        fontsize=13
    )

    ax.set_title(
        "Top 15 nuisance parameters by impact",
        fontsize=18,
        fontweight="bold"
    )

    ax.legend(
        fontsize=12,
        loc="lower right"
    )

    ax.grid(
        True,
        axis="x",
        alpha=0.25
    )

    for i, n in enumerate(names):

        maximum = max(
            sog_imp[n],
            dcb_imp[n]
        )

        ax.text(
            maximum * 1.01,
            i,
            (
                f"Δ = "
                f"{relative_difference(sog_imp[n], dcb_imp[n]):.1f}%"
            ),
            va="center",
            fontsize=8
        )

    save_fig(
        fig,
        outdir,
        "03_top15_impacts"
    )


# ============================================================
# Plot 4
# Rank comparison
# ============================================================

def plot_rank_comparison(
    outdir,
    common_names,
    sog_imp,
    dcb_imp
):

    sog_rank = rank_dict(sog_imp)
    dcb_rank = rank_dict(dcb_imp)

    fig, ax = plt.subplots(
        figsize=FIGSIZE
    )

    xs = [
        sog_rank[n]
        for n in common_names
    ]

    ys = [
        dcb_rank[n]
        for n in common_names
    ]

    ax.scatter(
        xs,
        ys,
        s=38,
        alpha=0.85
    )

    n = len(common_names)

    ax.plot(
        [1, n],
        [1, n],
        linestyle="--",
        color="0.55",
        linewidth=1.5
    )

    ax.set_xlabel(
        "SoG impact rank",
        fontsize=13
    )

    ax.set_ylabel(
        "DCB impact rank",
        fontsize=13
    )

    ax.set_title(
        "NP ranking: SoG vs DCB",
        fontsize=18,
        fontweight="bold"
    )

    ax.grid(
        True,
        alpha=0.25
    )

    ax.set_xlim(
        0.5,
        n + 0.5
    )

    ax.set_ylim(
        0.5,
        n + 0.5
    )

    rank_changes = sorted(
        common_names,
        key=lambda x:
        abs(
            sog_rank[x] -
            dcb_rank[x]
        ),
        reverse=True
    )[:8]

    for name in rank_changes:

        ax.annotate(
            name,
            (
                sog_rank[name],
                dcb_rank[name]
            ),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8
        )

    save_fig(
        fig,
        outdir,
        "04_rank_comparison"
    )


# ============================================================
# Plot 5
# Largest relative differences
# ============================================================

def plot_relative_differences(
    outdir,
    common_names,
    sog_imp,
    dcb_imp
):

    rows = []

    for name in common_names:

        rows.append(
            (
                name,
                sog_imp[name],
                dcb_imp[name],
                relative_difference(
                    sog_imp[name],
                    dcb_imp[name]
                )
            )
        )

    rows.sort(
        key=lambda x: x[3],
        reverse=True
    )

    rows = rows[:20]

    rows = rows[::-1]

    names = [
        r[0]
        for r in rows
    ]

    values = [
        r[3]
        for r in rows
    ]

    y = np.arange(len(names))

    fig, ax = plt.subplots(
        figsize=FIGSIZE
    )

    ax.barh(
        y,
        values,
        color="0.45"
    )

    ax.set_yticks(y)

    ax.set_yticklabels(
        names,
        fontsize=9
    )

    ax.set_xlabel(
        "Symmetric relative difference [%]",
        fontsize=13
    )

    ax.set_title(
        "Largest SoG–DCB differences in NP impact",
        fontsize=18,
        fontweight="bold"
    )

    ax.grid(
        True,
        axis="x",
        alpha=0.25
    )

    maximum = max(values) if values else 1.0

    for i, value in enumerate(values):

        ax.text(
            value + maximum * 0.01,
            i,
            f"{value:.1f}%",
            va="center",
            fontsize=9
        )

    save_fig(
        fig,
        outdir,
        "05_largest_relative_differences"
    )


# ============================================================
# Plot 6
# DCB / SoG ratio
# ============================================================

def plot_ratio(
    outdir,
    common_names,
    sog_imp,
    dcb_imp
):

    ratios = {}

    for name in common_names:

        if sog_imp[name] > 0:

            ratios[name] = (
                dcb_imp[name] /
                sog_imp[name]
            )

    ordered = sorted(
        ratios,
        key=lambda n:
        abs(math.log(ratios[n])),
        reverse=True
    )

    ordered = ordered[:20]

    ordered = ordered[::-1]

    names = ordered

    values = [
        ratios[n]
        for n in names
    ]

    y = np.arange(len(names))

    fig, ax = plt.subplots(
        figsize=FIGSIZE
    )

    # IMPORTANT:
    # linestyle must be specified explicitly.
    ax.axvline(
        1.0,
        linestyle="--",
        color="0.45",
        linewidth=1.5
    )

    ax.barh(
        y,
        values,
        color="0.45"
    )

    ax.set_yticks(y)

    ax.set_yticklabels(
        names,
        fontsize=9
    )

    ax.set_xlabel(
        "DCB / SoG impact",
        fontsize=13
    )

    ax.set_title(
        "Largest changes in NP impact: DCB / SoG",
        fontsize=18,
        fontweight="bold"
    )

    ax.grid(
        True,
        axis="x",
        alpha=0.25
    )

    for i, value in enumerate(values):

        if value >= 1:

            ax.text(
                value + 0.01,
                i,
                f"{value:.2f}",
                va="center",
                ha="left",
                fontsize=9
            )

        else:

            ax.text(
                value - 0.01,
                i,
                f"{value:.2f}",
                va="center",
                ha="right",
                fontsize=9
            )

    save_fig(
        fig,
        outdir,
        "06_DCB_over_SoG_ratio"
    )


# ============================================================
# Main
# ============================================================

def main():

    if len(sys.argv) < 3:

        print()
        print("Usage:")
        print()
        print(
            "python3 compare_impacts.py "
            "SOG.json DCB.json"
        )
        print()

        print(
            "Optional:"
        )

        print(
            "python3 compare_impacts.py "
            "SOG.json DCB.json output_directory"
        )

        sys.exit(1)

    sog_file = Path(
        sys.argv[1]
    ).resolve()

    dcb_file = Path(
        sys.argv[2]
    ).resolve()

    if not sog_file.exists():

        raise FileNotFoundError(
            f"SoG JSON not found:\n{sog_file}"
        )

    if not dcb_file.exists():

        raise FileNotFoundError(
            f"DCB JSON not found:\n{dcb_file}"
        )

    if len(sys.argv) >= 4:

        outdir = Path(
            sys.argv[3]
        ).resolve()

    else:

        outdir = (
            sog_file.parent /
            "NP_DCB_vs_SoG"
        )

    outdir.mkdir(
        parents=True,
        exist_ok=True
    )

    print("=" * 70)
    print("Combine impacts comparison: SoG vs DCB")
    print("=" * 70)

    print(
        f"SoG JSON : {sog_file}"
    )

    print(
        f"DCB JSON : {dcb_file}"
    )

    print(
        f"Output   : {outdir}"
    )

    print()

    # --------------------------------------------------------
    # Load JSON
    # --------------------------------------------------------

    sog_data = load_json(
        sog_file
    )

    dcb_data = load_json(
        dcb_file
    )

    sog = get_params(
        sog_data
    )

    dcb = get_params(
        dcb_data
    )

    # --------------------------------------------------------
    # NP sets
    # --------------------------------------------------------

    sog_names = set(sog)

    dcb_names = set(dcb)

    common = sorted(
        sog_names & dcb_names
    )

    sog_only = sorted(
        sog_names - dcb_names
    )

    dcb_only = sorted(
        dcb_names - sog_names
    )

    # --------------------------------------------------------
    # Impacts
    # --------------------------------------------------------

    sog_imp = {
        n: get_impact(sog[n])
        for n in common
    }

    dcb_imp = {
        n: get_impact(dcb[n])
        for n in common
    }

    rel = {
        n: relative_difference(
            sog_imp[n],
            dcb_imp[n]
        )
        for n in common
    }

    # --------------------------------------------------------
    # Counts
    # --------------------------------------------------------

    within10 = sum(
        value <= 10
        for value in rel.values()
    )

    over10 = sum(
        value > 10
        for value in rel.values()
    )

    within20 = sum(
        value <= 20
        for value in rel.values()
    )

    over20 = sum(
        value > 20
        for value in rel.values()
    )

    # --------------------------------------------------------
    # Ranks
    # --------------------------------------------------------

    sog_rank = rank_dict(
        sog_imp
    )

    dcb_rank = rank_dict(
        dcb_imp
    )

    # --------------------------------------------------------
    # Smearing
    # --------------------------------------------------------

    smearing = (
        "CMS_hgg_nuisance_Smearing"
    )

    smearing_sog = sog_imp.get(
        smearing,
        0.0
    )

    smearing_dcb = dcb_imp.get(
        smearing,
        0.0
    )

    summary = {

        "n_total_sog":
            len(sog_names),

        "n_total_dcb":
            len(dcb_names),

        "n_common":
            len(common),

        "n_sog_only":
            len(sog_only),

        "n_dcb_only":
            len(dcb_only),

        "within10":
            within10,

        "within10_pct":
            100 * within10 / len(common)
            if common else 0,

        "over10":
            over10,

        "over10_pct":
            100 * over10 / len(common)
            if common else 0,

        "within20":
            within20,

        "within20_pct":
            100 * within20 / len(common)
            if common else 0,

        "over20":
            over20,

        "over20_pct":
            100 * over20 / len(common)
            if common else 0,

        "smearing_sog":
            smearing_sog,

        "smearing_dcb":
            smearing_dcb,

        "smearing_rel":
            relative_difference(
                smearing_sog,
                smearing_dcb
            ),

        "smearing_sog_rank":
            sog_rank.get(
                smearing,
                -1
            ),

        "smearing_dcb_rank":
            dcb_rank.get(
                smearing,
                -1
            )
    }

    # --------------------------------------------------------
    # Full comparison CSV
    # --------------------------------------------------------

    rows = []

    ordered_names = sorted(
        common,
        key=lambda x:
        max(
            sog_imp[x],
            dcb_imp[x]
        ),
        reverse=True
    )

    for name in ordered_names:

        rows.append({

            "NP":
                name,

            "SoG_impact":
                sog_imp[name],

            "DCB_impact":
                dcb_imp[name],

            "DCB_over_SoG":
                (
                    dcb_imp[name] /
                    sog_imp[name]
                    if sog_imp[name] != 0
                    else ""
                ),

            "relative_difference_percent":
                rel[name],

            "SoG_rank":
                sog_rank[name],

            "DCB_rank":
                dcb_rank[name],

            "rank_change_DCB_minus_SoG":
                dcb_rank[name] -
                sog_rank[name],

            "SoG_type":
                sog[name].get(
                    "type",
                    ""
                ),

            "DCB_type":
                dcb[name].get(
                    "type",
                    ""
                )
        })

    write_csv(

        outdir /
        "NP_DCB_vs_SoG_comparison.csv",

        rows,

        [
            "NP",
            "SoG_impact",
            "DCB_impact",
            "DCB_over_SoG",
            "relative_difference_percent",
            "SoG_rank",
            "DCB_rank",
            "rank_change_DCB_minus_SoG",
            "SoG_type",
            "DCB_type"
        ]
    )

    # --------------------------------------------------------
    # Rank CSV
    # --------------------------------------------------------

    rank_rows = []

    for name in sorted(
        common,
        key=lambda x:
        sog_rank[x]
    ):

        rank_rows.append({

            "NP":
                name,

            "SoG_rank":
                sog_rank[name],

            "DCB_rank":
                dcb_rank[name],

            "rank_change_DCB_minus_SoG":
                dcb_rank[name] -
                sog_rank[name],

            "SoG_impact":
                sog_imp[name],

            "DCB_impact":
                dcb_imp[name],

            "relative_difference_percent":
                rel[name]
        })

    write_csv(

        outdir /
        "rank_comparison.csv",

        rank_rows,

        [
            "NP",
            "SoG_rank",
            "DCB_rank",
            "rank_change_DCB_minus_SoG",
            "SoG_impact",
            "DCB_impact",
            "relative_difference_percent"
        ]
    )

    # --------------------------------------------------------
    # Summary text
    # --------------------------------------------------------

    with open(
        outdir / "summary.txt",
        "w"
    ) as f:

        f.write(
            "Combine impacts comparison: SoG vs DCB\n"
        )

        f.write(
            "=" * 60 + "\n\n"
        )

        f.write(
            f"SoG JSON: {sog_file}\n"
        )

        f.write(
            f"DCB JSON: {dcb_file}\n\n"
        )

        f.write(
            "NP content\n"
        )

        f.write(
            "-" * 60 + "\n"
        )

        f.write(
            f"Total SoG NPs : {len(sog_names)}\n"
        )

        f.write(
            f"Total DCB NPs : {len(dcb_names)}\n"
        )

        f.write(
            f"Common NPs   : {len(common)}\n"
        )

        f.write(
            f"SoG-only NPs : {len(sog_only)}\n"
        )

        f.write(
            f"DCB-only NPs : {len(dcb_only)}\n\n"
        )

        f.write(
            "Impact comparison\n"
        )

        f.write(
            "-" * 60 + "\n"
        )

        f.write(
            f"Within 10% : "
            f"{within10}/{len(common)} "
            f"({summary['within10_pct']:.1f}%)\n"
        )

        f.write(
            f"> 10%      : "
            f"{over10}/{len(common)} "
            f"({summary['over10_pct']:.1f}%)\n"
        )

        f.write(
            f"Within 20% : "
            f"{within20}/{len(common)} "
            f"({summary['within20_pct']:.1f}%)\n"
        )

        f.write(
            f"> 20%      : "
            f"{over20}/{len(common)} "
            f"({summary['over20_pct']:.1f}%)\n\n"
        )

        f.write(
            "Top 15 by maximum impact\n"
        )

        f.write(
            "-" * 60 + "\n"
        )

        top15 = sorted(
            common,
            key=lambda x:
            max(
                sog_imp[x],
                dcb_imp[x]
            ),
            reverse=True
        )[:15]

        for i, name in enumerate(
            top15,
            1
        ):

            f.write(

                f"{i:2d}. "
                f"{name:45s} "
                f"SoG={sog_imp[name]:.8f}  "
                f"DCB={dcb_imp[name]:.8f}  "
                f"relDiff={rel[name]:6.2f}%  "
                f"rank={sog_rank[name]}->"
                f"{dcb_rank[name]}\n"
            )

        f.write(
            "\nLargest rank changes\n"
        )

        f.write(
            "-" * 60 + "\n"
        )

        rank_change_order = sorted(

            common,

            key=lambda x:
            abs(
                dcb_rank[x] -
                sog_rank[x]
            ),

            reverse=True
        )[:15]

        for i, name in enumerate(
            rank_change_order,
            1
        ):

            f.write(

                f"{i:2d}. "
                f"{name:45s} "
                f"rank "
                f"{sog_rank[name]} -> "
                f"{dcb_rank[name]}  "
                f"Δrank="
                f"{dcb_rank[name] - sog_rank[name]:+d}\n"
            )

    # --------------------------------------------------------
    # Generate plots
    # --------------------------------------------------------

    plot_summary(
        outdir,
        summary
    )

    plot_all_impacts(
        outdir,
        common,
        sog_imp,
        dcb_imp
    )

    plot_top15(
        outdir,
        common,
        sog_imp,
        dcb_imp
    )

    plot_rank_comparison(
        outdir,
        common,
        sog_imp,
        dcb_imp
    )

    plot_relative_differences(
        outdir,
        common,
        sog_imp,
        dcb_imp
    )

    plot_ratio(
        outdir,
        common,
        sog_imp,
        dcb_imp
    )

    # --------------------------------------------------------
    # README
    # --------------------------------------------------------

    with open(
        outdir / "README.txt",
        "w"
    ) as f:

        f.write(
            "NP DCB vs SoG comparison output\n"
            "================================\n\n"
        )

        f.write(
            "All plots are 16:9 slide-friendly format.\n"
            "Each plot is saved as both PNG and PDF.\n\n"
        )

        f.write(
            "01_summary.pdf/png\n"
            "    Main presentation summary.\n\n"
        )

        f.write(
            "02_all_NP_impacts.pdf/png\n"
            "    All common NPs.\n\n"
        )

        f.write(
            "03_top15_impacts.pdf/png\n"
            "    Top 15 NP impacts, SoG vs DCB.\n\n"
        )

        f.write(
            "04_rank_comparison.pdf/png\n"
            "    SoG rank vs DCB rank.\n\n"
        )

        f.write(
            "05_largest_relative_differences.pdf/png\n"
            "    Largest relative impact differences.\n\n"
        )

        f.write(
            "06_DCB_over_SoG_ratio.pdf/png\n"
            "    DCB / SoG impact ratio.\n\n"
        )

        f.write(
            "NP_DCB_vs_SoG_comparison.csv\n"
            "    Complete numerical comparison.\n\n"
        )

        f.write(
            "rank_comparison.csv\n"
            "    NP ranking comparison.\n\n"
        )

        f.write(
            "summary.txt\n"
            "    Numerical summary.\n"
        )

    # --------------------------------------------------------
    # Print result
    # --------------------------------------------------------

    print()
    print("RESULT")
    print("-" * 70)

    print(
        f"Total NPs:       "
        f"SoG = {len(sog_names)}, "
        f"DCB = {len(dcb_names)}"
    )

    print(
        f"Common NPs:      {len(common)}"
    )

    print(
        f"SoG-only:        {len(sog_only)}"
    )

    print(
        f"DCB-only:        {len(dcb_only)}"
    )

    print()

    print(
        f"Within 10%:      "
        f"{within10}/{len(common)} "
        f"({summary['within10_pct']:.1f}%)"
    )

    print(
        f"> 10%:           "
        f"{over10}/{len(common)} "
        f"({summary['over10_pct']:.1f}%)"
    )

    print(
        f"Within 20%:      "
        f"{within20}/{len(common)} "
        f"({summary['within20_pct']:.1f}%)"
    )

    print(
        f"> 20%:           "
        f"{over20}/{len(common)} "
        f"({summary['over20_pct']:.1f}%)"
    )

    print()

    print(
        "Most important ranking change:"
    )

    print(

        f"  {smearing}: "
        f"rank "
        f"{sog_rank.get(smearing, -1)} -> "
        f"{dcb_rank.get(smearing, -1)}, "

        f"{smearing_sog:.6f} -> "
        f"{smearing_dcb:.6f}, "
        f"{summary['smearing_rel']:.1f}% relative difference"
    )

    print()

    print(
        f"All output written to:\n"
        f"{outdir}"
    )

    print("=" * 70)


if __name__ == "__main__":
    main()
