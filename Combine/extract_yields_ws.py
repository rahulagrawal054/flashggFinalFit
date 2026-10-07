#!/usr/bin/env python3
"""
Extract signal yields + background at 125 GeV from final datacard workspace.
Produces LaTeX table in Run 2 style (Table 13 equivalent).

Usage:
    python extract_yields_ws.py -i Datacard_fiducial_allCats_r_2D_fiducial.root
"""

import pandas as pd
import ROOT
import re
import sys
import numpy as np
from optparse import OptionParser
from collections import defaultdict

def get_options():
    parser = OptionParser()
    parser.add_option("-i", "--inputWS",   dest="inputWS",   default="", help="Input RooWorkspace (datacard .root)")
    parser.add_option("-o", "--outputTex", dest="outputTex", default="yield_table.tex", help="Output LaTeX file")
    return parser.parse_args()
(opt, args) = get_options()

# Process name mapping
def proc_to_short(p):
    pl = p.lower()
    if   "tth" in pl: return "ttH"
    elif "thq" in pl: return "tHq"
    elif "thw" in pl: return "tHW"
    elif "ggh" in pl or "glugluh" in pl: return "ggH"
    elif "qqh" in pl or "vbf" in pl:     return "VBF"
    elif "wh"  in pl: return "WH"
    elif "zh"  in pl: return "ZH"
    elif "bbh" in pl: return "bbH"
    else:             return p

proc_order = ["ttH", "tHq", "tHW", "ggH", "VBF", "WH", "ZH", "bbH"]

cat_display = {
    "ttH_had_1": r"$t\bar{t}$H Had 1",
    "ttH_had_2": r"$t\bar{t}$H Had 2",
    "ttH_had_3": r"$t\bar{t}$H Had 3",
    "ttH_had_4": r"$t\bar{t}$H Had 4",
    "ttH_lep_1": r"$t\bar{t}$H Lep 1",
    "ttH_lep_2": r"$t\bar{t}$H Lep 2",
    "ttH_lep_3": r"$t\bar{t}$H Lep 3",
    "ttH_lep_4": r"$t\bar{t}$H Lep 4",
    "tH_had_1":  r"$tH$ Had 1",
    "tH_had_2":  r"$tH$ Had 2",
    "tH_had_3":  r"$tH$ Had 3",
    "tH_had_4":  r"$tH$ Had 4",
    "tH_lep_1":  r"$tH$ Lep 1",
    "tH_lep_2":  r"$tH$ Lep 2",
    "bkg_had":   r"Bkg Had",
    "bkg_lep":   r"Bkg Lep",
}
cats = list(cat_display.keys())

def rooiter(x):
    it = x.iterator()
    r  = it.Next()
    while r:
        yield r
        r = it.Next()

print(f" --> Opening: {opt.inputWS}")
f  = ROOT.TFile(opt.inputWS)
ws = None
for wsname in ["w", "w_all", "workspace"]:
    ws = f.Get(wsname)
    if ws:
        print(f" --> Workspace: {wsname}")
        break
if not ws:
    print("[ERROR] workspace not found"); sys.exit(1)

columns = ['proc', 'proc_short', 'cat', 'yield']
data    = pd.DataFrame(columns=columns)

allNorms = ws.allFunctions().selectByName("n_exp_final*")
for func in rooiter(allNorms):
    name = func.GetName()
    if "bkg_mass" in name: continue
    try:
        cat        = name.split("_proc_")[0].split("bin")[-1]
        proc       = name.split("_proc_")[-1]
        proc_short = proc_to_short(proc)
        yld        = func.getVal()
        data.loc[len(data)] = [proc, proc_short, cat, yld]
    except Exception:
        continue

print(f" --> {len(data)} signal normalisations found.")
print(f"     Cats:  {sorted(data['cat'].unique())}")
print(f"     Procs: {sorted(data['proc_short'].unique())}")

procs_present = [p for p in proc_order if p in data['proc_short'].values]
pivot = data.groupby(['cat','proc_short'])['yield'].sum().unstack(fill_value=0.0)

# 2) Background: events per GeV at 125.08 GeV
#    Method: N_bkg_total * f_bkg(125.08)
#    where f_bkg is the normalised background PDF
print("\n --> Extracting background at 125.08 GeV...")

# Find mass variable
mgg = ws.var("CMS_hgg_mass")
if mgg is None: mgg = ws.var("mass")

bkg_at_125 = {}
if mgg is None:
    print("    [WARNING] mass variable not found — skipping background column")
    for cat in cats: bkg_at_125[cat] = None
else:
    mgg.setVal(125.08)
    mgg_argset = ROOT.RooArgSet(mgg)

    for cat in cats:
        val = None

        # Correct naming from workspace inspection:
        # norm: n_exp_final_bin<cat>_proc_bkg_mass  (no trailing _<cat>)
        # pdf:  shapeBkg_bkg_mass_<cat>
        norm_name = f"n_exp_final_bin{cat}_proc_bkg_mass"
        pdf_name  = f"shapeBkg_bkg_mass_{cat}"

        bkg_norm = ws.function(norm_name)
        bkg_pdf  = ws.pdf(pdf_name)

        if bkg_norm and bkg_pdf:
            N    = bkg_norm.getVal()
            fpdf = bkg_pdf.getVal(mgg_argset)   # normalised PDF value at 125.08 GeV (GeV^-1)
            val  = N * fpdf                      # events / GeV at 125.08 GeV
            print(f"    {cat:<15}: N={N:8.2f}  f(125.08)={fpdf:.6f}  => {val:.3f} GeV^-1")
        elif bkg_pdf:
            fpdf = bkg_pdf.getVal(mgg_argset)
            val  = fpdf
            print(f"    {cat:<15}: norm missing, PDF value = {fpdf:.6f}")
        else:
            print(f"    {cat:<15}: [NOT FOUND] - will show N/A")
            val = None

        bkg_at_125[cat] = val

# 3) Print plain text table
bkg_col = any(v is not None for v in bkg_at_125.values())
print("\n" + "="*110)
print("  YIELD TABLE — signal yields + background at 125 GeV")
print("="*110)
header = f"{'Category':<14}  {'Total':>7}" + "".join(f"  {p:>7}" for p in procs_present)
if bkg_col: header += f"  {'Bkg/GeV':>8}"
print(header)
print("-"*len(header))

for cat in cats:
    if cat not in pivot.index: continue
    row_yields = {p: pivot.loc[cat,p] if p in pivot.columns else 0.0 for p in procs_present}
    total = sum(row_yields.values())
    row   = f"{cat:<14}  {total:>7.3f}" + "".join(f"  {row_yields[p]:>7.3f}" for p in procs_present)
    if bkg_col:
        bv = bkg_at_125.get(cat)
        row += f"  {bv:>8.3f}" if bv is not None else f"  {'N/A':>8}"
    print(row)

print("-"*len(header))
totals    = {p: pivot[p].sum() if p in pivot.columns else 0.0 for p in procs_present}
grand     = sum(totals.values())
total_row = f"{'Total':<14}  {grand:>7.3f}" + "".join(f"  {totals[p]:>7.3f}" for p in procs_present)
if bkg_col: total_row += f"  {'—':>8}"
print(total_row)

# 4) LaTeX table
def fmt_frac(val, total):
    if total == 0: return r"$<0.05\%$"
    frac = val / total * 100
    if frac < 0.05: return r"$<0.05\%$"
    return f"${frac:.2f}\\%$"

# column spec: cat | total | proc fractions | bkg
extra_col = "r" if bkg_col else ""
col_spec   = "l" + "r" + "r"*len(procs_present) + extra_col

lines = []
lines.append(r"\begin{table}[htbp]")
lines.append(r"  \centering")
lines.append(r"  \caption{Expected number of signal events per category at $m_H = 125.08~\GeV$")
lines.append(r"           for $62.4~\fbinv$ of Run~3 data (2022--2023), broken down by")
lines.append(r"           production mode contribution. The last column lists the expected")
lines.append(r"           number of background events per \GeV at 125~\GeV.}")
lines.append(r"  \label{tab:signal_yields}")
lines.append(r"  \small")
lines.append(r"  \renewcommand{\arraystretch}{1.3}")
lines.append(f"  \\begin{{tabular}}{{{col_spec}}}")
lines.append(r"    \hline\hline")

# header
proc_hdrs = " & ".join(f"\\textbf{{{p}}}" for p in procs_present)
bkg_hdr   = r" & \textbf{Bkg} ($\GeV^{-1}$)" if bkg_col else ""
lines.append(f"    \\textbf{{Category}} & \\textbf{{Total}} & {proc_hdrs}{bkg_hdr} \\\\")
lines.append(r"    \hline")

for cat in cats:
    if cat not in pivot.index: continue
    row_yields = {p: pivot.loc[cat,p] if p in pivot.columns else 0.0 for p in procs_present}
    total = sum(row_yields.values())
    fracs = " & ".join(fmt_frac(row_yields[p], total) for p in procs_present)
    bkg_str = ""
    if bkg_col:
        bv = bkg_at_125.get(cat)
        bkg_str = f" & ${bv:.2f}$" if bv is not None else " & N/A"
    lines.append(f"    {cat_display[cat]} & ${total:.2f}$ & {fracs}{bkg_str} \\\\")

lines.append(r"    \hline")
fracs_tot = " & ".join(fmt_frac(totals[p], grand) for p in procs_present)
bkg_tot   = r" & ---" if bkg_col else ""
lines.append(f"    \\textbf{{Total}} & $\\mathbf{{{grand:.2f}}}$ & {fracs_tot}{bkg_tot} \\\\")
lines.append(r"    \hline\hline")
lines.append(r"  \end{tabular}")
lines.append(r"\end{table}")

latex = "\n".join(lines)
print(f"\n --> Writing LaTeX to: {opt.outputTex}")
with open(opt.outputTex, "w") as fout:
    fout.write(latex + "\n")
print(latex)
print("\n --> Done.")
