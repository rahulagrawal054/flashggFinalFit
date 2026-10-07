#!/usr/bin/env python3
"""
mplhep + uproot remake of the S+B model plotter.

Notes:
- This script plots from simple TH1 shapes read with uproot (no PyROOT).
- Provide a ROOT file with TH1 histograms for data, background, and signal
  (optionally split into components). Example naming conventions supported:
    - data_<cat>, bkg_<cat>, sig_<cat>
    - OR h_data_<cat>, h_bkg_<cat>, h_sig_<cat>
    - If --splitResonant is used:
        sig_top_<cat>, sig_thq_<cat>, [sig_res_<cat>]

Limitations vs. the original ROOT script:
- Reading directly from a RooWorkspace (e.g. 'w' in a Combine workspace) is not
  supported with uproot. You need a shapes ROOT file with TH1s. I can provide
  a small ROOT-based exporter on request.
- --saveToyYields/--doToyVeto and toy extraction are not implemented here. If you
  have a pickled toy yields DataFrame (from the original tool), pass it with
  --loadToyYields to draw bands.
"""

import argparse
import os
import math
import numpy as np
import pandas as pd
import uproot
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.plotter import plot_splusb_model


def _rebin_arrays(bin_edges, arrays, target_bins):
    """Rebin arrays to target_bins if the current bin count is an exact multiple."""
    n_old = len(bin_edges) - 1
    if target_bins <= 0 or n_old == target_bins or n_old % target_bins != 0:
        return bin_edges, arrays
    factor = n_old // target_bins
    new_edges = bin_edges[::factor]
    if len(new_edges) != target_bins + 1:
        new_edges = np.r_[new_edges, bin_edges[-1]]
    rebinned = []
    for arr in arrays:
        if arr is None:
            rebinned.append(None)
            continue
        arr_np = np.asarray(arr)
        if arr_np.size != n_old:
            rebinned.append(arr)
            continue
        rebinned.append(arr_np.reshape(target_bins, factor).sum(axis=1))
    return new_edges, rebinned


def _rebin_bands(bands, target_len):
    """Rebin bands by summing medians and adding deviations in quadrature."""
    n_old = len(bands["median"])
    if target_len <= 0 or n_old == target_len or n_old % target_len != 0:
        return bands
    factor = n_old // target_len
    med_old = np.asarray(bands["median"], dtype=float)
    up1_old = np.asarray(bands["up1"], dtype=float)
    dn1_old = np.asarray(bands["down1"], dtype=float)
    up2_old = np.asarray(bands["up2"], dtype=float)
    dn2_old = np.asarray(bands["down2"], dtype=float)

    def _sum_and_quad(arr, med):
        delta = arr - med
        med_new = med.reshape(target_len, factor).sum(axis=1)
        delta_new = np.sqrt((delta.reshape(target_len, factor) ** 2).sum(axis=1))
        return med_new, delta_new

    med_new = med_old.reshape(target_len, factor).sum(axis=1)
    _, du1 = _sum_and_quad(up1_old, med_old)
    _, dd1 = _sum_and_quad(dn1_old, med_old)
    _, du2 = _sum_and_quad(up2_old, med_old)
    _, dd2 = _sum_and_quad(dn2_old, med_old)

    return {
        "median": med_new,
        "up1": med_new + du1,
        "down1": med_new - dd1,
        "up2": med_new + du2,
        "down2": med_new - dd2,
    }


def parse_args():
    ap = argparse.ArgumentParser(description="S+B model plotter (mplhep + uproot)")
    ap.add_argument("--inputWSFile", required=True, help="Path to workspace or shapes ROOT file")
    ap.add_argument("--shapesFile", default=None, help="Explicit shapes ROOT file with TH1s (overrides inputWSFile)")
    ap.add_argument("--cats", default="all", help="Comma-separated category names or 'all'")
    ap.add_argument("--unblind", action="store_true", help="Unblind signal region")
    ap.add_argument("--blindingRegion", default="116,134", help="Comma-separated blinded region: low,high")
    ap.add_argument("--doZeroes", action="store_true", help="Give zero bins unit error to show markers")
    ap.add_argument("--ext", default="", help="Extension tag for outputs (subdirectory and filename prefix)")
    ap.add_argument("--xvar", default="CMS_hgg_mass,m_{#gamma#gamma},GeV", help="name,title,units; only name is used in filenames")
    ap.add_argument("--nBins", type=int, default=80, help="Number of bins (used to validate shapes and bands)")
    ap.add_argument("--translateCats", default=None, help="JSON mapping for category labels")
    ap.add_argument("--doBands", action="store_true", help="Draw ±1σ/±2σ bands from toy yields")
    ap.add_argument("--loadToyYields", default="", help="Pickle file with toy yields DataFrame (from original tool)")
    ap.add_argument("--splitResonant", action="store_true", help="Split signal into (top,thq,resonant)")
    ap.add_argument("--topPOIs", default="r_ttH", help="Unused here (kept for CLI parity)")
    ap.add_argument("--thqPOIs", default="r_tHq", help="Unused here (kept for CLI parity)")
    ap.add_argument("--topScale", type=float, default=1.0, help="Visual scale factor for ttH+tHW component")
    ap.add_argument("--thqScale", type=float, default=5.0, help="Visual scale factor for tHq component")
    ap.add_argument(
        "--splitLabels",
        default=None,
        help="Legend labels for split components (comma-separated). If omitted, labels are built from scale factors.",
    )
    return ap.parse_args()


def load_translations(path):
    if not path:
        return {}
    import json
    with open(path) as f:
        return json.load(f)


def _with_suffix(path, suffix):
    base, ext = os.path.splitext(path)
    if not ext:
        return path + suffix
    return base + suffix + ext


def _plot_with_cms_variants(**kwargs):
    kwargs.setdefault("y_label", "Events")
    outname = kwargs["output_filename"]
    plot_splusb_model(**kwargs, cms_label_style="mplhep")
    plot_splusb_model(**{**kwargs, "output_filename": _with_suffix(outname, "_noCMS")}, cms_label_style="plain")


def _format_scaled_label(base_label, scale):
    if scale is None:
        return base_label
    if math.isclose(scale, 1.0):
        return base_label
    return f"{base_label} \\times {scale:g}"


def _build_split_labels(opt):
    if opt.splitLabels:
        return [s.strip() for s in opt.splitLabels.split(",")]
    top_label = _format_scaled_label(r"$t\\bar{t}H + tHW$", opt.topScale)
    thq_label = _format_scaled_label(r"$tH$", opt.thqScale)
    return [top_label, thq_label, "Resonant bkg."]


def discover_categories_and_components(file):
    """Scan TH1 keys and infer available categories and components.

    Supports names like data_<cat>, bkg_<cat>, sig_<cat>, sig_top_<cat>, sig_thq_<cat>, sig_res_<cat>.
    Returns (categories, components) where components is a set of component tags found.
    """
    keys = [k.decode() if isinstance(k, bytes) else k for k in file.keys()]
    # uproot v5 returns keys like 'hname;1' — strip ';N'
    def hname(k):
        return k.split(";")[0]

    names = [hname(k) for k in keys]
    def base_cat(s):
        # Strip RooFit suffix like '__CMS_hgg_mass' from category fragments
        return s.split("__")[0]
    cats = set()
    comps = set()
    for n in names:
        for pref in ("data_", "h_data_"):
            if n.startswith(pref):
                cats.add(base_cat(n[len(pref):]))
        for pref in ("bkg_", "h_bkg_", "b_", "h_b_"):
            if n.startswith(pref):
                cats.add(base_cat(n[len(pref):]))
        for pref in ("sig_", "h_sig_"):
            if n.startswith(pref):
                rest = n[len(pref):]
                # Could be 'top_<cat>' or '<cat>'
                if rest.startswith("top_"):
                    comps.add("top")
                    cats.add(base_cat(rest[len("top_"):]))
                elif rest.startswith("thq_"):
                    comps.add("thq")
                    cats.add(base_cat(rest[len("thq_"):]))
                elif rest.startswith("res_") or rest.startswith("resonant_"):
                    comps.add("res")
                    cat = rest.split("_", 1)[1]
                    cats.add(base_cat(cat))
                else:
                    cats.add(base_cat(rest))
    return sorted(cats), comps


def get_th1(file, name):
    """Fetch TH1 by base name, allowing RooFit-style suffixes like '__CMS_hgg_mass'."""
    for k in file.keys():
        base = k.split(";")[0]
        if base == name or base.startswith(name + "__"):
            return file[base]
    return None


def read_shapes_for_category(f, cat, split=False):
    """Return (bin_edges, data, bkg, sig) or (bin_edges, data, bkg, sig_total, (top, thq, res)).

    Accept several naming patterns. Raises if required shapes are missing.
    """
    # Accept multiple prefixes; normalize category (strip suffixes)
    cat_base = cat.split("__")[0]
    # Accept multiple prefixes
    data = None
    for nm in (f"data_{cat}", f"h_data_{cat}", f"data_{cat_base}", f"h_data_{cat_base}"):
        h = get_th1(f, nm)
        if h is not None:
            data = h
            break
    if data is None:
        raise FileNotFoundError(f"No data TH1 found for category '{cat}'")

    bkg = None
    for nm in (
        f"bkg_{cat}", f"h_bkg_{cat}", f"b_{cat}", f"h_b_{cat}",
        f"bkg_{cat_base}", f"h_bkg_{cat_base}", f"b_{cat_base}", f"h_b_{cat_base}"
    ):
        h = get_th1(f, nm)
        if h is not None:
            bkg = h
            break
    if bkg is None:
        raise FileNotFoundError(f"No background TH1 found for category '{cat}'")

    # Edges from one of the histograms (uproot v5 TH1 interface)
    if hasattr(data, "axis"):
        edges = data.axis().edges()  # some uproot models
    else:
        edges = data.axes[0].edges()
    data_vals = data.values(flow=False)
    bkg_vals = bkg.values(flow=False)
    sig_total = None
    for nm in (f"sig_{cat}", f"h_sig_{cat}", f"sig_{cat_base}", f"h_sig_{cat_base}"):
        h = get_th1(f, nm)
        if h is not None:
            sig_total = h.values(flow=False)
            break

    if split:
        # Top / thq optional resonant
        top = None
        thq = None
        res = None
        for nm in (f"sig_top_{cat}", f"h_sig_top_{cat}", f"sig_top_{cat_base}", f"h_sig_top_{cat_base}"):
            h = get_th1(f, nm)
            if h is not None:
                top = h.values(flow=False)
                break
        for nm in (f"sig_thq_{cat}", f"h_sig_thq_{cat}", f"sig_thq_{cat_base}", f"h_sig_thq_{cat_base}"):
            h = get_th1(f, nm)
            if h is not None:
                thq = h.values(flow=False)
                break
        for nm in (
            f"sig_res_{cat}", f"h_sig_res_{cat}", f"sig_resonant_{cat}",
            f"sig_res_{cat_base}", f"h_sig_res_{cat_base}", f"sig_resonant_{cat_base}"
        ):
            h = get_th1(f, nm)
            if h is not None:
                res = h.values(flow=False)
                break
        if top is None and thq is None and res is None:
            raise FileNotFoundError(
                f"--splitResonant set but no split signal components found for '{cat}'"
            )
        if sig_total is None:
            raise FileNotFoundError(f"No total signal TH1 found for category '{cat}'")
        return edges, data_vals, bkg_vals, sig_total, (top, thq, res)
    else:
        if sig_total is None:
            raise FileNotFoundError(f"No signal TH1 found for category '{cat}'")
        return edges, data_vals, bkg_vals, sig_total


def _toy_matrix(df, category):
    """Return toy matrix shape (n_toys, n_bins) for a category; bins must be contiguous starting at 1."""
    cols = [c for c in df.columns if c.startswith(f"{category}_")]
    if not cols:
        raise KeyError(f"Toy yields missing columns for category '{category}'")
    # sort by bin index
    pairs = []
    for c in cols:
        tail = c.split("_")[-1]
        if tail.isdigit():
            pairs.append((int(tail), c))
    pairs = sorted(pairs, key=lambda x: x[0])
    max_bin = pairs[-1][0]
    # expect contiguous bins 1..max_bin
    for i, (idx, _) in enumerate(pairs, start=1):
        if idx != i:
            raise KeyError(f"Toy yields missing bin {i} for category '{category}'")
    matrix = np.stack([df[c].values for _, c in pairs], axis=1)
    return matrix


def _rebin_toy_matrix(mat, target_bins):
    n_toys, n_old = mat.shape
    if target_bins <= 0 or n_old == target_bins:
        return mat
    if n_old % target_bins != 0:
        raise ValueError(f"Cannot rebin toys: {n_old} bins to {target_bins} (not divisible).")
    factor = n_old // target_bins
    return mat.reshape(n_toys, target_bins, factor).sum(axis=2)


def compute_bands_from_toys(df, category, n_bins):
    """Compute toy percentiles; supports rebinning by exact factors."""
    from math import erf, sqrt
    p_up1 = 50 * (1 + erf(1.0 / sqrt(2)))
    p_dn1 = 50 * (1 + erf(-1.0 / sqrt(2)))
    p_up2 = 50 * (1 + erf(2.0 / sqrt(2)))
    p_dn2 = 50 * (1 + erf(-2.0 / sqrt(2)))

    mat = _toy_matrix(df, category)
    mat = _rebin_toy_matrix(mat, n_bins)

    med = np.median(mat, axis=0)
    up1 = np.percentile(mat, p_up1, axis=0)
    dn1 = np.percentile(mat, p_dn1, axis=0)
    up2 = np.percentile(mat, p_up2, axis=0)
    dn2 = np.percentile(mat, p_dn2, axis=0)
    return {
        "median": med,
        "up1": up1,
        "down1": dn1,
        "up2": up2,
        "down2": dn2,
    }


def compute_weighted_bands_from_toys(df, weights, n_bins):
    """Compute toy bands for a weighted sum over categories; supports rebinning."""
    if df is None or not weights:
        return None
    from math import erf, sqrt
    p_up1 = 50 * (1 + erf(1.0 / sqrt(2)))
    p_dn1 = 50 * (1 + erf(-1.0 / sqrt(2)))
    p_up2 = 50 * (1 + erf(2.0 / sqrt(2)))
    p_dn2 = 50 * (1 + erf(-2.0 / sqrt(2)))

    accum = None
    target_bins = n_bins
    for cat, w in weights.items():
        if w == 0:
            continue
        mat = _toy_matrix(df, cat)
        if mat.shape[1] != target_bins:
            mat = _rebin_toy_matrix(mat, target_bins)
        mat = mat * w
        if accum is None:
            accum = mat
        else:
            accum = accum + mat
    if accum is None:
        return None

    med = np.median(accum, axis=0)
    up1 = np.percentile(accum, p_up1, axis=0)
    dn1 = np.percentile(accum, p_dn1, axis=0)
    up2 = np.percentile(accum, p_up2, axis=0)
    dn2 = np.percentile(accum, p_dn2, axis=0)
    return {
        "median": med,
        "up1": up1,
        "down1": dn1,
        "up2": up2,
        "down2": dn2,
    }


def _soversb_weight(bin_edges, sig_vals, bkg_vals, res_vals=None, frac=0.68):
    """Compute per-category weight w = S/(S+B) in the smallest contiguous window containing `frac` of the signal."""
    if sig_vals is None or np.sum(sig_vals) <= 0:
        return 0.0, (0, 0)

    sig = np.asarray(sig_vals, dtype=float)
    bkg = np.asarray(bkg_vals, dtype=float)
    res = np.zeros_like(bkg) if res_vals is None else np.asarray(res_vals, dtype=float)

    total = sig.sum()
    target = frac * total
    csum = np.r_[0.0, np.cumsum(sig)]
    n = len(sig)
    best_width = np.inf
    best_pair = (0, n)

    for i in range(n):
        need = csum[i] + target
        j = np.searchsorted(csum, need, side="left")
        if j <= i or j > n:
            continue
        width = bin_edges[j] - bin_edges[i]
        if width < best_width:
            best_width = width
            best_pair = (i, j)

    start, end = best_pair
    s_window = sig[start:end].sum()
    b_window = (bkg[start:end] + res[start:end]).sum()
    denom = s_window + b_window
    w = s_window / denom if denom > 0 else 0.0
    w = np.log(1 + s_window/b_window) if b_window > 0 else 1.0
    return w, best_pair


def main():
    opt = parse_args()

    # Where to read shapes
    shapes_path = opt.shapesFile or opt.inputWSFile
    if not os.path.isfile(shapes_path):
        raise FileNotFoundError(f"Shapes file not found: {shapes_path}")

    # Try to open with uproot
    f = uproot.open(shapes_path)

    # If a RooWorkspace is present and no TH1s, we can't proceed without an exporter
    # We try to discover categories from TH1 keys
    cats_discovered, comps = discover_categories_and_components(f)
    if len(cats_discovered) == 0:
        raise RuntimeError(
            "No TH1 histograms found in shapes file. If you passed a RooWorkspace, "
            "please provide a shapes ROOT file with TH1s (data/bkg/sig per category)."
        )

    # Categories to process
    if opt.cats == "all":
        cats = cats_discovered
    else:
        cats = [c.strip() for c in opt.cats.split(",") if c.strip()]

    translate_cats = load_translations(opt.translateCats) if opt.translateCats else {}

    def human_readable_category(cat):
        # Prefer translation JSON if provided
        if cat in translate_cats:
            return translate_cats[cat]
        c = cat
        label = c
        try:
            parts = c.split("_")
            head = parts[0]
            rest = parts[1:]
            if head == "tH":
                head_lbl = "$tH$"
            elif head == "ttH":
                head_lbl = "ttH"
            else:
                head_lbl = head
            # replace had/lep
            rest_lbl = []
            for p in rest:
                if p == "had":
                    rest_lbl.append("had.")
                elif p == "lep":
                    rest_lbl.append("lep.")
                else:
                    rest_lbl.append(p)
            label = f"{head_lbl} {' '.join(rest_lbl)}"
        except Exception:
            pass
        return label
    blinded = tuple(float(x) for x in opt.blindingRegion.split(","))
    xvar_name = opt.xvar.split(",")[0]
    split_labels = _build_split_labels(opt)

    # Optional toy yields for bands
    toy_df = None
    if opt.doBands:
        if opt.loadToyYields:
            toy_df = pd.read_pickle(opt.loadToyYields)
        else:
            print("[warn] --doBands set but no --loadToyYields provided; skipping bands.")

    base_outdir = f"./SplusBModels{opt.ext}"
    outdir = os.path.join(base_outdir, "plots")
    os.makedirs(outdir, exist_ok=True)

    # Process categories and optionally build a sum
    have_split = bool(opt.splitResonant)
    summed = None  # to store running sums for 'all'
    summed_split = None
    bin_edges_ref = None
    weighted_ttH = None
    weighted_tHq = None
    weight_map_ttH = {}
    weight_map_tHq = {}

    for cat in cats:
        if have_split:
            edges, data, bkg, sig_total, split = read_shapes_for_category(f, cat, split=True)
            top, thq, res = split
            edges, (data, bkg, sig_total, top, thq, res) = _rebin_arrays(edges, [data, bkg, sig_total, top, thq, res], opt.nBins)
            # Keep unscaled copies for ratio panel
            top_unscaled = None if top is None else top.copy()
            thq_unscaled = None if thq is None else thq.copy()
            res_unscaled = None if res is None else res.copy()
            sig_model = sig_total.copy()
            if res_unscaled is not None:
                sig_model = sig_model - res_unscaled
            # Compute per-category S/(S+B) weights (unscaled)
            w_ttH, _ = _soversb_weight(edges, top_unscaled, bkg, res_unscaled)
            w_tHq, _ = _soversb_weight(edges, thq_unscaled, bkg, res_unscaled)
            print(f"Category '{cat}': S/(S+B) weights: ttH+tHW = {w_ttH:.4f}, tHq = {w_tHq:.4f}")
            weight_map_ttH[cat] = w_ttH
            weight_map_tHq[cat] = w_tHq
            if w_ttH > 0:
                if weighted_ttH is None:
                    weighted_ttH = {
                        "data": np.zeros_like(data),
                        "data_var": np.zeros_like(data),
                        "bkg": np.zeros_like(bkg),
                        "sig_top": np.zeros_like(bkg) if top_unscaled is not None else None,
                        "sig_thq": np.zeros_like(bkg) if thq_unscaled is not None else None,
                        "sig_res": np.zeros_like(bkg) if res_unscaled is not None else None,
                        "sig_model": np.zeros_like(bkg),
                    }
                weighted_ttH["data"] += w_ttH * data
                weighted_ttH["data_var"] += (w_ttH ** 2) * data
                weighted_ttH["bkg"] += w_ttH * (bkg + (res_unscaled if res_unscaled is not None else 0))
                if weighted_ttH["sig_top"] is not None and top_unscaled is not None:
                    weighted_ttH["sig_top"] += w_ttH * top_unscaled
                if weighted_ttH["sig_thq"] is not None and thq_unscaled is not None:
                    weighted_ttH["sig_thq"] += w_ttH * thq_unscaled
                if weighted_ttH["sig_res"] is not None and res_unscaled is not None:
                    weighted_ttH["sig_res"] += w_ttH * res_unscaled
                weighted_ttH["sig_model"] += w_ttH * sig_model
            if w_tHq > 0:
                if weighted_tHq is None:
                    weighted_tHq = {
                        "data": np.zeros_like(data),
                        "data_var": np.zeros_like(data),
                        "bkg": np.zeros_like(bkg),
                        "sig_top": np.zeros_like(bkg) if top_unscaled is not None else None,
                        "sig_thq": np.zeros_like(bkg) if thq_unscaled is not None else None,
                        "sig_res": np.zeros_like(bkg) if res_unscaled is not None else None,
                        "sig_model": np.zeros_like(bkg),
                    }
                weighted_tHq["data"] += w_tHq * data
                weighted_tHq["data_var"] += (w_tHq ** 2) * data
                weighted_tHq["bkg"] += w_tHq * (bkg + (res_unscaled if res_unscaled is not None else 0))
                if weighted_tHq["sig_top"] is not None and top_unscaled is not None:
                    weighted_tHq["sig_top"] += w_tHq * top_unscaled
                if weighted_tHq["sig_thq"] is not None and thq_unscaled is not None:
                    weighted_tHq["sig_thq"] += w_tHq * thq_unscaled
                if weighted_tHq["sig_res"] is not None and res_unscaled is not None:
                    weighted_tHq["sig_res"] += w_tHq * res_unscaled
                weighted_tHq["sig_model"] += w_tHq * sig_model
            # Apply visual scales
            if top is not None:
                top = opt.topScale * top
            if thq is not None:
                thq = opt.thqScale * thq
            sig_for_sum = sig_model.copy()
        else:
            edges, data, bkg, sig = read_shapes_for_category(f, cat, split=False)
            edges, (data, bkg, sig) = _rebin_arrays(edges, [data, bkg, sig], opt.nBins)
            split = None
            sig_for_sum = sig

        # Bands for this category (optional)
        bands = None
        if toy_df is not None:
            bands = compute_bands_from_toys(toy_df, cat, opt.nBins)
            if bands is not None and len(bands["median"]) != len(bkg):
                bands = _rebin_bands(bands, len(bkg))

        # Title/label for category (display on right under legend)
        title_right = None

        # Output path
        outname = os.path.join(outdir, f"{opt.ext}_{cat}_{xvar_name}.pdf")

        # Plot
        if have_split:
            _plot_with_cms_variants(
                bin_edges=edges,
                data_vals=data,
                bkg_vals=bkg,
                sig_vals=sig_model,
                sig_split=(top, thq, res),
                ratio_sig_split=(top_unscaled, thq_unscaled, res_unscaled),
                bands=bands,
                blinded_region=blinded,
                unblind=opt.unblind,
                output_filename=outname,
                split_labels=split_labels,
                cms_label="Private Work",
                lumi=62.4,
                title_right=title_right,
                title_left=None,
                xlim=(100, 180),
                hide_zero_points=not opt.doZeroes,
                figure_layout=0.48,
            )
        else:
            _plot_with_cms_variants(
                bin_edges=edges,
                data_vals=data,
                bkg_vals=bkg,
                sig_vals=sig_for_sum,
                sig_split=None,
                bands=bands,
                blinded_region=blinded,
                unblind=opt.unblind,
                output_filename=outname,
                split_labels=split_labels,
                cms_label="Private Work",
                lumi=62.4,
                title_right=title_right,
                title_left=None,
                xlim=(100, 180),
                figure_layout=0.48,
            )

        # Accumulate for sum plot
        if summed is None:
            bin_edges_ref = edges
            summed = {
                "data": data.copy(),
                "bkg": bkg.copy(),
                "sig": sig_for_sum.copy(),
            }
            if have_split:
                summed_split = {
                    "top": np.zeros_like(bkg) if top is not None else None,
                    "thq": np.zeros_like(bkg) if thq is not None else None,
                    "res": np.zeros_like(bkg) if res is not None else None,
                }
                if top is not None:
                    summed_split["top"] += top
                if thq is not None:
                    summed_split["thq"] += thq
                if res is not None:
                    summed_split["res"] += res
        else:
            # Ensure same binning
            if not np.allclose(bin_edges_ref, edges):
                raise ValueError("All categories must share identical binning for the sum plot.")
            summed["data"] += data
            summed["bkg"] += bkg
            summed["sig"] += sig_for_sum
            if have_split and summed_split is not None:
                if top is not None and summed_split["top"] is not None:
                    summed_split["top"] += top
                if thq is not None and summed_split["thq"] is not None:
                    summed_split["thq"] += thq
                if res is not None and summed_split["res"] is not None:
                    summed_split["res"] += res

    # Sum plot (for 'all')
    if len(cats) > 1 or (len(cats) == 1 and cats[0].lower() == "all"):
        if summed is not None:
            data = summed["data"]
            bkg = summed["bkg"]
            sig = summed["sig"]
            bands = None
            if toy_df is not None:
                # In toy pickle from original tool, the sum columns were named 'sum_<ibin>' or 'wsum_<ibin>'.
                # Try 'sum' first.
                try:
                    bands = compute_bands_from_toys(toy_df, "sum", opt.nBins)
                except Exception:
                    pass
            outname = os.path.join(outdir, f"{opt.ext}_all_{xvar_name}.pdf")
            if have_split and summed_split is not None:
                _plot_with_cms_variants(
                    bin_edges=bin_edges_ref,
                    data_vals=data,
                    bkg_vals=bkg,
                    sig_vals=sig,
                    sig_split=(
                        summed_split.get("top"),
                        summed_split.get("thq"),
                        summed_split.get("res"),
                    ),
                    ratio_sig_split=(
                        summed_split.get("top"),
                        summed_split.get("thq"),
                        summed_split.get("res"),
                    ),
                    bands=bands,
                    blinded_region=tuple(float(x) for x in opt.blindingRegion.split(",")),
                    unblind=opt.unblind,
                    output_filename=outname,
                    split_labels=split_labels,
                    cms_label="Private Work",
                    lumi=62.4,
                    title_right=None,
                    title_left=None,
                    xlim=(100, 180),
                    hide_zero_points=not opt.doZeroes,
                    figure_layout=0.48,
                )
            else:
                _plot_with_cms_variants(
                    bin_edges=bin_edges_ref,
                    data_vals=data,
                    bkg_vals=bkg,
                    sig_vals=sig,
                    sig_split=None,
                    bands=bands,
                    blinded_region=tuple(float(x) for x in opt.blindingRegion.split(",")),
                    unblind=opt.unblind,
                    output_filename=outname,
                    split_labels=split_labels,
                    cms_label="Private Work",
                    lumi=61.9,
                    title_right=None,
                    title_left=None,
                    xlim=(100, 180),
                    hide_zero_points=not opt.doZeroes,
                    figure_layout=0.48,
                )

    # S/(S+B) weighted combined plots
    if have_split and bin_edges_ref is not None:
        if weighted_ttH is not None and (weighted_ttH.get("sig_top") is not None or weighted_ttH.get("sig_thq") is not None):
            out_ttH = os.path.join(outdir, f"{opt.ext}_all_weighted_ttH_{xvar_name}.pdf")
            sig_ttH_scaled = opt.topScale * weighted_ttH["sig_top"] if weighted_ttH.get("sig_top") is not None else None
            sig_tHq_scaled = opt.thqScale * weighted_ttH["sig_thq"] if weighted_ttH.get("sig_thq") is not None else None
            sig_res_scaled = weighted_ttH.get("sig_res")
            data_err_ttH = np.sqrt(weighted_ttH.get("data_var", np.zeros_like(weighted_ttH["data"])))
            bands_ttH = None
            if toy_df is not None:
                bands_ttH = compute_weighted_bands_from_toys(toy_df, weight_map_ttH, opt.nBins)
            _plot_with_cms_variants(
                bin_edges=bin_edges_ref,
                data_vals=weighted_ttH["data"],
                bkg_vals=weighted_ttH["bkg"],
                sig_vals=weighted_ttH["sig_model"],
                sig_split=(sig_ttH_scaled, sig_tHq_scaled, sig_res_scaled),
                ratio_sig_split=(weighted_ttH.get("sig_top"), weighted_ttH.get("sig_thq"), weighted_ttH.get("sig_res")),
                bands=bands_ttH,
                data_err=data_err_ttH,
                blinded_region=tuple(float(x) for x in opt.blindingRegion.split(",")),
                unblind=opt.unblind,
                output_filename=out_ttH,
                split_labels=(split_labels[0], split_labels[1] if len(split_labels) > 1 else "tH", "Resonant bkg."),
                cms_label="Private Work",
                lumi=62.4,
                title_right=r"ln$(1+S/B)$ weighted ($S=t\bar tH+tHW$)",
                title_left=None,
                xlim=(100, 180),
                hide_zero_points=not opt.doZeroes,
                y_label="Weighted events",
                figure_layout=0.48,
                bkg_includes_resonant=True,
                show_resonant_legend=False,
            )
        if weighted_tHq is not None and (weighted_tHq.get("sig_top") is not None or weighted_tHq.get("sig_thq") is not None):
            out_tHq = os.path.join(outdir, f"{opt.ext}_all_weighted_tHq_{xvar_name}.pdf")
            sig_ttH_scaled = opt.topScale * weighted_tHq["sig_top"] if weighted_tHq.get("sig_top") is not None else None
            sig_thq_scaled = opt.thqScale * weighted_tHq["sig_thq"] if weighted_tHq.get("sig_thq") is not None else None
            sig_res_scaled = weighted_tHq.get("sig_res")
            data_err_tHq = np.sqrt(weighted_tHq.get("data_var", np.zeros_like(weighted_tHq["data"])))
            bands_tHq = None
            if toy_df is not None:
                bands_tHq = compute_weighted_bands_from_toys(toy_df, weight_map_tHq, opt.nBins)
            _plot_with_cms_variants(
                bin_edges=bin_edges_ref,
                data_vals=weighted_tHq["data"],
                bkg_vals=weighted_tHq["bkg"],
                sig_vals=weighted_tHq["sig_model"],
                sig_split=(sig_ttH_scaled, sig_thq_scaled, sig_res_scaled),
                ratio_sig_split=(weighted_tHq.get("sig_top"), weighted_tHq.get("sig_thq"), weighted_tHq.get("sig_res")),
                bands=bands_tHq,
                data_err=data_err_tHq,
                blinded_region=tuple(float(x) for x in opt.blindingRegion.split(",")),
                unblind=opt.unblind,
                output_filename=out_tHq,
            split_labels=(split_labels[0], split_labels[1] if len(split_labels) > 1 else "tH", "Resonant bkg."),
                cms_label="Private Work",
                lumi=62.4,
                title_right=r"ln$(1+S/B)$ weighted ($S=tH$)",
                title_left=None,
                xlim=(100, 180),
                hide_zero_points=not opt.doZeroes,
                y_label="Weighted events",
                figure_layout=0.48,
                bkg_includes_resonant=True,
                show_resonant_legend=False,
            )


if __name__ == "__main__":
    main()

