#!/bin/bash
# Run yields
python3 RunYields.py \
  --inputWSDirMap \
2022preEE=/eos/user/r/rkumarag/OLD_OUTPUT/OutputForFinalFit_WithSyst/workspaces/2022preEE/ws_signal,\
2022postEE=/eos/user/r/rkumarag/OLD_OUTPUT/OutputForFinalFit_WithSyst/workspaces/2022postEE/ws_signal,\
2023preBPix=/eos/user/r/rkumarag/OLD_OUTPUT/OutputForFinalFit_WithSyst/workspaces/2023preBPix/ws_signal,\
2023postBPix=/eos/user/r/rkumarag/OLD_OUTPUT/OutputForFinalFit_WithSyst/workspaces/2023postBPix/ws_signal\
  --cats auto \
  --procs auto \
  --ext tth_th_analysis \
  --mergeYears \
  --doSystematics \
  --skipZeroes \
  --batch local

# Make Datacard
python3 makeDatacard.py \
  --years 2022preEE,2022postEE,2023preBPix,2023postBPix \
  --ext tth_th_analysis \
  --prune \
  --pruneThreshold 0.001 \
  --doTrueYield \
  --doMCStatUncertainty \
  --analysis tth_th_analysis \
  --doSystematics 

##################################################
# Run yields
#python3 RunYields.py \
#  --inputWSDirMap \
#2022preEE=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/workspaces/2022preEE/ws_signal,\
#2022postEE=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/workspaces/2022postEE/ws_signal,\
#2023preBPix=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/workspaces/2023preBPix/ws_signal,\
#2023postBPix=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/workspaces/2023postBPix/ws_signal \
#  --cats auto \
#  --procs auto \
#  --ext tth_th_analysis \
#  --mergeYears \
#  --skipCOWCorr \
#  --doSystematics \
#  --skipZeroes \
#  --batch local

# Make datacard
#python3 makeDatacard.py \
#  --years 2022preEE,2022postEE,2023preBPix,2023postBPix \
#  --ext tth_th_analysis \
#  --prune \
#  --pruneThreshold 0.001 \
#  --doTrueYield \
#  --analysis tth_th_analysis \
#  --skipCOWCorr \
# --doSystematics

