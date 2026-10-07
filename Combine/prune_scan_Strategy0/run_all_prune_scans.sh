#!/bin/bash

set -euo pipefail

RUN_SCRIPT="./run_2D_fiducial_argument.sh"
STEPS="snapshot,scan-syst,scan-stat,limit,significance"
PARALLEL_JOBS=6

run_one() {
    WS_FILE="$1"
    TAG=$(echo "$WS_FILE" | sed -E 's/Datacard_fiducial_allCats_(.*)_r_2D_fiducial\.root/\1/')
    OUT_DIR="${TAG}"

    # Start completely fresh
    rm -rf "${OUT_DIR}"
    mkdir -p "${OUT_DIR}"

    ln -sf "$(pwd)/${WS_FILE}" "${OUT_DIR}/${WS_FILE}"

    echo "[start] ${TAG}"

    (
        cd "${OUT_DIR}"
        bash "../${RUN_SCRIPT#./}" \
            --workspace "${WS_FILE}" \
            --steps "${STEPS}" \
            > run.log 2>&1
    )

    echo "[done]  ${TAG}"
}

export -f run_one
export RUN_SCRIPT STEPS

ls Datacard_fiducial_allCats_*_r_2D_fiducial.root \
    | xargs -P "${PARALLEL_JOBS}" -I {} bash -c 'run_one "$@"' _ {}

echo "All workspaces processed successfully."
