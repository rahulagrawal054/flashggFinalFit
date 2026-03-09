#!/bin/bash

categories=(
ttH_had_1
)

for cat in "${categories[@]}"
do
    filename="Datacard_${cat}.root"
    echo "Running on $filename"
    python3 extractYields.py -i "$filename"
done

