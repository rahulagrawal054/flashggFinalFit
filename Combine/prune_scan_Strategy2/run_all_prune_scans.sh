#!/bin/bash

set -euo pipefail

RUN_SCRIPT="./run_2D_fiducial_argument.sh"
STEPS="snapshot,limit,significance"
# How many workspaces to process at once. lxplus nodes typically have
# several cores available; each combine job here is single-threaded, so
# running a handful in parallel gives a near-linear speedup. Adjust based
# on how many cores your session actually has (nproc).
PARALLEL_JOBS=6

run_one() {
    WS_FILE="$1"
    TAG=$(echo "$WS_FILE" | sed -E 's/Datacard_fiducial_allCats_(.*)_r_2D_fiducial\.root/\1/')
    OUT_DIR="${TAG}"
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

# Iterate over all workspace ROOT files, N at a time in parallel
ls Datacard_fiducial_allCats_*_r_2D_fiducial.root \
  | xargs -n 1 -P "${PARALLEL_JOBS}" -I {} bash -c 'run_one "$@"' _ {}

echo "All workspaces processed successfully."
echo ""
echo "To collect a summary table afterward, e.g.:"
echo "  for d in */; do"
echo "    echo -n \"\${d%/}: \""
echo "    grep -A2 'best fit parameter values' \"\${d}log_snapshot_Asimov.log\" 2>/dev/null | tr '\\n' ' '"
echo "    echo"
echo "  done"
