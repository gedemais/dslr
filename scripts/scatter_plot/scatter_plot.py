from sys import stderr, argv
from StatsComputor import StatsComputor
import pandas as pd
import matplotlib.pyplot as plt


def normalize(val, min_val, max_val):
    return (val - min_val) / (max_val - min_val)

def compute_similarity(a, b, sc):
    a_fc = (sc.compute_min(a), sc.compute_max(a))
    b_fc = (sc.compute_min(b), sc.compute_max(b))

    error = 0.0
    length = len(a)
    for i in range(length):
        n_a = normalize(a[i], a_fc[0], a_fc[1])
        n_b = normalize(b[i], b_fc[0], b_fc[1])
        error += abs(n_a - n_b)
    error /= length
    return (1.0 - error) * 100.0

def get_similaritys(sc):
    similaritys = {}
    for a in sc.df:
        for b in sc.df:
            if a != b:
                similaritys[a + '-' + b] = compute_similarity(sc.df[a].values, sc.df[b].values, sc)
    return similaritys

def main():
    if len(argv) != 2:
        stderr.write("usage: python3 scatter_plot.py dataset.csv\n")
        exit(1)

    sc = StatsComputor(argv[1])
    similaritys = get_similaritys(sc)
    for i in similaritys.keys():
        print(similaritys[i])


if __name__ == "__main__":
    main()
