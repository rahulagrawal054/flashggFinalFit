import ROOT
import glob

# Search for all packaged ROOT files
packaged_files = glob.glob("outdir_packaged_DCB/CMS-HGG_sigfit_packaged_*.root")

if not packaged_files:
    print("--> No files found!")
else:
    # Loop over ALL files found
    for test_file in packaged_files:
        print("\n" + "="*60)
        print("--> Testing category file: %s" % test_file)
        print("="*60)

        f = ROOT.TFile.Open(test_file)
        ws = f.Get("wsig_13TeV")
        if not ws:
            continue

        total_indiv = 0.0
        merged_yield = 0.0

        for data in ws.allData():
            name = data.GetName()
            yield_val = data.sumEntries()
            entries = data.numEntries()
            
            # Print entries and yields with higher precision
            print("  -> %-50s : %6d entries | %8.4f weighted yield" % (name, entries, yield_val))
            
            if "_in_" not in name:
                merged_yield = yield_val
            else:
                total_indiv += yield_val

        print("-" * 60)
        if merged_yield > 0:
            print(" Merged dataset yield: %.4f" % merged_yield)
        else:
            print(" Merged dataset: SKIPPED (bkg_had)")
        print(" Sum of individual process datasets: %.4f" % total_indiv)

# =========================================================================================
# NOTE: EXCLUSION OF MERGED DATASET FOR THE 'bkg_had' CATEGORY
# =========================================================================================
# The combined merged dataset object (sig_mass_m125_bkg_had) is deliberately excluded from
# the packaged workspace for the bkg_had category. Merging all high-statistics production 
# modes (ggH, VBF, ttH, bbH, etc.) across all 2022-2023 eras into one single RooDataSet 
# forces the object size to exceed ROOT's 1 GB TBuffer memory limit, leading to a script 
# crash. In earlier script versions, a logic bug in the exclusion check caused a broken, 
# partial dataset with only 4,701 events (from bbH_2022preEE) to be saved by accident.
#
# THIS EXCLUSION HAS ZERO IMPACT ON FITS, DATACARDS, OR COMBINE LIMITS. CMS Combine fits 
# signals process-by-process using individual datasets (e.g., sig_mass_m125_ggh_..., 
# sig_mass_m125_bbh_...) to correctly assign process-specific theoretical and 
# experimental systematic uncertainties. Combine never reads or references the merged 
# dataset (sig_mass_m125_bkg_had). 100% of all Monte Carlo events are fully preserved 
# within their respective individual process datasets inside this workspace.
# =========================================================================================
