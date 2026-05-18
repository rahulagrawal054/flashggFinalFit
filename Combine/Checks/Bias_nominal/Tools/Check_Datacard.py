import ROOT as r
r.gROOT.SetBatch(True)
r.gStyle.SetOptStat(0)

# ---------- INPUT ----------
rootfile = "Datacard/Datacard_ttH_had_1.root"
workspace_name = "w"   # change if different
# ---------------------------

print("\n[DEBUG] Opening file:", rootfile)
f = r.TFile.Open(rootfile)
if not f or f.IsZombie():
    raise RuntimeError("Cannot open ROOT file")

print("[DEBUG] Getting workspace:", workspace_name)
ws = f.Get(workspace_name)
if not ws:
    raise RuntimeError("Workspace not found")

print("\n[DEBUG] Workspace content:")
#ws.Print()

# ---------- FIND MULTIPDF ----------
multipdf = None
print("\n[DEBUG] Scanning PDFs...")
for pdf in ws.allPdfs():
    print("  PDF:", pdf.GetName(), "| Class:", pdf.ClassName())
    if pdf.InheritsFrom("RooMultiPdf"):
        multipdf = pdf

if not multipdf:
    raise RuntimeError("No RooMultiPdf found")

print("\n[DEBUG] Found RooMultiPdf:", multipdf.GetName())
print("[DEBUG] Number of PDFs:", multipdf.getNumPdfs())

# ---------- FIND INDEX ----------
indexCat = None
print("\n[DEBUG] Scanning categories...")
for cat in ws.allCats():
    print("  Category:", cat.GetName())
    if cat.GetName().startswith("pdfindex"):
        indexCat = cat

if not indexCat:
    raise RuntimeError("pdfindex category not found")

print("\n[DEBUG] Found index category:", indexCat.GetName())

# ---------- LIST COMPONENT PDFs ----------
print("\n[DEBUG] Component PDFs:")
for i in range(multipdf.getNumPdfs()):
    pdf = multipdf.getPdf(i)
    print(f"  [{i}] {pdf.GetName()}  ({pdf.ClassName()})")

print("\n[DEBUG] Done.")

