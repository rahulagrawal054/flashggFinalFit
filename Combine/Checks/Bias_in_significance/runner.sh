#!/bin/bash

# Categories
CATS=("tH_had_1" "tH_had_2" "ttH_had_1" "ttH_had_2" "ttH_lep_1" "ttH_lep_2" "tH_lep_1" "tH_lep_2")

# Base paths
SRC_DIR="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine"
BIAS_DIR="$SRC_DIR/Checks/Bias_in_significance"

# Move into SRC directory
cd $SRC_DIR || exit

echo "Running Text2Workspace for all categories..."
for CAT in "${CATS[@]}"; do
    python3 RunText2Workspace.py --mode r_ttH_1D --batch local --ext $CAT
done

echo "Starting Bias-in-Significance workflow..."
# Loop over categories
for CAT in "${CATS[@]}"; do

    echo "----------------------------------------"
    echo "Processing category: $CAT"
    echo "----------------------------------------"

    DATACARD_SRC="${SRC_DIR}/Datacard_${CAT}.root"
    DATACARD_DST="${BIAS_DIR}/Datacard_${CAT}.root"

    # 1. Move datacard into Bias_in_significance directory
    echo "Moving datacard → $BIAS_DIR"
    mv $DATACARD_SRC $DATACARD_DST

    # 2. Move into Bias_in_significance directory
    cd $BIAS_DIR

    # 3. Run all bias study modes
    python3 RunBiasInSignificance.py --inputWSFile Datacard_${CAT}.root --MH 125.38 --mode setup
    python3 RunBiasInSignificance.py --inputWSFile Datacard_${CAT}.root --MH 125.38 --mode generate
    python3 RunBiasInSignificance.py --inputWSFile Datacard_${CAT}.root --MH 125.38 --mode fixed
    python3 RunBiasInSignificance.py --inputWSFile Datacard_${CAT}.root --MH 125.38 --mode envelope

    # 4. Run summary
    python3 SummaryBiasSignificance.py

    # 5. Create output directory named after category
    mkdir -p $CAT

    # 6. Move relevant produced files into the category directory
    mv higgsCombine_initial.MultiDimFit.mH125.38.root $CAT/ 2>/dev/null
    mv pdfindex.json $CAT/ 2>/dev/null
    mv toys.root $CAT/ 2>/dev/null
    mv fit_fixed.root $CAT/ 2>/dev/null
    mv fit_envelope.root $CAT/ 2>/dev/null
    mv combine_logger.out $CAT/ 2>/dev/null
    mv plots $CAT/ 2>/dev/null

    echo "Finished processing category: $CAT"
    echo ""
done

echo "All categories completed."

