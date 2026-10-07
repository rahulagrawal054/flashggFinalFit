#!/usr/bin/env python3

import os

# ============================================================
# Configuration
# ============================================================

DCB_DIR = "/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/outdir_packaged_DCB/Plots"
SOG_DIR = "/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/outdir_packaged_SoG/Plots"

OUTPUT_TEX = "DCB_vs_SoG_signal_model_comparison.tex"

YEARS = [
    "2022preEE",
    "2022postEE",
    "2023preBPix",
    "2023postBPix"
]

CATS = [
    "tH_lep_1",
    "tH_lep_2",
    "ttH_lep_1",
    "ttH_lep_2",
    "ttH_lep_3",
    "ttH_lep_4",
    "bkg_lep",
    "tH_had_1",
    "tH_had_2",
    "tH_had_3",
    "tH_had_4",
    "ttH_had_1",
    "ttH_had_2",
    "ttH_had_3",
    "ttH_had_4",
    "bkg_had"
]

PROCS = [
    "bbh_in",
    "bbh_out",
    "ggh_in",
    "ggh_out",
    "tHW_in",
    "tHW_out",
    "tth_in",
    "tth_out",
    "tHqLep_in",
    "tHqLep_out",
    "tHqHad_in",
    "tHqHad_out",
    "vh_in",
    "vh_out",
    "vbf_in",
    "vbf_out"
]

# ============================================================
# Helper functions
# ============================================================

def exists(model_dir, filename):
    return os.path.isfile(os.path.join(model_dir, filename))


def include_plot(model_dir, filename, width="0.47\\textwidth"):
    """
    Return LaTeX code for a plot if it exists.
    """
    if exists(model_dir, filename):
        return (
            "\\includegraphics[width=%s]{%s}"
            % (width, os.path.join(model_dir, filename))
        )
    else:
        return "\\fbox{\\parbox[c][0.25\\textheight][c]{0.42\\textwidth}{\\centering Missing plot}}"


def latex_escape(text):
    """
    Escape characters that have special meaning in LaTeX.
    """
    text = str(text)
    text = text.replace("\\", r"\textbackslash{}")
    text = text.replace("_", r"\_")
    text = text.replace("&", r"\&")
    text = text.replace("%", r"\%")
    text = text.replace("#", r"\#")
    text = text.replace("{", r"\{")
    text = text.replace("}", r"\}")
    return text


def add_comparison_slide(tex, title, filename):
    """
    Add one DCB vs SoG comparison slide.
    """

    safe_title = latex_escape(title)

    tex.append("\\begin{frame}{%s}" % safe_title)
    tex.append("\\begin{columns}[T,totalwidth=\\textwidth]")
    tex.append("")

    # ---------------- DCB ----------------
    tex.append("\\begin{column}{0.49\\textwidth}")
    tex.append("\\centering")
    tex.append("{\\large\\textbf{DCB}}\\\\[0.15cm]")
    tex.append(
        include_plot(
            DCB_DIR,
            filename
        )
    )
    tex.append("\\end{column}")

    # ---------------- SoG ----------------
    tex.append("\\begin{column}{0.49\\textwidth}")
    tex.append("\\centering")
    tex.append("{\\large\\textbf{SoG}}\\\\[0.15cm]")
    tex.append(
        include_plot(
            SOG_DIR,
            filename
        )
    )
    tex.append("\\end{column}")

    tex.append("\\end{columns}")
    tex.append("\\end{frame}")
    tex.append("")

def add_four_year_slide(tex, cat):
    """
    One slide containing the four years.
    Each row has DCB and SoG.
    """

    tex.append("\\begin{frame}{%s: Year-by-year comparison}" % cat)
    tex.append("\\scriptsize")
    tex.append("\\begin{tabular}{c c c}")
    tex.append("\\textbf{Year} & \\textbf{DCB} & \\textbf{SoG} \\\\")
    tex.append("\\hline")

    for year in YEARS:

        filename = "smodel_%s_%s.pdf" % (cat, year)

        tex.append(
            "%s & \\includegraphics[width=0.40\\textwidth]{%s} "
            "& \\includegraphics[width=0.40\\textwidth]{%s} \\\\"
            %
            (
                year,
                os.path.join(DCB_DIR, filename)
                if exists(DCB_DIR, filename)
                else "",
                os.path.join(SOG_DIR, filename)
                if exists(SOG_DIR, filename)
                else ""
            )
        )

    tex.append("\\end{tabular}")
    tex.append("\\end{frame}")
    tex.append("")


def add_section_slide(tex, title):
    tex.append("\\begin{frame}")
    tex.append("\\centering")
    tex.append("\\vfill")
    tex.append("{\\Huge\\bfseries %s}" % title)
    tex.append("\\vfill")
    tex.append("\\end{frame}")
    tex.append("")


# ============================================================
# Start LaTeX document
# ============================================================

tex = []

tex.append(r"\documentclass[aspectratio=169]{beamer}")
tex.append(r"\usepackage{graphicx}")
tex.append(r"\usepackage{booktabs}")
tex.append(r"\usepackage{array}")
tex.append(r"\usepackage{xcolor}")
tex.append(r"\setbeamertemplate{navigation symbols}{}")
tex.append(r"\setbeamertemplate{footline}[frame number]")
tex.append("")
tex.append(r"\begin{document}")
tex.append("")


# ============================================================
# TITLE
# ============================================================

tex.append(r"\begin{frame}")
tex.append(r"\centering")
tex.append(r"\vfill")
tex.append(r"{\Huge\bfseries Signal Model Comparison}")
tex.append(r"\vspace{0.4cm}")
tex.append(r"{\Large DCB vs Sum of Gaussians (SoG)}")
tex.append(r"\vspace{0.4cm}")
tex.append(r"{\large ttH/tH fiducial cross-section analysis}")
tex.append(r"\vfill")
tex.append(r"\end{frame}")
tex.append("")


# ============================================================
# SECTION 1
# All years + all processes
# ============================================================

add_section_slide(
    tex,
    "1. Overall Signal Model Comparison"
)

for cat in CATS:

    filename = "smodel_%s.pdf" % cat

    add_comparison_slide(
        tex,
        "%s: All years + all production modes" % cat,
        filename
    )


# ============================================================
# SECTION 2
# Year-by-year
# ============================================================

add_section_slide(
    tex,
    "2. Year-by-year Comparison"
)

for cat in CATS:

    for year in YEARS:

        filename = "smodel_%s_%s.pdf" % (cat, year)

        add_comparison_slide(
            tex,
            "%s: %s" % (cat, year),
            filename
        )


# ============================================================
# SECTION 3
# All years + individual production modes
# ============================================================

add_section_slide(
    tex,
    "3. Production-mode Comparison"
)

for cat in CATS:

    for proc in PROCS:

        filename = "smodel_%s_%s.pdf" % (cat, proc)

        add_comparison_slide(
            tex,
            "%s: %s — All years" % (cat, proc),
            filename
        )


# ============================================================
# SECTION 4
# Individual production mode + year
# Backup / detailed diagnostic
# ============================================================

add_section_slide(
    tex,
    "4. Production mode + Year"
)

for cat in CATS:

    for proc in PROCS:

        for year in YEARS:

            filename = "smodel_%s_%s_%s.pdf" % (
                cat,
                proc,
                year
            )

            # Only create slide if at least one model has the plot
            if (
                exists(DCB_DIR, filename)
                or exists(SOG_DIR, filename)
            ):

                add_comparison_slide(
                    tex,
                    "%s: %s — %s" % (cat, proc, year),
                    filename
                )


# ============================================================
# END
# ============================================================

tex.append(r"\end{document}")

# ============================================================
# Write file
# ============================================================

with open(OUTPUT_TEX, "w") as f:
    f.write("\n".join(tex))

print("")
print("============================================================")
print("LaTeX file created:")
print("  %s" % OUTPUT_TEX)
print("============================================================")
print("")
print("Compile with:")
print("  pdflatex %s" % OUTPUT_TEX)
print("")
