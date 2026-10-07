#!/usr/bin/env bash
set -Eeuo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <config_file>"
    exit 1
fi

CONFIG_FILE="$1"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Config file not found -> $CONFIG_FILE"
    exit 1
fi

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="ftest_log_${TIMESTAMP}.log"
CLEAN_LOG="clean_${LOG_FILE}"
PVALUE_LOG="pvalues_${TIMESTAMP}.txt"
SUMMARY_LOG="summary_${TIMESTAMP}.txt"

START_TIME=$(date +%s)

echo "========================================"
echo "Starting fTest job"
echo "Config  : $CONFIG_FILE"
echo "Log     : $LOG_FILE"
echo "Start   : $(date)"
echo "========================================"

python3 RunBackgroundScripts.py \
    --inputConfig "$CONFIG_FILE" \
    --mode fTestParallel \
    2>&1 | tee "$LOG_FILE"

EXIT_CODE=${PIPESTATUS[0]}
END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo
echo "========================================"
echo "Job Finished"
echo "End Time : $(date)"
echo "Duration : ${ELAPSED} sec"
echo "Exit Code: $EXIT_CODE"
echo "========================================"

grep -v "^$" "$LOG_FILE" \
    | grep -v "^\[INFO\].*LoadPCM\|^\[INFO\].*TClassTable\|^Info in" \
    > "$CLEAN_LOG"

echo
echo "Cleaned log saved: $CLEAN_LOG"

echo
echo "========== GOF p-values per PDF =========="

awk '
/\[INFO\] Adding to Envelope/ {
    split($0, a, " ")
    pdf_name = a[5]
    pval     = a[6]
    nll      = a[11]
    printf "%-45s  GOF_p=%-8s  2xNLL+c=%s\n", pdf_name, pval, nll
}
' "$LOG_FILE" | tee "$PVALUE_LOG"

echo
echo "p-values saved: $PVALUE_LOG"

echo
echo "========== Best Fit per Category =========="
grep "Best Fit Pdf" "$LOG_FILE" | tee -a "$PVALUE_LOG"

echo
echo "========== Recommended Orders =========="
grep -A5 "\[RESULT\] Recommended options" "$LOG_FILE" \
    | grep -v "^\-\-$" | tee -a "$SUMMARY_LOG"

echo
echo "========== Skipped GOF (fit failures) =========="
SKIPPED=$(grep "Skipping GOF" "$LOG_FILE" | wc -l)
echo "Total skipped: $SKIPPED"
grep "Skipping GOF" "$LOG_FILE"

echo
echo "========== Error Check =========="
ERROR_FOUND=0

if grep -qi "segmentation fault" "$LOG_FILE"; then
    echo "[FAIL] Segmentation fault detected"
    ERROR_FOUND=1
fi

if grep -qi "traceback" "$LOG_FILE"; then
    echo "[FAIL] Python traceback detected"
    ERROR_FOUND=1
fi

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "[FAIL] Process exited with non-zero exit code: $EXIT_CODE"
    ERROR_FOUND=1
fi

if [[ $ERROR_FOUND -eq 0 ]]; then
    echo "[OK] No critical errors found"
fi

echo
echo "========================================"
echo "Output files:"
echo "  Full log    : $LOG_FILE"
echo "  Cleaned log : $CLEAN_LOG"
echo "  p-values    : $PVALUE_LOG"
echo "  Summary     : $SUMMARY_LOG"
echo "========================================"
echo "Done."
