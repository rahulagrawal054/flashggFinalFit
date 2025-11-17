#!/bin/bash

# ==============================
# Step 1: Create workspaces
# ==============================
python3 RunText2Workspace.py --mode r_ttH_1D --batch local
python3 RunText2Workspace.py --mode r_tHq_1D --batch local
python3 RunText2Workspace.py --mode r_ttH_1D_tHq_profiled --batch local
python3 RunText2Workspace.py --mode r_tHq_1D_ttH_profiled --batch local

# ==============================
# Step 2: Dry runs
# ==============================
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D --dryRun

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D --dryRun

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D_tHq_profiled --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D_tHq_profiled --dryRun

python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D_ttH_profiled --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D_ttH_profiled --dryRun
# ==============================
# Step 3: Submit fits
# ==============================
for i in {0..19}; do
    ./runFits_r_ttH_1D/condor_profile1D_WithSyst_fixedMH_r_ttH.sh $i
    ./runFits_r_ttH_1D/condor_profile1D_statonly_fixedMH_r_ttH.sh $i

    ./runFits_r_tHq_1D/condor_profile1D_WithSyst_fixedMH_r_tHq.sh $i
    ./runFits_r_tHq_1D/condor_profile1D_statonly_fixedMH_r_tHq.sh $i
    
    ./runFits_r_ttH_1D_tHq_profiled/condor_profile1D_WithSyst_fixedMH_r_tHq.sh $i
    ./runFits_r_ttH_1D_tHq_profiled/condor_profile1D_statonly_fixedMH_r_tHq.sh $i
    
    ./runFits_r_tHq_1D_ttH_profiled/condor_profile1D_WithSyst_fixedMH_r_tHq.sh $i
    ./runFits_r_tHq_1D_ttH_profiled/condor_profile1D_statonly_fixedMH_r_tHq.sh $i
    
done

# ==============================
# Step 4: Collect fits
# ==============================
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D

python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D

python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D_tHq_profiled 
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D_tHq_profiled 

python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D_ttH_profiled 
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D_ttH_profiled 
# ==============================
# Step 5: Plot results
# ==============================
plot1DScan.py \
  runFits_r_ttH_1D/profile1D_WithSyst_fixedMH_r_ttH.root \
  --main-label "ttH (With systematics)" \
  --main-color 2 \
  --others runFits_r_ttH_1D/profile1D_statonly_fixedMH_r_ttH.root:"ttH Stat-only":4 \
  -o combine_plot_ttH \
  --breakdown Syst,Stat \
  --logo-sub Internal \
  --POI r_ttH \
  --y-cut 50 \
  --y-max 20

plot1DScan.py \
  runFits_r_tHq_1D/profile1D_WithSyst_fixedMH_r_tHq.root \
  --main-label "tHq (With systematics)" \
  --main-color 2 \
  --others runFits_r_tHq_1D/profile1D_statonly_fixedMH_r_tHq.root:"tHq Stat-only":4 \
  -o combine_plot_tHq \
  --breakdown Syst,Stat \
  --logo-sub Internal \
  --POI r_tHq \
  --y-cut 50 \
  --y-max 20

plot1DScan.py \
  runFits_r_ttH_1D_tHq_profiled/profile1D_WithSyst_fixedMH_r_ttH.root \
  --main-label "ttH (tHq_Profiled With systematics)" \
  --main-color 2 \
  --others runFits_r_ttH_1D_tHq_profiled/profile1D_statonly_fixedMH_r_ttH.root:"ttH (tHq Profiled Stat-only)":4 \
  -o combine_plot_ttH_1D_tHq_profiled \
  --breakdown Syst,Stat \
  --logo-sub Internal \
  --POI r_ttH \
  --y-cut 50 \
  --y-max 20

plot1DScan.py \
  runFits_r_tHq_1D_ttH_profiled/profile1D_WithSyst_fixedMH_r_tHq.root \
  --main-label "tHq (ttH_Profiled With systematics)" \
  --main-color 2 \
  --others runFits_r_tHq_1D_ttH_profiled/profile1D_statonly_fixedMH_r_tHq.root:"tHq (ttH Profiled Stat-only)":4 \
  -o combine_plot_tHq_1D_ttH_profiled \
  --breakdown Syst,Stat \
  --logo-sub Internal \
  --POI r_tHq \
  --y-cut 50 \
  --y-max 20


# Make timestamped directory
TARGET_DIR="/eos/user/r/rkumarag/www/Plot_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$TARGET_DIR"

# Move plots into the new directory
mv combine_plot_t* "$TARGET_DIR"

# Run copy_index.sh in www
cd /eos/user/r/rkumarag/www
./copy_index.sh

# Return to previous directory
cd -
