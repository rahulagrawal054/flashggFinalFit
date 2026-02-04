#!/bin/bash

# Categories
CATS=(
  "ttH_had_1" "ttH_had_2"
  "ttH_lep_1" "ttH_lep_2"
)

EOS_BASE="/eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/Checks/Bias_in_significance"
WWW_BASE="/eos/user/r/rkumarag/www"
TIMESTAMP=$(date +"%d%b_%H%M")
FOLDER="biasStudy_${TIMESTAMP}"

for CAT in "${CATS[@]}"; do
  echo "----------------------------------------"
  echo "Processing category: ${CAT}"
  echo "----------------------------------------"

  python3 $EOS_BASE/RunBiasInSignificance.py --inputWSFile "$EOS_BASE/Datacard_${CAT}.root" --MH 125.38 --mode setup
  python3 $EOS_BASE/RunBiasInSignificance.py --inputWSFile "$EOS_BASE/Datacard_${CAT}.root" --MH 125.38 --mode generate
  python3 $EOS_BASE/RunBiasInSignificance.py --inputWSFile "$EOS_BASE/Datacard_${CAT}.root" --MH 125.38 --mode fixed
  python3 $EOS_BASE/RunBiasInSignificance.py --inputWSFile "$EOS_BASE/Datacard_${CAT}.root" --MH 125.38 --mode envelope

  python3 $EOS_BASE/SummaryBiasSignificance.py

  OUT_DIR="${EOS_BASE}/${FOLDER}/${CAT}"
  WWW_DIR="${WWW_BASE}/${FOLDER}/${CAT}"

  mkdir -p "${OUT_DIR}" "${WWW_DIR}"

  mv $EOS_BASE/higgsCombine_initial.MultiDimFit.mH125.38.root "${OUT_DIR}/" 2>/dev/null
  mv $EOS_BASE/pdfindex.json $EOS_BASE/toys.root $EOS_BASE/fit_fixed.root $EOS_BASE/fit_envelope.root $EOS_BASE/combine_logger.out "${OUT_DIR}/" 2>/dev/null
  mv $EOS_BASE/Plots "${OUT_DIR}/" 2>/dev/null

  cp -r "${OUT_DIR}/Plots/"* "${WWW_DIR}/" 2>/dev/null

  echo "Finished processing category: ${CAT}"
done

echo "All categories completed."

