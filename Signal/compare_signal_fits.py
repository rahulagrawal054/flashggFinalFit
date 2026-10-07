#!/usr/bin/env python3
"""
compare_signal_fits.py

Parses signalFit (and, where available, fTest) log files from the
Sum-of-Gaussian (SoG) and DCB+Gaussian (DCB) signal-modeling pipelines,
and produces one combined table per era:

    category | process | numEntries(SoG) | numEntries(DCB) | sumEntries(SoG)
    | sumEntries(DCB) | replaced?(SoG) | replaced?(DCB) | replacement_proc
    | nGauss (SoG, from fTest) | chi2/ndof (SoG, from fTest)

Also prints a per-era summary:
    - total proc x cat combinations seen
    - how many were fit directly vs. replaced (per pipeline)
    - whether SoG and DCB agree on which combinations were fit/replaced

Usage:
    python3 compare_signal_fits.py \
        --sog-signalfit logs_SoG/signalFit_2022preEE.log \
        --dcb-signalfit logs_DCB/signalFit_2022preEE.log \
        --sog-ftest     logs_SoG/fTest_2022preEE.log \
        --era 2022preEE \
        --out table_2022preEE.csv

    # Or run over all 4 eras at once (expects the standard logs_SoG/
    # and logs_DCB/ naming convention used throughout this analysis):
    python3 compare_signal_fits.py --auto --out-dir tables/
"""

import argparse
import csv
import os
import re
import sys
from collections import OrderedDict as od

ERAS = ["2022preEE", "2022postEE", "2023preBPix", "2023postBPix"]

# ----------------------------------------------------------------------
# Parsers
# ----------------------------------------------------------------------

def parse_signalfit_log(path):
    """
    Returns OrderedDict keyed by (proc, cat) -> dict with:
        numEntries, sumEntries, replaced (bool), replacement_proc (or None)
    """
    results = od()
    if not path or not os.path.isfile(path):
        return results

    with open(path, "r", errors="replace") as f:
        lines = f.readlines()

    cur_key = None
    replacement = None
    for i, line in enumerate(lines):
        m = re.search(r"Running fit for \(proc,cat\) = \(([^,]+),([^)]+)\)", line)
        if m:
            cur_key = (m.group(1), m.group(2))
            replacement = None
            continue

        m = re.search(
            r"Too few entries in nominal dataset \((\d+) < (\d+)\)\. "
            r"Using replacement \(proc,cat\) = \(([^,]+),([^)]+)\)",
            line,
        )
        if m and cur_key:
            replacement = (m.group(3), m.group(4))
            continue

        m = re.search(r"numEntries = (\d+),\s*sumEntries = ([\d.eE+-]+)", line)
        if m and cur_key:
            numE = int(m.group(1))
            sumE = float(m.group(2))
            results[cur_key] = {
                "numEntries": numE,
                "sumEntries": sumE,
                "replaced": replacement is not None,
                "replacement_proc": replacement[0] if replacement else "",
            }
            cur_key = None  # reset until the next "Running fit for" block

    return results


def parse_ftest_log(path):
    """
    Returns OrderedDict keyed by (proc, cat) -> dict with:
        nGauss_opt, chi2, ndof, chi2_over_ndof

    fTest prints one line per nGauss tested, e.g.:
        * (tth_in,ttH_had_1,RV): nGauss = 3, chi^2/n(dof) = 1.0421
    We keep only the *last* (i.e. best/chosen) nGauss line reported by
    fTest for each (proc,cat) -- fTest.py itself picks the minimum
    reduced chi2 internally and prints every candidate, so we track the
    minimum ourselves here directly from the printed values, which is
    robust even if fTest's own internal bookkeeping differs slightly.
    """
    results = {}
    if not path or not os.path.isfile(path):
        return results

    with open(path, "r", errors="replace") as f:
        for line in f:
            m = re.search(
                r"\(([^,]+),([^,]+),RV\):\s*nGauss\s*=\s*(\d+),\s*"
                r"chi\^2/n\(dof\)\s*=\s*([\d.]+)",
                line,
            )
            if not m:
                continue
            proc, cat, nGauss, chi2ndof = m.group(1), m.group(2), int(m.group(3)), float(m.group(4))
            key = (proc, cat)
            prev = results.get(key)
            if prev is None or chi2ndof < prev["chi2_over_ndof"]:
                results[key] = {"nGauss_opt": nGauss, "chi2_over_ndof": chi2ndof}

    return results


# ----------------------------------------------------------------------
# Table building
# ----------------------------------------------------------------------

def build_table(sog_sf, dcb_sf, sog_ft):
    all_keys = sorted(set(sog_sf.keys()) | set(dcb_sf.keys()))
    rows = []
    for proc, cat in all_keys:
        key = (proc, cat)
        s = sog_sf.get(key, {})
        d = dcb_sf.get(key, {})
        ft = sog_ft.get(key, {})
        rows.append(
            {
                "category": cat,
                "process": proc,
                "numEntries_SoG": s.get("numEntries", ""),
                "numEntries_DCB": d.get("numEntries", ""),
                "sumEntries_SoG": s.get("sumEntries", ""),
                "sumEntries_DCB": d.get("sumEntries", ""),
                "replaced_SoG": s.get("replaced", ""),
                "replaced_DCB": d.get("replaced", ""),
                "replacement_proc": s.get("replacement_proc", "") or d.get("replacement_proc", ""),
                "nGauss_opt_SoG": ft.get("nGauss_opt", ""),
                "chi2_over_ndof_SoG": ft.get("chi2_over_ndof", ""),
            }
        )
    # Sort: category, then process, for easy reading
    rows.sort(key=lambda r: (r["category"], r["process"]))
    return rows


FIELDNAMES = [
    "category", "process",
    "numEntries_SoG", "numEntries_DCB",
    "sumEntries_SoG", "sumEntries_DCB",
    "replaced_SoG", "replaced_DCB",
    "replacement_proc",
    "nGauss_opt_SoG", "chi2_over_ndof_SoG",
]


def write_csv(rows, out_path):
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def print_table(rows, era):
    print(f"\n{'='*140}")
    print(f"  Era: {era}   ({len(rows)} proc x cat combinations found)")
    print(f"{'='*140}")
    header = (
        f"{'Category':<14}{'Process':<12}"
        f"{'N_SoG':>8}{'N_DCB':>8}"
        f"{'sumE_SoG':>12}{'sumE_DCB':>12}"
        f"{'Repl_SoG':>9}{'Repl_DCB':>9}"
        f"{'ReplProc':>10}"
        f"{'nGauss':>8}{'chi2/ndof':>11}"
    )
    print(header)
    print("-" * len(header))
    for r in rows:
        def fmt(v, spec=""):
            return f"{v:{spec}}" if v != "" else "-"
        print(
            f"{r['category']:<14}{r['process']:<12}"
            f"{fmt(r['numEntries_SoG']):>8}{fmt(r['numEntries_DCB']):>8}"
            f"{fmt(r['sumEntries_SoG'], '.6f') if r['sumEntries_SoG']!='' else '-':>12}"
            f"{fmt(r['sumEntries_DCB'], '.6f') if r['sumEntries_DCB']!='' else '-':>12}"
            f"{fmt(r['replaced_SoG']):>9}{fmt(r['replaced_DCB']):>9}"
            f"{fmt(r['replacement_proc']):>10}"
            f"{fmt(r['nGauss_opt_SoG']):>8}"
            f"{fmt(r['chi2_over_ndof_SoG'], '.3f') if r['chi2_over_ndof_SoG']!='' else '-':>11}"
        )


def print_summary(rows, era):
    total = len(rows)
    fit_both = sum(1 for r in rows if r["replaced_SoG"] is False and r["replaced_DCB"] is False)
    replaced_both = sum(1 for r in rows if r["replaced_SoG"] is True and r["replaced_DCB"] is True)
    mismatched = sum(
        1 for r in rows
        if r["replaced_SoG"] != "" and r["replaced_DCB"] != ""
        and r["replaced_SoG"] != r["replaced_DCB"]
    )
    bad_chi2 = [
        r for r in rows
        if r["chi2_over_ndof_SoG"] != "" and r["chi2_over_ndof_SoG"] > 2.0
    ]

    print(f"\n  --- Summary for {era} ---")
    print(f"  Total proc x cat combinations: {total}")
    print(f"  Directly fit in BOTH pipelines: {fit_both}")
    print(f"  Replaced in BOTH pipelines:     {replaced_both}")
    print(f"  MISMATCH (replaced in one, fit in other): {mismatched}")
    if mismatched > 0:
        print("  [WARNING] mismatch found -- SoG and DCB disagree on which combos "
              "are replaced. Investigate the flagged rows above.")
    if bad_chi2:
        print(f"  [FLAG] {len(bad_chi2)} combination(s) with chi2/ndof > 2.0 (possible poor fit):")
        for r in bad_chi2:
            print(f"      {r['category']:<14}{r['process']:<12} chi2/ndof = {r['chi2_over_ndof_SoG']:.2f}")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def run_one_era(era, sog_sf_path, dcb_sf_path, sog_ft_path, out_dir):
    sog_sf = parse_signalfit_log(sog_sf_path)
    dcb_sf = parse_signalfit_log(dcb_sf_path)
    sog_ft = parse_ftest_log(sog_ft_path)

    if not sog_sf and not dcb_sf:
        print(f"[SKIP] {era}: no signalFit logs found "
              f"(looked for {sog_sf_path} and {dcb_sf_path})")
        return

    rows = build_table(sog_sf, dcb_sf, sog_ft)
    print_table(rows, era)
    print_summary(rows, era)

    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"table_{era}.csv")
        write_csv(rows, out_path)
        print(f"  --> wrote {out_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--auto", action="store_true",
                     help="Auto-discover logs_SoG/signalFit_<era>.log, "
                          "logs_DCB/signalFit_<era>.log, logs_SoG/fTest_<era>.log "
                          "for all 4 eras, run from the directory containing logs_SoG/ and logs_DCB/.")
    ap.add_argument("--era", default=None, help="Single era label (for manual mode)")
    ap.add_argument("--sog-signalfit", default=None)
    ap.add_argument("--dcb-signalfit", default=None)
    ap.add_argument("--sog-ftest", default=None)
    ap.add_argument("--out", default=None, help="Output CSV path (manual mode)")
    ap.add_argument("--out-dir", default=None, help="Output directory for per-era CSVs (--auto mode)")
    args = ap.parse_args()

    if args.auto:
        for era in ERAS:
            sog_sf_path = os.path.join("logs_SoG", f"signalFit_{era}.log")
            dcb_sf_path = os.path.join("logs_DCB", f"signalFit_{era}.log")
            sog_ft_path = os.path.join("logs_SoG", f"fTest_{era}.log")
            run_one_era(era, sog_sf_path, dcb_sf_path, sog_ft_path, args.out_dir)
        return

    if not args.era:
        print("ERROR: either use --auto, or provide --era plus the log paths.")
        sys.exit(1)

    sog_sf = parse_signalfit_log(args.sog_signalfit)
    dcb_sf = parse_signalfit_log(args.dcb_signalfit)
    sog_ft = parse_ftest_log(args.sog_ftest)
    rows = build_table(sog_sf, dcb_sf, sog_ft)
    print_table(rows, args.era)
    print_summary(rows, args.era)
    if args.out:
        write_csv(rows, args.out)
        print(f"\n  --> wrote {args.out}")


if __name__ == "__main__":
    main()
