import argparse
import json
import os
import ROOT as r

def main():
    parser = argparse.ArgumentParser(description="Generate Bias Pull Plots from Combine Fit Trees")
    parser.add_argument("-f", "--file", required=True, help="Input ROOT file from Combine fit")
    parser.add_argument("-n", "--nToys", type=int, default=1000, help="Number of toys to process")
    parser.add_argument("-s", "--expectSignal", type=float, default=0.0, help="Expected signal mu value")
    parser.add_argument("-p", "--poi", default="r_ttH", help="Parameter of interest name")
    parser.add_argument("--gaussianFit", action="store_true", default=True, help="Perform Gaussian fit")

    opts = parser.parse_args()

    r.gROOT.SetBatch(True)

    out_dir = f"BiasPlots_Expected.{opts.expectSignal}"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    tfile = r.TFile.Open(opts.file)
    if not tfile or tfile.IsZombie():
        print(f"Error: Could not open file {opts.file}")
        return

    tree = tfile.Get("limit")
    if not tree:
        print("Error: 'limit' tree not found in file")
        return

    name = os.path.basename(opts.file).replace(".root", "")
    pullHist = r.TH1F(f"pullsForTruth_{name}", f"Pull distribution using the envelope to fit {name}", 80, -4.0, 4.0)
    pullHist.GetXaxis().SetTitle("Pull")
    pullHist.GetYaxis().SetTitle("Entries")

    FIT_BOUNDARY = 800.0
    CHECK_LIMIT = FIT_BOUNDARY - 0.1

    boundaryHits = 0
    pullEntries = 0

    total_entries = tree.GetEntries()
    max_toys = total_entries // 3
    n_toys = min(opts.nToys, max_toys)

    for itoy in range(n_toys):
        # Best-fit value
        tree.GetEntry(3 * itoy)
        if getattr(tree, "quantileExpected") != -1:
            continue
        bf = getattr(tree, opts.poi)

        # -1 sigma value
        tree.GetEntry(3 * itoy + 1)
        if abs(getattr(tree, "quantileExpected") - (-0.32)) >= 0.001:
            continue
        lo = getattr(tree, opts.poi)

        # +1 sigma value
        tree.GetEntry(3 * itoy + 2)
        if abs(getattr(tree, "quantileExpected") - 0.32) >= 0.001:
            continue
        hi = getattr(tree, opts.poi)

        if abs(bf) >= CHECK_LIMIT or abs(lo) >= CHECK_LIMIT or abs(hi) >= CHECK_LIMIT:
            boundaryHits += 1

        diff = bf - opts.expectSignal
#        unc = 0.5 * (hi - lo)

        if diff >= 0:
            unc = bf - lo  # Use low error for positive fluctuations
        else:
            unc = hi - bf  # Use high error for negative fluctuations

        if unc > 0.0:
            pullHist.Fill(diff / unc)
            pullEntries += 1

    canv = r.TCanvas("canv", "", 800, 600)
    pullHist.Draw()

    mean = -999.0
    sigma = -999.0

    if opts.gaussianFit:
        r.gStyle.SetOptFit(111)
        pullHist.Fit("gaus")
        fitFunc = pullHist.GetFunction("gaus")
        if fitFunc:
            mean = fitFunc.GetParameter(1)
            sigma = fitFunc.GetParameter(2)

    failedToys = opts.nToys - pullEntries
    biasResults = {
        name: {
            "expectSignal": opts.expectSignal,
            "bias": mean,
            "sigma": sigma,
            "pullEntries": int(pullEntries),
            "failedToys": int(failedToys),
            "boundaryHits": int(boundaryHits),
            "meanPull": pullHist.GetMean(),
            "rmsPull": pullHist.GetRMS()
        }
    }

    out_prefix = os.path.join(out_dir, name)
    canv.SaveAs(f"{out_prefix}.pdf")
    canv.SaveAs(f"{out_prefix}.png")

    outJson = os.path.join(out_dir, "BiasResults.json")
    with open(outJson, "w") as f:
        json.dump(biasResults, f, indent=2)

    print(f"\nProcessing complete:")
    print(f" - Saved plots to: {out_prefix}.pdf / .png")
    print(f" - Saved JSON to:  {outJson}\n")

if __name__ == "__main__":
    main()
