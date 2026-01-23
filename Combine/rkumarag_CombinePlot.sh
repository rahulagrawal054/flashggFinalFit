#!/bin/bash
# ==============================================================================
# PLOT ALL 1D SCANS (FIXED)
# ==============================================================================

# 1. Create the rename file for nice axis labels
echo '{"r_ttH": "#mu_{ttH}", "r_tHq": "#mu_{tHq}", "r_tH": "#mu_{tHq+tHW}"}' > rename.json

echo ">> Created rename.json"

# ==============================================================================
# PLOTTING COMMANDS
# ==============================================================================

# --- 1) r_ttH (1D Scan) ---
echo ">> Plotting 1/6: r_ttH (1D Scan)..."
mkdir -p runFits_r_ttH_1D/Plots
plot1DScan.py "runFits_r_ttH_1D/profile1D_WithSyst_fixedMH_r_ttH.root" \
  --others "runFits_r_ttH_1D/profile1D_statonly_fixedMH_r_ttH.root:Stat-Only:2" \
  --POI r_ttH \
  --output "runFits_r_ttH_1D/Plots/CombinePlot_r_ttH" \
  --main-label "Total Uncert." --main-color 1 --y-cut 50 --y-max 20 --translate rename.json --breakdown "Syst,Stat" \
  --logo-sub "Internal"

# --- 2) r_ttH (Profiled tHq) ---
echo ">> Plotting 2/6: r_ttH (Profiled tHq)..."
mkdir -p runFits_r_ttH_1D_tHq_profiled/Plots
plot1DScan.py "runFits_r_ttH_1D_tHq_profiled/profile1D_WithSyst_fixedMH_r_ttH.root" \
  --others "runFits_r_ttH_1D_tHq_profiled/profile1D_statonly_fixedMH_r_ttH.root:Stat-Only:2" \
  --POI r_ttH \
  --output "runFits_r_ttH_1D_tHq_profiled/Plots/CombinePlot_r_ttH_tHq_profiled" \
  --main-label "Total Uncert." --main-color 1 --y-cut 50 --y-max 20 --translate rename.json --breakdown "Syst,Stat" \
  --logo-sub "Internal"

# --- 3) r_tH (1D Scan for tHq+tHW) ---
echo ">> Plotting 3/6: r_tH (1D Scan)..."
mkdir -p runFits_r_tHq_plus_tHW_1D/Plots
plot1DScan.py "runFits_r_tHq_plus_tHW_1D/profile1D_WithSyst_fixedMH_r_tH.root" \
  --others "runFits_r_tHq_plus_tHW_1D/profile1D_statonly_fixedMH_r_tH.root:Stat-Only:2" \
  --POI r_tH \
  --output "runFits_r_tHq_plus_tHW_1D/Plots/CombinePlot_r_tH" \
  --main-label "Total Uncert." --main-color 1 --y-cut 50 --y-max 20 --translate rename.json --breakdown "Syst,Stat" \
  --logo-sub "Internal)"

# --- 4) r_tH (Profiled ttH) ---
echo ">> Plotting 4/6: r_tH (Profiled ttH)..."
mkdir -p runFits_r_tHq_plus_tHW_1D_ttH_profiled/Plots
plot1DScan.py "runFits_r_tHq_plus_tHW_1D_ttH_profiled/profile1D_WithSyst_fixedMH_r_tH.root" \
  --others "runFits_r_tHq_plus_tHW_1D_ttH_profiled/profile1D_statonly_fixedMH_r_tH.root:Stat-Only:2" \
  --POI r_tH \
  --output "runFits_r_tHq_plus_tHW_1D_ttH_profiled/Plots/CombinePlot_r_tH_ttH_profiled" \
  --main-label "Total Uncert." --main-color 1 --y-cut 50 --y-max 20 --translate rename.json --breakdown "Syst,Stat" \
  --logo-sub "Internal"

# --- 5) r_tHq (1D Scan) ---
echo ">> Plotting 5/6: r_tHq (1D Scan)..."
mkdir -p runFits_r_tHq_1D/Plots
plot1DScan.py "runFits_r_tHq_1D/profile1D_WithSyst_fixedMH_r_tHq.root" \
  --others "runFits_r_tHq_1D/profile1D_statonly_fixedMH_r_tHq.root:Stat-Only:2" \
  --POI r_tHq \
  --output "runFits_r_tHq_1D/Plots/CombinePlot_r_tHq" \
  --main-label "Total Uncert." --main-color 1 --y-cut 50 --y-max 20 --translate rename.json --breakdown "Syst,Stat" \
  --logo-sub "Internal"

# --- 6) r_tHq (Profiled ttH) ---
echo ">> Plotting 6/6: r_tHq (Profiled ttH)..."
mkdir -p runFits_r_tHq_1D_ttH_profiled/Plots
plot1DScan.py "runFits_r_tHq_1D_ttH_profiled/profile1D_WithSyst_fixedMH_r_tHq.root" \
  --others "runFits_r_tHq_1D_ttH_profiled/profile1D_statonly_fixedMH_r_tHq.root:Stat-Only:2" \
  --POI r_tHq \
  --output "runFits_r_tHq_1D_ttH_profiled/Plots/CombinePlot_r_tHq_ttH_profiled" \
  --main-label "Total Uncert." --main-color 1 --y-cut 50 --y-max 20 --translate rename.json --breakdown "Syst,Stat" \
  --logo-sub "Internal (tHq profiled)"

echo "=========================================================="
echo "Done! All plots saved in their respective Plots/ folders."
echo "=========================================================="

