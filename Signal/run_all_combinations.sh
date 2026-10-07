#!/bin/bash

# ============================================================
# Usage:
#   ./run_all_combinations.sh DCB
#   ./run_all_combinations.sh SoG
# ============================================================

EXT="$1"

if [ -z "$EXT" ]; then
    echo "Usage: $0 <EXT>"
    echo "Example: $0 DCB"
    echo "         $0 SoG"
    exit 1
fi

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

YEARS=("2022preEE" "2022postEE" "2023preBPix" "2023postBPix")

ALL_YEARS="2022preEE,2022postEE,2023preBPix,2023postBPix"

CATS=(
    "tH_lep_1"
    "tH_lep_2"
    "ttH_lep_1"
    "ttH_lep_2"
    "ttH_lep_3"
    "ttH_lep_4"
    "bkg_lep"
    "tH_had_1"
    "tH_had_2"
    "tH_had_3"
    "tH_had_4"
    "ttH_had_1"
    "ttH_had_2"
    "ttH_had_3"
    "ttH_had_4"
    "bkg_had"
)

PROCS=(
    "bbh_in"
    "bbh_out"
    "ggh_in"
    "ggh_out"
    "tHW_in"
    "tHW_out"
    "tth_in"
    "tth_out"
    "tHqLep_in"
    "tHqLep_out"
    "tHqHad_in"
    "tHqHad_out"
    "vh_in"
    "vh_out"
    "vbf_in"
    "vbf_out"
)

MH="125.08"

echo "============================================================"
echo " Signal model plots"
echo " Model: ${EXT}"
echo "============================================================"


# ============================================================
# Loop over all categories
# ============================================================

for CAT in "${CATS[@]}"; do

    echo ""
    echo "############################################################"
    echo " Category: ${CAT}"
    echo " Model   : ${EXT}"
    echo "############################################################"


    # ========================================================
    # COMBINATION 1
    # All years + all processes
    # ========================================================

    echo ""
    echo ">>> Combination 1:"
    echo "    All years + all processes"

    python3 RunPlotter.py \
        --procs all \
        --years "${ALL_YEARS}" \
        --cats "${CAT}" \
        --ext "${EXT}" \
        --MH "${MH}" \
        --doFWHM


    # ========================================================
    # COMBINATION 2
    # One year + all processes
    # ========================================================

    for YEAR in "${YEARS[@]}"; do

        echo ""
        echo ">>> Combination 2:"
        echo "    Year = ${YEAR}"
        echo "    All processes"

        python3 RunPlotter.py \
            --procs all \
            --years "${YEAR}" \
            --cats "${CAT}" \
            --ext "${EXT}" \
            --MH "${MH}" \
            --doFWHM

    done


    # ========================================================
    # COMBINATION 3
    # All years + one process
    # ========================================================

    for PROC in "${PROCS[@]}"; do

        echo ""
        echo ">>> Combination 3:"
        echo "    All years"
        echo "    Process = ${PROC}"

        python3 RunPlotter.py \
            --procs "${PROC}" \
            --years "${ALL_YEARS}" \
            --cats "${CAT}" \
            --ext "${EXT}" \
            --MH "${MH}" \
            --doFWHM

    done


    # ========================================================
    # COMBINATION 4
    # One year + one process
    # ========================================================

    for YEAR in "${YEARS[@]}"; do

        for PROC in "${PROCS[@]}"; do

            echo ""
            echo ">>> Combination 4:"
            echo "    Year    = ${YEAR}"
            echo "    Process = ${PROC}"

            python3 RunPlotter.py \
                --procs "${PROC}" \
                --years "${YEAR}" \
                --cats "${CAT}" \
                --ext "${EXT}" \
                --MH "${MH}" \
                --doFWHM

        done
    done

done


echo ""
echo "============================================================"
echo " DONE"
echo " Model: ${EXT}"
echo "============================================================"
