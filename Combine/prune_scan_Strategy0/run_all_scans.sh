#!/bin/bash
# Save as run_all_scans.sh in /eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/prune_scan_Strategy0/

SCRIPT_DIR="/eos/home-r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine"

# ==============================================================================
# LOOP 1: Extract yields for ALL directories first (Command 1)
# ==============================================================================
echo "=================================================="
echo " STEP 1: Extracting CSV Yields for All Directories"
echo "=================================================="

for dir in *_SoG; do
    if [ -d "$dir" ]; then
        root_file="${dir}/Datacard_fiducial_allCats_${dir}_r_2D_fiducial.root"
        
        if [ -f "$root_file" ]; then
            echo "--> Extracting: $dir"
            python3 "${SCRIPT_DIR}/extractYields_V1.py" -i "$root_file"
        else
            echo "Skipping $dir: $root_file not found."
        fi
    fi
done

# ==============================================================================
# LOOP 2: Analyze yields for ALL directories second (Command 2)
# ==============================================================================
echo ""
echo "=================================================="
echo " STEP 2: Running v6 Analysis on All Generated CSVs"
echo "=================================================="

for dir in *_SoG; do
    if [ -d "$dir" ]; then
        csv_file="${dir}/Datacard_fiducial_allCats_${dir}_r_2D_fiducial_yields.csv"
        
        if [ -f "$csv_file" ]; then
            echo "--> Analyzing: $dir"
            python3 "${SCRIPT_DIR}/analyze_yields_v6.py" "$csv_file"
        else
            echo "Skipping $dir: $csv_file not found."
        fi
    fi
done

echo ""
echo "All steps completed!"
