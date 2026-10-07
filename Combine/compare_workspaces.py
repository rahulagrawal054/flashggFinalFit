#!/usr/bin/env python3
"""
compare_workspaces.py

Compare two Combine RooWorkspace ROOT files (e.g. a DCB workspace vs a SoG
workspace) and report what's different: variables, PDFs, categories
(pdfIndex), and POIs.

Usage:
    python3 compare_workspaces.py <fileA.root> <fileB.root> [--workspace w] [--verbose]

Designed to answer: "other than the signal-shape parameterization itself,
is everything else (categories, background PDFs, nuisance list, POI
definitions) actually identical between the two workspaces?"
"""

import argparse
import sys

import ROOT


def load_workspace(path, wsname):
    f = ROOT.TFile.Open(path)
    if not f or f.IsZombie():
        print(f"[ERROR] Could not open file: {path}", file=sys.stderr)
        sys.exit(1)
    w = f.Get(wsname)
    if not w:
        print(f"[ERROR] Workspace '{wsname}' not found in {path}", file=sys.stderr)
        print(f"        Keys in file: {[k.GetName() for k in f.GetListOfKeys()]}", file=sys.stderr)
        sys.exit(1)
    return f, w


def get_var_info(w):
    """Return {name: (value, lo, hi, is_constant)} for every RooRealVar."""
    info = {}
    it = w.allVars().createIterator()
    v = it.Next()
    while v:
        try:
            info[v.GetName()] = (
                round(v.getVal(), 6),
                round(v.getMin(), 6),
                round(v.getMax(), 6),
                v.isConstant(),
            )
        except Exception:
            info[v.GetName()] = (None, None, None, None)
        v = it.Next()
    return info


def get_cat_info(w):
    """Return {name: {label: index}} for every RooCategory (pdfIndex etc.)."""
    info = {}
    it = w.allCats().createIterator()
    c = it.Next()
    while c:
        states = {}
        state_it = c.typeIterator()
        s = state_it.Next()
        while s:
            states[s.GetName()] = s.getVal()
            s = state_it.Next()
        info[c.GetName()] = {"current": c.getLabel(), "states": states}
        c = it.Next()
    return info


def get_pdf_names(w):
    """Return {name: class_name} for every PDF in the workspace."""
    info = {}
    it = w.allPdfs().createIterator()
    p = it.Next()
    while p:
        info[p.GetName()] = p.ClassName()
        p = it.Next()
    return info


def classify_name(name, keywords):
    return any(k.lower() in name.lower() for k in keywords)


def diff_report(labelA, labelB, dictA, dictB, kind, signal_shape_keywords, verbose):
    keysA, keysB = set(dictA), set(dictB)
    only_a = keysA - keysB
    only_b = keysB - keysA
    common = keysA & keysB

    print(f"\n=== {kind}: {labelA} vs {labelB} ===")
    print(f"  Total in {labelA}: {len(keysA)}   Total in {labelB}: {len(keysB)}")

    def split_expected(names):
        expected = sorted(n for n in names if classify_name(n, signal_shape_keywords))
        unexpected = sorted(n for n in names if not classify_name(n, signal_shape_keywords))
        return expected, unexpected

    exp_a, unexp_a = split_expected(only_a)
    exp_b, unexp_b = split_expected(only_b)

    print(f"  Only in {labelA}: {len(only_a)}  "
          f"({len(exp_a)} look signal-shape-related, {len(unexp_a)} do NOT)")
    if unexp_a:
        print(f"    [FLAG] Unexpected-only-in-{labelA} (not signal-shape-looking):")
        for n in unexp_a:
            print(f"      - {n}")
    elif verbose and exp_a:
        print(f"    (signal-shape-related, expected): {exp_a[:10]}"
              f"{' ...' if len(exp_a) > 10 else ''}")

    print(f"  Only in {labelB}: {len(only_b)}  "
          f"({len(exp_b)} look signal-shape-related, {len(unexp_b)} do NOT)")
    if unexp_b:
        print(f"    [FLAG] Unexpected-only-in-{labelB} (not signal-shape-looking):")
        for n in unexp_b:
            print(f"      - {n}")
    elif verbose and exp_b:
        print(f"    (signal-shape-related, expected): {exp_b[:10]}"
              f"{' ...' if len(exp_b) > 10 else ''}")

    # For common entries, check if values actually differ (only meaningful for var dicts)
    if kind == "Variables":
        mismatched = []
        for n in sorted(common):
            if dictA[n] != dictB[n]:
                mismatched.append((n, dictA[n], dictB[n]))
        print(f"  Common variables with DIFFERENT value/range/const flag: {len(mismatched)}")
        if mismatched:
            unexpected_mismatch = [m for m in mismatched if not classify_name(m[0], signal_shape_keywords)]
            if unexpected_mismatch:
                print(f"    [FLAG] Non-signal-shape variables differing between workspaces:")
                for n, a, b in unexpected_mismatch[:30]:
                    print(f"      - {n}: {labelA}={a}  {labelB}={b}")
                if len(unexpected_mismatch) > 30:
                    print(f"      ... and {len(unexpected_mismatch) - 30} more")
            if verbose:
                sig_mismatch = [m for m in mismatched if classify_name(m[0], signal_shape_keywords)]
                if sig_mismatch:
                    print(f"    (signal-shape variables differing, expected): {len(sig_mismatch)} params")

    return only_a, only_b, common


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("fileA", help="First workspace ROOT file (e.g. DCB)")
    ap.add_argument("fileB", help="Second workspace ROOT file (e.g. SoG)")
    ap.add_argument("--labelA", default="A", help="Short label for fileA in output (e.g. DCB)")
    ap.add_argument("--labelB", default="B", help="Short label for fileB in output (e.g. SoG)")
    ap.add_argument("--workspace", default="w", help="Workspace object name (default: w)")
    ap.add_argument("--verbose", action="store_true", help="Also print expected/matching entries, not just flags")
    args = ap.parse_args()

    ROOT.gROOT.SetBatch(True)
    ROOT.gErrorIgnoreLevel = ROOT.kWarning

    fA, wA = load_workspace(args.fileA, args.workspace)
    fB, wB = load_workspace(args.fileB, args.workspace)

    print(f"Loaded {args.labelA}: {args.fileA}")
    print(f"Loaded {args.labelB}: {args.fileB}")

    # Keywords that identify parameters we EXPECT to differ purely because
    # the signal-shape parameterization is different (DCB vs SoG naming).
    signal_shape_keywords = [
        "dcb", "gaus", "sigma", "mean", "alpha", "cbn", "nCB", "frac",
        "sig_", "_sig", "signal", "MH", "dm", "mass_sig",
    ]

    var_a, var_b = get_var_info(wA), get_var_info(wB)
    pdf_a, pdf_b = get_pdf_names(wA), get_pdf_names(wB)
    cat_a, cat_b = get_cat_info(wA), get_cat_info(wB)

    diff_report(args.labelA, args.labelB, var_a, var_b, "Variables", signal_shape_keywords, args.verbose)
    diff_report(args.labelA, args.labelB, pdf_a, pdf_b, "PDFs", signal_shape_keywords, args.verbose)

    # Categories (pdfIndex etc.) -- these should be IDENTICAL between DCB and
    # SoG if only the signal shape changed; any difference here is a real flag.
    print(f"\n=== Categories / discrete indices: {args.labelA} vs {args.labelB} ===")
    keys_cat = set(cat_a) | set(cat_b)
    any_cat_diff = False
    for name in sorted(keys_cat):
        a = cat_a.get(name)
        b = cat_b.get(name)
        if a is None:
            print(f"  [FLAG] '{name}' only in {args.labelB} (missing from {args.labelA})")
            any_cat_diff = True
        elif b is None:
            print(f"  [FLAG] '{name}' only in {args.labelA} (missing from {args.labelB})")
            any_cat_diff = True
        elif a["current"] != b["current"]:
            print(f"  [FLAG] '{name}' selected different index: "
                  f"{args.labelA}={a['current']}  {args.labelB}={b['current']}")
            any_cat_diff = True
        elif args.verbose:
            print(f"  OK  '{name}': both = {a['current']}")
    if not any_cat_diff:
        print("  No differences found -- category/background-function selections match.")

    # POIs, if present as named sets
    print(f"\n=== Quick POI check ===")
    for poi_name in ["r_ttH", "r_tHq"]:
        va = var_a.get(poi_name)
        vb = var_b.get(poi_name)
        print(f"  {poi_name}: {args.labelA}={va}  {args.labelB}={vb}")

    print("\nDone. Review any [FLAG] lines above -- those are differences NOT "
          "explained by the signal-shape parameterization, and are worth "
          "investigating before trusting a DCB-vs-SoG comparison.")


if __name__ == "__main__":
    main()
