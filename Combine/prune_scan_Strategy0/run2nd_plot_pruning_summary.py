#!/usr/bin/env python3

import os
import csv
import math
import ROOT
import matplotlib.pyplot as plt


# ============================================================
# Configuration
# ============================================================

SUMMARY_DIR = "pruning_summary_output"
CSV_FILE = os.path.join(
    SUMMARY_DIR,
    "pruning_summary_global.csv"
)

PLOT_DIR = os.path.join(
    SUMMARY_DIR,
    "plots"
)

MODELS = ["DCB", "SoG"]


# ============================================================
# Read CSV
# ============================================================

def read_rows():

    rows = []

    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            rows.append(row)

    return rows


# ============================================================
# Likelihood scan best fit
# ============================================================

def get_scan_bestfit(tag, model, poi):

    filename = os.path.join(
        f"{tag}_{model}",
        f"higgsCombine_scan_syst_{poi}.MultiDimFit.mH125.08.root"
    )

    if not os.path.exists(filename):
        print(f"[warning] missing {filename}")
        return float("nan")

    f = ROOT.TFile.Open(filename)

    if not f or f.IsZombie():
        return float("nan")

    tree = f.Get("limit")

    if not tree:
        f.Close()
        return float("nan")

    best_nll = float("inf")
    best_value = float("nan")

    for entry in tree:

        nll = float(entry.deltaNLL)

        # Ignore failed scan points
        if not math.isfinite(nll):
            continue

        if nll >= 9000:
            continue

        value = float(getattr(entry, poi))

        if not math.isfinite(value):
            continue

        if nll < best_nll:
            best_nll = nll
            best_value = value

    f.Close()

    return best_value


# ============================================================
# Plot 1
# Sensitivity: significance + expected limit
# ============================================================

def plot_sensitivity(rows):

    fig, ax1 = plt.subplots(figsize=(9, 6))

    ax2 = ax1.twinx()

    for model in MODELS:

        rr = sorted(
            [r for r in rows if r["model"] == model],
            key=lambda r: float(r["threshold"])
        )

        x = [
            float(r["threshold"])
            for r in rr
        ]

        significance = [
            float(r["significance"])
            for r in rr
        ]

        limit = [
            float(r["expected_r_tHq_limit"])
            for r in rr
        ]

        linestyle = "-" if model == "DCB" else "--"

        ax1.plot(
            x,
            significance,
            marker="o",
            linestyle=linestyle,
            label=f"{model} significance"
        )

        ax2.plot(
            x,
            limit,
            marker="s",
            linestyle=linestyle,
            label=f"{model} expected r_tHq limit"
        )

    ax1.set_xlabel("Pruning threshold (%)")
    ax1.set_ylabel("Expected significance")
    ax2.set_ylabel("Expected 50% upper limit on $r_{tHq}$")

    ax1.set_title(
        "Sensitivity vs pruning threshold"
    )

    ax1.grid(True, alpha=0.3)

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()

    ax1.legend(
        h1 + h2,
        l1 + l2,
        fontsize=9,
        loc="best"
    )

    fig.tight_layout()

    outfile = os.path.join(
        PLOT_DIR,
        "01_sensitivity_vs_pruning.png"
    )

    fig.savefig(
        outfile,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"[plot] {outfile}")


# ============================================================
# Plot 2
# Snapshot best fit vs likelihood scan
# ============================================================

def plot_bestfit(rows):

    fig, ax = plt.subplots(figsize=(9, 6))

    for model in MODELS:

        rr = sorted(
            [r for r in rows if r["model"] == model],
            key=lambda r: float(r["threshold"])
        )

        x = [
            float(r["threshold"])
            for r in rr
        ]

        snapshot_ttH = [
            float(r["r_ttH"])
            for r in rr
        ]

        snapshot_tHq = [
            float(r["r_tHq"])
            for r in rr
        ]

        scan_ttH = []
        scan_tHq = []

        for r in rr:

            tag = r["threshold_tag"]

            scan_ttH.append(
                get_scan_bestfit(
                    tag,
                    model,
                    "r_ttH"
                )
            )

            scan_tHq.append(
                get_scan_bestfit(
                    tag,
                    model,
                    "r_tHq"
                )
            )

        linestyle = "-" if model == "DCB" else "--"

        ax.plot(
            x,
            snapshot_ttH,
            marker="o",
            linestyle=linestyle,
            label=f"{model} snapshot $r_{{ttH}}$"
        )

        ax.plot(
            x,
            scan_ttH,
            marker="x",
            linestyle=linestyle,
            label=f"{model} likelihood $r_{{ttH}}$"
        )

        ax.plot(
            x,
            snapshot_tHq,
            marker="s",
            linestyle=linestyle,
            label=f"{model} snapshot $r_{{tHq}}$"
        )

        ax.plot(
            x,
            scan_tHq,
            marker="+",
            linestyle=linestyle,
            label=f"{model} likelihood $r_{{tHq}}$"
        )

    ax.axhline(
        1.0,
        linestyle=":",
        linewidth=2,
        label="$r=1$"
    )

    ax.set_xlabel("Pruning threshold (%)")
    ax.set_ylabel("Best-fit signal strength")

    ax.set_title(
        "Snapshot best fit vs likelihood-scan minimum"
    )

    ax.grid(True, alpha=0.3)

    ax.legend(
        fontsize=8,
        ncol=2
    )

    fig.tight_layout()

    outfile = os.path.join(
        PLOT_DIR,
        "02_bestfit_snapshot_vs_likelihood.png"
    )

    fig.savefig(
        outfile,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"[plot] {outfile}")


# ============================================================
# Plot 3
# Statistical / systematic / total uncertainty
# ============================================================

def plot_uncertainties(rows):

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(13, 5.5)
    )

    for ax, poi in zip(
        axes,
        ["r_ttH", "r_tHq"]
    ):

        key = poi.replace("r_", "")

        for model in MODELS:

            rr = sorted(
                [r for r in rows if r["model"] == model],
                key=lambda r: float(r["threshold"])
            )

            x = [
                float(r["threshold"])
                for r in rr
            ]

            stat = [
                0.5 * (
                    float(r[f"stat_{key}_up"]) +
                    float(r[f"stat_{key}_down"])
                )
                for r in rr
            ]

            syst = [
                0.5 * (
                    float(r[f"syst_{key}_up"]) +
                    float(r[f"syst_{key}_down"])
                )
                for r in rr
            ]

            total = [
                0.5 * (
                    float(r[f"total_{key}_up"]) +
                    float(r[f"total_{key}_down"])
                )
                for r in rr
            ]

            linestyle = "-" if model == "DCB" else "--"

            ax.plot(
                x,
                stat,
                marker="o",
                linestyle=linestyle,
                label=f"{model} statistical"
            )

            ax.plot(
                x,
                syst,
                marker="^",
                linestyle=linestyle,
                label=f"{model} systematic"
            )

            ax.plot(
                x,
                total,
                marker="s",
                linestyle=linestyle,
                linewidth=2,
                label=f"{model} total"
            )

        ax.set_xlabel("Pruning threshold (%)")
        ax.set_ylabel(f"Uncertainty on {poi}")

        ax.set_title(poi)

        ax.grid(True, alpha=0.3)

        ax.legend(
            fontsize=8
        )

    fig.suptitle(
        "Statistical, systematic and total uncertainties"
    )

    fig.tight_layout()

    outfile = os.path.join(
        PLOT_DIR,
        "03_uncertainties_vs_pruning.png"
    )

    fig.savefig(
        outfile,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"[plot] {outfile}")


# ============================================================
# Main
# ============================================================

def main():

    os.makedirs(PLOT_DIR, exist_ok=True)

    rows = read_rows()

    print(f"[info] Read {len(rows)} rows from:")
    print(f"       {CSV_FILE}")

    plot_sensitivity(rows)

    plot_bestfit(rows)

    plot_uncertainties(rows)

    print()
    print("Done.")
    print()
    print("Created:")
    print(
        os.path.join(
            PLOT_DIR,
            "01_sensitivity_vs_pruning.png"
        )
    )
    print(
        os.path.join(
            PLOT_DIR,
            "02_bestfit_snapshot_vs_likelihood.png"
        )
    )
    print(
        os.path.join(
            PLOT_DIR,
            "03_uncertainties_vs_pruning.png"
        )
    )


if __name__ == "__main__":
    main()
