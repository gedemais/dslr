#!/bin/bash

# Trains logistic regression models with the training dataset.
echo "TRAINING SCRIPT"
echo "---------------------------------------------------"

#python3.9 scripts/logistic_regression/logreg_train.py datasets/dataset_train.csv

echo "---------------------------------------------------"

echo "Weights Files :"
ls weights/

echo "---------------------------------------------------"

echo "PREDICTION SCRIPT"
echo "---------------------------------------------------"

python3.9 scripts/logistic_regression/logreg_predict.py datasets/dataset_test.csv 2>/dev/null

ls

echo "---------------------------------------------------"

echo "EVALUATION SCRIPT"
echo "---------------------------------------------------"
python3.9 scripts/logistic_regression/evaluate.py houses.csv datasets/dataset_truth.csv

