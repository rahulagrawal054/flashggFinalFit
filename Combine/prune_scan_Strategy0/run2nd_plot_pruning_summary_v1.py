#!/usr/bin/env python3

import os
import csv
import math
import glob
import ROOT
import matplotlib.pyplot as plt

# ============================================================
# Configuration
# ============================================================

SUMMARY_DIR = "pruning_summary_output"
CSV_FILE = os.path.join(SUMMARY_DIR, "pruning_summary_global.csv")
PLOT_DIR = os.path.join(SUMMARY_DIR, "plots")

MODELS = ["DCB", "SoG"]

# Distinct light colors for model 1sigma bands
MODEL_COLORS = {
    "DCB": {"line": "#1f77b4", "band": "#1f77b4", "marker": "o"}, # Blue line, light blue band
    "SoG": {"line": "#ff7f0e", "band": "#ff7f0e", "marker": "s"}  # Orange line, light orange band
}


# ============================================================
# Extract 1-Sigma Quantiles Directly from Combine ROOT Files
# ============================================================

def get_limit_quantiles(tag, model, poi="r_tHq"):
    """Reads 1-sigma quantiles (16% and 84%) and median (50%) from Combine limit ROOT files."""
    folder = f"{tag}_{model}"
    if not os.path.exists(folder):
        return {}

    search_patterns = [
        os.path.join(folder, f"*limit*{poi}*.root"),
        os.path.join(folder, "*AsymptoticLimits*.root"),
        os.path.join(folder, "higgsCombine*.root")
    ]
    
    root_files = []
    for pattern in search_patterns:
        root_files.extend(glob.glob(pattern))
    root_files = list(set(root_files))

    for rfile in root_files:
        f = ROOT.TFile.Open(rfile)
        if not f or f.IsZombie():
            continue

        tree = f.Get("limit")
        if not tree or tree.GetEntries() < 3:
            f.Close()
            continue

        limits = {}
        for entry in tree:
            q = round(float(entry.quantileExpected), 3)
            val = float(entry.limit)
            if q == 0.160:
                limits["m1s"] = val
            elif q == 0.500:
                limits["median"] = val
            elif q == 0.840:
                limits["p1s"] = val

        f.Close()
        if "median" in limits and "m1s" in limits and "p1s" in limits:
            return limits

    return {}


def read_rows():
    rows = []
    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# ============================================================
# Plot 1: Significance Comparison (DCB vs SoG with 1-Sigma Band)
# ============================================================

def plot_significance_comparison(rows):
    fig, ax = plt.subplots(figsize=(9.5, 6))

    for model in MODELS:
        rr = sorted(
            [r for r in rows if r["model"] == model],
            key=lambda r: float(r["threshold"])
        )

        x = []
        significance = []
        sig_m1s = []
        sig_p1s = []

        for r in rr:
            thresh = float(r["threshold"])
            sig = float(r["significance"])

            # Determine 1-sigma significance band from CSV total uncertainty on POI
            key = "tHq"
            tot_up = float(r.get(f"total_{key}_up", 0.0))
            tot_down = float(r.get(f"total_{key}_down", 0.0))
            rel_err = 0.5 * (tot_up + tot_down) if (tot_up > 0 or tot_down > 0) else 0.10

            x.append(thresh)
            significance.append(sig)
            sig_m1s.append(max(0.0, sig * (1.0 - rel_err)))
            sig_p1s.append(sig * (1.0 + rel_err))

        color_cfg = MODEL_COLORS[model]

        # 1. Very light 1-sigma shaded band (NO 2-sigma band)
        ax.fill_between(
            x, sig_m1s, sig_p1s,
            color=color_cfg["band"], alpha=0.18,
            label=f"{model} Expected $\\pm 1\\sigma$"
        )

        # 2. Median significance line
        ax.plot(
            x, significance,
            marker=color_cfg["marker"], color=color_cfg["line"],
            linestyle="-", linewidth=2.2, markersize=7,
            label=f"{model} Significance"
        )

    ax.set_xlabel("Pruning threshold (%)", fontsize=11, fontweight="bold")
    ax.set_ylabel(r"Expected Significance ($Z$)", fontsize=11, fontweight="bold")
    ax.set_title("Expected Significance Comparison: DCB vs SoG", fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.legend(fontsize=9.5, loc="best", framealpha=0.9)

    fig.tight_layout()

    outfile = os.path.join(PLOT_DIR, "01a_significance_comparison.png")
    fig.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved Significance Comparison to: {outfile}")


# ============================================================
# Plot 2: 95% CL Limits Comparison (DCB vs SoG with 1-Sigma Band)
# ============================================================

def plot_limits_comparison(rows):
    fig, ax = plt.subplots(figsize=(9.5, 6))

    for model in MODELS:
        rr = sorted(
            [r for r in rows if r["model"] == model],
            key=lambda r: float(r["threshold"])
        )

        x = []
        median_list, m1s_list, p1s_list = [], [], []

        for r in rr:
            thresh = float(r["threshold"])
            tag = r["threshold_tag"]

            q_dict = get_limit_quantiles(tag, model, poi="r_tHq")
            med_val = q_dict.get("median", float(r.get("expected_r_tHq_limit", "nan")))

            if math.isnan(med_val):
                continue

            x.append(thresh)
            median_list.append(med_val)
            m1s_list.append(q_dict.get("m1s", float("nan")))
            p1s_list.append(q_dict.get("p1s", float("nan")))

        color_cfg = MODEL_COLORS[model]

        # 1. Very light 1-sigma shaded band (NO 2-sigma yellow band)
        if not math.isnan(m1s_list[0]) and not math.isnan(p1s_list[0]):
            ax.fill_between(
                x, m1s_list, p1s_list,
                color=color_cfg["band"], alpha=0.20,
                label=f"{model} Expected $\\pm 1\\sigma$"
            )

        # 2. Median limit line
        ax.plot(
            x, median_list,
            marker=color_cfg["marker"], color=color_cfg["line"],
            linestyle="-", linewidth=2.2, markersize=7,
            label=f"{model} Median $r_{{tHq}}$ Limit"
        )

    ax.set_xlabel("Pruning threshold (%)", fontsize=11, fontweight="bold")
    ax.set_ylabel(r"Expected 95% CL Upper Limit on $r_{tHq}$", fontsize=11, fontweight="bold")
    ax.set_title("Expected Upper Limit Comparison ($r_{tHq}$): DCB vs SoG", fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.legend(fontsize=9.5, loc="best", framealpha=0.9)

    fig.tight_layout()

    outfile = os.path.join(PLOT_DIR, "01b_limits_comparison.png")
    fig.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved Limits Comparison to: {outfile}")


def main():
    os.makedirs(PLOT_DIR, exist_ok=True)
    rows = read_rows()
    print(f"[info] Read {len(rows)} rows from {CSV_FILE}")
    
    plot_significance_comparison(rows)
    plot_limits_comparison(rows)


if __name__ == "__main__":
    main()
