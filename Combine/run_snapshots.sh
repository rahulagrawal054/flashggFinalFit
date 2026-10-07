#!/bin/bash

# Run snapshot for all fiducial datacards
# Usage:
#   chmod +x run_snapshots.sh
#   ./run_snapshots.sh

MASS="125.08"
ASIMOV=1

DATA_FLAG="-t -1"
SNAPSHOT_PREFIX="Asimov"

if [[ ${ASIMOV} -eq 0 ]]; then
    DATA_FLAG=""
    SNAPSHOT_PREFIX="Observed"
fi

MINIMIZER_OPTS="--cminDefaultMinimizerStrategy 0 \
--X-rtd MINIMIZER_freezeDisassociatedParams \
--X-rtd MINIMIZER_multiMin_hideConstants \
--X-rtd MINIMIZER_multiMin_maskConstraints \
--X-rtd MINIMIZER_multiMin_maskChannels=2"

OUTDIR="snapshot_outputs"
mkdir -p "${OUTDIR}"

FILES=(
Datacard_bkg_had_r_2D_fiducial.root
Datacard_bkg_lep_r_2D_fiducial.root
Datacard_tH_had_1_r_2D_fiducial.root
Datacard_tH_had_2_r_2D_fiducial.root
Datacard_tH_had_3_r_2D_fiducial.root
Datacard_tH_had_4_r_2D_fiducial.root
Datacard_tH_lep_1_r_2D_fiducial.root
Datacard_tH_lep_2_r_2D_fiducial.root
Datacard_ttH_had_1_r_2D_fiducial.root
Datacard_ttH_had_2_r_2D_fiducial.root
Datacard_ttH_had_3_r_2D_fiducial.root
Datacard_ttH_had_4_r_2D_fiducial.root
Datacard_ttH_lep_1_r_2D_fiducial.root
Datacard_ttH_lep_2_r_2D_fiducial.root
Datacard_ttH_lep_3_r_2D_fiducial.root
Datacard_ttH_lep_4_r_2D_fiducial.root
)

for WORKSPACE in "${FILES[@]}"; do
    NAME=$(basename "${WORKSPACE}" .root)

    echo "=================================================="
    echo "Running: ${WORKSPACE}"
    echo "=================================================="

    combine -M MultiDimFit "${WORKSPACE}" -m "${MASS}" ${DATA_FLAG} \
        --setParameters r_tHq=1,r_ttH=1,MH="${MASS}" \
        --freezeParameters MH \
        --saveWorkspace --saveFitResult \
        -n "_${NAME}_${SNAPSHOT_PREFIX}Postfit" \
        -P r_tHq -P r_ttH \
        --floatOtherPOIs 1 \
        ${MINIMIZER_OPTS}

    # Save output files
    mkdir -p "${OUTDIR}/${NAME}"

    mv higgsCombine_"${NAME}"_"${SNAPSHOT_PREFIX}"Postfit.MultiDimFit.mH${MASS}.root \
       "${OUTDIR}/${NAME}/" 2>/dev/null

    mv multidimfit_"${NAME}"_"${SNAPSHOT_PREFIX}"Postfit.root \
       "${OUTDIR}/${NAME}/" 2>/dev/null

done

echo "All snapshots finished."
echo "Outputs saved in: ${OUTDIR}/"
