import ROOT
import argparse
import sys
import os
import re
import glob

def set_cms_style():
    """Sets professional CMS styling for the pads and histograms."""
    ROOT.gStyle.SetOptStat(1111)  # Show Entries, Mean, RMS
    ROOT.gStyle.SetOptFit(111)    # Show Fit Parameters
    ROOT.gStyle.SetStatX(0.9)     # Stat box top-right X
    ROOT.gStyle.SetStatY(0.9)     # Stat box top-right Y
    ROOT.gStyle.SetStatW(0.2)     # Width of stat box
    ROOT.gStyle.SetStatH(0.15)    # Height of stat box
    ROOT.gStyle.SetPadTickX(1)
    ROOT.gStyle.SetPadTickY(1)
    ROOT.gStyle.SetLegendBorderSize(0)
    return ROOT.TLatex()

def process_file(file_path, truth, poi, category, out_name):
    if not os.path.exists(file_path): return
    
    f = ROOT.TFile.Open(file_path)
    tree = f.Get("limit")
    if not tree: return
    
    n_entries = tree.GetEntries()
    n_toys = int(n_entries / 3) # 

    h_bias = ROOT.TH1F(f"h_bias_{out_name}", f";Measured {poi};Entries", 40, truth - 3.0, truth + 3.0)
    h_pull = ROOT.TH1F(f"h_pull_{out_name}", ";(#hat{#mu} - #mu_{true}) / #sigma;Entries", 40, -4, 4)

    # Triplet processing logic 
    for i in range(n_toys):
        tree.GetEntry(3 * i)
        r_bf = getattr(tree, poi)
        tree.GetEntry(3 * i + 1)
        r_lo = getattr(tree, poi)
        tree.GetEntry(3 * i + 2)
        r_hi = getattr(tree, poi)

        sigma = (r_hi - r_lo) / 2.0
        if sigma > 1e-5:
            h_bias.Fill(r_bf)
            h_pull.Fill((r_bf - truth) / sigma)

    # --- Canvas Configuration ---
    # Increased height slightly to accommodate the labels "above" the box
    c = ROOT.TCanvas(f"c_{out_name}", "", 1200, 700)
    c.Divide(2, 1)
    latex = set_cms_style()

    # Panel 1: Bias
    c.cd(1)
    ROOT.gPad.SetTopMargin(0.12) # Extra space for CMS label
    ROOT.gPad.SetLeftMargin(0.15)
    h_bias.SetLineColor(ROOT.kBlue+1)
    h_bias.SetLineWidth(2)
    h_bias.Draw("HIST")
    h_bias.Fit("gaus", "SQ")
    
    # CMS Label (placed slightly above the frame)
    latex.SetTextFont(61); latex.SetTextSize(0.05)
    latex.DrawLatexNDC(0.15, 0.91, "CMS")
    latex.SetTextFont(52); latex.SetTextSize(0.04)
    latex.DrawLatexNDC(0.26, 0.91, "Preliminary Simulation") # Italics

    # Panel 2: Pull
    c.cd(2)
    ROOT.gPad.SetTopMargin(0.12)
    ROOT.gPad.SetLeftMargin(0.15)
    h_pull.SetLineColor(ROOT.kRed+1)
    h_pull.SetLineWidth(2)
    h_pull.Draw("E") # Standard pull draw with error bars
    h_pull.Fit("gaus", "SQ", "", -3, 3)

    # Lumi and Energy Header (Top Right, out of box)
    latex.SetTextFont(42); latex.SetTextSize(0.04)
    latex.DrawLatexNDC(0.58, 0.91, "61.9 fb^{-1} (13.6 TeV)")

    # Category and Mu labels (Placed in clear area of the plot)
    latex.SetTextSize(0.035)
    latex.DrawLatexNDC(0.18, 0.84, f"Category: {category}")
    latex.DrawLatexNDC(0.18, 0.79, f"Injected #mu = {truth}")

    # Final Save
    c.SaveAs(f"Diagnostic_{out_name}.png")
    c.SaveAs(f"Diagnostic_{out_name}.pdf")
    f.Close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="ROOT file")
    parser.add_argument("-t", "--truth", type=float, help="Truth value")
    parser.add_argument("--poi", default="r_ttH")
    parser.add_argument("--cat", default="Category")
    parser.add_argument("--auto", action="store_true", help="Run over all mu folders")
    args = parser.parse_args()

    ROOT.gROOT.SetBatch(True)

    if args.auto:
        # Automated looping over the 88 folders structure
        categories = ["ttH_had_1", "ttH_had_2", "ttH_lep_1", "ttH_lep_2", 
                      "tH_had_1", "tH_had_2", "tH_lep_1", "tH_lep_2"]
        
        for cat in categories:
            # Set POI based on category name 
            poi_to_use = "r_ttH" if "ttH" in cat else "r_tH"
            folders = glob.glob(f"{cat}_mu*")
            
            for folder in folders:
                mu_match = re.search(r"mu([0-9.]+)", folder)
                if not mu_match: continue
                mu_val = float(mu_match.group(1))
                
                # Check within the Expected results subfolder 
                root_files = glob.glob(f"{folder}/BiasFits_Expected.{mu_val}/*_fits.root")
                for rf in root_files:
                    func = os.path.basename(rf).split('_')[1]
                    out_tag = f"{cat}_mu{mu_val}_{func}"
                    process_file(rf, mu_val, poi_to_use, cat, out_tag)
    else:
        # Manual run for single file
        if args.file and args.truth is not None:
            process_file(args.file, args.truth, args.poi, args.cat, "manual_plot")
        else:
            print("Usage: python3 plotBias3.py --auto  OR  -f <file> -t <truth>")

if __name__ == "__main__":
    main()
