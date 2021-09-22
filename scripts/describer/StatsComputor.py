from sys import stderr
import pandas as pd
import math

class StatsComputor():

    def __init__(self, csv_path):
        try:
            self.df = pd.read_csv(csv_path)

            self.df = self.df.dropna()
            self.df = self.df.drop(["First Name",
                                    "Last Name",
                                    "Birthday",
                                    "Best Hand"], 1)
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
                self.stats[self.df[column].name] = self.__compute_student_stats(self.df[column])


    def __compute_student_stats(self, column):
        self.__compute_count(column)
        self.__compute_mean(column)
        self.__compute_std(column)
        self.__compute_min(column)
        self.__compute_max(column)

        s = []
        for i in column:
            if pd.isna(i):
                continue
            s.append(i)
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
            if f < min_val:
                min_val = f
        self.min_val =  min_val


    def __compute_max(self, column):
        """ Toujours plus haut. On vise le sommet."""
        max_val = float('-inf')
        for f in column:
            if f > max_val:
                max_val = f
        self.max_val =  max_val


    def __compute_count(self, column):
        count = 0
        for f in column:
            count += 1
        self.count = count


    def __compute_mean(self, column):
        tmp = 0.0
        for f in column:
            tmp += f
        self.mean =  tmp / self.count


    def __compute_std(self, column):
        tmp = 0.0
        for f in column:
            tmp += (f - self.mean) * (f - self.mean)
        tmp = tmp / self.count
        self.std =  math.sqrt(tmp)