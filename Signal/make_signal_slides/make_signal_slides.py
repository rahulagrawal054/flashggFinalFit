#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path


# ============================================================
# Configuration
# ============================================================

BASE = Path(
    "/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/"
    "flashggFinalFit/Signal"
)

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

PRODUCTION_MODES = [
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


OUTPUT_DIR = Path("output")


# ============================================================
# Find plot
# ============================================================

def get_plot(era, model, production, category):

    plot_dir = (
        BASE
        / f"outdir_tth_th_analysis_{era}_{model}"
        / "signalFit"
        / "Plots"
    )

    filename = (
        f"total_shape_pdf_components_"
        f"{production}_{category}.pdf"
    )

    path = plot_dir / filename

    return path


# ============================================================
# Escape LaTeX special characters
# ============================================================

def latex_escape(text):

    replacements = {
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


# ============================================================
# Create LaTeX document
# ============================================================

def make_tex(era, tex_file):

    missing = []

    with open(tex_file, "w") as f:

        f.write(r"""\documentclass[aspectratio=169]{beamer}

\usepackage{graphicx}
\usepackage{helvet}
\usepackage{array}

\setbeamertemplate{navigation symbols}{}

\setbeamertemplate{footline}{
    \hfill
    \insertframenumber/\inserttotalframenumber
    \hspace{0.4cm}
    \vspace{0.15cm}
}

\begin{document}

""")

        slide_number = 0

        for category in CATEGORIES:

            for production in PRODUCTION_MODES:

                sog = get_plot(
                    era,
                    "SoG",
                    production,
                    category
                )

                dcb = get_plot(
                    era,
                    "DCB",
                    production,
                    category
                )

                slide_number += 1

                # Check files
                if not sog.exists():
                    missing.append(str(sog))

                if not dcb.exists():
                    missing.append(str(dcb))

                category_tex = latex_escape(category)
                production_tex = latex_escape(production)

                f.write(r"\begin{frame}" + "\n")

                f.write(
                    r"\frametitle{"
                    + category_tex
                    + r"\quad -- \quad "
                    + production_tex
                    + "}\n"
                )

                # ------------------------------------------------
                # SoG
                # ------------------------------------------------

                f.write(r"""
\begin{columns}[T,onlytextwidth]

\begin{column}{0.49\textwidth}
\centering
{\large\textbf{Sum of Gaussians}}

\vspace{0.15cm}

""")

                if sog.exists():
                    f.write(
                        r"\includegraphics[width=\textwidth,height=0.78\textheight,keepaspectratio]{"
                        + str(sog)
                        + "}\n"
                    )
                else:
                    f.write(
                        r"{\Large\textbf{MISSING PLOT}}"
                        + "\n"
                    )

                f.write(r"""
\end{column}

\begin{column}{0.49\textwidth}
\centering
{\large\textbf{Double Crystal Ball}}

\vspace{0.15cm}

""")

                if dcb.exists():
                    f.write(
                        r"\includegraphics[width=\textwidth,height=0.78\textheight,keepaspectratio]{"
                        + str(dcb)
                        + "}\n"
                    )
                else:
                    f.write(
                        r"{\Large\textbf{MISSING PLOT}}"
                        + "\n"
                    )

                f.write(r"""
\end{column}

\end{columns}

\end{frame}

""")

        f.write(r"\end{document}" + "\n")

    return missing


# ============================================================
# Compile
# ============================================================

def compile_pdf(era, tex_file):

    output_dir = OUTPUT_DIR / era
    output_dir.mkdir(parents=True, exist_ok=True)

    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={output_dir}",
        str(tex_file),
    ]

    print("\nCompiling:", era)

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    if result.returncode != 0:

        print("\nERROR while compiling", era)
        print(result.stdout[-5000:])

        return False

    return True


# ============================================================
# Main
# ============================================================

def main():

    OUTPUT_DIR.mkdir(exist_ok=True)

    for era in ERAS:

        print("\n" + "=" * 70)
        print("ERA:", era)
        print("=" * 70)

        tex_file = OUTPUT_DIR / f"signal_comparison_{era}.tex"

        missing = make_tex(
            era,
            tex_file
        )

        print(
            f"Created {len(CATEGORIES) * len(PRODUCTION_MODES)} slides"
        )

        if missing:

            print("\nWARNING:")
            print(f"{len(missing)} plot files are missing.")

            for path in missing:
                print("  ", path)

        else:

            print("All 512 plot files found.")

        success = compile_pdf(
            era,
            tex_file
        )

        if success:

            pdf = (
                OUTPUT_DIR
                / era
                / f"signal_comparison_{era}.pdf"
            )

            print("\nSUCCESS:")
            print(pdf)

        else:

            print("\nCompilation failed.")


if __name__ == "__main__":
    main()
