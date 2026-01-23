#!/bin/bash
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode Z_ttH --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode Z_ttH --dryRun
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode Z_tHq_plus_tHW --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode Z_tHq_plus_tHW --dryRun
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode Z_tHq --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode Z_tHq --dryRun
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode limit_tHq_plus_tHW --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode limit_tHq_plus_tHW --dryRun
python3 RunFits.py --inputJson inputs_statonly_tth_th.json --mode limit_tHq --dryRun
python3 RunFits.py --inputJson inputs_WithSyst_tth_th.json --mode limit_tHq --dryRun
# Function to run command and intelligently parse the output
run_smart() {
    CMD="$1"
    LABEL="$2"
    
    # 1. Print Label
    printf "%-60s" ">> $LABEL..."
    TMP_LOG=$(mktemp)

    # 2. Run Command
    eval "$CMD" > "$TMP_LOG" 2>&1
    EXIT_CODE=$?

    # 3. Check for Failure
    if [ $EXIT_CODE -ne 0 ]; then
        echo -e "\033[0;31m[CRASHED]\033[0m"
        echo "   -> Error Log (Last 5 lines):"
        tail -n 5 "$TMP_LOG"
        rm "$TMP_LOG"
        return
    fi

    # 4. Success - Now let's find out what happened inside
    echo -e "\033[0;32m[DONE]\033[0m"

    # --- PARSING LOGIC ---

    # A) Check for SIGNIFICANCE
    SIG_VAL=$(grep "Significance:" "$TMP_LOG" | awk '{print $2}')
    if [ ! -z "$SIG_VAL" ]; then
        # Check if 0
        if [[ "$SIG_VAL" == "0" || "$SIG_VAL" == "0.00000" ]]; then
             echo -e "   \033[0;33m[WARNING] Significance is 0!\033[0m"
             # Try to find best fit 'r' to see if it was negative
             BEST_R=$(grep "Best fit r" "$TMP_LOG")
             if [ ! -z "$BEST_R" ]; then
                 echo -e "   Reason: $BEST_R"
             else
                 echo -e "   Reason: Signal strength likely negative or fit failed."
             fi
        else
             echo -e "   Method: Significance -> \033[1;36m$SIG_VAL sigma\033[0m"
        fi
    fi

    # B) Check for ASYMPTOTIC LIMITS
    ASYMP_VAL=$(grep "Expected 50.0%:" "$TMP_LOG" | awk '{print $5}')
    if [ ! -z "$ASYMP_VAL" ]; then
        echo -e "   Method: Asymptotic   -> \033[1;36mr < $ASYMP_VAL\033[0m (Exp 50%)"
    fi

    # C) Check for HYBRID NEW (Toys)
    # HybridNew usually prints "Limit: r < X +/- Y"
    HYBRID_VAL=$(grep "Limit: r <" "$TMP_LOG")
    if [ ! -z "$HYBRID_VAL" ]; then
        echo -e "   Method: HybridNew    -> \033[1;35m$HYBRID_VAL\033[0m"
    fi

    # Clean up
    rm "$TMP_LOG"
}

echo "========================================================"
echo " INTELLIGENT FIT RUNNER"
echo "========================================================"

# --- SIGNIFICANCE ---
run_smart "./runFits_Z_ttH/condor_Significance_WithSyst_fixedMH_r_ttH.sh 0"      "Z_ttH (WithSyst)"
run_smart "./runFits_Z_ttH/condor_Significance_statonly_fixedMH_r_ttH.sh 0"     "Z_ttH (StatOnly)"

run_smart "./runFits_Z_tHq_plus_tHW/condor_Significance_WithSyst_fixedMH_r_tH.sh 0"  "Z_tH (WithSyst)"
run_smart "./runFits_Z_tHq_plus_tHW/condor_Significance_statonly_fixedMH_r_tH.sh 0" "Z_tH (StatOnly)"

run_smart "./runFits_Z_tHq/condor_Significance_WithSyst_fixedMH_r_tHq.sh 0"     "Z_tHq (WithSyst)"
run_smart "./runFits_Z_tHq/condor_Significance_statonly_fixedMH_r_tHq.sh 0"    "Z_tHq (StatOnly)"

echo ""
# --- LIMITS ---
run_smart "./runFits_limit_tHq_plus_tHW/condor_AsymptoticLimit_WithSyst_fixedMH_r_tH.sh 0" "Limit tH (WithSyst)"
run_smart "./runFits_limit_tHq_plus_tHW/condor_AsymptoticLimit_statonly_fixedMH_r_tH.sh 0" "Limit tH (StatOnly)"

run_smart "./runFits_limit_tHq/condor_AsymptoticLimit_WithSyst_fixedMH_r_tHq.sh 0"      "Limit tHq (WithSyst)"
run_smart "./runFits_limit_tHq/condor_AsymptoticLimit_statonly_fixedMH_r_tHq.sh 0"     "Limit tHq (StatOnly)"

echo ""
echo "Done."
