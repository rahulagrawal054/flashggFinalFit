#!/usr/bin/env python3

import ROOT
import argparse
import sys

parser = argparse.ArgumentParser(description="Basic check for toy ROOT file before fitting")
parser.add_argument("--inputToyRootFile", required=True, help="Path to toy ROOT file")
args = parser.parse_args()

f = ROOT.TFile.Open(args.inputToyRootFile)

if not f or f.IsZombie():
    print("❌ Cannot open ROOT file")
    sys.exit(1)

t = f.Get("limit")
if not t:
    print("❌ 'limit' TTree not found")
    sys.exit(1)

entries = t.GetEntries()

itoys = set()
seeds = set()

for i in range(entries):
    t.GetEntry(i)
    itoys.add(t.iToy)
    seeds.add(t.iSeed)

print("Total entries:", entries)
print("Unique toys:", len(itoys))
print("Seed values:", list(seeds))

if entries > 0 and len(itoys) == entries:
    print("✅ Toy file looks good and ready for fitting")
else:
    print("❌ Toy file structure problem detected")
