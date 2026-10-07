#!/usr/bin/env python3
"""
compare_signal_fits.py  (v2)

Parses signalFit log files from the Sum-of-Gaussian (SoG) and
DCB+Gaussian (DCB) signal-modeling pipelines and produces one combined
table per era:

    category | process | numEntries(SoG) | numEntries(DCB)
    | replaced?(SoG) | replaced?(DCB) | replacement_proc
    | donor_numEntries(SoG) | donor_numEntries(DCB)
    | chi2/ndof (SoG, post-fit) | chi2/ndof (DCB, post-fit)

chi2/ndof is read directly from signalFit's own "* chi2 = ..., n(dof) = ...
--> chi2/n(dof) = ..." line -- no fTest log needed. Each proc/cat block in
signalFit prints this TWICE (once pre-fit with initial guessed parameters,
once post-fit after convergence) -- this script always keeps the LAST
(post-fit, converged) value, which is the physically meaningful one.

Also prints a per-era summary flagging:
    - mismatches (replaced in one pipeline but not the other)
    - any combination with chi2/ndof > 2.0 in either pipeline

And can generate comparison plots (bar charts of chi2/ndof per category,
scatter of SoG vs DCB chi2/ndof) via matplotlib -- see --plots.

Usage:
    # Table only, all 4 eras, from the directory containing logs_SoG/ and logs_DCB/:
    python3 compare_signal_fits.py --auto --out-dir tables/

    # Table + plots:
    python3 compare_signal_fits.py --auto --out-dir tables/ --plots --plot-dir plots/

    # Single era, manual paths:
    python3 compare_signal_fits.py --era 2022preEE \
        --sog-signalfit logs_SoG/signalFit_2022preEE.log \
        --dcb-signalfit logs_DCB/signalFit_2022preEE.log \
        --out table_2022preEE.csv
"""

import argparse
import csv
import os
import re
import sys
from collections import OrderedDict as od

ERAS = ["2022preEE", "2022postEE", "2023preBPix", "2023postBPix"]

# ----------------------------------------------------------------------
# Parser
# ----------------------------------------------------------------------

def parse_signalfit_log(path):
    """
    Returns OrderedDict keyed by (proc, cat) -> dict with:
        numEntries          -- this process's OWN entries (the small
                                (X < threshold) count when replaced;
                                NOT the donor's numEntries)
        donor_numEntries    -- the replacement process's own entries
                                (only set when replaced=True)
        replaced            -- bool
        replacement_proc    -- str or ""
        chi2, ndof, chi2_over_ndof  -- POST-FIT (converged) values, i.e.
                                the LAST "* chi2 = ..." line seen in this
                                proc/cat's block, not the first (pre-fit) one
    """
    results = od()
    if not path or not os.path.isfile(path):
        return results

    with open(path, "r", errors="replace") as f:
        lines = f.readlines()

    cur_key = None
    replacement = None
    own_numE = None
    # holds every chi2 line seen for the CURRENT proc/cat block, in order;
    # we keep the LAST one (post-fit) once the block ends
    chi2_lines_this_block = []

    def flush_block():
        """Commit the current proc/cat block's data into results."""
        if cur_key is None:
            return
        entry = results.setdefault(cur_key, {})
        if chi2_lines_this_block:
            # last entry = post-fit (converged) chi2/ndof
            entry["chi2"], entry["ndof"], entry["chi2_over_ndof"] = chi2_lines_this_block[-1]

    for line in lines:
        m = re.search(r"Running fit for \(proc,cat\) = \(([^,]+),([^)]+)\)", line)
        if m:
            flush_block()
            cur_key = (m.group(1), m.group(2))
            replacement = None
            own_numE = None
            chi2_lines_this_block = []
            results[cur_key] = {
                "numEntries": None,
                "donor_numEntries": None,
                "replaced": False,
                "replacement_proc": "",
                "chi2": None,
                "ndof": None,
                "chi2_over_ndof": None,
            }
            continue

        m = re.search(
            r"Too few entries in nominal dataset \((\d+) < (\d+)\)\. "
            r"Using replacement \(proc,cat\) = \(([^,]+),([^)]+)\)",
            line,
        )
        if m and cur_key:
            own_numE = int(m.group(1))
            replacement = (m.group(3), m.group(4))
            results[cur_key]["numEntries"] = own_numE
            results[cur_key]["replaced"] = True
            results[cur_key]["replacement_proc"] = replacement[0]
            continue

        m = re.search(r"numEntries = (\d+),\s*sumEntries = ([\d.eE+-]+)", line)
        if m and cur_key:
            numE = int(m.group(1))
            if replacement is not None:
                results[cur_key]["donor_numEntries"] = numE
            else:
                results[cur_key]["numEntries"] = numE
            continue

        # Post/pre-fit chi2 summary line, e.g.:
        #   * chi2 = 53.219392, n(dof) = 21 --> chi2/n(dof) = 2.534
        # Deliberately NOT matching the "[VERBOSE] chi2 = ..." line, which
        # repeats the same value without n(dof) and would just duplicate it.
        m = re.search(
            r"^\s*\*\s*chi2\s*=\s*([\d.eE+-]+),\s*n\(dof\)\s*=\s*(\d+)\s*"
            r"-->\s*chi2/n\(dof\)\s*=\s*([\d.eE+-]+)",
            line,
        )
        if m and cur_key:
            chi2_lines_this_block.append(
                (float(m.group(1)), int(m.group(2)), float(m.group(3)))
            )
            continue

    flush_block()  # commit the final block in the file
    return results


# ----------------------------------------------------------------------
# Table building
# ----------------------------------------------------------------------

def build_table(sog_sf, dcb_sf):
    all_keys = sorted(set(sog_sf.keys()) | set(dcb_sf.keys()))
    rows = []
    for proc, cat in all_keys:
        s = sog_sf.get((proc, cat), {})
        d = dcb_sf.get((proc, cat), {})
        rows.append(
            {
                "category": cat,
                "process": proc,
                "numEntries_SoG": s.get("numEntries", ""),
                "numEntries_DCB": d.get("numEntries", ""),
                "replaced_SoG": s.get("replaced", ""),
                "replaced_DCB": d.get("replaced", ""),
                "replacement_proc": s.get("replacement_proc", "") or d.get("replacement_proc", ""),
                "donor_numEntries_SoG": s.get("donor_numEntries", ""),
                "donor_numEntries_DCB": d.get("donor_numEntries", ""),
                "chi2_over_ndof_SoG": s.get("chi2_over_ndof", ""),
                "chi2_over_ndof_DCB": d.get("chi2_over_ndof", ""),
            }
        )
    rows.sort(key=lambda r: (r["category"], r["process"]))
    return rows


FIELDNAMES = [
    "category", "process",
    "numEntries_SoG", "numEntries_DCB",
    "replaced_SoG", "replaced_DCB",
    "replacement_proc",
    "donor_numEntries_SoG", "donor_numEntries_DCB",
    "chi2_over_ndof_SoG", "chi2_over_ndof_DCB",
]


def write_csv(rows, out_path):
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def fmt(v, spec=""):
    if v is None or v == "":
        return "-"
    return f"{v:{spec}}" if spec else f"{v}"


def print_table(rows, era):
    print(f"\n{'='*130}")
    print(f"  Era: {era}   ({len(rows)} proc x cat combinations found)")
    print(f"{'='*130}")
    header = (
        f"{'Category':<14}{'Process':<12}"
        f"{'N_own_SoG':>10}{'N_own_DCB':>10}"
        f"{'Repl_SoG':>9}{'Repl_DCB':>9}"
        f"{'DonorProc':>11}"
        f"{'chi2/ndof_SoG':>15}{'chi2/ndof_DCB':>15}"
    )
    print(header)
    print("-" * len(header))
    print("  (N_own = this process's OWN entries -- when Replaced=True, the shape fit")
    print("   comes from DonorProc's data instead. chi2/ndof is POST-FIT, per pipeline.)")
    print("-" * len(header))
    for r in rows:
        print(
            f"{r['category']:<14}{r['process']:<12}"
            f"{fmt(r['numEntries_SoG']):>10}{fmt(r['numEntries_DCB']):>10}"
            f"{fmt(r['replaced_SoG']):>9}{fmt(r['replaced_DCB']):>9}"
            f"{fmt(r['replacement_proc']):>11}"
            f"{fmt(r['chi2_over_ndof_SoG'], '.3f'):>15}"
            f"{fmt(r['chi2_over_ndof_DCB'], '.3f'):>15}"
        )


def print_summary(rows, era):
    total = len(rows)
    mismatched = [
        r for r in rows
        if r["replaced_SoG"] != "" and r["replaced_DCB"] != ""
        and r["replaced_SoG"] != r["replaced_DCB"]
    ]
    bad_sog = [r for r in rows if isinstance(r["chi2_over_ndof_SoG"], float) and r["chi2_over_ndof_SoG"] > 2.0]
    bad_dcb = [r for r in rows if isinstance(r["chi2_over_ndof_DCB"], float) and r["chi2_over_ndof_DCB"] > 2.0]

    print(f"\n  --- Summary for {era} ---")
    print(f"  Total proc x cat combinations: {total}")
    if mismatched:
        print(f"  [WARNING] {len(mismatched)} MISMATCH(es) -- replaced in one pipeline, fit in the other:")
        for r in mismatched:
            print(f"      {r['category']:<14}{r['process']}")
    else:
        print("  Replacement logic agrees between SoG and DCB for every combination. Good.")

    if bad_sog:
        print(f"  [FLAG] {len(bad_sog)} SoG fit(s) with chi2/ndof > 2.0:")
        for r in bad_sog:
            print(f"      {r['category']:<14}{r['process']:<12} chi2/ndof = {r['chi2_over_ndof_SoG']:.2f}")
    if bad_dcb:
        print(f"  [FLAG] {len(bad_dcb)} DCB fit(s) with chi2/ndof > 2.0:")
        for r in bad_dcb:
            print(f"      {r['category']:<14}{r['process']:<12} chi2/ndof = {r['chi2_over_ndof_DCB']:.2f}")


# ----------------------------------------------------------------------
# Plotting (optional, requires matplotlib)
# ----------------------------------------------------------------------

def make_plots(rows, era, plot_dir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("  [SKIP PLOTS] matplotlib not available in this environment "
              "(pip install matplotlib --user, or --break-system-packages on lxplus)")
        return

    os.makedirs(plot_dir, exist_ok=True)

    plot_rows = [
        r for r in rows
        if isinstance(r["chi2_over_ndof_SoG"], float) and isinstance(r["chi2_over_ndof_DCB"], float)
    ]
    if not plot_rows:
        print(f"  [SKIP PLOTS] no rows with both SoG and DCB chi2/ndof for {era}")
        return

    labels = [f"{r['category']}\n{r['process']}" for r in plot_rows]
    sog_vals = [r["chi2_over_ndof_SoG"] for r in plot_rows]
    dcb_vals = [r["chi2_over_ndof_DCB"] for r in plot_rows]

    # --- Plot 1: grouped bar chart, chi2/ndof per proc x cat, SoG vs DCB ---
    fig, ax = plt.subplots(figsize=(max(10, len(labels) * 0.35), 6))
    x = range(len(labels))
    width = 0.4
    ax.bar([i - width/2 for i in x], sog_vals, width, label="SoG", color="tab:blue")
    ax.bar([i + width/2 for i in x], dcb_vals, width, label="DCB", color="tab:orange")
    ax.axhline(1.0, color="green", linestyle="--", linewidth=1, label="chi2/ndof = 1 (ideal)")
    ax.axhline(2.0, color="red", linestyle=":", linewidth=1, label="chi2/ndof = 2 (flag threshold)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, rotation=90, fontsize=6)
    ax.set_ylabel("chi2 / ndof (post-fit)")
    ax.set_title(f"Signal fit quality per process x category -- {era}")
    ax.legend()
    ax.set_yscale("log")  # chi2/ndof can span orders of magnitude (e.g. 97 vs 1.3)
    fig.tight_layout()
    out1 = os.path.join(plot_dir, f"chi2ndof_bars_{era}.png")
    fig.savefig(out1, dpi=150)
    plt.close(fig)
    print(f"  --> wrote {out1}")

    # --- Plot 2: scatter, SoG chi2/ndof vs DCB chi2/ndof, one point per combo ---
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(sog_vals, dcb_vals, alpha=0.7)
    lims = [0, max(max(sog_vals), max(dcb_vals)) * 1.05]
    ax.plot(lims, lims, color="gray", linestyle="--", linewidth=1, label="SoG = DCB")
    ax.set_xlabel("chi2/ndof (SoG)")
    ax.set_ylabel("chi2/ndof (DCB)")
    ax.set_title(f"SoG vs DCB fit quality -- {era}")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.legend()
    fig.tight_layout()
    out2 = os.path.join(plot_dir, f"chi2ndof_scatter_{era}.png")
    fig.savefig(out2, dpi=150)
    plt.close(fig)
    print(f"  --> wrote {out2}")

    # --- Plot 3: per-category summary -- mean chi2/ndof across processes ---
    from collections import defaultdict
    cat_sog = defaultdict(list)
    cat_dcb = defaultdict(list)
    for r in plot_rows:
        cat_sog[r["category"]].append(r["chi2_over_ndof_SoG"])
        cat_dcb[r["category"]].append(r["chi2_over_ndof_DCB"])
    cats = sorted(cat_sog.keys())
    sog_means = [sum(cat_sog[c]) / len(cat_sog[c]) for c in cats]
    dcb_means = [sum(cat_dcb[c]) / len(cat_dcb[c]) for c in cats]

    fig, ax = plt.subplots(figsize=(max(8, len(cats) * 0.5), 5))
    x = range(len(cats))
    width = 0.4
    ax.bar([i - width/2 for i in x], sog_means, width, label="SoG (mean)", color="tab:blue")
    ax.bar([i + width/2 for i in x], dcb_means, width, label="DCB (mean)", color="tab:orange")
    ax.axhline(1.0, color="green", linestyle="--", linewidth=1)
    ax.set_xticks(list(x))
    ax.set_xticklabels(cats, rotation=45, ha="right")
    ax.set_ylabel("mean chi2/ndof across processes")
    ax.set_title(f"Per-category average fit quality -- {era}")
    ax.set_yscale("log")
    ax.legend()
    fig.tight_layout()
    out3 = os.path.join(plot_dir, f"chi2ndof_per_category_{era}.png")
    fig.savefig(out3, dpi=150)
    plt.close(fig)
    print(f"  --> wrote {out3}")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def run_one_era(era, sog_sf_path, dcb_sf_path, out_dir, do_plots, plot_dir):
    sog_sf = parse_signalfit_log(sog_sf_path)
    dcb_sf = parse_signalfit_log(dcb_sf_path)

    if not sog_sf and not dcb_sf:
        print(f"[SKIP] {era}: no signalFit logs found "
              f"(looked for {sog_sf_path} and {dcb_sf_path})")
        return

    rows = build_table(sog_sf, dcb_sf)
    print_table(rows, era)
    print_summary(rows, era)

    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"table_{era}.csv")
        write_csv(rows, out_path)
        print(f"  --> wrote {out_path}")

    if do_plots:
        make_plots(rows, era, plot_dir or "plots")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--auto", action="store_true",
                     help="Auto-discover logs_SoG/signalFit_<era>.log and "
                          "logs_DCB/signalFit_<era>.log for all 4 eras. "
                          "Run from the directory containing logs_SoG/ and logs_DCB/.")
    ap.add_argument("--era", default=None, help="Single era label (manual mode)")
    ap.add_argument("--sog-signalfit", default=None)
    ap.add_argument("--dcb-signalfit", default=None)
    ap.add_argument("--out", default=None, help="Output CSV path (manual mode)")
    ap.add_argument("--out-dir", default=None, help="Output directory for per-era CSVs (--auto mode)")
    ap.add_argument("--plots", action="store_true", help="Also generate comparison plots (needs matplotlib)")
    ap.add_argument("--plot-dir", default="plots", help="Directory to write plots into")
    args = ap.parse_args()

    if args.auto:
        for era in ERAS:
            sog_sf_path = os.path.join("logs_SoG", f"signalFit_{era}.log")
            dcb_sf_path = os.path.join("logs_DCB", f"signalFit_{era}.log")
            run_one_era(era, sog_sf_path, dcb_sf_path, args.out_dir, args.plots, args.plot_dir)
        return

    if not args.era:
        print("ERROR: either use --auto, or provide --era plus the log paths.")
        sys.exit(1)

    sog_sf = parse_signalfit_log(args.sog_signalfit)
    dcb_sf = parse_signalfit_log(args.dcb_signalfit)
    rows = build_table(sog_sf, dcb_sf)
    print_table(rows, args.era)
    print_summary(rows, args.era)
    if args.out:
        write_csv(rows, args.out)
        print(f"\n  --> wrote {args.out}")
    if args.plots:
        make_plots(rows, args.era, args.plot_dir)


if __name__ == "__main__":
    main()
