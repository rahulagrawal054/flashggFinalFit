#!/bin/bash

# ==============================================================================
# Step 1: Generate Submission Scripts (Dry Run)
# We run RunFits.py with --dryRun to create the folders and .sh scripts
# ==============================================================================
echo ">> [Step 1] Generating submission scripts..."

# --- r_ttH ---
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D --dryRun

# --- r_tHq ---
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D --dryRun

# --- r_ttH (Profiled) ---
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D_tHq_profiled --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D_tHq_profiled --dryRun

# --- r_tHq (Profiled) ---
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D_ttH_profiled --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D_ttH_profiled --dryRun

# --- r_tHq + r_tHW ---
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_plus_tHW_1D --dryRun

# --- r_tHq + r_tHW (Profiled)---
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D_ttH_profiled --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_plus_tHW_1D_ttH_profiled --dryRun


# ==============================================================================
# Step 2: Make Scripts Executable
# Ensure the generated scripts can be run
# ==============================================================================
echo ">> [Step 2] Setting permissions..."
chmod +x runFits_r_ttH_1D/*.sh
chmod +x runFits_r_tHq_1D/*.sh
chmod +x runFits_r_ttH_1D_tHq_profiled/*.sh
chmod +x runFits_r_tHq_1D_ttH_profiled/*.sh
chmod +x runFits_r_tHq_plus_tHW_1D/*.sh
chmod +x runFits_r_tHq_plus_tHW_1D_ttH_profiled/*.sh

# ==============================================================================
# Step 3: Run Fits (The Loop)
# Iterating 0..19 (1000 points / 50 per job = 20 jobs)
# ==============================================================================
echo ">> [Step 3] Running fits (0 to 19)..."

for i in {0..19}; do
    echo "Running batch $i..."
    # r_ttH
    ./runFits_r_ttH_1D/condor_profile1D_WithSyst_fixedMH_r_ttH.sh $i
    ./runFits_r_ttH_1D/condor_profile1D_statonly_fixedMH_r_ttH.sh $i
    
    # r_tHq
    ./runFits_r_tHq_1D/condor_profile1D_WithSyst_fixedMH_r_tHq.sh $i
    ./runFits_r_tHq_1D/condor_profile1D_statonly_fixedMH_r_tHq.sh $i
    
    # r_tHq + r_tHW
    ./runFits_r_tHq_plus_tHW_1D/condor_profile1D_statonly_fixedMH_r_tH.sh $i
    ./runFits_r_tHq_plus_tHW_1D/condor_profile1D_WithSyst_fixedMH_r_tH.sh $i
    
    # r_ttH (Profiled)
    ./runFits_r_ttH_1D_tHq_profiled/condor_profile1D_WithSyst_fixedMH_r_ttH.sh $i
    ./runFits_r_ttH_1D_tHq_profiled/condor_profile1D_statonly_fixedMH_r_ttH.sh $i
    
    # r_tHq (Profiled)
    ./runFits_r_tHq_1D_ttH_profiled/condor_profile1D_WithSyst_fixedMH_r_tHq.sh $i
    ./runFits_r_tHq_1D_ttH_profiled/condor_profile1D_statonly_fixedMH_r_tHq.sh $i

    # r_tHq + r_tHW (Profiled)
    ./runFits_r_tHq_plus_tHW_1D_ttH_profiled/condor_profile1D_statonly_fixedMH_r_tH.sh $i
    ./runFits_r_tHq_plus_tHW_1D_ttH_profiled/condor_profile1D_WithSyst_fixedMH_r_tH.sh $i

done


# ==============================================================================
# Step 4: Collect Fits
# Merges the split jobs into the final ROOT files
# ==============================================================================
echo ">> [Step 4] Collecting and merging results..."

# --- r_ttH ---
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D

# --- r_tHq ---
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D

# --- r_tHq + r_tHW ---
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_plus_tHW_1D
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D

# --- r_ttH (Profiled) ---
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_ttH_1D_tHq_profiled
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_ttH_1D_tHq_profiled

# --- r_tHq (Profiled) ---
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_1D_ttH_profiled
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_1D_ttH_profiled

# --- r_tHq + r_tHW (Profiled) ---
python3 CollectFits.py --inputJson inputs_WithSyst_tth_th.json --mode r_tHq_plus_tHW_1D_ttH_profiled
python3 CollectFits.py --inputJson inputs_statonly_tth_th.json --mode r_tHq_plus_tHW_1D_ttH_profiled

echo "All Done! Check the generated root files."
