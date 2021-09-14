from sys import stdout, stderr, argv
import pandas as pd
import numpy as np
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

df = df.drop("Index", 1)

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

padding_offset = 7

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

################################################################################

def get_column_length(stats, matiere):
    max_length = len(matiere)
    for stat in stats[matiere].values():
        stat_len = len(format(stat, ".6f"))
        if stat_len > max_length:
            max_length = stat_len
    return max_length

def print_features_titles(stats, lengths):
    stdout.write(' ' * padding_offset)
    for i, feature in enumerate(stats):
        pad = lengths[i] - len(feature)
        if pad > 0:
            stdout.write(' ' * pad)
        stdout.write(feature)
        stdout.write(' ' * 2)
    stdout.write('\n')

def print_stat_content(stats, lengths, line):
    for i, matiere in enumerate(stats.keys()):
        s = format(stats[matiere][line], ".6f")
        pad = lengths[i] - len(s)
        if pad > 0:
            stdout.write(' ' * pad)
        stdout.write(s)
        stdout.write(' ' * 2)
    stdout.write('\n')

def describe(stats):
    lengths = []
    for matiere in stats.keys():
        lengths.append(get_column_length(stats, matiere))

    print_features_titles(stats, lengths)
    lines = [
                "count", "mean", "std", "min",
                "25%", "50%", "75%", "max"
            ]

    for line in lines:
        stdout.write(line)
        if len(line) < padding_offset:
            stdout.write(' ' * (padding_offset - len(line)))
        print_stat_content(stats, lengths, line)


def compute_stats(column):
    count = compute_count(column)
    mean = compute_mean(column, count)
    std = compute_std(column, count, mean)
    min_val = compute_min(column)
    max_val = compute_max(column)

    s = [x for x in column]
    s.sort()
    tf_pct = s[math.ceil(count / 4.0) - 1]
    fifty_pct = s[math.ceil(count / 2.0) - 1]
    sf_pct = s[math.ceil(3 * count / 4.0) - 1]

    return {"count": count,
            "mean": mean,
            "std": std,
            "min": min_val,
            "25%": tf_pct,
            "50%": fifty_pct,
            "75%": sf_pct,
            "max": max_val}

for column in df:
    if df[column].name in stats.keys():
        stats[df[column].name] = compute_stats(df[column])
        #print(stats[df[column].name])

print("-------------------------------------------------------------------------")
describe(stats)
print("-------------------------------------------------------------------------")
print(df.describe())
