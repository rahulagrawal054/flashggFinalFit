g!/bin/bash
# ==========================================================
# Script: run_impacts_r_tHq.sh
# Purpose: Run Combine impact plot workflow for r_tHq analysis locally
# Author: Rahul Kumar A G
# ==========================================================

# Exit immediately if a command fails
#set -e

# ----------------------------------------------------------
# 1. Go to the Combine directory and create a clean impacts folder
# ----------------------------------------------------------
cd $CMSSW_BASE/src/flashggFinalFit/Combine
mkdir -p Impacts_r_tHq
cd Impacts_r_tHq

# ----------------------------------------------------------
# 2. Copy your datacard (adjust path if needed)
# ----------------------------------------------------------
cp ../Datacard_r_tHq_1D.root .

# ----------------------------------------------------------
# 3. Define common minimizer options to stabilize fits
# ----------------------------------------------------------
COMMON_OPTS="--cminDefaultMinimizerStrategy 0 \
--X-rtd MINIMIZER_freezeDisassociatedParams \
--X-rtd MINIMIZER_multiMin_hideConstants \
--X-rtd MINIMIZER_multiMin_maskConstraints \
--X-rtd MINIMIZER_multiMin_maskChannels=2"

# ----------------------------------------------------------
# 4. Run the initial fit to find the best-fit POI (r_tHq)
# ----------------------------------------------------------
combineTool.py -M Impacts \
-d Datacard_r_tHq_1D.root \
-m 125.38 \
--doInitialFit \
--robustFit 1 \
-t -1 \
--setParameters r_tHq=1 \
--setParameterRanges r_tHq=-25.0,25.0 \
$COMMON_OPTS \
--freezeParameters MH

# ----------------------------------------------------------
# 5. Run all nuisance parameter fits locally (this may take time)
# ----------------------------------------------------------
combineTool.py -M Impacts \
-d Datacard_r_tHq_1D.root \
-m 125.38 \
--doFits \
--robustFit 1 \
-t -1 \
--setParameters r_tHq=1 \
--setParameterRanges r_tHq=-25.0,25.0 \
$COMMON_OPTS \
--freezeParameters MH

# ----------------------------------------------------------
# 6. Collect all fit results into one JSON file
# ----------------------------------------------------------
combineTool.py -M Impacts \
-d Datacard_r_tHq_1D.root \
-m 125.38 \
-o impacts_r_tHq.json

# ----------------------------------------------------------
# 7. Plot the initial impacts including all parameters
# ----------------------------------------------------------
plotImpacts.py \
-i impacts_r_tHq.json \
-o impacts_r_tHq_allParams

# ----------------------------------------------------------
# 8. Correct impacts JSON to drop background-model parameters
# ----------------------------------------------------------
python3 ../../Plots/correctImpacts.py \
--impactsJson impacts_r_tHq.json \
--dropBkgModelParams \
--frozenParam MH

# ----------------------------------------------------------
# 9. Plot the final impact plot (PDF + PNG)
# ----------------------------------------------------------
plotImpacts.py \
-i impacts_r_tHq_corrected_dropBkgModelParams.json \
-o impacts_r_tHq_corrected_dropBkgModelParams

# ----------------------------------------------------------
# 10. Done
# ----------------------------------------------------------
echo "Impact plots successfully created:"
echo "  - impacts_r_tHq_allParams.pdf / .png"
echo "  - impacts_r_tHq_corrected_dropBkgModelParams.pdf / .png"

