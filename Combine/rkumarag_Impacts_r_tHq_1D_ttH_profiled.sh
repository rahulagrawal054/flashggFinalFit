#!/bin/bash
# ==========================================================
# Script: run_impacts_r_tHq_1D_ttH_profiled.sh
# Purpose: Run Combine impact plot workflow for r_tHq analysis (profiling r_ttH)
# Author: Rahul Kumar A G
# ==========================================================

# Exit immediately on error
set -e

# ----------------------------------------------------------
# 1. Go to the Combine directory and create a clean impacts folder
# ----------------------------------------------------------
cd $CMSSW_BASE/src/flashggFinalFit/Combine
mkdir -p Impacts_r_tHq_1D_ttH_profiled
cd Impacts_r_tHq_1D_ttH_profiled

# ----------------------------------------------------------
# 2. Copy the datacard (adjust the name/path as needed)
# ----------------------------------------------------------
cp ../Datacard_r_tHq_1D_ttH_profiled.root .

# ----------------------------------------------------------
# 3. Define common minimizer options
# ----------------------------------------------------------
COMMON_OPTS="--cminDefaultMinimizerStrategy 0 \
--X-rtd MINIMIZER_freezeDisassociatedParams \
--X-rtd MINIMIZER_multiMin_hideConstants \
--X-rtd MINIMIZER_multiMin_maskConstraints \
--X-rtd MINIMIZER_multiMin_maskChannels=2"

# ----------------------------------------------------------
# 4. Define the physics model mapping for production modes
# ----------------------------------------------------------

# ----------------------------------------------------------
# 5. Run the initial fit for the parameter of interest (r_tHq)
# ----------------------------------------------------------
combineTool.py -M Impacts \
-d Datacard_r_tHq_1D_ttH_profiled.root \
-m 125.38 \
--doInitialFit \
--robustFit 1 \
-t -1 \
--setParameters r_tHq=1,r_ttH=1 \
--setParameterRanges r_tHq=-25,25:r_ttH=-1,3 \
$COMMON_OPTS $MODEL_OPTS \
--freezeParameters MH

# ----------------------------------------------------------
# 6. Run all nuisance parameter fits (can take time)
# ----------------------------------------------------------
combineTool.py -M Impacts \
-d Datacard_r_tHq_1D_ttH_profiled.root \
-m 125.38 \
--doFits \
--robustFit 1 \
-t -1 \
--setParameters r_tHq=1,r_ttH=1 \
--setParameterRanges r_tHq=-25,25:r_ttH=-1,3 \
$COMMON_OPTS $MODEL_OPTS \
--freezeParameters MH

# ----------------------------------------------------------
# 7. Collect fit results into one JSON file
# ----------------------------------------------------------
combineTool.py -M Impacts \
-d Datacard_r_tHq_1D_ttH_profiled.root \
-m 125.38 \
-o impacts_r_tHq_1D_ttH_profiled.json

# ----------------------------------------------------------
# 8. Plot the initial impacts (all parameters)
# ----------------------------------------------------------
plotImpacts.py \
-i impacts_r_tHq_1D_ttH_profiled.json \
-o impacts_r_tHq_1D_ttH_profiled_allParams

# ----------------------------------------------------------
# 9. Correct impacts JSON to drop background-model parameters
# ----------------------------------------------------------
python3 ../../Plots/correctImpacts.py \
--impactsJson impacts_r_tHq_1D_ttH_profiled.json \
--dropBkgModelParams \
--frozenParam MH

# ----------------------------------------------------------
# 10. Plot the final cleaned impact plot
# ----------------------------------------------------------
plotImpacts.py \
-i impacts_r_tHq_1D_ttH_profiled_corrected_dropBkgModelParams.json \
-o impacts_r_tHq_1D_ttH_profiled_corrected_dropBkgModelParams

# ----------------------------------------------------------
# 11. Done
# ----------------------------------------------------------
echo "Impact plots successfully created:"
echo "  - impacts_r_tHq_1D_ttH_profiled_allParams.pdf / .png"
echo "  - impacts_r_tHq_1D_ttH_profiled_corrected_dropBkgModelParams.pdf / .png"

