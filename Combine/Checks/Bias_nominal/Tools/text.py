import ROOT

file = "tH_lep_1_mu0/BiasFits_Expected.0.0/biasStudy_bern1_fits.root"

f = ROOT.TFile.Open(file)
t = f.Get("limit")

entries = t.GetEntries()

n_toys = entries // 3

failed = 1000 - n_toys
boundary = 0

for i in range(n_toys):

    hit_boundary = False

    for j in range(3):   # nominal, +1σ, -1σ
        idx = i*3 + j
        t.GetEntry(idx)

        poi = t.r_tH

        if poi <= -50 or poi >= 50:
            hit_boundary = True

    if hit_boundary:
        boundary += 1


print("Total toys expected :",1000)
print("Toys fitted        :",n_toys)
print("Failed toys        :",failed)
print("Boundary toys      :",boundary)

f.Close()
