#!/bin/bash

# Shows the output of describe function
echo "describe function output (scripts/describer/describer.py):"
echo "-------------------------------------------------------------------------"
python scripts/describer/describe.py datasets/dataset_train.csv
echo "-------------------------------------------------------------------------"

# Shows the functions used by describe function in python source file
echo "Functions used by describe function (scripts/describer/StatsComputor.py):"
echo "-------------------------------------------------------------------------"
sed -n '86,92p;93q' scripts/describer/StatsComputor.py
echo "-------------------------------------------------------------------------"
sed -n '94,99p;100q' scripts/describer/StatsComputor.py
echo "-------------------------------------------------------------------------"
sed -n '102,108p;108q' scripts/describer/StatsComputor.py
echo "-------------------------------------------------------------------------"
sed -n '68,74p;75q' scripts/describer/StatsComputor.py
echo "-------------------------------------------------------------------------"
sed -n '54,56p;57q' scripts/describer/StatsComputor.py
echo "-------------------------------------------------------------------------"
sed -n '77,83p;84q' scripts/describer/StatsComputor.py
echo "-------------------------------------------------------------------------"
