#!/bin/bash
cp /eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Datacard/Datacard.txt .
# Step 1: Create workspaces
python3 RunText2Workspace.py --mode r_ttH_1D --batch local

# Step 2: Prepare fit jobs (dry run)
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D --dryRun

# Step 3: Run all fits (20 jobs)
for i in {0..19}; do
  ./runFits_r_ttH_1D/condor_profile1D_WithSyst_fixedMH_r_ttH.sh $i
done

# Step 4: Collect fit results
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D

