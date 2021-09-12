from sys import stdout, stderr, argv
import pandas as pd
import math

usage = "usage: python3 describe.py dataset.csv\n"

if len(argv) != 2:
    stderr.write(usage)
    exit(1)

try:
    df = pd.read_csv(argv[1])
except:
    print("csv parsing failed.")
    exit(1)

stats = {
        "Arithmancy": [],
        "Astronomy": [],
        "Herbology": [],
        "Defense Against the Dark Arts": [],
        "Divination": [],
        "Muggle Studies": [],
        "Ancient Runes": [],
        "History of Magic": [],
        "Transfiguration": [],
        "Potions": [],
        "Care of Magical Creatures": [],
        "Charms": [],
        "Flying": []
        }

def compute_min(column):
    """ Je tiens a remercier 42 pour m'avoir permis de faire ca."""
    min_val = float('inf')
    for f in column:
        if pd.isna(f):
            continue
        if f < min_val:
            min_val = f
    return min_val

def compute_max(column):
    """ Toujours plus haut. On vise le sommet."""
    max_val = float('-inf')
    for f in column:
        if pd.isna(f):
            continue
        if f > max_val:
            max_val = f
    return max_val

def compute_count(column):
    count = 0
    for f in column:
        if pd.isna(f):
            continue
        count += 1
    return count

def compute_mean(column, count):
    tmp = 0.0
    for f in column:
        if pd.isna(f):
            continue
        tmp += f
    return tmp / count

def compute_std(column, count, mean):
    tmp = 0.0
    for f in column:
        if pd.isna(f):
            continue
        tmp += (f - mean) * (f - mean)
    tmp = tmp / count
    return math.sqrt(tmp)

def compute_percentile(column, count, percentile):
    s = [x for x in column]
    s.sort()

    k = (count - 1) * float(percentile / 100.0)
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return s[int(k)]

    d0 = s[int(f)] * (c - k)
    d1 = s[int(c)] * (k - f)
    return d0+d1


def compute_stats(column):
    count = compute_count(column)
    mean = compute_mean(column, count)
    std = compute_std(column, count, mean)
    min_val = compute_min(column)
    max_val = compute_max(column)
    tf_pct = compute_percentile(column, count, 25)
    fifty_pct = compute_percentile(column, count, 50)
    sf_pct = compute_percentile(column, count, 75)

    return [count, mean, std, min_val, tf_pct, fifty_pct, sf_pct, max_val]

for column in df:
    if df[column].name in stats.keys():
        stats[df[column].name] = compute_stats(df[column])
        print(stats[df[column].name])

describe(stats)

print(df.describe())
