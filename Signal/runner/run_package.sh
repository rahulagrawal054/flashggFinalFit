#!/bin/bash
set -e

# Pass 'DCB' or 'SoG' as argument 1 (default to DCB if unspecified)
MODEL="${1:-DCB}"

cd /eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal

cats=(
  tH_lep_1 tH_lep_2 ttH_lep_1 ttH_lep_2 ttH_lep_3 ttH_lep_4 bkg_lep \
  tH_had_1 tH_had_2 tH_had_3 tH_had_4 \
  ttH_had_1 ttH_had_2 ttH_had_3 ttH_had_4 bkg_had
)

exts=(
  "tth_th_analysis_2022preEE_${MODEL}" \
  "tth_th_analysis_2022postEE_${MODEL}" \
  "tth_th_analysis_2023preBPix_${MODEL}" \
  "tth_th_analysis_2023postBPix_${MODEL}"
)

cat_str=$(IFS=,; echo "${cats[*]}")
ext_str=$(IFS=,; echo "${exts[*]}")

echo "--> Packaging Signal Workspaces [Model: ${MODEL}]..."
python3 RunPackager.py \
  --exts "${ext_str}" \
  --outputExt "packaged_${MODEL}" \
  --cats "${cat_str}" \
  --massPoints 125 \
  --mergeYears \
  --batch local
