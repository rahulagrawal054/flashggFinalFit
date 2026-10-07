#!/usr/bin/env python3
"""
Yield calculator for H to γγ signal processes from flashggFinalFit ROOT trees.

Usage:
    python calc_yields.py
    python calc_yields.py --inputDir /path/to/inputs_27June --output yields.txt
"""

import uproot
import numpy as np
import argparse
import os
from collections import defaultdict


lumi_dict = {
    "2022preEE":    7.98,
    "2022postEE":  26.68,
    "2023preBPix": 17.96,
    "2023postBPix":  9.68,
}

# Cross sections in fb (already multiplied by BR(H→γγ) = 0.00227)
dict_cross_sections = {
    "GluGluH":  52.23e3  * 0.00227,
    "VBFH":      4.078e3 * 0.00227,
    "VH":        2.4009e3* 0.00227,
    "ttH":       0.5700e3* 0.00227,
    "tHqLep":   83.26    * 0.3258      * 0.00227,
    "tHqHad":   83.26    * (1-0.3258)  * 0.00227,
    "tHW":      17.2     * 0.00227,
    "bbH":       0.5269e3* 0.00227,
}

# Tree prefix inside DiphotonTree to maps process key to tree prefix
# Tree name format: <prefix>_125_13TeV_<category>
tree_prefix_map = {
    "GluGluH":  "ggh",
    "VBFH":     "vbf",
    "VH":       "vh",
    "ttH":      "tth",
    "tHqLep":   "tHqLep",   # tree: tHqLep_125_13TeV_<cat>
    "tHqHad":   "tHqHad",   # tree: tHqHad_125_13TeV_<cat>
    "tHW":      "tHW",    # tree: tHW_125_13TeV_<cat>
    "bbH":      "bbh",
}

# File map: (process_key, era) → root file path
file_map = {
    ("GluGluH",  "2022preEE"):    "inputs_27June/GluGluH_2022preEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root",
    ("GluGluH",  "2022postEE"):   "inputs_27June/GluGluH_2022postEE/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root",
    ("GluGluH",  "2023preBPix"):  "inputs_27June/GluGluH_2023preBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root",
    ("GluGluH",  "2023postBPix"): "inputs_27June/GluGluH_2023postBPix/output_GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8.root",

    ("VBFH",     "2022preEE"):    "inputs_27June/VBFH_2022preEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("VBFH",     "2022postEE"):   "inputs_27June/VBFH_2022postEE/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("VBFH",     "2023preBPix"):  "inputs_27June/VBFH_2023preBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("VBFH",     "2023postBPix"): "inputs_27June/VBFH_2023postBPix/output_VBFHToGG_M125_13TeV_amcatnlo_pythia8.root",

    ("VH",       "2022preEE"):    "inputs_27June/VH_2022preEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("VH",       "2022postEE"):   "inputs_27June/VH_2022postEE/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("VH",       "2023preBPix"):  "inputs_27June/VH_2023preBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("VH",       "2023postBPix"): "inputs_27June/VH_2023postBPix/output_VHToGG_M125_13TeV_amcatnlo_pythia8.root",

    ("ttH",      "2022preEE"):    "inputs_27June/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("ttH",      "2022postEE"):   "inputs_27June/ttH_2022postEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("ttH",      "2023preBPix"):  "inputs_27June/ttH_2023preBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root",
    ("ttH",      "2023postBPix"): "inputs_27June/ttH_2023postBPix/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root",

    ("tHqLep",   "2022preEE"):    "inputs_27June/tHqLep_2022preEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root",
    ("tHqLep",   "2022postEE"):   "inputs_27June/tHqLep_2022postEE/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root",
    ("tHqLep",   "2023preBPix"):  "inputs_27June/tHqLep_2023preBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root",
    ("tHqLep",   "2023postBPix"): "inputs_27June/tHqLep_2023postBPix/output_THQtoGG_lep_M125_13TeV_amcatnlo_pythia8.root",

    ("tHqHad",   "2022preEE"):    "inputs_27June/tHqHad_2022preEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root",
    ("tHqHad",   "2022postEE"):   "inputs_27June/tHqHad_2022postEE/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root",
    ("tHqHad",   "2023preBPix"):  "inputs_27June/tHqHad_2023preBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root",
    ("tHqHad",   "2023postBPix"): "inputs_27June/tHqHad_2023postBPix/output_THQtoGG_had_M125_13TeV_amcatnlo_pythia8.root",

    ("tHW",      "2022preEE"):    "inputs_27June/tHW_2022preEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root",
    ("tHW",      "2022postEE"):   "inputs_27June/tHW_2022postEE/output_THWtoGG_M125_13TeV_madgraph_pythia8.root",
    ("tHW",      "2023preBPix"):  "inputs_27June/tHW_2023preBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root",
    ("tHW",      "2023postBPix"): "inputs_27June/tHW_2023postBPix/output_THWtoGG_M125_13TeV_madgraph_pythia8.root",

    ("bbH",      "2022preEE"):    "inputs_27June/bbH_2022preEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root",
    ("bbH",      "2022postEE"):   "inputs_27June/bbH_2022postEE/output_BBHToGG_M125_13TeV_powheg_pythia8.root",
    ("bbH",      "2023preBPix"):  "inputs_27June/bbH_2023preBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root",
    ("bbH",      "2023postBPix"): "inputs_27June/bbH_2023postBPix/output_BBHToGG_M125_13TeV_powheg_pythia8.root",
}

# Your 16 categories
categories = [
    "ttH_had_1", "ttH_had_2", "ttH_had_3", "ttH_had_4",
    "ttH_lep_1", "ttH_lep_2", "ttH_lep_3", "ttH_lep_4",
    "tH_had_1",  "tH_had_2",  "tH_had_3",  "tH_had_4",
    "tH_lep_1",  "tH_lep_2",
    "bkg_had",   "bkg_lep",
]

# Processes to show in final table
# tHqLep + tHqHad are summed into tHq
processes_final = ["ttH", "tHq", "tHW", "GluGluH", "VBFH", "VH", "bbH"]


def get_tree_name(proc_key, cat):
    """Build tree name: <prefix>_125_13TeV_<cat>"""
    prefix = tree_prefix_map[proc_key]
    return f"DiphotonTree/{prefix}_125_13TeV_{cat}"


def load_weights(f, tree_name):
    """
    Load weight, fiducialGeometricFlag, GenNBJet from a tree.
    Returns (weight, fid_flag, nb_jet) as numpy arrays.
    Returns None if tree not found or empty.
    """
    try:
        tree = f[tree_name]
    except Exception:
        return None, None, None

    if tree.num_entries == 0:
        return None, None, None

    branches = tree.keys()

    weight = tree["weight"].array(library="np")

    fid_flag = None
    if "fiducialGeometricFlag" in branches:
        fid_flag = tree["fiducialGeometricFlag"].array(library="np").astype(bool)

    nb_jet = None
    if "GenNBJet" in branches:
        nb_jet = tree["GenNBJet"].array(library="np")

    return weight, fid_flag, nb_jet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputDir", default=".", help="Base directory containing inputs_27June")
    parser.add_argument("--output",   default="yields.txt", help="Output text file")
    args = parser.parse_args()

    # yields[(proc_key, cat)] = [sum_w_lumi_xsec, sum_w2_lumi2_xsec2]
    # for incl, in, out separately
    yields_incl = defaultdict(lambda: [0.0, 0.0])
    yields_in   = defaultdict(lambda: [0.0, 0.0])
    yields_out  = defaultdict(lambda: [0.0, 0.0])

    # Loop over all process × era combinations
    for (proc_key, era), rel_path in file_map.items():
        full_path = os.path.join(args.inputDir, rel_path) if args.inputDir != "." else rel_path
        lumi = lumi_dict[era]
        xsec = dict_cross_sections[proc_key]

        if not os.path.exists(full_path):
            print(f"  [SKIP] File not found: {full_path}")
            continue

        print(f"\nProcessing: {proc_key} / {era}")
        print(f"  File: {full_path}")
        print(f"  Lumi: {lumi} fb-1  |  XSec: {xsec:.4f} fb")

        try:
            f = uproot.open(full_path)
        except Exception as e:
            print(f"  [ERROR] Cannot open file: {e}")
            continue

        for cat in categories:
            tree_name = get_tree_name(proc_key, cat)
            weight, fid_flag, nb_jet = load_weights(f, tree_name)

            if weight is None:
                continue

            # yield = sum(w) * L * sigma
            sw   = float(np.sum(weight))
            sw2  = float(np.sum(weight**2))
            y    = sw   * lumi * xsec
            y2   = sw2  * (lumi * xsec)**2
            yields_incl[(proc_key, cat)][0] += y
            yields_incl[(proc_key, cat)][1] += y2

            # IN:  fiducialGeometricFlag == True AND GenNBJet > 0
            # OUT: complement
            if fid_flag is not None and nb_jet is not None:
                mask_in  = fid_flag & (nb_jet > 0)
                mask_out = ~mask_in

                sw_in   = float(np.sum(weight[mask_in]))
                sw2_in  = float(np.sum(weight[mask_in]**2))
                yields_in[(proc_key, cat)][0]  += sw_in  * lumi * xsec
                yields_in[(proc_key, cat)][1]  += sw2_in * (lumi * xsec)**2

                sw_out  = float(np.sum(weight[mask_out]))
                sw2_out = float(np.sum(weight[mask_out]**2))
                yields_out[(proc_key, cat)][0] += sw_out  * lumi * xsec
                yields_out[(proc_key, cat)][1] += sw2_out * (lumi * xsec)**2

            n_events = len(weight)
            y_val = sw * lumi * xsec
            print(f"    cat={cat:15s}  n_events={n_events:6d}  yield={y_val:.4f}")

        f.file.close()

    def merge_tHq(d):
        out = defaultdict(lambda: [0.0, 0.0])
        for (proc_key, cat), (s, s2) in d.items():
            p2 = "tHq" if proc_key in ("tHqLep", "tHqHad") else proc_key
            out[(p2, cat)][0] += s
            out[(p2, cat)][1] += s2
        return out

    yields_incl = merge_tHq(yields_incl)
    yields_in   = merge_tHq(yields_in)
    yields_out  = merge_tHq(yields_out)

    lines = []

    def add(line=""):
        print(line)
        lines.append(line)

    for label, ydict in [("INCLUSIVE", yields_incl), ("FIDUCIAL IN", yields_in), ("FIDUCIAL OUT", yields_out)]:

        add()
        add("=" * 100)
        add(f"  YIELD TABLE — {label}  (summed over all eras: 2022preEE + 2022postEE + 2023preBPix + 2023postBPix)")
        add("=" * 100)

        # Header
        header = f"{'Category':<18}" + "".join(f"  {p:>10}" for p in processes_final) + f"  {'TOTAL':>10}"
        add(header)
        add("-" * len(header))

        for cat in categories:
            row_vals = []
            total = 0.0
            for proc in processes_final:
                y, _ = ydict.get((proc, cat), [0.0, 0.0])
                row_vals.append(y)
                total += y
            row = f"{cat:<18}" + "".join(f"  {v:10.4f}" for v in row_vals) + f"  {total:10.4f}"
            add(row)

        # Column totals
        add("-" * len(header))
        col_totals = []
        grand_total = 0.0
        for proc in processes_final:
            ct = sum(ydict.get((proc, cat), [0.0, 0.0])[0] for cat in categories)
            col_totals.append(ct)
            grand_total += ct
        row = f"{'TOTAL':<18}" + "".join(f"  {v:10.4f}" for v in col_totals) + f"  {grand_total:10.4f}"
        add(row)

    # Save to file
    with open(args.output, "w") as fout:
        fout.write("\n".join(lines))
    print(f"\n --> Saved to: {args.output}")


if __name__ == "__main__":
    main()
