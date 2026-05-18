import ROOT as r
f = r.TFile("tH_lep_1_mu0/BiasFits_Expected.0.0/biasStudy_bern1_fits.root")
tree = f.Get("limit")

# Count how many toys actually have 'valid' crossings
failures = 0
for i in range(tree.GetEntries()):
    tree.GetEntry(i)
    # Status < 0 or 0 often indicates issues depending on the algorithm
    # In MultiDimFit, we usually look at the 'deltaNLL'
    if tree.deltaNLL > 100: # Example: Extremely high NLL means the fit blew up
        failures += 1

print(f"Total entries: {tree.GetEntries()}")
