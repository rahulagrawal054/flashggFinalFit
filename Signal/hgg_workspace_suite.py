#!/usr/bin/env python3
"""
CMS HGG Workspace Inspection & Diagnostic Suite
Combines dataset mass-point checks, workspace object inventory, and dataset weight auditing.
"""

import argparse
import glob
import os
import re
import sys
import ROOT

ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = ROOT.kError


def get_argset_names(argset):
    """Safely extracts names from a RooArgSet."""
    names = []
    if not argset:
        return names
    it = argset.createIterator()
    obj = it.Next()
    while obj:
        names.append(obj.GetName())
        obj = it.Next()
    return sorted(names)


def get_files(input_path):
    """Resolves input path into a list of ROOT files."""
    if os.path.isdir(input_path):
        return sorted(glob.glob(os.path.join(input_path, "CMS-HGG_sigfit_packaged*.root")))
    elif "*" in input_path:
        return sorted(glob.glob(input_path))
    elif os.path.isfile(input_path):
        return [input_path]
    return []


def run_summary(files, ws_name, mass_points, show_weights=False):
    """Prints mass point presence matrix (numEntries and optional sumEntries)."""
    print("\n" + "=" * 120)
    print("MASS POINT SUMMARY")
    print("=" * 120)

    header = f"{'File':<42} {'Category':<22} " + " ".join([f"{'m'+mp:<18}" for mp in mass_points])
    print(header)
    print("-" * 120)

    for fpath in files:
        fname = os.path.basename(fpath)
        cat = re.sub(r"^CMS-HGG_sigfit_packaged_", "", fname)
        cat = re.sub(r"\.root$", "", cat)

        f = ROOT.TFile.Open(fpath, "READ")
        if not f or f.IsZombie():
            print(f"{fname:<42} ERROR: Cannot open")
            continue

        ws = f.Get(ws_name)
        if not ws:
            print(f"{fname:<42} NO_WORKSPACE")
            f.Close()
            continue

        results = []
        for mp in mass_points:
            dname = f"sig_mass_m{mp}_{cat}"
            d = ws.data(dname)
            if d:
                if show_weights:
                    results.append(f"Y N:{d.numEntries()} W:{d.sumEntries():.1f}")
                else:
                    results.append(f"YES({d.numEntries()})")
            else:
                results.append("NO")

        print(f"{fname:<42} {cat:<22} " + " ".join([f"{res:<18}" for res in results]))
        f.Close()


def run_inventory(files, ws_name):
    """Prints count of datasets, PDFs, functions, and variables per file."""
    print("\n" + "=" * 120)
    print("WORKSPACE OBJECT INVENTORY")
    print("=" * 120)
    print(f"{'File':<42} {'Data':>6} {'PDFs':>6} {'Funcs':>6} {'Vars':>8}")
    print("-" * 120)

    for fpath in files:
        fname = os.path.basename(fpath)
        f = ROOT.TFile.Open(fpath, "READ")
        ws = f.Get(ws_name) if f else None

        if not ws:
            print(f"{fname:<42} NO_WORKSPACE")
            if f:
                f.Close()
            continue

        data_names = [d.GetName() for d in ws.allData()]
        pdf_names = get_argset_names(ws.allPdfs())
        func_names = get_argset_names(ws.allFunctions())
        var_names = get_argset_names(ws.allVars())

        print(f"{fname:<42} {len(data_names):>6} {len(pdf_names):>6} {len(func_names):>6} {len(var_names):>8}")

        print("\n  Datasets contained:")
        for dname in sorted(data_names):
            ds = ws.data(dname)
            n_entries = ds.numEntries() if ds else -1
            s_weights = ds.sumEntries() if ds else -1.0
            print(f"    - {dname:<70} Entries: {n_entries:<8} SumW: {s_weights:.2f}")
        print("-" * 120)
        f.Close()


def run_audit(files, ws_name):
    """Audits merged category dataset against sub-component datasets."""
    print("\n" + "=" * 120)
    print("SUB-COMPONENT DATASET AUDIT")
    print("=" * 120)

    for fpath in files:
        fname = os.path.basename(fpath)
        cat = re.sub(r"^CMS-HGG_sigfit_packaged_", "", fname)
        cat = re.sub(r"\.root$", "", cat)

        f = ROOT.TFile.Open(fpath, "READ")
        ws = f.Get(ws_name) if f else None

        if not ws:
            continue

        cat_dataset_name = f"sig_mass_m125_{cat}"
        merged = ws.data(cat_dataset_name)

        print(f"\n--- File: {fname} | Target: {cat_dataset_name} ---")

        if not merged:
            print(f"  Target dataset '{cat_dataset_name}' not found.")
            f.Close()
            continue

        m_entries = merged.numEntries()
        m_weight = merged.sumEntries()
        print(f"  Merged Target  -> Entries: {m_entries:<8} SumW: {m_weight:.3f}")

        comp_entries = 0
        comp_weight = 0.0
        matches = []
        found_components = 0

        for d in ws.allData():
            dname = d.GetName()
            if dname == cat_dataset_name:
                continue

            # Look for process component datasets matching category suffix
            if dname.endswith(f"_{cat}_13TeV") or dname.endswith(f"_{cat}"):
                found_components += 1
                entries = d.numEntries()
                weight = d.sumEntries()
                comp_entries += entries
                comp_weight += weight

                print(f"    Sub-component: {dname:<60} Entries: {entries:<8} SumW: {weight:.3f}")

                if entries == m_entries and abs(weight - m_weight) < 1e-5:
                    matches.append(dname)

        if found_components > 0:
            print(f"  Component Sum -> Entries: {comp_entries:<8} SumW: {comp_weight:.3f}")
            if matches:
                print(f"  Exact Single Match Found: {matches}")
        else:
            print("  No sub-component datasets found.")

        f.Close()


def main():
    parser = argparse.ArgumentParser(
        description="Comprehensive CMS-HGG ROOT Workspace Inspector.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i", "--input", type=str, default=".", help="Input directory, ROOT file, or glob pattern."
    )
    parser.add_argument(
        "-w", "--workspace", type=str, default="wsig_13TeV", help="Name of RooWorkspace object."
    )
    parser.add_argument(
        "-m", "--masses", nargs="+", default=["120", "125", "130"], help="Mass points to inspect."
    )
    parser.add_argument(
        "--weights", action="store_true", help="Include sumOfWeights in summary view."
    )
    parser.add_argument(
        "--inventory", action="store_true", help="Run workspace object count and dataset listing."
    )
    parser.add_argument(
        "--audit", action="store_true", help="Run dataset composition and component matching audit."
    )
    parser.add_argument(
        "--all", action="store_true", help="Run summary, inventory, and dataset audit together."
    )

    args = parser.parse_args()

    files = get_files(args.input)
    if not files:
        print(f"Error: No ROOT files found for path '{args.input}'")
        sys.exit(1)

    # Run summary by default or when explicitly requested
    if not (args.inventory or args.audit) or args.all:
        run_summary(files, args.workspace, args.masses, args.weights or args.all)

    if args.inventory or args.all:
        run_inventory(files, args.workspace)

    if args.audit or args.all:
        run_audit(files, args.workspace)


if __name__ == "__main__":
    main()
