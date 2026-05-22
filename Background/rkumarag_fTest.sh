#!/usr/bin/env bash

set -Eeuo pipefail

# -------------------------------
# Usage check
# -------------------------------
if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <config_file>"
    exit 1
fi

CONFIG_FILE="$1"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Config file not found -> $CONFIG_FILE"
    exit 1
fi

# -------------------------------
# Variables
# -------------------------------
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="ftest_log_${TIMESTAMP}.log"
CLEAN_LOG="clean_${LOG_FILE}"

START_TIME=$(date +%s)

echo "========================================"
echo "Starting fTest job"
echo "Config : $CONFIG_FILE"
echo "Log    : $LOG_FILE"
echo "Start  : $(date)"
echo "========================================"

# -------------------------------
# Run process
# tee:
#   - shows live terminal output
#   - saves output to log file
# -------------------------------
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
echo "ExitCode : $EXIT_CODE"
echo "========================================"

# -------------------------------
# Create cleaned log
# -------------------------------
sed '/INFO/d;/Info/d;/ERROR/d;/^$/d' "$LOG_FILE" > "$CLEAN_LOG"

echo
echo "Cleaned log saved:"
echo "  $CLEAN_LOG"

# -------------------------------
# Envelope lines
# -------------------------------
echo
echo "========== Envelope Lines =========="

if grep -n "Adding to Envelope" "$CLEAN_LOG"; then
    :
else
    echo "No envelope entries found"
fi

# -------------------------------
# Error checks
# -------------------------------
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

if grep -qi "exception" "$LOG_FILE"; then
    echo "[WARN] Exception detected"
    ERROR_FOUND=1
fi

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "[FAIL] Process exited with non-zero code"
    ERROR_FOUND=1
fi

if [[ $ERROR_FOUND -eq 0 ]]; then
    echo "[OK] No critical errors found"
fi

echo
echo "Done."
