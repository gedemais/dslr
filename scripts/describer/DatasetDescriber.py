from sys import stdout, stderr, argv
from StatsComputor import StatsComputor
import pandas as pd

class DatasetDescriber():

    def __init__(self, csv_path):
        self.sc = StatsComputor(csv_path)
        self.padding_offset = 7


    def __get_column_length(self, matiere):
        max_length = len(matiere)
        for stat in self.sc.stats[matiere].values():
            stat_len = len(format(stat, ".6f"))
            if stat_len > max_length:
                max_length = stat_len
        return max_length


    def __print_features_titles(self):
        stdout.write(' ' * self.padding_offset)
        for i, feature in enumerate(self.sc.stats):
            pad = self.lengths[i] - len(feature)
            if pad > 0:
                stdout.write(' ' * pad)
            stdout.write(feature)
            stdout.write(' ' * 2)
        stdout.write('\n')


    def __print_stat_content(self, line):
        for i, matiere in enumerate(self.sc.stats.keys()):
            s = format(self.sc.stats[matiere][line], ".6f")
            pad = self.lengths[i] - len(s)
            if pad > 0:
                stdout.write(' ' * pad)
            stdout.write(s)
            stdout.write(' ' * 2)
        stdout.write('\n')


    def describe(self):
        self.lengths = []
        for matiere in self.sc.stats.keys():
            self.lengths.append(self.__get_column_length(matiere))

        self.__print_features_titles()
        lines = [
                    "count", "mean", "std", "min",
                    "25%", "50%", "75%", "max"
                ]

        for line in lines:
            stdout.write(line)
            if len(line) < self.padding_offset:
                stdout.write(' ' * (self.padding_offset - len(line)))
            self.__print_stat_content(line)
