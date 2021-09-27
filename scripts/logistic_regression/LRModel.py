from sys import stderr
import pandas as pd
import math
import random
from StatsComputor import StatsComputor

class   LRModel():

    __features =  [
                        "Arithmancy",
                        "Astronomy",
                        "Herbology",
                        "Defense Against the Dark Arts",
                        "Divination",
                        "Muggle Studies",
                        "Ancient Runes",
                        "History of Magic",
                        "Transfiguration",
                        "Potions",
                        "Care of Magical Creatures",
                        "Charms",
                        "Flying"
                    ]

    __learning_rate = 0.05

    def __init__(self, n_input, target, weights_path=""):
        try:
            self.target = target
            self.weights = [0.0 for x in range(n_input)]
            self.bias = 0.0
            self.output = 0.0
            self.n_input = n_input
        except:
            stderr.write('Failed to create linear regression model: invalid input/output size\n')
            exit(1)


    def __normalize(self, val, min_val, max_val):
        return (val - min_val) / (max_val - min_val)


    def __sigmoid(self, x):
        self.output = 1.0 / (1.0 + math.exp(-x))


    def run_model(self, input_data):
        if len(input_data) != self.n_input:
            stderr.write('Invalid input data for linear regression model.')

        i = 0
        sum_up = 0.0
        while i < self.n_input:
            if pd.isna(input_data[i]):
                i += 1
                continue
            sum_up += input_data[i] * self.weights[i]
            i += 1

        sum_up += self.bias
        self.__sigmoid(sum_up)
        return self.output

    def train_model(self, df):
        error = float('inf')
        prev_error = error
        threshold = 10.0
        houses = df['Hogwarts House']
        df=(df-df.mean())/df.std()
        while error > threshold:
            error = 0.0
            updates = [0.0 for x in range(self.n_input)]
            bias_update = 0.0
            for i, student in enumerate(df.iterrows()):
                house = houses[i]
                student = student[1].values[1:]
                target = 1.0 if house == self.target else 0.0
                self.run_model(student)
                if pd.isna(self.output):
                    continue
                error += (self.output - target) ** 2.0

                t = (target - self.output) * self.output * (1.0 - self.output)

                bias_update += t
                isnan = False
                for i, grade in enumerate(student):
                    if pd.isna(grade):
                        isnan = True
                        break
                    updates[i] += t * grade
                if isnan:
                    continue

            bias_update *= -2.0
            for i, grade in enumerate(student):
                updates[i] *= -2.0

            self.bias -= self.__learning_rate * bias_update
            for i, grade in enumerate(student):
                self.weights[i] -= self.__learning_rate * updates[i]

            #
            print("Error : ", error)
            print("Delta : ", prev_error - error)
            prev_error = error
            #
