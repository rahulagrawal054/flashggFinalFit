#!/usr/bin/env python3

"""
Automated pruning-scan summary for flashggFinalFit.

Scans:
    0p000 ... 0p010
    DCB / SoG

Extracts:
    * Combine Asimov significance
    * Expected 50% r_tHq limit
    * Best-fit r_ttH and r_tHq
    * Statistical uncertainties from scan_stat
    * Total/stat+syst uncertainties from scan_syst
    * Derived systematic uncertainties
    * All signal yields:
        ttH, tHq, tHW, ggH, VBF, WH, ZH, bbH
    * 16-category information
    * Background density at mH = 125.08 GeV
    * Signal losses relative to 0% pruning

Outputs:
    pruning_summary_global.csv
    pruning_summary_category.csv
    plots/*.png

Important:
    The Combine likelihood significance is the primary sensitivity metric.

    The requested counting-experiment Asimov formula is

        Z_A = sqrt(2 * ((S+B)*ln(1+S/B) - S))

    but it is NOT evaluated here from the workspace totals because the
    current background extraction is a density [events/GeV] at 125.08 GeV,
    while the signal normalization is an integrated yield. A mass window
    would have to be specified to make S and B dimensionally consistent.

    The systematic uncertainty is derived as:

        syst_up   = sqrt(total_up^2   - stat_up^2)
        syst_down = sqrt(total_down^2 - stat_down^2)

    where scan_syst = full systematics and scan_stat = all constrained
    nuisances frozen.
"""

import os
import re
import math
import csv
import argparse
from array import array

import ROOT

# Use non-interactive ROOT
ROOT.gROOT.SetBatch(True)


# ============================================================
# Configuration
# ============================================================

MASS = "125.08"

THRESHOLDS = [
    f"0p{i:03d}" for i in range(11)
]

MODELS = ["DCB", "SoG"]

SIGNAL_PROCS = [
    "ttH",
    "tHq",
    "tHW",
    "ggH",
    "VBF",
    "WH",
    "ZH",
    "bbH",
]

CATEGORIES = [
    "ttH_had_1",
    "ttH_had_2",
    "ttH_had_3",
    "ttH_had_4",
    "ttH_lep_1",
    "ttH_lep_2",
    "ttH_lep_3",
    "ttH_lep_4",
    "tH_had_1",
    "tH_had_2",
    "tH_had_3",
    "tH_had_4",
    "tH_lep_1",
    "tH_lep_2",
    "bkg_had",
    "bkg_lep",
]

SIGNAL_CATEGORIES = [
    c for c in CATEGORIES
    if not c.startswith("bkg_")
]


# ============================================================
# Helpers
# ============================================================

def threshold_percent(tag):
    """
    Convert 0p003 -> 0.3
    """
    return int(tag[2:]) / 10.0


def proc_to_short(proc):
    """
    Same mapping as user's extract_yields_ws.py.
    """
    pl = proc.lower()

    if "tth" in pl:
        return "ttH"
    elif "thq" in pl:
        return "tHq"
    elif "thw" in pl:
        return "tHW"
    elif "ggh" in pl or "glugluh" in pl:
        return "ggH"
    elif "qqh" in pl or "vbf" in pl:
        return "VBF"
    elif "wh" in pl:
        return "WH"
    elif "zh" in pl:
        return "ZH"
    elif "bbh" in pl:
        return "bbH"

    return proc


def rooiter(x):
    it = x.iterator()
    r = it.Next()

    while r:
        yield r
        r = it.Next()


def safe_float(x):
    try:
        return float(x)
    except Exception:
        return float("nan")


def derive_syst(total, stat):
    """
    Quadrature subtraction.

    Returns nan if subtraction is not physically meaningful.
    """
    if not math.isfinite(total) or not math.isfinite(stat):
        return float("nan")

    diff = total * total - stat * stat

    if diff < -1e-8:
        return float("nan")

    return math.sqrt(max(diff, 0.0))


def linear_interp(x1, y1, x2, y2, target):
    """
    Linear interpolation for y=target.
    """
    if y2 == y1:
        return 0.5 * (x1 + x2)

    return x1 + (target - y1) * (x2 - x1) / (y2 - y1)


# ============================================================
# ROOT likelihood scan
# ============================================================

def read_scan_points(filename, poi):
    """
    Read a Combine MultiDimFit scan.

    Returns a sorted list:
        [(poi_value, deltaNLL), ...]

    Failed points with deltaNLL >= 9000 are discarded.
    """
    if not os.path.exists(filename):
        print(f"    [WARNING] missing scan: {filename}")
        return []

    f = ROOT.TFile.Open(filename)

    if not f or f.IsZombie():
        print(f"    [WARNING] cannot open: {filename}")
        return []

    tree = f.Get("limit")

    if not tree:
        print(f"    [WARNING] no 'limit' tree in: {filename}")
        f.Close()
        return []

    if not tree.GetBranch(poi):
        print(f"    [WARNING] branch {poi} missing in {filename}")
        f.Close()
        return []

    if not tree.GetBranch("deltaNLL"):
        print(f"    [WARNING] deltaNLL missing in {filename}")
        f.Close()
        return []

    points = []

    for entry in tree:
        x = float(getattr(entry, poi))
        dnll = float(entry.deltaNLL)

        if not math.isfinite(x):
            continue

        if not math.isfinite(dnll):
            continue

        # Combine uses large values for failed points.
        if dnll >= 9000:
            continue

        points.append((x, dnll))

    f.Close()

    points.sort(key=lambda p: p[0])

    return points


def scan_uncertainty(filename, poi):
    """
    Extract best fit and approximate 68% CL asymmetric uncertainty
    from deltaNLL = 0.5.

    Combine's deltaNLL is half of the usual -2 Delta log L.
    Thus 1 sigma corresponds approximately to deltaNLL = 0.5.
    """

    points = read_scan_points(filename, poi)

    if len(points) < 3:
        return {
            "best": float("nan"),
            "up": float("nan"),
            "down": float("nan"),
        }

    # Find minimum
    best_x, best_dnll = min(points, key=lambda p: p[1])

    target = 0.5

    left_cross = None
    right_cross = None

    # Search for crossing on left side
    left_points = [p for p in points if p[0] < best_x]
    left_points.sort(key=lambda p: p[0], reverse=True)

    for p1, p2 in zip(left_points[:-1], left_points[1:]):
        x1, y1 = p1
        x2, y2 = p2

        if (y1 - target) * (y2 - target) <= 0:
            left_cross = linear_interp(
                x1, y1, x2, y2, target
            )
            break

    # Search for crossing on right side
    right_points = [p for p in points if p[0] > best_x]
    right_points.sort(key=lambda p: p[0])

    for p1, p2 in zip(right_points[:-1], right_points[1:]):
        x1, y1 = p1
        x2, y2 = p2

        if (y1 - target) * (y2 - target) <= 0:
            right_cross = linear_interp(
                x1, y1, x2, y2, target
            )
            break

    if left_cross is None:
        down = float("nan")
    else:
        down = best_x - left_cross

    if right_cross is None:
        up = float("nan")
    else:
        up = right_cross - best_x

    return {
        "best": best_x,
        "up": up,
        "down": down,
    }


# ============================================================
# Snapshot best fit
# ============================================================

def read_snapshot(filename):
    """
    Read r_ttH and r_tHq from log_snapshot_Asimov.log.
    """

    result = {
        "r_ttH": float("nan"),
        "r_tHq": float("nan"),
    }

    if not os.path.exists(filename):
        print(f"    [WARNING] missing snapshot log: {filename}")
        return result

    with open(filename, "r", errors="ignore") as f:
        text = f.read()

    # Example:
    # r_tHq :    +1.000
    # r_ttH :    +1.033

    for poi in ["r_ttH", "r_tHq"]:
        pattern = rf"\b{re.escape(poi)}\s*:\s*([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)"
        match = re.search(pattern, text)

        if match:
            result[poi] = float(match.group(1))

    return result


# ============================================================
# Significance
# ============================================================

def read_significance(filename):
    """
    Extract significance from Combine log.
    """

    if not os.path.exists(filename):
        print(f"    [WARNING] missing significance log: {filename}")
        return float("nan")

    with open(filename, "r", errors="ignore") as f:
        text = f.read()

    patterns = [
        r"Significance\s*:\s*([+-]?\d+(?:\.\d+)?)",
        r"significance\s*=\s*([+-]?\d+(?:\.\d+)?)",
        r"Z\s*=\s*([+-]?\d+(?:\.\d+)?)",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)

        if matches:
            try:
                return float(matches[-1])
            except Exception:
                pass

    print(f"    [WARNING] significance not found in {filename}")
    return float("nan")


# ============================================================
# Expected limit
# ============================================================

def read_expected_limit(filename):
    """
    Extract expected 50% r_tHq limit.

    Handles typical Combine text forms.
    """

    if not os.path.exists(filename):
        print(f"    [WARNING] missing limit log: {filename}")
        return float("nan")

    with open(filename, "r", errors="ignore") as f:
        text = f.read()

    patterns = [
        r"Expected\s+50\.0%.*?<\s*([+-]?\d+(?:\.\d+)?)",
        r"Expected\s+50\.0%\s*:\s*r_tHq\s*<\s*([+-]?\d+(?:\.\d+)?)",
        r"50\.0%\s*:\s*([+-]?\d+(?:\.\d+)?)",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)

        if matches:
            try:
                return float(matches[-1])
            except Exception:
                pass

    # Fallback: search lines containing Expected and median
    for line in text.splitlines():
        if "Expected" in line and "50" in line:
            nums = re.findall(
                r"([+-]?\d+(?:\.\d+)?)",
                line
            )

            if nums:
                try:
                    return float(nums[-1])
                except Exception:
                    pass

    print(f"    [WARNING] expected limit not found in {filename}")
    return float("nan")


# ============================================================
# Workspace yields
# ============================================================

def extract_workspace_yields(filename):
    """
    Extract all signal process yields by category.

    Returns:
        category_yields[cat][proc_short] = yield

    and:
        background_density[cat] = events / GeV at 125.08 GeV
    """

    category_yields = {
        cat: {proc: 0.0 for proc in SIGNAL_PROCS}
        for cat in CATEGORIES
    }

    background_density = {
        cat: float("nan")
        for cat in CATEGORIES
    }

    if not os.path.exists(filename):
        print(f"    [WARNING] missing workspace: {filename}")
        return category_yields, background_density

    f = ROOT.TFile.Open(filename)

    if not f or f.IsZombie():
        print(f"    [WARNING] cannot open workspace: {filename}")
        return category_yields, background_density

    ws = None

    for wsname in ["w", "w_all", "workspace"]:
        obj = f.Get(wsname)

        if obj:
            ws = obj
            break

    if not ws:
        print(f"    [WARNING] workspace not found: {filename}")
        f.Close()
        return category_yields, background_density

    # --------------------------------------------------------
    # Signal normalisations
    # --------------------------------------------------------

    allNorms = ws.allFunctions().selectByName("n_exp_final*")

    for func in rooiter(allNorms):

        name = func.GetName()

        if "bkg_mass" in name:
            continue

        try:
            cat = name.split("_proc_")[0].split("bin")[-1]
            proc = name.split("_proc_")[-1]

            proc_short = proc_to_short(proc)

            if cat not in category_yields:
                continue

            if proc_short not in SIGNAL_PROCS:
                continue

            yld = float(func.getVal())

            if math.isfinite(yld):
                category_yields[cat][proc_short] += yld

        except Exception:
            continue

    # --------------------------------------------------------
    # Background density at 125.08 GeV
    # --------------------------------------------------------

    mgg = ws.var("CMS_hgg_mass")

    if mgg is None:
        mgg = ws.var("mass")

    if mgg:

        mgg.setVal(float(MASS))
        mgg_argset = ROOT.RooArgSet(mgg)

        for cat in CATEGORIES:

            norm_name = f"n_exp_final_bin{cat}_proc_bkg_mass"
            pdf_name = f"shapeBkg_bkg_mass_{cat}"

            bkg_norm = ws.function(norm_name)
            bkg_pdf = ws.pdf(pdf_name)

            if bkg_norm and bkg_pdf:

                try:
                    N = float(bkg_norm.getVal())
                    fpdf = float(bkg_pdf.getVal(mgg_argset))

                    background_density[cat] = N * fpdf

                except Exception:
                    pass

            elif bkg_pdf:

                try:
                    background_density[cat] = float(
                        bkg_pdf.getVal(mgg_argset)
                    )
                except Exception:
                    pass

    f.Close()

    return category_yields, background_density


# ============================================================
# Requested Asimov formula
# ============================================================

def asimov_Z(S, B):
    """
    Requested counting-experiment Asimov significance:

        Z_A = sqrt(2*((S+B)*ln(1+S/B)-S))

    This function is available for use once S and B refer to
    yields in the SAME mass interval.
    """

    if not math.isfinite(S) or not math.isfinite(B):
        return float("nan")

    if S <= 0 or B <= 0:
        return float("nan")

    value = 2.0 * (
        (S + B) * math.log(1.0 + S / B) - S
    )

    if value < 0:
        return float("nan")

    return math.sqrt(value)


# ============================================================
# Main
# ============================================================

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--base",
        default=".",
        help="Base pruning directory"
    )

    parser.add_argument(
        "--outdir",
        default="pruning_summary_output",
        help="Output directory"
    )

    args = parser.parse_args()

    base = os.path.abspath(args.base)
    outdir = os.path.abspath(args.outdir)

    os.makedirs(outdir, exist_ok=True)

    plotdir = os.path.join(outdir, "plots")
    os.makedirs(plotdir, exist_ok=True)

    print("=" * 80)
    print(" Pruning scan summary")
    print("=" * 80)
    print(f"Base directory : {base}")
    print(f"Output         : {outdir}")
    print("=" * 80)

    global_rows = []
    category_rows = []

    # --------------------------------------------------------
    # Loop over 22 configurations
    # --------------------------------------------------------

    for threshold in THRESHOLDS:

        for model in MODELS:

            tag = f"{threshold}_{model}"
            workdir = os.path.join(base, tag)

            print()
            print("-" * 80)
            print(f"[processing] {tag}")
            print("-" * 80)

            if not os.path.isdir(workdir):
                print(f"[WARNING] directory missing: {workdir}")
                continue

            # ------------------------------------------------
            # Files
            # ------------------------------------------------

            workspace = os.path.join(
                workdir,
                f"Datacard_fiducial_allCats_{tag}_r_2D_fiducial.root"
            )

            sig_log = os.path.join(
                workdir,
                "log_significance_r_ttH.log"
            )

            limit_log = os.path.join(
                workdir,
                "log_limit_r_tHq.log"
            )

            snapshot_log = os.path.join(
                workdir,
                "log_snapshot_Asimov.log"
            )

            stat_ttH_file = os.path.join(
                workdir,
                "higgsCombine_scan_stat_r_ttH.MultiDimFit.mH125.08.root"
            )

            stat_tHq_file = os.path.join(
                workdir,
                "higgsCombine_scan_stat_r_tHq.MultiDimFit.mH125.08.root"
            )

            syst_ttH_file = os.path.join(
                workdir,
                "higgsCombine_scan_syst_r_ttH.MultiDimFit.mH125.08.root"
            )

            syst_tHq_file = os.path.join(
                workdir,
                "higgsCombine_scan_syst_r_tHq.MultiDimFit.mH125.08.root"
            )

            # ------------------------------------------------
            # Basic sensitivity
            # ------------------------------------------------

            significance = read_significance(sig_log)
            expected_limit = read_expected_limit(limit_log)

            snapshot = read_snapshot(snapshot_log)

            # ------------------------------------------------
            # Likelihood uncertainties
            # ------------------------------------------------

            stat_ttH = scan_uncertainty(
                stat_ttH_file,
                "r_ttH"
            )

            stat_tHq = scan_uncertainty(
                stat_tHq_file,
                "r_tHq"
            )

            total_ttH = scan_uncertainty(
                syst_ttH_file,
                "r_ttH"
            )

            total_tHq = scan_uncertainty(
                syst_tHq_file,
                "r_tHq"
            )

            syst_ttH_up = derive_syst(
                total_ttH["up"],
                stat_ttH["up"]
            )

            syst_ttH_down = derive_syst(
                total_ttH["down"],
                stat_ttH["down"]
            )

            syst_tHq_up = derive_syst(
                total_tHq["up"],
                stat_tHq["up"]
            )

            syst_tHq_down = derive_syst(
                total_tHq["down"],
                stat_tHq["down"]
            )

            # ------------------------------------------------
            # Workspace yields
            # ------------------------------------------------

            cat_yields, bkg_density = extract_workspace_yields(
                workspace
            )

            # ------------------------------------------------
            # Global signal totals
            # ------------------------------------------------

            proc_totals = {
                proc: 0.0
                for proc in SIGNAL_PROCS
            }

            for cat in SIGNAL_CATEGORIES:

                for proc in SIGNAL_PROCS:

                    proc_totals[proc] += cat_yields[cat][proc]

            total_signal = sum(proc_totals.values())

            total_bkg_density = sum(
                v for c, v in bkg_density.items()
                if c in SIGNAL_CATEGORIES
                and math.isfinite(v)
            )

            # ------------------------------------------------
            # Global row
            # ------------------------------------------------

            row = {
                "threshold": threshold_percent(threshold),
                "threshold_tag": threshold,
                "model": model,

                "significance": significance,
                "expected_r_tHq_limit": expected_limit,

                "r_ttH": snapshot["r_ttH"],
                "r_tHq": snapshot["r_tHq"],

                "stat_ttH_up": stat_ttH["up"],
                "stat_ttH_down": stat_ttH["down"],

                "total_ttH_up": total_ttH["up"],
                "total_ttH_down": total_ttH["down"],

                "syst_ttH_up": syst_ttH_up,
                "syst_ttH_down": syst_ttH_down,

                "stat_tHq_up": stat_tHq["up"],
                "stat_tHq_down": stat_tHq["down"],

                "total_tHq_up": total_tHq["up"],
                "total_tHq_down": total_tHq["down"],

                "syst_tHq_up": syst_tHq_up,
                "syst_tHq_down": syst_tHq_down,

                "total_signal": total_signal,
                "total_bkg_density": total_bkg_density,
            }

            # Add process totals
            for proc in SIGNAL_PROCS:
                row[f"yield_{proc}"] = proc_totals[proc]

            # Add signal fractions
            for proc in SIGNAL_PROCS:

                if total_signal > 0:
                    frac = (
                        proc_totals[proc]
                        / total_signal
                        * 100.0
                    )
                else:
                    frac = float("nan")

                row[f"fraction_{proc}_pct"] = frac

            global_rows.append(row)

            # ------------------------------------------------
            # Category rows
            # ------------------------------------------------

            for cat in CATEGORIES:

                crow = {
                    "threshold": threshold_percent(threshold),
                    "threshold_tag": threshold,
                    "model": model,
                    "category": cat,
                    "background_density": bkg_density.get(
                        cat,
                        float("nan")
                    ),
                }

                cat_total = 0.0

                for proc in SIGNAL_PROCS:

                    val = cat_yields[cat][proc]

                    crow[proc] = val
                    cat_total += val

                crow["total_signal"] = cat_total

                category_rows.append(crow)

            print(
                f"  significance      = {significance:.5f}"
            )

            print(
                f"  expected limit    = {expected_limit:.5f}"
            )

            print(
                f"  r_ttH             = {snapshot['r_ttH']:.5f}"
            )

            print(
                f"  r_tHq             = {snapshot['r_tHq']:.5f}"
            )

            print(
                f"  total signal      = {total_signal:.5f}"
            )

    # ========================================================
    # Write CSV
    # ========================================================

    global_csv = os.path.join(
        outdir,
        "pruning_summary_global.csv"
    )

    category_csv = os.path.join(
        outdir,
        "pruning_summary_category.csv"
    )

    if global_rows:

        fields = list(global_rows[0].keys())

        with open(
            global_csv,
            "w",
            newline=""
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=fields
            )

            writer.writeheader()
            writer.writerows(global_rows)

    if category_rows:

        fields = list(category_rows[0].keys())

        with open(
            category_csv,
            "w",
            newline=""
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=fields
            )

            writer.writeheader()
            writer.writerows(category_rows)

    print()
    print("=" * 80)
    print("CSV files written:")
    print(f"  {global_csv}")
    print(f"  {category_csv}")
    print("=" * 80)

    # ========================================================
    # Plotting
    # ========================================================

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

    except ImportError:
        print("[WARNING] matplotlib not available.")
        return

    # --------------------------------------------------------
    # Helper
    # --------------------------------------------------------

    def get_model_rows(model):
        return sorted(
            [
                r for r in global_rows
                if r["model"] == model
            ],
            key=lambda r: r["threshold"]
        )

    def plot_two_models(
        xkey,
        ykey,
        ylabel,
        filename,
        title=None
    ):

        plt.figure(figsize=(8, 6))

        for model in MODELS:

            rows = get_model_rows(model)

            x = [
                r[xkey]
                for r in rows
                if math.isfinite(safe_float(r[xkey]))
                and math.isfinite(safe_float(r[ykey]))
            ]

            y = [
                r[ykey]
                for r in rows
                if math.isfinite(safe_float(r[xkey]))
                and math.isfinite(safe_float(r[ykey]))
            ]

            plt.plot(
                x,
                y,
                marker="o",
                label=model
            )

        plt.xlabel("Pruning threshold (%)")
        plt.ylabel(ylabel)

        if title:
            plt.title(title)

        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()

        plt.savefig(
            os.path.join(plotdir, filename),
            dpi=160
        )

        plt.close()

    # --------------------------------------------------------
    # Sensitivity
    # --------------------------------------------------------

    plot_two_models(
        "threshold",
        "significance",
        "Combine Asimov significance",
        "significance_vs_pruning.png",
        "Expected significance vs pruning"
    )

    plot_two_models(
        "threshold",
        "expected_r_tHq_limit",
        "Expected 50% upper limit on r_tHq",
        "limit_r_tHq_vs_pruning.png",
        "Expected r_tHq limit vs pruning"
    )

    # --------------------------------------------------------
    # Best fits
    # --------------------------------------------------------

    plot_two_models(
        "threshold",
        "r_ttH",
        "Best-fit r_ttH",
        "r_ttH_vs_pruning.png",
        "Best-fit r_ttH vs pruning"
    )

    plot_two_models(
        "threshold",
        "r_tHq",
        "Best-fit r_tHq",
        "r_tHq_vs_pruning.png",
        "Best-fit r_tHq vs pruning"
    )

    # --------------------------------------------------------
    # Uncertainty helper
    # --------------------------------------------------------
def plot_uncertainty(rows, poi, outdir):
    """
    Plot stat, total and derived syst uncertainties for a POI.
    poi should be 'r_ttH' or 'r_tHq'.
    """

    key = poi.replace("r_", "")

    x = sorted(set(float(r["threshold"]) for r in rows))

    fig, ax = plt.subplots(figsize=(8, 6))

    for model in MODELS:
        model_rows = [
            r for r in rows
            if r["model"] == model
        ]

        model_rows = sorted(
            model_rows,
            key=lambda r: float(r["threshold"])
        )

        xx = [float(r["threshold"]) for r in model_rows]

        stat_up = [float(r[f"stat_{key}_up"]) for r in model_rows]
        stat_down = [float(r[f"stat_{key}_down"]) for r in model_rows]

        total_up = [float(r[f"total_{key}_up"]) for r in model_rows]
        total_down = [float(r[f"total_{key}_down"]) for r in model_rows]

        syst_up = [float(r[f"syst_{key}_up"]) for r in model_rows]
        syst_down = [float(r[f"syst_{key}_down"]) for r in model_rows]

        # Use central values of the asymmetric uncertainties for plotting
        stat = [
            0.5 * (u + d)
            for u, d in zip(stat_up, stat_down)
        ]

        total = [
            0.5 * (u + d)
            for u, d in zip(total_up, total_down)
        ]

        syst = [
            0.5 * (u + d)
            for u, d in zip(syst_up, syst_down)
        ]

        ax.plot(
            xx, stat,
            marker="o",
            linestyle="-",
            label=f"{model} stat"
        )

        ax.plot(
            xx, total,
            marker="s",
            linestyle="-",
            label=f"{model} total"
        )

        ax.plot(
            xx, syst,
            marker="^",
            linestyle="--",
            label=f"{model} syst"
        )

    ax.set_xlabel("Pruning threshold (%)")
    ax.set_ylabel(f"Uncertainty on {poi}")
    ax.set_title(f"{poi}: statistical, systematic and total uncertainty")
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.tight_layout()

    outfile = os.path.join(
        outdir,
        f"uncertainty_{poi}_vs_pruning.png"
    )

    fig.savefig(outfile, dpi=150)
    plt.close(fig)

    print(f"[plot] {outfile}")

    # Statistical
    plot_uncertainty(
        "r_ttH",
        "stat",
        "stat_uncertainty_r_ttH.png",
        "r_ttH ± statistical uncertainty"
    )

    plot_uncertainty(
        "r_tHq",
        "stat",
        "stat_uncertainty_r_tHq.png",
        "r_tHq ± statistical uncertainty"
    )

    # Total
    plot_uncertainty(
        "r_ttH",
        "total",
        "total_uncertainty_r_ttH.png",
        "r_ttH ± total uncertainty"
    )

    plot_uncertainty(
        "r_tHq",
        "total",
        "total_uncertainty_r_tHq.png",
        "r_tHq ± total uncertainty"
    )

    # Systematic
    def plot_syst(poi, filename):

        plt.figure(figsize=(8, 6))

        for model in MODELS:

            rows = get_model_rows(model)

            x = []
            up = []
            down = []

            for r in rows:

                su = r[f"syst_{poi}_up"]
                sd = r[f"syst_{poi}_down"]

                if not (
                    math.isfinite(safe_float(su))
                    and math.isfinite(safe_float(sd))
                ):
                    continue

                x.append(r["threshold"])
                up.append(su)
                down.append(sd)

            plt.plot(
                x,
                up,
                marker="o",
                label=f"{model} syst. up"
            )

            plt.plot(
                x,
                down,
                marker="s",
                linestyle="--",
                label=f"{model} syst. down"
            )

        plt.xlabel("Pruning threshold (%)")
        plt.ylabel(f"Systematic uncertainty on {poi}")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()

        plt.savefig(
            os.path.join(plotdir, filename),
            dpi=160
        )

        plt.close()

    plot_syst(
        "r_ttH",
        "systematic_uncertainty_r_ttH.png"
    )

    plot_syst(
        "r_tHq",
        "systematic_uncertainty_r_tHq.png"
    )

    # ========================================================
    # Signal yield plots
    # ========================================================

    def plot_signal_processes():

        plt.figure(figsize=(9, 6))

        for model in MODELS:

            rows = get_model_rows(model)

            for proc in SIGNAL_PROCS:

                x = [
                    r["threshold"]
                    for r in rows
                ]

                y = [
                    r[f"yield_{proc}"]
                    for r in rows
                ]

                linestyle = "-" if model == "DCB" else "--"

                plt.plot(
                    x,
                    y,
                    marker="o",
                    linestyle=linestyle,
                    label=f"{proc} ({model})"
                )

        plt.xlabel("Pruning threshold (%)")
        plt.ylabel("Total expected signal yield")
        plt.title("Signal yields vs pruning")
        plt.grid(True, alpha=0.3)
        plt.legend(
            ncol=2,
            fontsize=8
        )
        plt.tight_layout()

        plt.savefig(
            os.path.join(
                plotdir,
                "signal_process_yields_vs_pruning.png"
            ),
            dpi=160
        )

        plt.close()

    plot_signal_processes()

    # --------------------------------------------------------
    # Total signal
    # --------------------------------------------------------

    plot_two_models(
        "threshold",
        "total_signal",
        "Total expected signal yield",
        "total_signal_vs_pruning.png",
        "Total signal yield vs pruning"
    )

    # --------------------------------------------------------
    # Category plots
    # --------------------------------------------------------

    def plot_category_process(proc):

        plt.figure(figsize=(10, 7))

        for model in MODELS:

            rows = [
                r for r in category_rows
                if r["model"] == model
            ]

            for cat in SIGNAL_CATEGORIES:

                sub = [
                    r for r in rows
                    if r["category"] == cat
                ]

                sub.sort(
                    key=lambda r: r["threshold"]
                )

                x = [
                    r["threshold"]
                    for r in sub
                ]

                y = [
                    r[proc]
                    for r in sub
                ]

                linestyle = "-" if model == "DCB" else "--"

                plt.plot(
                    x,
                    y,
                    linestyle=linestyle,
                    marker="o",
                    markersize=3,
                    label=f"{cat} ({model})"
                )

        plt.xlabel("Pruning threshold (%)")
        plt.ylabel(f"{proc} yield")
        plt.title(
            f"{proc} yield by category vs pruning"
        )

        plt.grid(True, alpha=0.3)

        plt.legend(
            fontsize=6,
            ncol=2
        )

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                plotdir,
                f"category_{proc}_vs_pruning.png"
            ),
            dpi=160
        )

        plt.close()

    # Produce category plots for the three processes
    # most relevant to the current ttH/tHq analysis.
    for proc in ["ttH", "tHq", "tHW"]:
        plot_category_process(proc)

    # ========================================================
    # Signal loss relative to 0%
    # ========================================================

    baseline = {}

    for model in MODELS:

        rows = get_model_rows(model)

        if not rows:
            continue

        baseline_row = None

        for r in rows:
            if abs(r["threshold"]) < 1e-9:
                baseline_row = r
                break

        if baseline_row:
            baseline[model] = baseline_row

    loss_rows = []

    for r in global_rows:

        model = r["model"]

        if model not in baseline:
            continue

        b = baseline[model]

        lr = {
            "threshold": r["threshold"],
            "model": model,
        }

        for proc in SIGNAL_PROCS:

            base_val = b[f"yield_{proc}"]
            current = r[f"yield_{proc}"]

            if base_val > 0:
                loss = (
                    1.0 - current / base_val
                ) * 100.0
            else:
                loss = float("nan")

            lr[f"{proc}_loss_pct"] = loss

        base_total = b["total_signal"]

        if base_total > 0:
            lr["total_signal_loss_pct"] = (
                1.0 - r["total_signal"] / base_total
            ) * 100.0
        else:
            lr["total_signal_loss_pct"] = float("nan")

        loss_rows.append(lr)

    loss_csv = os.path.join(
        outdir,
        "signal_loss.csv"
    )

    if loss_rows:

        fields = list(loss_rows[0].keys())

        with open(
            loss_csv,
            "w",
            newline=""
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=fields
            )

            writer.writeheader()
            writer.writerows(loss_rows)

    # Plot total signal loss
    plt.figure(figsize=(8, 6))

    for model in MODELS:

        rows = [
            r for r in loss_rows
            if r["model"] == model
        ]

        rows.sort(
            key=lambda r: r["threshold"]
        )

        plt.plot(
            [r["threshold"] for r in rows],
            [r["total_signal_loss_pct"] for r in rows],
            marker="o",
            label=model
        )

    plt.xlabel("Pruning threshold (%)")
    plt.ylabel("Signal loss relative to 0% (%)")
    plt.title("Total signal loss vs pruning")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            plotdir,
            "total_signal_loss_vs_pruning.png"
        ),
        dpi=160
    )

    plt.close()

    # ========================================================
    # Print compact summary
    # ========================================================

    print()
    print("=" * 110)
    print(
        f"{'Threshold':>10} "
        f"{'Model':>6} "
        f"{'Z':>10} "
        f"{'r_tHq lim':>12} "
        f"{'r_ttH':>10} "
        f"{'r_tHq':>10} "
        f"{'S total':>12}"
    )
    print("=" * 110)

    for r in sorted(
        global_rows,
        key=lambda x: (
            x["threshold"],
            x["model"]
        )
    ):

        print(
            f"{r['threshold']:10.1f} "
            f"{r['model']:>6} "
            f"{r['significance']:10.5f} "
            f"{r['expected_r_tHq_limit']:12.5f} "
            f"{r['r_ttH']:10.5f} "
            f"{r['r_tHq']:10.5f} "
            f"{r['total_signal']:12.5f}"
        )

    print("=" * 110)

    print()
    print("Finished.")
    print(f"Global summary  : {global_csv}")
    print(f"Category summary: {category_csv}")
    print(f"Signal loss     : {loss_csv}")
    print(f"Plots           : {plotdir}")


if __name__ == "__main__":
    main()

