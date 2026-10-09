#!/usr/bin/env bash
set -Eeuo pipefail
if [[ $# -ne 1 || ! -f "$1" ]]; then
    echo "Usage: $0 <existing_config_file>"
    exit 1
fi
CONFIG_FILE="$1"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="ftest_log_${TIMESTAMP}.log"
CLEAN_LOG="clean_${LOG_FILE}"
PVALUE_LOG="pvalues_${TIMESTAMP}.txt"
SUMMARY_LOG="summary_${TIMESTAMP}.txt"
START_TIME=$(date +%s)
echo "Starting fTest: $CONFIG_FILE; log: $LOG_FILE"
# Capture both commands before strict mode can terminate the wrapper.
set +e
python3 -u RunBackgroundScripts.py --inputConfig "$CONFIG_FILE" --mode fTestParallel 2>&1 | tee "$LOG_FILE"
PIPE_STATUS=("${PIPESTATUS[@]}")
set -e
EXIT_CODE=${PIPE_STATUS[0]}
if [[ ${PIPE_STATUS[1]} -ne 0 ]]; then EXIT_CODE=${PIPE_STATUS[1]}; fi
echo "Duration: $(( $(date +%s) - START_TIME )) sec; runner exit code: $EXIT_CODE"
awk 'NF && !/^Info in/ { print }' "$LOG_FILE" > "$CLEAN_LOG"
awk '/\[INFO\] Adding to Envelope/ {
    printf "%-45s GOF_p=%-10s 2xNLL+c=%s\n", $5, $6, $11
}' "$LOG_FILE" > "$PVALUE_LOG"
awk '/Best Fit Pdf/ {print}' "$LOG_FILE" | tee -a "$PVALUE_LOG"
awk '/\[RESULT\] Recommended options/ {remaining=6} remaining>0 {print; remaining--}' "$LOG_FILE" > "$SUMMARY_LOG"
awk '/Skipping GOF|Rejecting failed candidate|GOF rejected/ {print; count++}
END {printf "Fit/GOF rejection messages: %d\n",count}' "$LOG_FILE"
ERROR_FOUND=0
# Unsupported orders and rejected candidate fits are expected diagnostics.
# ROOT input, generation, evaluation, and import errors indicate an invalid run.
if grep -Eiq '\[#0\] ERROR:|Error in <|segmentation fault|traceback|terminate called|what\(\):' "$LOG_FILE"; then
    echo "[FAIL] Runtime errors found in $LOG_FILE"
    ERROR_FOUND=1
fi
if [[ $EXIT_CODE -ne 0 ]]; then
    echo "[FAIL] Runner failed with status $EXIT_CODE"
    ERROR_FOUND=1
fi
if ! grep -q 'Created MultiPdf' "$LOG_FILE"; then
    echo "[FAIL] No background models were reported"
    ERROR_FOUND=1
fi
echo "Output files: $LOG_FILE $CLEAN_LOG $PVALUE_LOG $SUMMARY_LOG"
if [[ $ERROR_FOUND -ne 0 ]]; then exit 1; fi
echo "[OK] No detected runtime errors; inspect GOF diagnostics before using results."
