#!/bin/bash

# --- Configuration ---
DATACARDS=(
    "Datacard_StatOnly_tH_lep_1.root"
    "Datacard_StatOnly_tH_lep_2.root"
    "Datacard_StatOnly_tH_had_1.root"
    "Datacard_StatOnly_tH_had_2.root"
    "Datacard_StatOnly_ttH_lep_1.root"
    "Datacard_StatOnly_ttH_lep_2.root"
    "Datacard_StatOnly_ttH_had_1.root"
    "Datacard_StatOnly_ttH_had_2.root"
)

MH="125.38"
NTOYS=20000
SEED="12345"

for WS_FILE in "${DATACARDS[@]}"; do
    if [ ! -f "$WS_FILE" ]; then 
        echo "Warning: $WS_FILE not found, skipping..."
        continue 
    fi

    # Determine POI based on filename
    if [[ "$WS_FILE" == *"ttH"* ]]; then
        CURRENT_POI="r_ttH"
    else
        CURRENT_POI="r_tH"
    fi

    # Extract Directory Name
    DIR_NAME=$(echo $WS_FILE | sed 's/Datacard_//;s/.root//')

    echo "-------------------------------------------------------"
    echo "Starting Bias Study for: $DIR_NAME"
    echo "Using POI: $CURRENT_POI"
    echo "-------------------------------------------------------"

    # --- Run Python Workflow ---
    # FIXED: Changed $POI to $CURRENT_POI
    echo "Step 1: Setup"
    python3 RunBiasInSignificance.py --inputWSFile $WS_FILE --POI $CURRENT_POI --MH $MH --mode setup

    echo "Step 2: Generate Toys"
    python3 RunBiasInSignificance.py --mode generate --seed $SEED --POI $CURRENT_POI --MH $MH --nToys $NTOYS

    echo "Step 3: Fixed Significance"
    python3 RunBiasInSignificance.py --inputWSFile $WS_FILE --MH $MH --mode fixed --nToys $NTOYS --POI $CURRENT_POI

    echo "Step 4: Envelope Significance"
    python3 RunBiasInSignificance.py --inputWSFile $WS_FILE --MH $MH --mode envelope --nToys $NTOYS --POI $CURRENT_POI

    echo "Step 5: Summary and Plotting"
    python3 SummaryBiasSignificance.py

    # --- Cleanup and Organization ---
    echo "Moving files to directory: $DIR_NAME"
    mkdir -p $DIR_NAME

    mv $WS_FILE $DIR_NAME/
    mv higgsCombine_initial.MultiDimFit.mH$MH.root $DIR_NAME/
    mv pdfindex.json $DIR_NAME/
    
    # FIXED: Use variables for the toy filename so it's dynamic
    mv higgsCombine_toy_$NTOYS.GenerateOnly.mH$MH.$SEED.root $DIR_NAME/ 2>/dev/null || mv toys.root $DIR_NAME/
    
    mv fit_fixed.root $DIR_NAME/
    mv fit_envelope.root $DIR_NAME/
    mv combine_logger.out $DIR_NAME/ 2>/dev/null || true 

    if [ -d "plots" ]; then
        mv plots $DIR_NAME/
    fi

    echo "-------------------------------------------------------"
    echo "Work Complete. Results are in $DIR_NAME"
    echo "-------------------------------------------------------"
done
