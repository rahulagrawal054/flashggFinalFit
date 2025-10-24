# 1 Run Yields
python3 RunYields.py \
  --cats auto \
  --inputWSDirMap \
  2022preEE=/eos/home-r/rkumarag/OutputForFinalFit_WithOutSyst/workspaces/2022preEE/ws_signal,\
2022postEE=/eos/home-r/rkumarag/OutputForFinalFit_WithOutSyst/workspaces/2022postEE/ws_signal,\
2023preBPix=/eos/home-r/rkumarag/OutputForFinalFit_WithOutSyst/workspaces/2023preBPix/ws_signal,\
2023postBPix=/eos/home-r/rkumarag/OutputForFinalFit_WithOutSyst/workspaces/2023postBPix/ws_signal \
  --procs auto \
  --ext tth_th_analysis \
  --batch local \
  --mergeYears \
  --doSystematics

# 2 Run Datacard
python3 makeDatacard.py \
  --years 2022preEE,2022postEE,2023preBPix,2023postBPix \
  --ext tth_th_analysis \
  --prune \
  --pruneThreshold 0.001 \
  --doTrueYield \
  --analysis tth_th_analysis \
  --skipCOWCorr \
  --doSystematics

