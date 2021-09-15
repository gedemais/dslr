from sys import stdout, stderr, argv
import pandas as pd
import numpy as np
import math

usage = "usage: python3 describe.py dataset.csv\n"

if len(argv) != 2:
    stderr.write(usage)
    exit(1)

padding_offset = 7

class DatasetDescriber():

    def __init__(self, csv_path):
        try:
            self.df = pd.read_csv(csv_path)
        except:
            stderr.write(csv_path + " : Parsing failed.\n")
            exit(1)
        self.stats =    {
                            "Index": [],
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
        for column in self.df:
            if self.df[column].name in self.stats.keys():
                self.stats[self.df[column].name] = self.__compute_stats(self.df[column])

    def __compute_stats(self, column):
        self.__compute_count(column)
        self.__compute_mean(column)
        self.__compute_std(column)
        self.__compute_min(column)
        self.__compute_max(column)

        s = [x for x in column]
        s.sort()
        self.tf_pct = s[math.ceil(self.count / 4.0) - 1]
        self.fifty_pct = s[math.ceil(self.count / 2.0) - 1]
        self.sf_pct = s[math.ceil(3 * self.count / 4.0) - 1]

        return {"count": self.count,
                "mean": self.mean,
                "std": self.std,
                "min": self.min_val,
                "25%": self.tf_pct,
                "50%": self.fifty_pct,
                "75%": self.sf_pct,
                "max": self.max_val}

    def __compute_min(self, column):
        """ Je tiens a remercier 42 pour m'avoir permis de faire ca."""
        min_val = float('inf')
        for f in column:
            if pd.isna(f):
                continue
            if f < min_val:
                min_val = f
        self.min_val =  min_val

    def __compute_max(self, column):
        """ Toujours plus haut. On vise le sommet."""
        max_val = float('-inf')
        for f in column:
            if pd.isna(f):
                continue
            if f > max_val:
                max_val = f
        self.max_val =  max_val

    def __compute_count(self, column):
        count = 0
        for f in column:
            if pd.isna(f):
                continue
            count += 1
        self.count = count

    def __compute_mean(self, column):
        tmp = 0.0
        for f in column:
            if pd.isna(f):
                continue
            tmp += f
        self.mean =  tmp / self.count

    def __compute_std(self, column):
        tmp = 0.0
        for f in column:
            if pd.isna(f):
                continue
            tmp += (f - self.mean) * (f - self.mean)
        tmp = tmp / self.count
        self.std =  math.sqrt(tmp)

describer = DatasetDescriber(argv[1])

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



        #print(stats[df[column].name])



print("-------------------------------------------------------------------------")
describe(describer.stats)
print("-------------------------------------------------------------------------")
print(describer.df.describe())
