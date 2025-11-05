python3 RunYields.py \
    --cats auto \
    --inputWSDirMap 2022preEE=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025_Nominal/workspaces/2022preEE/ws_signal,2022postEE=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025_Nominal/workspaces/2022postEE/ws_signal,2023preBPix=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025_Nominal/workspaces/2023preBPix/ws_signal,2023postBPix=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025_Nominal/workspaces/2023postBPix/ws_signal \
    --procs auto \
    --ext tth_th_analysis_StatOnly \
    --batch local \
    --mergeYears

python3 makeDatacard.py \
    --years 2022preEE,2022postEE,2023preBPix,2023postBPix \
    --ext tth_th_analysis_StatOnly \
    --prune \
    --pruneThreshold 0.001 \
    --doTrueYield \
    --analysis tth_th_analysis \
    --skipCOWCorr

