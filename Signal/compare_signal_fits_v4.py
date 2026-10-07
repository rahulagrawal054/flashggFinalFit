#!/usr/bin/env python3
"""
compare_signal_fits.py  (v3 -- category-centric)

Parses signalFit log files from the Sum-of-Gaussian (SoG) and
DCB+Gaussian (DCB) pipelines, across all 4 eras, and produces ONE
TABLE PER CATEGORY (16 tables total), each with up to
4 eras x 16 processes = 64 rows:

    era | process | numEntries(SoG) | numEntries(DCB)
    | replaced?(SoG) | replaced?(DCB) | replacement_proc
    | chi2/ndof (SoG, post-fit) | chi2/ndof (DCB, post-fit)

For each category, also produces two plots:

    1) entries_<cat>.png
       -- bar chart of numEntries, one bar per (era,process), sorted
          descending, with a horizontal line at 100 (the signalFit
          replacement threshold). Bars below the line are exactly the
          combinations that got a BORROWED shape; bars above got their
          own fit. This makes the threshold mechanism visible directly.

    2) chi2ndof_<cat>.png
       -- SoG vs DCB chi2/ndof, grouped bars, but ONLY for the
          (era,process) combinations that were DIRECTLY FIT in both
          pipelines (replaced=False). Replaced combinations are
          deliberately excluded from this comparison, since their
          chi2/ndof is just a copy of whichever donor process was
          borrowed from -- including them would duplicate the same few
          donor values dozens of times and make the comparison
          meaningless. Replaced combinations are instead listed in a
          separate small table beneath the chart (donor + count).

Usage (run from the directory containing logs_SoG/ and logs_DCB/):
    python3 compare_signal_fits.py --auto --out-dir tables/ --plots --plot-dir plots/

    # Sort entries ascending instead of descending:
    python3 compare_signal_fits.py --auto --out-dir tables/ --plots --entries-order asc

    # Change the replacement threshold line (must match your actual
    # --threshold if you ever changed it from the framework default):
    python3 compare_signal_fits.py --auto --plots --threshold 100
"""

import argparse
import csv
import os
import re
import sys
from collections import OrderedDict as od, defaultdict

ERAS = ["2022preEE", "2022postEE", "2023preBPix", "2023postBPix"]

# ----------------------------------------------------------------------
# Parser (per single log file -> dict[(proc,cat)] = {...})
# ----------------------------------------------------------------------

def parse_signalfit_log(path):
    """
    Returns dict keyed by (proc, cat) -> dict with:
        numEntries          -- this process's OWN entries (small count
                                if replaced; NOT the donor's numEntries)
        replaced            -- bool
        replacement_proc    -- str or ""
        chi2_over_ndof      -- POST-FIT (converged, i.e. the LAST
                                "* chi2 = ..." line in this block's) value
    """
    results = {}
    if not path or not os.path.isfile(path):
        return results

    with open(path, "r", errors="replace") as f:
        lines = f.readlines()

    cur_key = None
    replacement = None
    chi2_lines_this_block = []

    def flush_block():
        if cur_key is None:
            return
        entry = results.setdefault(cur_key, {})
        if chi2_lines_this_block:
            entry["chi2_over_ndof"] = chi2_lines_this_block[-1]  # last = post-fit

    for line in lines:
        m = re.search(r"Running fit for \(proc,cat\) = \(([^,]+),([^)]+)\)", line)
        if m:
            flush_block()
            cur_key = (m.group(1), m.group(2))
            replacement = None
            chi2_lines_this_block = []
            results[cur_key] = {
                "numEntries": None,
                "replaced": False,
                "replacement_proc": "",
                "chi2_over_ndof": None,
            }
            continue

        m = re.search(
            r"Too few entries in nominal dataset \((\d+) < (\d+)\)\. "
            r"Using replacement \(proc,cat\) = \(([^,]+),([^)]+)\)",
            line,
        )
        if m and cur_key:
            results[cur_key]["numEntries"] = int(m.group(1))
            results[cur_key]["replaced"] = True
            results[cur_key]["replacement_proc"] = m.group(3)
            replacement = m.group(3)
            continue

        m = re.search(r"numEntries = (\d+),\s*sumEntries = ([\d.eE+-]+)", line)
        if m and cur_key and replacement is None:
            # only take this as OWN numEntries if not currently inside a
            # replacement block (otherwise this is the donor's line)
            results[cur_key]["numEntries"] = int(m.group(1))
            continue

        m = re.search(
            r"^\s*\*\s*chi2\s*=\s*([\d.eE+-]+),\s*n\(dof\)\s*=\s*(\d+)\s*"
            r"-->\s*chi2/n\(dof\)\s*=\s*([\d.eE+-]+)",
            line,
        )
        if m and cur_key:
            chi2_lines_this_block.append(float(m.group(3)))
            continue

    flush_block()
    return results


def load_all_eras(log_dir_template):
    """
    log_dir_template e.g. 'logs_SoG/signalFit_{era}.log'
    Returns dict[era] = dict[(proc,cat)] = {...}
    """
    out = {}
    for era in ERAS:
        path = log_dir_template.format(era=era)
        out[era] = parse_signalfit_log(path)
    return out


# ----------------------------------------------------------------------
# Build per-category tables (64 rows: 4 eras x up to 16 processes)
# ----------------------------------------------------------------------

def build_category_tables(sog_by_era, dcb_by_era):
    """
    Returns dict[category] = list of row-dicts, one per (era, process).
    """
    all_cats = set()
    all_procs_per_cat = defaultdict(set)
    for era in ERAS:
        for (proc, cat) in sog_by_era.get(era, {}).keys():
            all_cats.add(cat)
            all_procs_per_cat[cat].add(proc)
        for (proc, cat) in dcb_by_era.get(era, {}).keys():
            all_cats.add(cat)
            all_procs_per_cat[cat].add(proc)

    tables = {}
    for cat in sorted(all_cats):
        rows = []
        for era in ERAS:
            for proc in sorted(all_procs_per_cat[cat]):
                s = sog_by_era.get(era, {}).get((proc, cat), {})
                d = dcb_by_era.get(era, {}).get((proc, cat), {})
                if not s and not d:
                    continue  # this proc/cat simply wasn't run for this era
                rows.append({
                    "era": era,
                    "process": proc,
                    "numEntries_SoG": s.get("numEntries"),
                    "numEntries_DCB": d.get("numEntries"),
                    "replaced_SoG": s.get("replaced"),
                    "replaced_DCB": d.get("replaced"),
                    "replacement_proc": s.get("replacement_proc") or d.get("replacement_proc") or "",
                    "chi2_over_ndof_SoG": s.get("chi2_over_ndof"),
                    "chi2_over_ndof_DCB": d.get("chi2_over_ndof"),
                })
        tables[cat] = rows
    return tables


FIELDNAMES = [
    "era", "process",
    "numEntries_SoG", "numEntries_DCB",
    "replaced_SoG", "replaced_DCB",
    "replacement_proc",
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


def print_category_table(cat, rows, sort_key, descending):
    rows_sorted = sorted(
        rows,
        key=lambda r: (r[sort_key] if r[sort_key] is not None else -1),
        reverse=descending,
    )
    print(f"\n{'='*110}")
    print(f"  Category: {cat}   ({len(rows)} (era,process) rows)")
    print(f"{'='*110}")
    header = (
        f"{'Era':<14}{'Process':<12}"
        f"{'N_SoG':>8}{'N_DCB':>8}"
        f"{'Repl_SoG':>9}{'Repl_DCB':>9}"
        f"{'DonorProc':>11}"
        f"{'chi2/ndof_SoG':>15}{'chi2/ndof_DCB':>15}"
    )
    print(header)
    print("-" * len(header))
    for r in rows_sorted:
        print(
            f"{r['era']:<14}{r['process']:<12}"
            f"{fmt(r['numEntries_SoG']):>8}{fmt(r['numEntries_DCB']):>8}"
            f"{fmt(r['replaced_SoG']):>9}{fmt(r['replaced_DCB']):>9}"
            f"{fmt(r['replacement_proc']):>11}"
            f"{fmt(r['chi2_over_ndof_SoG'], '.3f'):>15}"
            f"{fmt(r['chi2_over_ndof_DCB'], '.3f'):>15}"
        )
    n_replaced = sum(1 for r in rows if r["replaced_SoG"] or r["replaced_DCB"])
    n_direct = len(rows) - n_replaced
    print("-" * len(header))
    print(f"  Directly fit: {n_direct}   Replaced (borrowed shape): {n_replaced}")


# ----------------------------------------------------------------------
# Plotting
# ----------------------------------------------------------------------

def make_entries_plot(cat, rows, plot_dir, threshold, order):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("  [SKIP PLOTS] matplotlib not available")
        return

    plot_rows = [r for r in rows if r["numEntries_SoG"] is not None]
    if not plot_rows:
        return
    descending = (order == "desc")
    plot_rows.sort(key=lambda r: r["numEntries_SoG"], reverse=descending)

    labels = [f"{r['era']}\n{r['process']}" for r in plot_rows]
    values = [r["numEntries_SoG"] for r in plot_rows]
    colors = ["tab:red" if r["replaced_SoG"] else "tab:blue" for r in plot_rows]

    fig, ax = plt.subplots(figsize=(max(10, len(labels) * 0.28), 6))
    x = range(len(labels))
    ax.bar(x, values, color=colors)
    ax.axhline(threshold, color="black", linestyle="--", linewidth=1.2,
               label=f"replacement threshold ({threshold})")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, rotation=90, fontsize=6)
    ax.set_ylabel("numEntries (own dataset)")
    ax.set_yscale("log")
    ax.set_title(f"Entries per (era, process) -- {cat}\n"
                 f"(red = shape borrowed, blue = directly fit)")
    ax.legend()
    fig.tight_layout()
    out = os.path.join(plot_dir, f"entries_{cat}.png")
    os.makedirs(plot_dir, exist_ok=True)
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  --> wrote {out}")


def make_chi2_plot(cat, rows, plot_dir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("  [SKIP PLOTS] matplotlib not available")
        return

    # Only combinations that were DIRECTLY FIT (not replaced) in BOTH
    # pipelines, and that have a real chi2/ndof value from each.
    direct_rows = [
        r for r in rows
        if not r["replaced_SoG"] and not r["replaced_DCB"]
        and r["chi2_over_ndof_SoG"] is not None
        and r["chi2_over_ndof_DCB"] is not None
    ]
    replaced_rows = [r for r in rows if r["replaced_SoG"] or r["replaced_DCB"]]

    fig, ax = plt.subplots(figsize=(max(9, len(direct_rows) * 0.4), 6))

    if direct_rows:
        labels = [f"{r['era']}\n{r['process']}" for r in direct_rows]
        sog_vals = [r["chi2_over_ndof_SoG"] for r in direct_rows]
        dcb_vals = [r["chi2_over_ndof_DCB"] for r in direct_rows]
        x = range(len(labels))
        width = 0.4
        ax.bar([i - width/2 for i in x], sog_vals, width, label="SoG", color="tab:blue")
        ax.bar([i + width/2 for i in x], dcb_vals, width, label="DCB", color="tab:orange")
        ax.axhline(1.0, color="green", linestyle="--", linewidth=1, label="chi2/ndof = 1")
        ax.axhline(2.0, color="red", linestyle=":", linewidth=1, label="chi2/ndof = 2 (flag)")
        ax.set_xticks(list(x))
        ax.set_xticklabels(labels, rotation=90, fontsize=7)
        ax.set_yscale("log")
    else:
        ax.text(0.5, 0.5, "No directly-fit (era,process) combinations\n"
                           "in this category -- everything used a borrowed shape.",
                ha="center", va="center", transform=ax.transAxes)

    ax.set_ylabel("chi2 / ndof (post-fit)")
    ax.set_title(f"SoG vs DCB fit quality -- {cat}\n"
                 f"(directly-fit combinations only; "
                 f"{len(replaced_rows)} of {len(rows)} used a borrowed shape)")
    if direct_rows:
        ax.legend()
    fig.tight_layout()
    os.makedirs(plot_dir, exist_ok=True)
    out = os.path.join(plot_dir, f"chi2ndof_{cat}.png")
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  --> wrote {out}")

    # Separate small summary of what got replaced from what, for this category
    if replaced_rows:
        donor_counts = defaultdict(int)
        for r in replaced_rows:
            donor_counts[r["replacement_proc"]] += 1
        print(f"  Replaced-shape summary for {cat} "
              f"({len(replaced_rows)} of {len(rows)} combinations):")
        for donor, count in sorted(donor_counts.items(), key=lambda kv: -kv[1]):
            print(f"      borrowed from '{donor}': {count} combination(s)")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--auto", action="store_true",
                     help="Auto-discover logs_SoG/signalFit_<era>.log and "
                          "logs_DCB/signalFit_<era>.log for all 4 eras.")
    ap.add_argument("--out-dir", default=None, help="Output directory for per-category CSVs")
    ap.add_argument("--plots", action="store_true", help="Generate plots (needs matplotlib)")
    ap.add_argument("--plot-dir", default="plots", help="Directory to write plots into")
    ap.add_argument("--entries-order", choices=["asc", "desc"], default="desc",
                     help="Sort order for the entries plot/table (default: descending)")
    ap.add_argument("--threshold", type=int, default=100,
                     help="Replacement threshold to draw as a reference line (default: 100, "
                          "matching signalFit.py's default -- change if you configured it differently)")
    args = ap.parse_args()

    if not args.auto:
        print("This version is category-centric and expects --auto "
              "(run from the directory containing logs_SoG/ and logs_DCB/).")
        sys.exit(1)

    sog_by_era = load_all_eras(os.path.join("logs_SoG", "signalFit_{era}.log"))
    dcb_by_era = load_all_eras(os.path.join("logs_DCB", "signalFit_{era}.log"))

    if not any(sog_by_era.values()) and not any(dcb_by_era.values()):
        print("[ERROR] No signalFit logs found under logs_SoG/ or logs_DCB/.")
        sys.exit(1)

    tables = build_category_tables(sog_by_era, dcb_by_era)

    for cat, rows in tables.items():
        print_category_table(cat, rows, sort_key="numEntries_SoG",
                              descending=(args.entries_order == "desc"))

        if args.out_dir:
            os.makedirs(args.out_dir, exist_ok=True)
            out_path = os.path.join(args.out_dir, f"table_{cat}.csv")
            rows_sorted = sorted(
                rows,
                key=lambda r: (r["numEntries_SoG"] if r["numEntries_SoG"] is not None else -1),
                reverse=(args.entries_order == "desc"),
            )
            write_csv(rows_sorted, out_path)
            print(f"  --> wrote {out_path}")

        if args.plots:
            make_entries_plot(cat, rows, args.plot_dir, args.threshold, args.entries_order)
            make_chi2_plot(cat, rows, args.plot_dir)

    print(f"\n{'='*60}")
    print(f"  Done. {len(tables)} category table(s) processed.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
