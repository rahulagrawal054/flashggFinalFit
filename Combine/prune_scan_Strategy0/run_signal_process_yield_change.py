#!/usr/bin/env python3

import ROOT
import numpy as np
import matplotlib.pyplot as plt
import os

# =========================================================
# Configuration
# =========================================================

BASE = "/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/prune_scan_Strategy0"

# 0p000 -> 0.0%, 0p001 -> 0.1%, ..., 0p010 -> 1.0%
tags = [f"0p{i:03d}" for i in range(11)]
thresholds = np.array([i * 0.1 for i in range(11)])

models = ["DCB", "SoG"]


# =========================================================
# Process mapping
# =========================================================

def proc_to_short(p):

    pl = p.lower()

    if "tth" in pl:
        return "ttH"
    elif "thq" in pl:
        return "tHq"
    elif "thw" in pl:
        return "tHW"

    return p


# =========================================================
# Extract signal yields
# =========================================================

def extract_yields(filename):

    f = ROOT.TFile.Open(filename)

    if not f or f.IsZombie():
        print(f"[ERROR] Cannot open: {filename}")
        return None

    ws = None

    for wsname in ["w", "w_all", "workspace"]:
        ws = f.Get(wsname)
        if ws:
            break

    if not ws:
        print(f"[ERROR] Workspace not found: {filename}")
        f.Close()
        return None

    yields = {
        "ttH": 0.0,
        "tHq": 0.0,
        "tHW": 0.0
    }

    funcs = ws.allFunctions().selectByName("n_exp_final*")

    it = funcs.iterator()
    func = it.Next()

    while func:

        name = func.GetName()

        if "bkg_mass" not in name:

            proc = name.split("_proc_")[-1]
            proc_short = proc_to_short(proc)

            if proc_short in yields:
                yields[proc_short] += func.getVal()

        func = it.Next()

    f.Close()

    yields["total"] = (
        yields["ttH"]
        + yields["tHq"]
        + yields["tHW"]
    )

    return yields


# =========================================================
# Read all ROOT files
# =========================================================

results = {
    "DCB": {},
    "SoG": {}
}

for tag, threshold in zip(tags, thresholds):

    for model in models:

        filename = (
            f"Datacard_fiducial_allCats_{tag}_{model}"
            f"_r_2D_fiducial.root"
        )

        filepath = os.path.join(BASE, filename)

        print(f"Reading {filename}")

        if not os.path.exists(filepath):
            print(f"[WARNING] Missing file: {filepath}")
            continue

        results[model][threshold] = extract_yields(filepath)


# =========================================================
# Print table
# =========================================================

print("\n" + "=" * 105)
print("SIGNAL YIELDS VS PRUNING THRESHOLD")
print("=" * 105)

print(
    f"{'Threshold':>10}"
    f"{'DCB total':>12}"
    f"{'SoG total':>12}"
    f"{'DCB ttH':>12}"
    f"{'SoG ttH':>12}"
    f"{'DCB tHq':>12}"
    f"{'SoG tHq':>12}"
    f"{'DCB tHW':>12}"
    f"{'SoG tHW':>12}"
)

print("-" * 105)

for threshold in thresholds:

    d = results["DCB"].get(threshold)
    s = results["SoG"].get(threshold)

    if d is None or s is None:
        continue

    print(
        f"{threshold:9.1f}%"
        f"{d['total']:12.3f}"
        f"{s['total']:12.3f}"
        f"{d['ttH']:12.3f}"
        f"{s['ttH']:12.3f}"
        f"{d['tHq']:12.3f}"
        f"{s['tHq']:12.3f}"
        f"{d['tHW']:12.3f}"
        f"{s['tHW']:12.3f}"
    )


# =========================================================
# Arrays
# =========================================================

def get_array(model, process):

    values = []

    for threshold in thresholds:

        result = results[model].get(threshold)

        if result is None:
            values.append(np.nan)
        else:
            values.append(result[process])

    return np.array(values)


dcb_total = get_array("DCB", "total")
sog_total = get_array("SoG", "total")

dcb_tth = get_array("DCB", "ttH")
sog_tth = get_array("SoG", "ttH")

dcb_thq = get_array("DCB", "tHq")
sog_thq = get_array("SoG", "tHq")

dcb_thw = get_array("DCB", "tHW")
sog_thw = get_array("SoG", "tHW")


# =========================================================
# Relative change with respect to 0%
# =========================================================

def relative_change(values):

    return 100.0 * (values - values[0]) / values[0]


dcb_total_rel = relative_change(dcb_total)
sog_total_rel = relative_change(sog_total)

dcb_tth_rel = relative_change(dcb_tth)
sog_tth_rel = relative_change(sog_tth)

dcb_thq_rel = relative_change(dcb_thq)
sog_thq_rel = relative_change(sog_thq)

dcb_thw_rel = relative_change(dcb_thw)
sog_thw_rel = relative_change(sog_thw)


# =========================================================
# Plot 1: Total yield
# =========================================================

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(
    thresholds, dcb_total,
    marker="o",
    linewidth=2,
    label="DCB"
)

ax.plot(
    thresholds, sog_total,
    marker="s",
    linewidth=2,
    label="SoG"
)

ax.set_xlabel("Pruning threshold (%)", fontsize=13)
ax.set_ylabel("Total signal yield", fontsize=13)

ax.set_xticks(thresholds)
ax.set_xticklabels([f"{x:.1f}%" for x in thresholds])

ax.grid(True, alpha=0.3)
ax.legend()

ax.set_title("Total Signal Yield vs Pruning Threshold")

plt.tight_layout()

plt.savefig(
    "total_signal_yield_vs_pruning.pdf"
)

plt.savefig(
    "total_signal_yield_vs_pruning.png",
    dpi=300
)

plt.show()


# =========================================================
# Plot 2: Relative total yield change
# =========================================================

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(
    thresholds, dcb_total_rel,
    marker="o",
    linewidth=2,
    label="DCB"
)

ax.plot(
    thresholds, sog_total_rel,
    marker="s",
    linewidth=2,
    label="SoG"
)

ax.axhline(
    0,
    linestyle="--",
    linewidth=1
)

ax.set_xlabel("Pruning threshold (%)", fontsize=13)

ax.set_ylabel(
    "Signal yield change relative to 0% (%)",
    fontsize=13
)

ax.set_xticks(thresholds)
ax.set_xticklabels([f"{x:.1f}%" for x in thresholds])

ax.grid(True, alpha=0.3)
ax.legend()

ax.set_title("Relative Signal Yield Change")

plt.tight_layout()

plt.savefig(
    "relative_signal_yield_change.pdf"
)

plt.savefig(
    "relative_signal_yield_change.png",
    dpi=300
)

plt.show()


# =========================================================
# Plot 3: Individual production modes
# =========================================================

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    thresholds, dcb_tth_rel,
    marker="o",
    linewidth=2,
    label="DCB $ttH$"
)

ax.plot(
    thresholds, dcb_thq_rel,
    marker="o",
    linewidth=2,
    label="DCB $tHq$"
)

ax.plot(
    thresholds, dcb_thw_rel,
    marker="o",
    linewidth=2,
    label="DCB $tHW$"
)

ax.plot(
    thresholds, sog_tth_rel,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="SoG $ttH$"
)

ax.plot(
    thresholds, sog_thq_rel,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="SoG $tHq$"
)

ax.plot(
    thresholds, sog_thw_rel,
    marker="s",
    linestyle="--",
    linewidth=2,
    label="SoG $tHW$"
)

ax.axhline(
    0,
    linestyle="--",
    linewidth=1
)

ax.set_xlabel("Pruning threshold (%)", fontsize=13)

ax.set_ylabel(
    "Yield change relative to 0% (%)",
    fontsize=13
)

ax.set_xticks(thresholds)
ax.set_xticklabels([f"{x:.1f}%" for x in thresholds])

ax.grid(True, alpha=0.3)
ax.legend(ncol=2, fontsize=9)

ax.set_title("Signal Yield Change by Production Mode")

plt.tight_layout()

plt.savefig(
    "signal_process_yield_change.pdf"
)

plt.savefig(
    "signal_process_yield_change.png",
    dpi=300
)

plt.show()
