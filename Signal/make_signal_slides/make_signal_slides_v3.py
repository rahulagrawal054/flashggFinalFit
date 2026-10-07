#!/usr/bin/env python3

import os
import shutil
import subprocess
import argparse


# ============================================================
# Configuration
# ============================================================

BASE = "/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal"

ERAS = [
    "2022preEE",
    "2022postEE",
    "2023preBPix",
    "2023postBPix",
]

CATEGORIES = [
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
    "bkg_had",
]

PROCESSES = [
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
    "vbf_out",
]

MODELS = ["SoG", "DCB"]


# ============================================================
# Utility
# ============================================================

def latex_escape(text):
    """
    Escape characters that have special meaning in LaTeX.
    """
    replacements = {
        "\\": r"\textbackslash{}",
        "_": r"\_",
        "&": r"\&",
        "%": r"\%",
        "#": r"\#",
        "{": r"\{",
        "}": r"\}",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def get_plot_path(era, model, process, category):
    """
    Return the expected signal-fit plot path.
    Return None if the file does not exist.
    """

    plot_dir = os.path.join(
        BASE,
        f"outdir_tth_th_analysis_{era}_{model}",
        "signalFit",
        "Plots",
    )

    filename = (
        f"total_shape_pdf_components_"
        f"{process}_{category}.pdf"
    )

    path = os.path.join(plot_dir, filename)

    if os.path.isfile(path):
        return path

    return None


# ============================================================
# LaTeX panel
# ============================================================

def make_panel(model, plot_path):
    """
    Create one side of the SoG/DCB comparison.
    Width is kept at 0.48\textwidth to fit side-by-side cleanly.
    """

    model_name = latex_escape(model)

    if plot_path is not None:

        plot_path_tex = plot_path.replace("\\", "/")

        return rf"""\begin{{minipage}}[t]{{0.48\textwidth}}
\centering
\textbf{{{model_name}}}

\vspace{{1mm}}

\includegraphics[
    width=\textwidth,
    height=0.67\textheight,
    keepaspectratio
]{{{plot_path_tex}}}
\end{{minipage}}"""

    else:

        return rf"""\begin{{minipage}}[t]{{0.48\textwidth}}
\centering
\textbf{{{model_name}}}

\vspace{{1mm}}

\fbox{{%
\begin{{minipage}}[c][0.67\textheight][c]{{0.92\textwidth}}
\centering

\Large\textbf{{MISSING PLOT}}

\vspace{{5mm}}

\normalsize
No PDF was found for this\\
era / production / category.

\end{{minipage}}
}}
\end{{minipage}}"""


# ============================================================
# Make one slide
# ============================================================

def make_slide(category, era, process):

    category_tex = latex_escape(category)
    era_tex = latex_escape(era)
    process_tex = latex_escape(process)

    sog_path = get_plot_path(
        era,
        "SoG",
        process,
        category,
    )

    dcb_path = get_plot_path(
        era,
        "DCB",
        process,
        category,
    )

    sog_panel = make_panel("SoG", sog_path)
    dcb_panel = make_panel("DCB", dcb_path)

    return rf"""
\begin{{frame}}[t]
\frametitle{{Category: {category_tex} \quad | \quad Era: {era_tex} \quad | \quad Production: {process_tex}}}

\vspace{{-3mm}}

\centering
{sog_panel}%
\hfill
{dcb_panel}

\end{{frame}}
"""


# ============================================================
# Make complete TEX file for one category
# ============================================================

def make_category_tex(category, output_dir):

    tex_file = os.path.join(
        output_dir,
        f"signal_comparison_{category}.tex",
    )

    with open(tex_file, "w") as f:

        f.write(r"""
\documentclass[
    10pt,
    aspectratio=169
]{beamer}

\usepackage{graphicx}
\usepackage{xcolor}

\setbeamertemplate{navigation symbols}{}

\setbeamertemplate{footline}{
    \hfill
    \insertframenumber/\inserttotalframenumber
    \hspace{0.4cm}
    \vspace{0.15cm}
}

\begin{document}
""")

        # ----------------------------------------------------
        # 4 eras × 16 production modes = 64 slides
        # ----------------------------------------------------

        for era in ERAS:
            for process in PROCESSES:

                slide = make_slide(
                    category,
                    era,
                    process,
                )

                f.write(slide)

        f.write(r"""
\end{document}
""")

    return tex_file


# ============================================================
# Compile TEX -> PDF
# ============================================================

def compile_tex(tex_file):

    tex_dir = os.path.dirname(tex_file)
    tex_name = os.path.basename(tex_file)

    print()
    print("=" * 70)
    print(f"Compiling: {tex_name}")
    print("=" * 70)

    # Prefer latexmk if available
    if shutil.which("latexmk"):

        command = [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            tex_name,
        ]

        subprocess.run(
            command,
            cwd=tex_dir,
            check=True,
        )

    else:

        # Fallback to pdflatex
        for _ in range(2):

            command = [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex_name,
            ]

            subprocess.run(
                command,
                cwd=tex_dir,
                check=True,
            )

    pdf_file = tex_file.replace(".tex", ".pdf")

    if os.path.isfile(pdf_file):
        print(f"\nCreated:")
        print(pdf_file)
    else:
        raise RuntimeError(
            f"PDF was not created: {pdf_file}"
        )

    return pdf_file


# ============================================================
# Count available plots
# ============================================================

def print_summary():

    print()
    print("=" * 70)
    print("Signal plot availability")
    print("=" * 70)

    for model in MODELS:

        total = 0
        missing = 0

        for era in ERAS:
            for category in CATEGORIES:
                for process in PROCESSES:

                    path = get_plot_path(
                        era,
                        model,
                        process,
                        category,
                    )

                    if path is not None:
                        total += 1
                    else:
                        missing += 1

        print(
            f"{model}: "
            f"{total} available, "
            f"{missing} missing"
        )


# ============================================================
# Main
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Create SoG vs DCB signal-fit comparison PDFs."
        )
    )

    parser.add_argument(
        "--output",
        default="signal_comparison_output",
        help="Output directory",
    )

    parser.add_argument(
        "--category",
        default=None,
        help=(
            "Create only this category. "
            "If omitted, create all 16 categories."
        ),
    )

    args = parser.parse_args()

    output_dir = os.path.abspath(args.output)

    os.makedirs(output_dir, exist_ok=True)

    # Check category name if supplied
    if args.category is not None:

        if args.category not in CATEGORIES:

            print("ERROR: Unknown category:")
            print(args.category)
            print()
            print("Available categories:")

            for cat in CATEGORIES:
                print("  ", cat)

            return

        categories_to_make = [args.category]

    else:

        categories_to_make = CATEGORIES

    print_summary()

    print()
    print("=" * 70)
    print("Creating comparison PDFs")
    print("=" * 70)

    print(
        f"Output directory: {output_dir}"
    )

    print(
        f"Number of categories: "
        f"{len(categories_to_make)}"
    )

    print(
        f"Slides per category: "
        f"{len(ERAS) * len(PROCESSES)}"
    )

    # --------------------------------------------------------
    # Create one PDF per category
    # --------------------------------------------------------

    created_pdfs = []

    for i, category in enumerate(categories_to_make, start=1):

        print()
        print(
            f"[{i}/{len(categories_to_make)}] "
            f"Category: {category}"
        )

        tex_file = make_category_tex(
            category,
            output_dir,
        )

        pdf_file = compile_tex(tex_file)

        created_pdfs.append(pdf_file)

    # --------------------------------------------------------
    # Final summary
    # --------------------------------------------------------

    print()
    print("=" * 70)
    print("DONE")
    print("=" * 70)

    print(
        f"\nCreated {len(created_pdfs)} PDF file(s):\n"
    )

    for pdf in created_pdfs:
        print("  ", pdf)


if __name__ == "__main__":
    main()
