from LRModel import LRModel
import pandas as pd
import numpy as np
from sys import argv, stderr
from time import sleep


def main():
    if len(argv) != 3:
        stderr.write("usage: python evaluate.py houses.csv dataset_truth.csv\n")
        exit(1)

    # Read both predictions and truth datasets
    try:
        df_houses = pd.read_csv(argv[1])
        df_truth = pd.read_csv(argv[2])
    except:
        stderr.write('CSV parsing failed. Abort.\n')
        exit(1)

    # If datasets are not the same length, abort.
    if len(df_houses) != len(df_truth):
        stderr.write('Invalid input datasets. Abort')
        exit(1)

    rights = 0
    wrongs = 0
    # Iterating through the datasets to count rights and wrongs classifications.
    for i in range(len(df_houses)):
        if df_houses.values[i][0] == df_truth.values[i][1]:
            rights += 1
        else:
            wrongs += 1

    # Compute precision score and display it.
    precision = float(rights) / float(len(df_houses))

    print(  "Precision score = {0} / {1} == {2}"
            .format(rights, len(df_houses), precision))


if __name__ == "__main__":
    main()
