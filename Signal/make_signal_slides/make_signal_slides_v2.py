#!/usr/bin/env python3

import os
import re
import argparse
import subprocess
import shutil

# ============================================================
# Configuration
# ============================================================

BASE = (
    "/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/"
    "src/flashggFinalFit/Signal"
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


# ============================================================
# Signal-fit log parser
# ============================================================

def parse_signalfit_log(path):

    results = {}

    if not os.path.isfile(path):
        print(f"[WARNING] Log file not found: {path}")
        return results

    with open(path, "r", errors="replace") as f:
        lines = f.readlines()

    current_key = None
    replacement = None
    chi2_values = []

    def flush_block():

        if current_key is None:
            return

        entry = results.setdefault(current_key, {})

        if chi2_values:
            # Last chi2 value = post-fit value
            entry["chi2_over_ndof"] = chi2_values[-1]

    for line in lines:

        # ----------------------------------------------------
        # New process/category block
        # ----------------------------------------------------

        m = re.search(
            r"Running fit for \(proc,cat\) = \(([^,]+),([^)]+)\)",
            line
        )

        if m:

            flush_block()

            current_key = (
                m.group(1).strip(),
                m.group(2).strip()
            )

            replacement = None
            chi2_values = []

            results[current_key] = {
                "numEntries": None,
                "replaced": False,
                "replacement_proc": "",
                "chi2_over_ndof": None,
            }

            continue

        # ----------------------------------------------------
        # Too few entries -> replacement
        # ----------------------------------------------------

        m = re.search(
            r"Too few entries in nominal dataset \((\d+) < (\d+)\)\. "
            r"Using replacement \(proc,cat\) = \(([^,]+),([^)]+)\)",
            line
        )

        if m and current_key:

            results[current_key]["numEntries"] = int(m.group(1))

            results[current_key]["replaced"] = True

            results[current_key]["replacement_proc"] = (
                m.group(3).strip()
            )

            replacement = m.group(3).strip()

            continue

        # ----------------------------------------------------
        # Normal numEntries
        # ----------------------------------------------------

        m = re.search(
            r"numEntries = (\d+),\s*sumEntries = ([\d.eE+-]+)",
            line
        )

        if m and current_key and replacement is None:

            results[current_key]["numEntries"] = int(m.group(1))

            continue

        # ----------------------------------------------------
        # chi2 / ndof
        # ----------------------------------------------------

        m = re.search(
            r"^\s*\*\s*chi2\s*=\s*([\d.eE+-]+),\s*n\(dof\)\s*=\s*(\d+)"
            r"\s*-->\s*chi2/n\(dof\)\s*=\s*([\d.eE+-]+)",
            line
        )

        if m and current_key:

            chi2_values.append(float(m.group(3)))

    flush_block()

    return results


def load_logs(log_dir):

    all_data = {}

    for era in ERAS:

        path = os.path.join(
            log_dir,
            f"signalFit_{era}.log"
        )

        all_data[era] = parse_signalfit_log(path)

    return all_data


# ============================================================
# Find plot
# ============================================================

def get_plot_path(era, model, process, category):

    plot_dir = os.path.join(
        BASE,
        f"outdir_tth_th_analysis_{era}_{model}",
        "signalFit",
        "Plots"
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
# Escape LaTeX text
# ============================================================

def latex_escape(text):

    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


# ============================================================
# Format fit information
# ============================================================

def fit_info(data, process, category):

    info = data.get((process, category), {})

    entries = info.get("numEntries")
    replaced = info.get("replaced", False)
    donor = info.get("replacement_proc", "")
    chi2 = info.get("chi2_over_ndof")

    lines = []

    # Entries
    if entries is None:
        lines.append(r"\textbf{Entries:} --")
    else:
        lines.append(
            rf"\textbf{{Entries:}} {entries}"
        )

    # Fit status
    if replaced:

        if donor:
            donor_tex = latex_escape(donor)

            lines.append(
                rf"\textbf{{Status:}} "
                rf"\textcolor{{red}}{{Borrowed from {donor_tex}}}"
            )
        else:
            lines.append(
                r"\textbf{Status:} "
                r"\textcolor{red}{Borrowed shape}"
            )

    else:

        lines.append(
            r"\textbf{Status:} "
            r"\textcolor{green!50!black}{Direct fit}"
        )

    # Chi2
    if chi2 is not None:

        lines.append(
            rf"\textbf{{$\chi^2$/ndof:}} {chi2:.3f}"
        )

    return r"\\ ".join(lines)


# ============================================================
# Generate one slide
# ============================================================

def make_slide(
    era,
    process,
    category,
    sog_data,
    dcb_data,
):

    sog_plot = get_plot_path(
        era,
        "SoG",
        process,
        category
    )

    dcb_plot = get_plot_path(
        era,
        "DCB",
        process,
        category
    )

    title = (
        f"Category: {category}  |  "
        f"Era: {era}  |  "
        f"Production: {process}"
    )

    # --------------------------------------------------------
    # SoG panel
    # --------------------------------------------------------

    if sog_plot:

        sog_panel = rf"""
\begin{{minipage}}[c][0.72\textheight][c]{{0.47\textwidth}}
\centering

\textbf{{Sum of Gaussians (SoG)}}\\[2mm]

\includegraphics[
    width=\textwidth,
    height=0.58\textheight,
    keepaspectratio
]{{{sog_plot}}}

\vspace{{1mm}}

\scriptsize
{fit_info(sog_data, process, category)}

\end{{minipage}}
"""

    else:

        sog_panel = rf"""
\begin{{minipage}}[c][0.72\textheight][c]{{0.47\textwidth}}
\centering

\textbf{{Sum of Gaussians (SoG)}}\\[5mm]

\fbox{{
\begin{{minipage}}[c][0.58\textheight][c]{{0.90\textwidth}}
\centering
\Large
\textcolor{{red}}{{MISSING PLOT}}

\vspace{{5mm}}

\normalsize
No PDF found for this\\
era / production / category.
\end{{minipage}}
}}

\vspace{{2mm}}

\scriptsize
{fit_info(sog_data, process, category)}

\end{{minipage}}
"""

    # --------------------------------------------------------
    # DCB panel
    # --------------------------------------------------------

    if dcb_plot:

        dcb_panel = rf"""
\begin{{minipage}}[c][0.72\textheight][c]{{0.47\textwidth}}
\centering

\textbf{{Double Crystal Ball (DCB)}}\\[2mm]

\includegraphics[
    width=\textwidth,
    height=0.58\textheight,
    keepaspectratio
]{{{dcb_plot}}}

\vspace{{1mm}}

\scriptsize
{fit_info(dcb_data, process, category)}

\end{{minipage}}
"""

    else:

        dcb_panel = rf"""
\begin{{minipage}}[c][0.72\textheight][c]{{0.47\textwidth}}
\centering

\textbf{{Double Crystal Ball (DCB)}}\\[5mm]

\fbox{{
\begin{{minipage}}[c][0.58\textheight][c]{{0.90\textwidth}}
\centering
\Large
\textcolor{{red}}{{MISSING PLOT}}

\vspace{{5mm}}

\normalsize
No PDF found for this\\
era / production / category.
\end{{minipage}}
}}

\vspace{{2mm}}

\scriptsize
{fit_info(dcb_data, process, category)}

\end{{minipage}}
"""

    # --------------------------------------------------------
    # Complete frame
    # --------------------------------------------------------

    return rf"""
\begin{{frame}}[t]{{{latex_escape(title)}}}

\vspace{{2mm}}

\begin{{columns}}[T]

\column{{0.50\textwidth}}
{sog_panel}

\column{{0.50\textwidth}}
{dcb_panel}

\end{{columns}}

\end{{frame}}
"""


# ============================================================
# Generate one category .tex
# ============================================================

def generate_category_tex(
    category,
    sog_data,
    dcb_data,
    output_dir,
):

    tex_path = os.path.join(
        output_dir,
        f"signal_comparison_{category}.tex"
    )

    with open(tex_path, "w") as f:

        f.write(
r"""
\documentclass[aspectratio=169,10pt]{beamer}

\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{array}

\setbeamertemplate{navigation symbols}{}

\setbeamertemplate{footline}{
  \hbox{
    \begin{beamercolorbox}[
      wd=\paperwidth,
      ht=2.5ex,
      dp=1.2ex,
      leftskip=1em,
      rightskip=1em
    ]{author in head/foot}

    \hfill
    \insertframenumber/\inserttotalframenumber

    \end{beamercolorbox}
  }
}

\setbeamertemplate{frametitle}{
  \vspace{0.25cm}
  \begin{beamercolorbox}[wd=\paperwidth,ht=1.0cm]{frametitle}
    \hspace{0.3cm}
    \usebeamerfont{frametitle}
    \insertframetitle
  \end{beamercolorbox}
}

\begin{document}

"""
        )

        # ----------------------------------------------------
        # 64 slides
        # ----------------------------------------------------

        for era in ERAS:

            for process in PROCESSES:

                f.write(
                    make_slide(
                        era,
                        process,
                        category,
                        sog_data.get(era, {}),
                        dcb_data.get(era, {}),
                    )
                )

        f.write(
r"""
\end{document}
"""
        )

    return tex_path


# ============================================================
# Compile PDF
# ============================================================

def compile_tex(tex_path, output_dir):

    tex_name = os.path.basename(tex_path)

    print(f"  Compiling {tex_name}")

    latexmk = shutil.which("latexmk")

    if latexmk:

        cmd = [
            latexmk,
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-output-directory=" + output_dir,
            tex_path,
        ]

        result = subprocess.run(cmd)

    else:

        print(
            "  [INFO] latexmk not found, using pdflatex twice"
        )

        cmd = [
            "pdflatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-output-directory",
            output_dir,
            tex_path,
        ]

        result = subprocess.run(cmd)

        if result.returncode == 0:
            result = subprocess.run(cmd)

    if result.returncode != 0:

        print(
            f"[ERROR] LaTeX compilation failed for {tex_name}"
        )

        return False

    pdf = os.path.join(
        output_dir,
        tex_name.replace(".tex", ".pdf")
    )

    if os.path.isfile(pdf):

        print(f"  --> {pdf}")
        return True

    print(
        f"[ERROR] PDF was not created: {pdf}"
    )

    return False


# ============================================================
# Missing plot report
# ============================================================

def write_missing_report(
    output_dir,
    sog_data,
    dcb_data,
):

    report = os.path.join(
        output_dir,
        "missing_plots.txt"
    )

    with open(report, "w") as f:

        f.write(
            "Missing signal-fit plots\n"
            "========================\n\n"
        )

        for category in CATEGORIES:

            f.write(
                f"\nCategory: {category}\n"
                f"{'-' * 60}\n"
            )

            for era in ERAS:

                for process in PROCESSES:

                    sog_plot = get_plot_path(
                        era,
                        "SoG",
                        process,
                        category
                    )

                    dcb_plot = get_plot_path(
                        era,
                        "DCB",
                        process,
                        category
                    )

                    if not sog_plot or not dcb_plot:

                        f.write(
                            f"{era:15s} "
                            f"{process:15s} "
                            f"SoG={'OK' if sog_plot else 'MISSING':7s} "
                            f"DCB={'OK' if dcb_plot else 'MISSING':7s}\n"
                        )

    print(f"  --> Missing report: {report}")


# ============================================================
# Main
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Create category-centric SoG vs DCB signal-fit "
            "comparison PDFs."
        )
    )

    parser.add_argument(
        "--output",
        default="signal_comparison_output",
        help="Output directory"
    )

    parser.add_argument(
        "--category",
        default=None,
        help="Only generate one category"
    )

    args = parser.parse_args()

    output_dir = os.path.abspath(args.output)

    os.makedirs(output_dir, exist_ok=True)

    # --------------------------------------------------------
    # Load logs
    # --------------------------------------------------------

    print("\nLoading SoG logs...")

    sog_data = load_logs(
        os.path.join(
            BASE,
            "logs_SoG"
        )
    )

    print("\nLoading DCB logs...")

    dcb_data = load_logs(
        os.path.join(
            BASE,
            "logs_DCB"
        )
    )

    # --------------------------------------------------------
    # Categories
    # --------------------------------------------------------

    if args.category:

        if args.category not in CATEGORIES:

            print(
                f"[ERROR] Unknown category: {args.category}"
            )

            print("Available categories:")

            for c in CATEGORIES:
                print("  ", c)

            return

        categories = [args.category]

    else:

        categories = CATEGORIES

    # --------------------------------------------------------
    # Generate
    # --------------------------------------------------------

    print("\n============================================")
    print("Generating category-centric signal slides")
    print("============================================\n")

    for category in categories:

        print(
            f"\n{'=' * 60}\n"
            f"Category: {category}\n"
            f"{'=' * 60}"
        )

        tex_path = generate_category_tex(
            category,
            sog_data,
            dcb_data,
            output_dir,
        )

        compile_tex(
            tex_path,
            output_dir
        )

    # --------------------------------------------------------
    # Missing report
    # --------------------------------------------------------

    write_missing_report(
        output_dir,
        sog_data,
        dcb_data
    )

    print(
        "\n============================================"
    )

    print(
        f"Done.\n"
        f"Output directory:\n"
        f"{output_dir}"
    )

    print(
        "============================================\n"
    )


if __name__ == "__main__":
    main()
