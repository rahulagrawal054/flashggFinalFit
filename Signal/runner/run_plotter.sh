#!/bin/bash
set -e

MODEL="${1:-DCB}"
cd /eos/user/r/rkumarag/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal

cats=(
  tH_lep_1 tH_lep_2 ttH_lep_1 ttH_lep_2 ttH_lep_3 ttH_lep_4 bkg_lep \
  tH_had_1 tH_had_2 tH_had_3 tH_had_4 \
  ttH_had_1 ttH_had_2 ttH_had_3 ttH_had_4 bkg_had
)

YEARS="2022preEE,2022postEE,2023preBPix,2023postBPix"
EXT="packaged_${MODEL}"

echo "--> Processing categories sequentially for ${MODEL}..."

#for cat in "${cats[@]}"; do
#  echo " Processing category: ${cat}"
#  python3 RunPlotter.py \
#    --procs all \
#    --years "${YEARS}" \
#    --cats "${cat}" \
#    --ext "${EXT}" \
#    --MH 125.08 \
#    --plot-years-separate \
#    --doFWHM
#done

for cat in "${cats[@]}"; do
  echo " Processing category: ${cat}"
  python3 RunPlotter.py \
    --procs all \
    --years "${YEARS}" \
    --cats "${cat}" \
    --ext "${EXT}" \
    --MH 125.08 \
    --doFWHM
done
