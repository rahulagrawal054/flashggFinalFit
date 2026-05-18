#!/usr/bin/env python3
import ROOT
import sys

def check_effective_entries(filenames, max_toys=10):
    for filename in filenames:
        print(f"\nFile: {filename}")
        f = ROOT.TFile.Open(filename)
        if not f or f.IsZombie():
            print(f"Cannot open file {filename}")
            continue

        toys = f.Get("toys")
        if not toys:
            print("No 'toys' directory found!")
            f.Close()
            continue

        keys = toys.GetListOfKeys()
        n_toys = min(max_toys, len(keys))
        for i in range(n_toys):
            key = keys[i]
            ds = key.ReadObj()
            n_entries = ds.numEntries()
            eff_entries = ds.sumEntries()
            print(f"Dataset {key.GetName()} has {n_entries} entries, effective entries: {eff_entries:.2f}")

        f.Close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_effective_entries.py file1.root [file2.root ...]")
    else:
        check_effective_entries(sys.argv[1:])

