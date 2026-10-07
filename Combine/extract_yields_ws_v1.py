"""
Extract signal yields + background at 125 GeV from final datacard workspace.

Modes:
  fiducial  : use only *_in processes
  inclusive : use *_in + *_out processes

Production modes are combined across years.
VH processes are combined into a single vH column.

Usage:

  Fiducial:
    python extract_yields_ws.py \
      -i Datacard_fiducial_allCats_r_2D_fiducial.root \
      --mode fiducial \
      -o yield_table_fiducial.tex

  Inclusive:
    python extract_yields_ws.py \
      -i Datacard_fiducial_allCats_r_2D_fiducial.root \
      --mode inclusive \
      -o yield_table_inclusive.tex
"""

import pandas as pd
import ROOT
import sys
from optparse import OptionParser


# ============================================================
# Options
# ============================================================

def get_options():

    parser = OptionParser()

    parser.add_option(
        "-i", "--inputWS",
        dest="inputWS",
        default="",
        help="Input RooWorkspace (datacard .root)"
    )

    parser.add_option(
        "-o", "--outputTex",
        dest="outputTex",
        default="yield_table.tex",
        help="Output LaTeX file"
    )

    parser.add_option(
        "--mode",
        dest="mode",
        default="fiducial",
        choices=["fiducial", "inclusive"],
        help="fiducial = *_in only; inclusive = *_in + *_out"
    )

    return parser.parse_args()


(opt, args) = get_options()


if not opt.inputWS:
    print("[ERROR] Please provide an input workspace with -i")
    sys.exit(1)


# ============================================================
# Process name mapping
# ============================================================

def proc_to_short(p):

    pl = p.lower()

    # Remove in/out from consideration automatically.
    # The production mode itself is identified below.

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

    elif "vh_" in pl:
        return "vH"

    elif "wh" in pl:
        return "WH"

    elif "zh" in pl:
        return "ZH"

    elif "bbh" in pl:
        return "bbH"

    else:
        return p


# ============================================================
# Production mode order in final table
# ============================================================

proc_order = [
    "ttH",
    "tHq",
    "tHW",
    "ggH",
    "VBF",
    "vH",
    "WH",
    "ZH",
    "bbH"
]


# ============================================================
# Category display names
# ============================================================

cat_display = {

    "ttH_had_1": r"$t\bar{t}$H Had 1",
    "ttH_had_2": r"$t\bar{t}$H Had 2",
    "ttH_had_3": r"$t\bar{t}$H Had 3",
    "ttH_had_4": r"$t\bar{t}$H Had 4",

    "ttH_lep_1": r"$t\bar{t}$H Lep 1",
    "ttH_lep_2": r"$t\bar{t}$H Lep 2",
    "ttH_lep_3": r"$t\bar{t}$H Lep 3",
    "ttH_lep_4": r"$t\bar{t}$H Lep 4",

    "tH_had_1": r"$tH$ Had 1",
    "tH_had_2": r"$tH$ Had 2",
    "tH_had_3": r"$tH$ Had 3",
    "tH_had_4": r"$tH$ Had 4",

    "tH_lep_1": r"$tH$ Lep 1",
    "tH_lep_2": r"$tH$ Lep 2",

    "bkg_had": r"Bkg Had",
    "bkg_lep": r"Bkg Lep",
}

cats = list(cat_display.keys())


# ============================================================
# RooFit iterator
# ============================================================

def rooiter(x):

    it = x.iterator()
    r = it.Next()

    while r:
        yield r
        r = it.Next()


# ============================================================
# Open ROOT file
# ============================================================

print(f" --> Opening: {opt.inputWS}")

f = ROOT.TFile(opt.inputWS)

if not f or f.IsZombie():

    print("[ERROR] Could not open ROOT file")
    sys.exit(1)


# ============================================================
# Find workspace
# ============================================================

ws = None

for wsname in ["w", "w_all", "workspace"]:

    ws = f.Get(wsname)

    if ws:

        print(f" --> Workspace: {wsname}")
        break


if not ws:

    print("[ERROR] workspace not found")
    sys.exit(1)


print(f" --> Mode: {opt.mode}")


# ============================================================
# Extract all signal normalisations
# ============================================================

columns = [
    "proc",
    "proc_short",
    "cat",
    "yield"
]

data = pd.DataFrame(columns=columns)


allNorms = ws.allFunctions().selectByName("n_exp_final*")


for func in rooiter(allNorms):

    name = func.GetName()

    # Background normalization is handled separately
    if "bkg_mass" in name:
        continue

    try:

        # Example:
        # n_exp_final_binttH_had_1_proc_ttH_in_2022preEE
        #
        # Existing naming convention from your workspace:
        # <...>bin<CATEGORY>_proc_<PROCESS>

        cat = name.split("_proc_")[0].split("bin")[-1]

        proc = name.split("_proc_")[-1]

        proc_short = proc_to_short(proc)

        yld = func.getVal()

        data.loc[len(data)] = [
            proc,
            proc_short,
            cat,
            yld
        ]

    except Exception:

        continue


print(
    f" --> {len(data)} signal normalisations found."
)

print(
    f"     Cats: {sorted(data['cat'].unique())}"
)

print(
    f"     Procs: {sorted(data['proc_short'].unique())}"
)


# ============================================================
# Select fiducial / inclusive
# ============================================================
#
# IMPORTANT:
#
# Fiducial:
#   only *_in
#
# Inclusive:
#   *_in + *_out
#
# This is done BEFORE grouping production modes.
# Therefore it applies to every process:
#
#   ttH
#   tHq
#   tHW
#   ggH
#   VBF
#   bbH
#   vH
#   etc.
#
# ============================================================

if opt.mode == "fiducial":

    # Keep ONLY processes containing "_in"
    data = data[
        data["proc"].str.contains(
            "_in",
            case=False,
            na=False
        )
    ].copy()

    print(
        f" --> Fiducial selection: "
        f"keeping only *_in processes."
    )


elif opt.mode == "inclusive":

    # Keep both _in and _out.
    #
    # We explicitly require either _in or _out
    # so unrelated processes are not accidentally included.

    data = data[
        data["proc"].str.contains(
            "_in|_out",
            case=False,
            na=False,
            regex=True
        )
    ].copy()

    print(
        f" --> Inclusive selection: "
        f"keeping *_in + *_out processes."
    )


print(
    f" --> {len(data)} normalisations after "
    f"{opt.mode} selection."
)


# ============================================================
# Show selected raw processes
# ============================================================

print(
    " --> Selected processes:"
)

for proc in sorted(data["proc"].unique()):

    print(
        f"       {proc}"
    )


# ============================================================
# Group production modes
# ============================================================
#
# At this point:
#
#   fiducial:
#       ttH_in_*  -> ttH
#       tHq_in_*  -> tHq
#       ...
#
#   inclusive:
#       ttH_in_* + ttH_out_* -> ttH
#       tHq_in_* + tHq_out_* -> tHq
#       ...
#
# VH years are also automatically combined:
#
#   vh_in_2022preEE_hgg
#   vh_in_2022postEE_hgg
#   vh_in_2023preBPix_hgg
#   ...
#
#   -> vH
#
# ============================================================

pivot = (
    data
    .groupby(
        ["cat", "proc_short"]
    )["yield"]
    .sum()
    .unstack(
        fill_value=0.0
    )
)


procs_present = [
    p
    for p in proc_order
    if p in data["proc_short"].values
]


# ============================================================
# Background at 125.08 GeV
# ============================================================

print(
    "\n --> Extracting background at 125.08 GeV..."
)


# Find mass variable

mgg = ws.var("CMS_hgg_mass")

if mgg is None:
    mgg = ws.var("mass")


bkg_at_125 = {}


if mgg is None:

    print(
        "    [WARNING] mass variable not found — "
        "skipping background column"
    )

    for cat in cats:
        bkg_at_125[cat] = None


else:

    mgg.setVal(125.08)

    mgg_argset = ROOT.RooArgSet(mgg)


    for cat in cats:

        val = None

        # Workspace naming
        norm_name = (
            f"n_exp_final_bin{cat}_proc_bkg_mass"
        )

        pdf_name = (
            f"shapeBkg_bkg_mass_{cat}"
        )


        bkg_norm = ws.function(
            norm_name
        )

        bkg_pdf = ws.pdf(
            pdf_name
        )


        if bkg_norm and bkg_pdf:

            N = bkg_norm.getVal()

            fpdf = bkg_pdf.getVal(
                mgg_argset
            )

            val = N * fpdf

            print(
                f"    {cat:<15}: "
                f"N={N:8.2f}  "
                f"f(125.08)={fpdf:.6f}  "
                f"=> {val:.3f} GeV^-1"
            )


        elif bkg_pdf:

            fpdf = bkg_pdf.getVal(
                mgg_argset
            )

            val = fpdf

            print(
                f"    {cat:<15}: "
                f"norm missing, "
                f"PDF value = {fpdf:.6f}"
            )


        else:

            print(
                f"    {cat:<15}: "
                f"[NOT FOUND] - will show N/A"
            )


        bkg_at_125[cat] = val


# ============================================================
# Print plain-text table
# ============================================================

bkg_col = any(
    v is not None
    for v in bkg_at_125.values()
)


print(
    "\n" + "=" * 130
)


if opt.mode == "fiducial":

    print(
        "  YIELD TABLE — FIDUCIAL "
        "(*_in only) — signal yields + background "
        "at 125 GeV"
    )

else:

    print(
        "  YIELD TABLE — INCLUSIVE "
        "(*_in + *_out) — signal yields + background "
        "at 125 GeV"
    )


print(
    "=" * 130
)


header = (
    f"{'Category':<14}  "
    f"{'Total':>7}"
)


header += "".join(
    f"  {p:>7}"
    for p in procs_present
)


if bkg_col:

    header += (
        f"  {'Bkg/GeV':>8}"
    )


print(header)

print(
    "-" * len(header)
)


# ============================================================
# Category rows
# ============================================================

for cat in cats:

    if cat not in pivot.index:
        continue


    row_yields = {

        p:
        pivot.loc[cat, p]
        if p in pivot.columns
        else 0.0

        for p in procs_present
    }


    total = sum(
        row_yields.values()
    )


    row = (
        f"{cat:<14}  "
        f"{total:>7.3f}"
    )


    row += "".join(
        f"  {row_yields[p]:>7.3f}"
        for p in procs_present
    )


    if bkg_col:

        bv = bkg_at_125.get(cat)

        if bv is not None:

            row += (
                f"  {bv:>8.3f}"
            )

        else:

            row += (
                f"  {'N/A':>8}"
            )


    print(row)


# ============================================================
# Total row
# ============================================================

print(
    "-" * len(header)
)


totals = {

    p:
    pivot[p].sum()
    if p in pivot.columns
    else 0.0

    for p in procs_present
}


grand = sum(
    totals.values()
)


total_row = (
    f"{'Total':<14}  "
    f"{grand:>7.3f}"
)


total_row += "".join(
    f"  {totals[p]:>7.3f}"
    for p in procs_present
)


if bkg_col:

    total_row += (
        f"  {'—':>8}"
    )


print(total_row)


# ============================================================
# LaTeX formatting
# ============================================================

def fmt_frac(val, total):

    if total == 0:

        return r"$<0.05\%$"


    frac = val / total * 100


    if frac < 0.05:

        return r"$<0.05\%$"


    return (
        f"${frac:.2f}\\%$"
    )


# ============================================================
# LaTeX table
# ============================================================

extra_col = (
    "r"
    if bkg_col
    else ""
)


col_spec = (
    "l"
    + "r"
    + "r" * len(procs_present)
    + extra_col
)


lines = []


lines.append(
    r"\begin{table}[htbp]"
)

lines.append(
    r"  \centering"
)


if opt.mode == "fiducial":

    lines.append(
        r"  \caption{Expected number of signal events per "
        r"category at $m_H = 125.08~\GeV$"
    )

    lines.append(
        r"           for $62.4~\fbinv$ of Run~3 data "
        r"(2022--2023), using only the fiducial"
    )

    lines.append(
        r"           production contributions "
        r"($\mathrm{in}$), broken down by production mode."
    )


else:

    lines.append(
        r"  \caption{Expected number of signal events per "
        r"category at $m_H = 125.08~\GeV$"
    )

    lines.append(
        r"           for $62.4~\fbinv$ of Run~3 data "
        r"(2022--2023), using both fiducial and"
    )

    lines.append(
        r"           non-fiducial production contributions "
        r"($\mathrm{in}+\mathrm{out}$), broken down by "
        r"production mode."
    )


lines.append(
    r"           The last column lists the expected "
    r"number of background events per \GeV at 125~\GeV.}"
)


if opt.mode == "fiducial":

    lines.append(
        r"  \label{tab:signal_yields_fiducial}"
    )

else:

    lines.append(
        r"  \label{tab:signal_yields_inclusive}"
    )


lines.append(
    r"  \small"
)

lines.append(
    r"  \renewcommand{\arraystretch}{1.3}"
)

lines.append(
    f"  \\begin{{tabular}}{{{col_spec}}}"
)

lines.append(
    r"    \hline\hline"
)


# ============================================================
# LaTeX header
# ============================================================

proc_hdrs = " & ".join(
    f"\\textbf{{{p}}}"
    for p in procs_present
)


bkg_hdr = (
    r" & \textbf{Bkg} ($\GeV^{-1}$)"
    if bkg_col
    else ""
)


lines.append(
    f"    \\textbf{{Category}} "
    f"& \\textbf{{Total}} "
    f"& {proc_hdrs}"
    f"{bkg_hdr} \\\\"
)


lines.append(
    r"    \hline"
)


# ============================================================
# LaTeX category rows
# ============================================================

for cat in cats:

    if cat not in pivot.index:
        continue


    row_yields = {

        p:
        pivot.loc[cat, p]
        if p in pivot.columns
        else 0.0

        for p in procs_present
    }


    total = sum(
        row_yields.values()
    )


    fracs = " & ".join(
        fmt_frac(
            row_yields[p],
            total
        )
        for p in procs_present
    )


    bkg_str = ""


    if bkg_col:

        bv = bkg_at_125.get(cat)

        if bv is not None:

            bkg_str = (
                f" & ${bv:.2f}$"
            )

        else:

            bkg_str = (
                " & N/A"
            )


    lines.append(
        f"    {cat_display[cat]} "
        f"& ${total:.2f}$ "
        f"& {fracs}"
        f"{bkg_str} \\\\"
    )


# ============================================================
# LaTeX total
# ============================================================

lines.append(
    r"    \hline"
)


fracs_tot = " & ".join(
    fmt_frac(
        totals[p],
        grand
    )
    for p in procs_present
)


bkg_tot = (
    r" & ---"
    if bkg_col
    else ""
)


lines.append(
    f"    \\textbf{{Total}} "
    f"& $\\mathbf{{{grand:.2f}}}$ "
    f"& {fracs_tot}"
    f"{bkg_tot} \\\\"
)


lines.append(
    r"    \hline\hline"
)

lines.append(
    r"  \end{tabular}"
)

lines.append(
    r"\end{table}"
)


# ============================================================
# Write LaTeX
# ============================================================

latex = "\n".join(lines)


print(
    f"\n --> Writing LaTeX to: "
    f"{opt.outputTex}"
)


with open(
    opt.outputTex,
    "w"
) as fout:

    fout.write(
        latex + "\n"
    )


print(latex)

print("\n --> Done.")
