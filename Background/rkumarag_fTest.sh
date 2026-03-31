#!/bin/bash

CONFIG_FILE=$1
LOG_FILE="ftest_log_$(date +%Y%m%d_%H%M%S).log"

python3 RunBackgroundScripts.py --inputConfig "$CONFIG_FILE" --mode fTestParallel > "$LOG_FILE" 2>&1 &

PID=$!

echo "Started job with config: $CONFIG_FILE"
echo "Logs: $LOG_FILE"

# Wait for process to finish
wait $PID

echo "Job completed for config: $CONFIG_FILE"
echo "Check logs: $LOG_FILE"
