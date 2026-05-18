import ROOT as r
import sys

rootfile = sys.argv[1]   # pass file as argument
treename = "limit"
poi = "r_ttH"                # change if needed

f = r.TFile.Open(rootfile)
if not f or f.IsZombie():
    print("❌ Cannot open file")
    sys.exit(1)

tree = f.Get(treename)
if not tree:
    print("❌ Tree 'limit' not found")
    sys.exit(1)

print("\n✅ File opened:", rootfile)
print("Entries:", tree.GetEntries())

print("\n📌 Tree structure:")
tree.Print()

print("\n📌 First 20 entries:")
for i in range(min(20, tree.GetEntries())):
    tree.GetEntry(i)
    print(
        f"Entry {i:3d} | "
        f"quantileExpected={tree.quantileExpected:6.3f} | "
        f"{poi}={getattr(tree, poi):8.4f}"
    )

print("\n📌 Check toy structure (groups of 3):")
for itoy in range(min(5, tree.GetEntries()//3)):
    print(f"\nToy {itoy}")
    for j in range(3):
        idx = 3*itoy + j
        tree.GetEntry(idx)
        print(
            f"  Entry {idx}: "
            f"quantileExpected={tree.quantileExpected:6.3f}, "
            f"{poi}={getattr(tree, poi):8.4f}"
        )

print("\n✅ Debug done.")

