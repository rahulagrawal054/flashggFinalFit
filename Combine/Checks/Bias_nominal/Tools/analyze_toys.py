import sys
import argparse
import ROOT

def main():
    # 1. Setup command line arguments
    parser = argparse.ArgumentParser(description="Analyze Combine Toys and plot distributions.")
    parser.add_argument("filename", help="Path to the ROOT file (e.g., biasStudy_bern1_fits.root)")
    parser.add_argument("--poi", default="r_ttH", help="Parameter of Interest name (default: r_ttH)")
    args = parser.parse_args()

    # 2. Open the file and get the tree
    f = ROOT.TFile.Open(args.filename)
    if not f or f.IsZombie():
        print(f"[ERROR] Could not open {args.filename}")
        sys.exit(1)

    tree = f.Get("limit")
    if not tree:
        print(f"[ERROR] Could not find 'limit' tree in {args.filename}")
        sys.exit(1)

    # ---------------------------------------------------------
    # TASK 1: Total Entries
    # ---------------------------------------------------------
    total_entries = tree.GetEntries()
    print("="*50)
    print(f"FILE: {args.filename}")
    print(f"Total entries in tree : {total_entries}")

    # ---------------------------------------------------------
    # TASK 2: Count Specific Quantiles
    # ---------------------------------------------------------
    # We use small ranges to safely catch the floating-point numbers
    cut_bf   = "quantileExpected == -1.0"
    cut_down = "quantileExpected > -0.33 && quantileExpected < -0.31"
    cut_up   = "quantileExpected > 0.31 && quantileExpected < 0.33"

    n_bf   = tree.GetEntries(cut_bf)
    n_down = tree.GetEntries(cut_down)
    n_up   = tree.GetEntries(cut_up)

    print("-" * 50)
    print(f"Best Fit entries (-1.0)   : {n_bf}")
    print(f"-1 Sigma entries (-0.32)  : {n_down}")
    print(f"+1 Sigma entries (+0.32)  : {n_up}")
    print("="*50)

    # ---------------------------------------------------------
    # TASK 3: Plot the Distributions
    # ---------------------------------------------------------
    # Run in batch mode so it doesn't try to open a graphical window on lxplus
    ROOT.gROOT.SetBatch(True) 
    
    c1 = ROOT.TCanvas("c1", "Distributions", 800, 600)

    # Draw the branches directly into temporary histograms. 
    # ROOT automatically figures out the best X-axis range!
    tree.Draw(f"{args.poi}>>h_bf", cut_bf)
    h_bf = ROOT.gDirectory.Get("h_bf")

    tree.Draw(f"{args.poi}>>h_down", cut_down)
    h_down = ROOT.gDirectory.Get("h_down")

    tree.Draw(f"{args.poi}>>h_up", cut_up)
    h_up = ROOT.gDirectory.Get("h_up")

    # Format the Best Fit histogram
    h_bf.SetLineColor(ROOT.kBlack)
    h_bf.SetLineWidth(2)
    h_bf.SetTitle(f"Distribution of Toys ({args.poi}); {args.poi}; Number of Toys")
    h_bf.SetStats(0) # Turn off the ugly stat box

    # Format the -1 Sigma histogram
    h_down.SetLineColor(ROOT.kBlue)
    h_down.SetLineWidth(2)
    h_down.SetLineStyle(2) # Dashed line

    # Format the +1 Sigma histogram
    h_up.SetLineColor(ROOT.kRed)
    h_up.SetLineWidth(2)
    h_up.SetLineStyle(2) # Dashed line

    # Find the tallest peak so none of the plots get cut off at the top
    max_y = max(h_bf.GetMaximum(), h_down.GetMaximum(), h_up.GetMaximum())
    h_bf.SetMaximum(max_y * 1.3)

    # Draw them on top of each other
    h_bf.Draw("HIST")
    h_down.Draw("HIST SAME")
    h_up.Draw("HIST SAME")

    # Add a nice legend
    leg = ROOT.TLegend(0.65, 0.75, 0.88, 0.88)
    leg.SetBorderSize(0)
    leg.AddEntry(h_bf, "Best Fit", "l")
    leg.AddEntry(h_up, "+1 Sigma", "l")
    leg.AddEntry(h_down, "-1 Sigma", "l")
    leg.Draw()

    # Save the output
    plot_name = "ToyDistributions.png"
    c1.SaveAs(plot_name)
    c1.SaveAs(plot_name.replace(".png", ".pdf"))
    
    print(f"\n[SUCCESS] Saved plots to {plot_name} and .pdf")

if __name__ == "__main__":
    main()
