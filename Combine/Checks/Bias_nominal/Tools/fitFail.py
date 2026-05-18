import os
import re
import ROOT
import matplotlib.pyplot as plt

base_dir = "."
data_fail = {}
data_bound = {}

for d in os.listdir(base_dir):

    m = re.match(r"(.*)_mu(\d+)", d)
    if not m:
        continue

    cat = m.group(1)
    mu = int(m.group(2))

    poi_name = "r_ttH" if cat.startswith("ttH") else "r_tH"

    mu_dir = os.path.join(base_dir,d)

    for sub in os.listdir(mu_dir):

        if not sub.startswith("BiasFits_Expected"):
            continue

        fit_dir = os.path.join(mu_dir,sub)

        for f in os.listdir(fit_dir):

            if not f.endswith(".root") or "split" in f:
                continue

            func = re.search(r"biasStudy_(.*)_fits.root",f).group(1)

            path = os.path.join(fit_dir,f)
            rf = ROOT.TFile.Open(path)

            t = rf.Get("limit")
            entries = t.GetEntries()

            n_toys = entries // 3
            failed = 1000 - n_toys

            boundary = 0

            for i in range(n_toys):

                hit = False

                for j in range(3):

                    idx = i*3 + j
                    t.GetEntry(idx)

                    poi = getattr(t,poi_name)

                    if poi <= -50 or poi >= 50:
                        hit = True

                if hit:
                    boundary += 1

            data_fail.setdefault(cat,{})
            data_fail[cat].setdefault(func,{})
            data_fail[cat][func][mu] = failed

            data_bound.setdefault(cat,{})
            data_bound[cat].setdefault(func,{})
            data_bound[cat][func][mu] = boundary

            rf.Close()


for cat in data_fail:

    plt.figure()

    for func in data_fail[cat]:

        mus = sorted(data_fail[cat][func].keys())

        fails = [data_fail[cat][func][m] for m in mus]
        bounds = [data_bound[cat][func][m] for m in mus]

        plt.plot(mus,fails,marker='o',label=f"{func} fail")
        plt.plot(mus,bounds,marker='o',linestyle='dotted',label=f"{func} boundary")

    plt.xlabel("mu")
    plt.ylabel("Number of toys")
    plt.title(cat)
    plt.legend(fontsize=8)
    plt.grid(True)

    plt.savefig(f"{cat}_fail_boundary.png")
    plt.close()
