#!/bin/bash
# ==========================================================
# Script: run_impacts_fiducial.sh
# Purpose: Run Combine impact plot workflow for fiducial 2D analysis
# Author: Rahul Kumar A G
# ==========================================================

# Exit immediately if a command fails
set -e

# ==========================================
# 1. Configuration & Variables
# ==========================================
EXT="fiducial_allCats_SoG"
MODE="r_2D_fiducial"
MASS="125.08"
POI="r_tHq"
PROFILE_POI="r_ttH"

# Ranges for the fit to prevent it from wandering off into unphysical territory
PROFILE_POI_RANGE="-0.5,3.0"
POI_RANGE="-20.0,25.0"

# Common minimizer options packaged into a single variable
COMMON_OPTS="--cminDefaultMinimizerStrategy 0 \
  --X-rtd MINIMIZER_freezeDisassociatedParams \
  --X-rtd MINIMIZER_multiMin_hideConstants \
  --X-rtd MINIMIZER_multiMin_maskConstraints \
  --X-rtd MINIMIZER_multiMin_maskChannels=2"

## ==========================================
## 2. Directory Setup
## ==========================================
# Assuming this script is run from $CMSSW_BASE/src/flashggFinalFit/Combine
IMPACT_DIR="Impacts_${POI}_Scan_${PROFILE_POI}_Profile_${EXT}"
echo ">>> Creating and entering directory: ${IMPACT_DIR}"
mkdir -p "${IMPACT_DIR}"

# Copy the workspace datacard into the impacts folder
cp "Datacard_${EXT}_${MODE}.root" "${IMPACT_DIR}/"
cd "${IMPACT_DIR}"

# Create translation json for pretty plotting
echo '{"r_ttH": "#mu_{t#bar{t}H+tHW}", "r_tHq": "#mu_{tHq}"}' > rename.json

# ==========================================
# 3. Initial Fit
# ==========================================
echo ">>> Running initial fit for Impacts..."
combineTool.py -M Impacts \
  -d "Datacard_${EXT}_${MODE}.root" \
  -m "${MASS}" \
  --doInitialFit \
  --robustFit 1 \
  -t -1 \
  --setParameters "${PROFILE_POI}=1,${POI}=1,MH=${MASS}" \
  --freezeParameters MH \
  --redefineSignalPOIs "${POI}" \
  --setParameterRanges "${POI}=${POI_RANGE}:${PROFILE_POI}=${PROFILE_POI_RANGE}" \
  ${COMMON_OPTS}

# ==========================================
# 4. Nuisance Parameter Fits
# ==========================================
echo ">>> Running nuisance parameter fits (parallelized)..."
combineTool.py -M Impacts \
  -d "Datacard_${EXT}_${MODE}.root" \
  -m "${MASS}" \
  --doFits \
  --robustFit 1 \
  -t -1 \
  --setParameters "${PROFILE_POI}=1,${POI}=1,MH=${MASS}" \
  --freezeParameters MH \
  --redefineSignalPOIs "${POI}" \
  --setParameterRanges "${POI}=${POI_RANGE}:${PROFILE_POI}=${PROFILE_POI_RANGE}" \
  --parallel 4 \
  ${COMMON_OPTS}

# ==========================================
# 5. Collect Fit Results
# ==========================================
echo ">>> Collecting fit results into JSON..."
combineTool.py -M Impacts \
  -d "Datacard_${EXT}_${MODE}.root" \
  -m "${MASS}" \
  --redefineSignalPOIs "${POI}" \
  -o "impacts_${POI}_${EXT}.json"

# ==========================================
# 6. Plot Original Impacts
# ==========================================
echo ">>> Plotting initial impacts (All Parameters)..."
plotImpacts.py \
  -i "impacts_${POI}_${EXT}.json" \
  -o "impacts_${POI}_${EXT}_allParams" \
  --translate rename.json

# ==========================================
# 7. Correct Impacts (Drop Background Params)
# ==========================================
echo ">>> Correcting Impacts to drop background model parameters..."
# Make sure the path to correctImpacts.py is correct relative to your current folder
python3 /eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Plots/correctImpacts.py \
  --impactsJson "impacts_${POI}_${EXT}.json" \
  --dropBkgModelParams \
  --frozenParam MH

# ==========================================
# 7.5 Fix JSON Syntax & Create "Removed POI" Data
# ==========================================
echo ">>> Fixing JSON syntax and preparing plotting data..."
python3 -c "
import json

in_file = 'impacts_${POI}_${EXT}_corrected_dropBkgModelParams.json'
out_file = 'impacts_${POI}_${EXT}_corrected_dropBkgModelParams_remove_POI.json'
poi_to_remove = '${PROFILE_POI}'

# Read the file and fix the single quotes syntax error
with open(in_file, 'r') as f:
    raw_text = f.read()
    raw_text = raw_text.replace(\"['POI']\", '[\"POI\"]')

# Overwrite the original file with fixed syntax (This one keeps the Profiled POI)
with open(in_file, 'w') as f:
    f.write(raw_text)

# Load the data, remove the Profiled POI, and save as the second file
data = json.loads(raw_text)
data['params'] = [p for p in data['params'] if p.get('name') != poi_to_remove]
with open(out_file, 'w') as f:
    json.dump(data, f, indent=4)
"

# ==========================================
# 8. Plot Corrected Impacts (WITH Profiled POI)
# ==========================================
echo ">>> Plotting corrected impacts (With ${PROFILE_POI})..."
plotImpacts.py \
  -i "impacts_${POI}_${EXT}_corrected_dropBkgModelParams.json" \
  -o "impacts_${POI}_${EXT}_corrected_WITH_POI" \
  --translate rename.json

# ==========================================
# 9. Plot Corrected Impacts (WITHOUT Profiled POI)
# ==========================================
echo ">>> Plotting corrected impacts (Without ${PROFILE_POI})..."
plotImpacts.py \
  -i "impacts_${POI}_${EXT}_corrected_dropBkgModelParams_remove_POI.json" \
  -o "impacts_${POI}_${EXT}_corrected_WITHOUT_POI" \
  --translate rename.json

# ==========================================
echo ">>> Impact plots successfully created!"
