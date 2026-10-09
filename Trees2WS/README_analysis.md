# Trees2WS: ttH and tH analysis documentation

This document describes the local Trees2WS workflow for the 2022 and 2023 analysis.
The official README.md is retained separately.

Last updated: 2026-10-09. Based on source inspection; the commands below are
examples and were not executed when writing this document.

## Purpose

Trees2WS converts category-based HiggsDNA ROOT trees into RooWorkspaces for
flashggFinalFit signal and background modelling. A RooWorkspace is a container
inside a ROOT file holding variables and datasets.

### Weighted RooDataSet: individual events

A RooDataSet is like a table with one row for each event. This is **unbinned**:
each event keeps its individual mass.

| Event | Mass (GeV) | Weight |
| --- | --- | --- |
| 1 | 124.10 | 0.8 |
| 2 | 124.35 | 1.4 |
| 3 | 125.20 | 0.5 |

There are three event rows, but their total weighted contribution is
0.8 + 1.4 + 0.5 = 2.7.

trees2ws.py uses the nominal tree's weight branch as the event weight.
Additional columns such as weight_central and Up/Down weight branches are
stored for later use; they are not automatically multiplied into that weight.
MC weights can be fractional or negative.

numEntries() counts event rows. sumEntries() gives the sum of event weights.

### What is a bin?

A **bin is an interval of values**. Here the mass range from 100 to 180 GeV
is divided into 160 intervals, each 0.5 GeV wide:

```text
100.0–100.5, 100.5–101.0, ..., 124.0–124.5, 124.5–125.0, ...
```

A histogram groups events into these intervals:

| Mass interval (GeV) | Example events in it | Sum of weights |
| --- | --- | --- |
| 124.0–124.5 | 124.10 and 124.35 GeV | 0.8 + 1.4 = 2.2 |
| 124.5–125.0 | No events | 0 |
| 125.0–125.5 | 125.20 GeV | 0.5 |

### Weighted RooDataHist: accumulated weights in bins

A RooDataHist stores bin coordinates and the accumulated weight in each bin.
For example, the interval 124.0–124.5 GeV is represented by its centre,
124.25 GeV, and content 2.2. It no longer retains 124.10 and 124.35 as
separate event masses.

**The systematic RooDataHists are also weighted.** Each event adds its weight
from the corresponding variation tree to its bin. The weight is a contribution
to bin content, not a histogram axis. Negative weights can reduce bin content.

With the current config, the histogram coordinates are CMS_hgg_mass and GenNBJet.
GenNBJet has one bin in the code, so it does not separate different b-jet
counts into distinct bins. The example above explains the mass axis.

For RooDataHist, numEntries() refers to stored bins, not original events.
sumEntries() gives the total bin content.

### Observed data are unbinned

Yes. trees2ws_data.py keeps one row per accepted data event, retaining its
individual mass and assigning weight 1. Three accepted events contribute three.

| Output object | Mass storage | Contribution |
| --- | --- | --- |
| Nominal MC RooDataSet | Individual masses: unbinned | Nominal event weight |
| Systematic MC RooDataHist | Mass intervals: binned | Variation weights summed in each bin |
| Data RooDataSet | Individual masses: unbinned | 1 per accepted event |

Setting 160 bins on the mass variable does **not** bin a RooDataSet.
Those intervals are used when creating the RooDataHist.

## Files

| File or directory | Role |
| --- | --- |
| trees2ws.py | Convert MC trees into inclusive or fiducial in/out workspaces |
| trees2ws_data.py | Convert observed-data trees |
| config_ttH_tH_2022_2023.py | Configure branches, variations, and categories |
| inputs_27June/ | Input trees and per-sample conversion outputs |
| workspaces/ | Outputs organized for downstream use |

## Input samples and eras

The input collection is inputs_27June/, organized into <sample>_<era> directories.

Samples: GluGluH, VBFH, VH, bbH, ttH, tHqHad, tHqLep, and tHW.

Eras: 2022preEE, 2022postEE, 2023preBPix, and 2023postBPix.

Observed-data input: inputs_27June/Data/allData.root.

The code uses 13TeV in tree and workspace names, including for these Run 3
samples. This is its naming convention.

### Tree naming

```text
Nominal MC:
DiphotonTree/<productionMode>_125_13TeV_<category>

Systematic MC:
DiphotonTree/<productionMode>_125_13TeV_<category>_<systematic>Up01sigma
DiphotonTree/<productionMode>_125_13TeV_<category>_<systematic>Down01sigma

Observed data:
DiphotonTree/Data_13TeV_<category>
```

Example: DiphotonTree/tth_125_13TeV_ttH_had_1.
The MC converter tries a ttH prefix if the requested tth tree is missing.

Analysis categories:

- ttH_had_1 through ttH_had_4
- ttH_lep_1 through ttH_lep_4
- tH_had_1 through tH_had_4
- tH_lep_1 and tH_lep_2
- bkg_had and bkg_lep

The configuration discovers categories from nominal tree names using cats = 'auto'.

## Analysis configuration

config_ttH_tH_2022_2023.py contains the trees2wsCfg dictionary.

| Setting | Value | Meaning |
| --- | --- | --- |
| inputTreeDir | DiphotonTree | Directory inside the ROOT file holding trees |
| mainVars | CMS_hgg_mass, weight, weight_central, dZ, *Up, *Down, fiducialGeometricFlag, GenNBJet | Branches read from nominal MC |
| dataVars | CMS_hgg_mass, weight | Branches read from observed data |
| systematicsVars | CMS_hgg_mass, weight, fiducialGeometricFlag, GenNBJet | Branches read from variation trees |
| theoryWeightContainers | weight_LHEScale: 9 | Array branch and number of values per event |
| cats | auto | Discover reconstructed categories from tree names |

### mainVars: nominal MC branches

| Branch or pattern | Use |
| --- | --- |
| CMS_hgg_mass | Diphoton mass observable |
| weight | Weight used when adding the nominal MC event |
| weight_central | Additional stored column; not automatically applied |
| dZ | Vertex-related quantity retained for later signal modelling |
| *Up and *Down | Wildcards matching nominal branches ending in Up or Down |
| fiducialGeometricFlag | Boolean value used for fiducial selection |
| GenNBJet | Generator-level b-jet count used for fiducial selection; also stored |

Most read branches become nominal dataset columns. fiducialGeometricFlag
is used for selection but excluded from workspace observables.

The wildcard patterns select branches inside nominal trees. They do not
select the separate systematic variation trees.

### dataVars: observed-data branches

The current list is CMS_hgg_mass and weight. The data converter reads both,
but its event loop sets only mass and assigns event weight 1.
It does not use the input weight values to weight accepted events.

### systematicsVars: variation-tree branches

CMS_hgg_mass supplies the varied mass and weight supplies the histogram
contribution. fiducialGeometricFlag and GenNBJet allow fiducial splitting
using each variation tree's values.

When creating histogram coordinates, the code excludes weight and
fiducialGeometricFlag. CMS_hgg_mass and GenNBJet remain.

### theoryWeightContainers: array-valued branches

weight_LHEScale contains nine values per event. The converter expands them
into nine scalar columns in the nominal dataset.

The naming code removes the last character of the container name before
appending an index: weight_LHEScal_0 through weight_LHEScal_8.

These values are stored for later use, not automatically applied to nominal
weights. Their interpretation as factors or absolute weights depends on the
input-tree production.

### systematics: separate variation tree families

The configured names are ElectronScale, ElectronSmearing, FNUF, JecSystTotal,
JerSyst, Material, MET, MuonResolution, MuonScale, ScaleEE, ScaleEB, and Smearing.

With --doSystematics, each name requires both Up01sigma and Down01sigma trees
for every processed category. A separate weighted RooDataHist is produced for
each direction. For example:

```text
tth_125_13TeV_ttH_had_1_ElectronScaleUp01sigma
tth_125_13TeV_ttH_had_1_ElectronScaleDown01sigma
```

### Other configuration entries

diffVar and notagVars are present but are not read by these converters.
The existing empty splitting field is retained for this inclusive/fiducial workflow.

## Conversion workflow

### trees2ws.py: MC

1. Load the config and discover categories.
2. Read nominal branches and theory arrays into pandas dataframes.
3. Read separate systematic trees when --doSystematics is enabled.
4. Select inclusive events or fiducial in/out groups.
5. Fill one weighted nominal RooDataSet per category.
6. Fill weighted RooDataHists for the requested variations.
7. Write the workspace at tagsDumper/cms_hgg_13TeV in a ROOT file.

The converter uses the input weight branch. It does not multiply event
weights by the era luminosity or process cross section.

CMS_hgg_mass is defined over 100–180 GeV with 160 bins.
dZ is defined over -20 to 20 with 40 bins.
Other retained columns, including GenNBJet, have one bin.

The workspace stores intLumi = 1000. The unit relation is
1 fb^-1 = 1000 pb^-1, so 1000 pb^-1 represents a reference luminosity of 1 fb^-1.
The shared code separately defines lumiScaleFactor = 1000 for this conversion.
Trees2WS only stores intLumi: it does not multiply event weights by this value,
and this is not the actual luminosity of an era.

### Inclusive and fiducial definitions

Without --doInOutSplitting, the output process receives the incl suffix.
The current inclusive dataframe mask is CMS_hgg_mass > 0.

With --doInOutSplitting:

```python
in_mask = (fiducialGeometricFlag == True) & (GenNBJet > 0)
out_mask = ~in_mask
```

This selection is applied separately to nominal and variation events.

### Example MC command

Run from Trees2WS after preparing the CMSSW environment:

```bash
python3 trees2ws.py \
  --inputConfig config_ttH_tH_2022_2023.py \
  --inputTreeFile inputs_27June/ttH_2022preEE/output_TTHToGG_M125_13TeV_amcatnlo_pythia8.root \
  --inputMass 125 --productionMode tth --year 2022preEE \
  --doSystematics
```

Add --doInOutSplitting to create both fiducial outputs.
--outputWSDir optionally changes the base output directory.

### trees2ws_data.py: observed data

The script reads the data category trees, rejects nonfinite masses and masses
outside 100–180 GeV, and adds each accepted event with weight 1 to an unbinned
RooDataSet. Each category gets a separate dataset.

```bash
python3 trees2ws_data.py \
  --inputConfig config_ttH_tH_2022_2023.py \
  --inputTreeFile inputs_27June/Data/allData.root
```

--applyMassCut and --massCutRange optionally apply an additional mass selection.
The workspace's 100–180 GeV bounds still apply.
--outputWSDir optionally changes the base output directory.

## Output layout

Default MC outputs:

```text
<input directory>/ws_<mapped process>_incl/<input stem>_<mapped process>_incl.root
<input directory>/ws_<mapped process>_in/<input stem>_<mapped process>_in.root
<input directory>/ws_<mapped process>_out/<input stem>_<mapped process>_out.root
```

The shared dataToProc() mapping determines the process label in filenames.
Dataset names use the requested productionMode and suffix, for example
tth_in_125_13TeV_ttH_had_1.

Default data output: inputs_27June/Data/ws/allData.root.
Data datasets are named Data_13TeV_<category>.

Existing outputs are organized as:

```text
workspaces/
├── Data/allData.root
├── inclusive/<era>/ws_signal/*.root
└── fiducial/<era>/ws_signal/*.root
```

The converters do not perform the later collection into this layout.
They open output files with RECREATE, replacing an existing file at that path.

### Retained data copies

On 2026-10-09, these converted data files were byte-identical:

- inputs_27June/Data/ws/allData.root
- workspaces/Data/allData.root

Size: 1,230,290 bytes.
SHA-256: 19c16a05c6bd6a3f10f3ebdfc7d619aa7dca96c5c7d0703fc3f06d1698d6ffe4

Both copies are intentionally retained. The original input tree file
inputs_27June/Data/allData.root was not part of this comparison.

## Opening and inspecting a converted workspace

### File directory and workspace key

A converted ROOT file has this structure:

```text
output_...root
└── tagsDumper                       ROOT directory
    └── cms_hgg_13TeV                 RooWorkspace
        ├── Variables                CMS_hgg_mass, intLumi, dZ, ...
        ├── Nominal datasets         RooDataSet objects
        └── Systematic histograms    RooDataHist objects
```

Listing tagsDumper shows a key like:

```text
KEY: RooWorkspace  cms_hgg_13TeV;1
```

tagsDumper is the directory; cms_hgg_13TeV is the workspace object.
The ;1 suffix is the ROOT key cycle. Variables and datasets are inside the
workspace, not separate file keys. Use the workspace methods to inspect them.

The examples below use the ttH 2022preEE inclusive workspace that was inspected
on 2026-10-09. Opening a file with READ does not change it.

### Open interactively with ROOT

From the Trees2WS directory, start ROOT:

```bash
root -l
```

At the ROOT prompt:

```cpp
auto f = TFile::Open("inputs_27June/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root", "READ");

// List the top-level keys, including tagsDumper.
f->ls();

// List the keys inside tagsDumper.
auto dir = f->GetDirectory("tagsDumper");
dir->ls();

// Retrieve the workspace and print its contents.
auto w = (RooWorkspace*)f->Get("tagsDumper/cms_hgg_13TeV");
w->Print("v");

// List workspace variables.
w->allVars().Print("v");

// Inspect a particular variable.
auto mass = w->var("CMS_hgg_mass");
mass->Print();
mass->getMin();
mass->getMax();
mass->getBins();
w->var("intLumi")->Print();

// List all datasets and histograms.
for (auto d : w->allData()) {
    std::cout << d->GetName() << "  " << d->ClassName()
              << "  entries=" << d->numEntries()
              << "  sumWeights=" << d->sumEntries() << std::endl;
}
```

### Inspect nominal events

Still at the ROOT prompt:

```cpp
auto nominal = w->data("tth_incl_125_13TeV_ttH_had_1");
nominal->ClassName();       // RooDataSet
nominal->numEntries();      // Number of event rows
nominal->sumEntries();      // Sum of event weights
nominal->Print("v");

// Read the first event, then obtain that event's weight.
auto event = nominal->get(0);
event->Print("v");
event->getRealValue("CMS_hgg_mass");
nominal->weight();
```

Call get(i) before weight(): weight() returns the weight of the current row.
The event weight need not appear as an ordinary column in the printed row.

### Inspect systematic bins

```cpp
auto syst = w->data("tth_incl_125_13TeV_ttH_had_1_ElectronScaleUp01sigma");
syst->ClassName();          // RooDataHist
syst->numEntries();         // Number of stored bins, not input events
syst->sumEntries();         // Sum of bin contents
syst->Print("v");

// Read the first bin.
auto bin = syst->get(0);
bin->Print("v");
bin->getRealValue("CMS_hgg_mass");  // Bin centre
syst->weight();                    // Accumulated weight in this bin

// Print the first five bins.
for (int i = 0; i < 5; ++i) {
    auto row = syst->get(i);
    std::cout << "bin=" << i
              << " massCentre=" << row->getRealValue("CMS_hgg_mass")
              << " content=" << syst->weight() << std::endl;
}
```

For this histogram the first mass centre is 100.25 GeV, representing the
100.0–100.5 GeV interval. It is a bin coordinate, not an individual event mass.
GenNBJet also appears as a coordinate, but has only one bin.

Keep the ROOT file open while using its workspace. When finished:

```cpp
f->Close();
.q
```

### Inspect with Python / PyROOT

Start Python in the prepared CMSSW environment:

```bash
python3 -B
```

Then enter:

```python
import ROOT

path = "inputs_27June/ttH_2022preEE/ws_tth_incl/output_TTHToGG_M125_13TeV_amcatnlo_pythia8_tth_incl.root"
f = ROOT.TFile.Open(path, "READ")
if not f or f.IsZombie():
    raise RuntimeError("Could not open the ROOT file")

f.ls()
f.GetDirectory("tagsDumper").ls()
w = f.Get("tagsDumper/cms_hgg_13TeV")
if not w:
    raise RuntimeError("Workspace not found")

w.Print("v")

# Every workspace variable: name, value, range, and bin count.
for var in w.allVars():
    if var.InheritsFrom("RooRealVar"):
        print(var.GetName(), var.getVal(),
              var.getMin(), var.getMax(), var.getBins())

# Every dataset or histogram.
for obj in w.allData():
    print(obj.GetName(), obj.ClassName(),
          obj.numEntries(), obj.sumEntries())

nominal = w.data("tth_incl_125_13TeV_ttH_had_1")
syst = w.data("tth_incl_125_13TeV_ttH_had_1_ElectronScaleUp01sigma")

# Show columns / coordinates and the first five rows of each object.
for obj in [nominal, syst]:
    print("\n", obj.GetName(), obj.ClassName())
    obj.get(0).Print("v")
    for i in range(min(5, obj.numEntries())):
        row = obj.get(i)
        print(i, row.getRealValue("CMS_hgg_mass"), obj.weight())

# Close only after finishing inspection.
f.Close()
```

For observed data, use workspaces/Data/allData.root and retrieve a dataset
such as w.data("Data_13TeV_ttH_had_1"). It is a RooDataSet with unit weights.

### Verified example from the existing ttH file

Direct inspection found 16 RooDataSets and 384 RooDataHists in this workspace:
16 categories × 12 systematic families × 2 directions = 384 histograms.

For category ttH_had_1:

| Object | Class in workspace | Stored entries | Sum of weights |
| --- | --- | --- | --- |
| Nominal | RooDataSet | 86,921 events | 0.0348150088 |
| ElectronScale Up | RooDataHist | 160 bins | 0.0348239238 |
| ElectronScale Down | RooDataHist | 160 bins | 0.0348947916 |

The original ElectronScale Up input is a TTree with 86,923 events. Its
converted RooDataHist has 160 bins: those events have been grouped and weighted.

Examples of actual ElectronScale Up contents:

| Mass interval (GeV) | Stored centre (GeV) | Bin content |
| --- | --- | --- |
| 100.0–100.5 | 100.25 | 0.0000078241 |
| 100.5–101.0 | 100.75 | 0.0000023249 |
| 101.0–101.5 | 101.25 | -0.0000032724 |

These are stored MC weight sums, not luminosity-scaled expected event counts.
The negative bin content reflects negative MC weights.

## Environment and dependencies

The repository setup.sh initializes the CMSSW runtime and adds
flashggFinalFit/commonTools to PYTHONPATH.

The converters use ROOT/PyROOT with RooFit, uproot, pandas, and NumPy.
Awkward is also imported by the MC script. The shared commonObjects.py
and commonTools.py modules provide paths, process mappings, the energy label,
and the workspace name.
