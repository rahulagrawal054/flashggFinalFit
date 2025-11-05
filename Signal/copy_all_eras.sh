#!/bin/bash

# Create output directory
mkdir -p ./all_eras_ws_signal_WithSyst

# Define eras
eras=(2022preEE 2022postEE 2023preBPix 2023postBPix)

# Loop over eras and copy files
for era in "${eras[@]}"; do
  for f in /eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/workspaces/${era}/ws_signal/*.root; do
    base=$(basename "$f" .root)
    cp -v "$f" ./all_eras_ws_signal_WithSyst/${base}_${era}.root
  done
done

