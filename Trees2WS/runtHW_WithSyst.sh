# where to write your per-era workspaces
BASE_WS_DIR=/eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/workspaces

# wipe out old outputs and recreate base dir
mkdir -p "${BASE_WS_DIR}"

# list of eras to process
eras=(2023preBPix 2023postBPix)

for era in "${eras[@]}"; do
  wsdir="${BASE_WS_DIR}/${era}"
  mkdir -p "${wsdir}"

  python3 trees2ws.py \
    --inputConfig config_ttH_tH_2022_2023_WithSyst.py \
    --inputTreeFile /eos/user/r/rkumarag/hgg_tth_th_cp_analysis/finalFitPreparation/outputForFinalFits_03Nov2025/root/tHW_${era}/output_THWtoGG_M125_13TeV_madgraph_pythia8.root \
    --inputMass 125 \
    --productionMode tHW \
    --year "${era}" \
    --doSystematics \
    --outputWSDir "${wsdir}"

done

