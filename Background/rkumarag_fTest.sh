#!/bin/bash

CONFIG_FILE=$1
LOG_FILE="ftest_log_$(date +%Y%m%d_%H%M%S).log"

START_TIME=$(date +%s)

python3 RunBackgroundScripts.py --inputConfig "$CONFIG_FILE" --mode fTestParallel > "$LOG_FILE" 2>&1 &

PID=$!

echo "Started job with config: $CONFIG_FILE"
echo "Logs: $LOG_FILE"

# Wait for process to finish
wait $PID

END_TIME=$(date +%s)
ELAPSED=$((END_TIME - START_TIME))

echo "Job completed for config: $CONFIG_FILE"
echo "Time taken: ${ELAPSED} seconds"
#echo "Processing log..."

# Remove unwanted lines (INFO, Info, ERROR, blank)
#sed -i '/INFO/d;/Info/d;/ERROR/d;/^$/d' "$LOG_FILE"

# Extract "Adding to Envelope" lines
#echo "---- Envelope Lines ----"
#grep -n "Adding to Envelope" "$LOG_FILE"

# Check for segmentation fault
#echo "---- Error Check ----"
#grep -i "segmentation fault" "$LOG_FILE" && echo "⚠️ Segmentation fault found!" || echo "No segmentation fault"

#echo "Done. Cleaned log: $LOG_FILE"
