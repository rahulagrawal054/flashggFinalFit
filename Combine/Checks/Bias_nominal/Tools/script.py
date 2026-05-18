import sys
import os
import glob
import argparse
import ROOT

# -----------------------------
# Get correct POI safely
# -----------------------------
def get_valid_poi(tree, category):
    branches = [b.GetName() for b in tree.GetListOfBranches()]

    if category.startswith("ttH") and "r_ttH" in branches:
        return "r_ttH"
    elif category.startswith("tH") and "r_tH" in branches:
        return "r_tH"
    return None


# -----------------------------
# Process each ROOT file
# -----------------------------
def process_file(root_file, category, func, out_dir):
    f = ROOT.TFile.Open(root_file)
    if not f or f.IsZombie():
        print(f"[ERROR] Cannot open {root_file}")
        return False

    tree = f.Get("limit")
    if not tree:
        print(f"[ERROR] No 'limit' tree in {root_file}")
        return False

    poi = get_valid_poi(tree, category)
    if poi is None:
        print(f"[ERROR] Missing POI in {root_file}")
        return False

    # -----------------------------
    # Counts
    # -----------------------------
    total_entries = tree.GetEntries()

    cut_bf   = "quantileExpected == -1.0"
    cut_down = "quantileExpected > -0.33 && quantileExpected < -0.31"
    cut_up   = "quantileExpected > 0.31 && quantileExpected < 0.33"

    n_bf   = tree.GetEntries(cut_bf)
    n_down = tree.GetEntries(cut_down)
    n_up   = tree.GetEntries(cut_up)

    print(f"FILE: {root_file}")
    print(f"Total: {total_entries} | BF: {n_bf} | -1σ: {n_down} | +1σ: {n_up}")

    # -----------------------------
    # Plot
    # -----------------------------
    ROOT.gROOT.SetBatch(True)
    c1 = ROOT.TCanvas("c1", "c1", 900, 700)

    tree.Draw(f"{poi}>>h_bf(50)", cut_bf)
    h_bf = ROOT.gDirectory.Get("h_bf")

    tree.Draw(f"{poi}>>h_down(50)", cut_down)
    h_down = ROOT.gDirectory.Get("h_down")

    tree.Draw(f"{poi}>>h_up(50)", cut_up)
    h_up = ROOT.gDirectory.Get("h_up")

    if not h_bf:
        print("[WARNING] Empty histogram")
        return False

    # Style improvements
    h_bf.SetLineColor(ROOT.kBlack)
    h_bf.SetLineWidth(3)
    h_bf.SetTitle(f"{category} ({func}); {poi}; Toys")
    h_bf.SetStats(0)

    if h_down:
        h_down.SetLineColor(ROOT.kBlue)
        h_down.SetLineWidth(2)
        h_down.SetLineStyle(2)

    if h_up:
        h_up.SetLineColor(ROOT.kRed)
        h_up.SetLineWidth(2)
        h_up.SetLineStyle(2)

    max_y = max(
        h_bf.GetMaximum(),
        h_down.GetMaximum() if h_down else 0,
        h_up.GetMaximum() if h_up else 0,
    )
    h_bf.SetMaximum(max_y * 1.4)

    h_bf.Draw("HIST")
    if h_down:
        h_down.Draw("HIST SAME")
    if h_up:
        h_up.Draw("HIST SAME")

    # Legend
    leg = ROOT.TLegend(0.65, 0.75, 0.88, 0.88)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.03)
    leg.AddEntry(h_bf, "Best Fit", "l")
    if h_up:
        leg.AddEntry(h_up, "+1 Sigma", "l")
    if h_down:
        leg.AddEntry(h_down, "-1 Sigma", "l")
    leg.Draw()

    # Text on plot
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.035)
    text = f"Total: {total_entries} | BF: {n_bf} | -1#sigma: {n_down} | +1#sigma: {n_up}"
    latex.DrawLatex(0.15, 0.85, text)

    # -----------------------------
    # Save
    # -----------------------------
    out_name = f"{category}_{func}"
    png_path = os.path.join(out_dir, out_name + ".png")
    pdf_path = os.path.join(out_dir, out_name + ".pdf")

    c1.SaveAs(png_path)
    c1.SaveAs(pdf_path)

    return True


# -----------------------------
# Main
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Batch Bias Plotter")
    parser.add_argument("--baseDir", required=True)
    parser.add_argument("--outDir", default="plots")
    args = parser.parse_args()

    os.makedirs(args.outDir, exist_ok=True)

    error_files = []

    for category in os.listdir(args.baseDir):
        cat_path = os.path.join(args.baseDir, category)
        if not os.path.isdir(cat_path):
            continue

        bias_dirs = glob.glob(os.path.join(cat_path, "BiasFits_*"))

        for bdir in bias_dirs:
            root_files = glob.glob(os.path.join(bdir, "biasStudy_*_fits.root"))

            for rf in root_files:
                func = os.path.basename(rf)\
                    .replace("biasStudy_", "")\
                    .replace("_fits.root", "")

                ok = process_file(rf, category, func, args.outDir)

                if not ok:
                    error_files.append(rf)

    # -----------------------------
    # Save failed files
    # -----------------------------
    error_txt = os.path.join(args.outDir, "failed_files.txt")
    with open(error_txt, "w") as f:
        for ef in error_files:
            f.write(ef + "\n")

    print("\nDone!")
    print(f"Failed files saved in: {error_txt}")


if __name__ == "__main__":
    main()
