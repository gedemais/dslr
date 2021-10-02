from sys import stderr, stdout
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

    __learning_rate = 0.04

    def __init__(self, n_input, target, max_error=19.0, weights_path=""):
        try:
            if weights_path == "":
                self.weights = [0.0 for x in range(n_input)]
                self.bias = 0.0
            else:
                self.weights, self.bias = self.__parse_weights(weights_path)

            self.max_error = max_error
            self.target = target
            self.output = 0.0
            self.n_input = n_input
        except:
            stderr.write('Failed to create linear regression model: invalid input/output size\n')
            exit(1)


    def __parse_weights(self, weights_path):
        with open(weights_path, 'r') as f:
            data = f.read()
            strs = data.split(',')
            weights = [float(x) for x in strs[:len(strs) - 1]]
            bias = float(strs[-1])
        return weights, bias


    def __sigmoid(self, x):
        self.output = 1.0 / (1.0 + math.exp(-x))


    def run_model(self, input_data):
        if len(input_data) != self.n_input:
            stderr.write('Invalid input data for linear regression model.')
            exit(1)

        sum_up = 0.0
        for i in range(self.n_input):
            if pd.isna(input_data[i]):
                continue
            sum_up += input_data[i] * self.weights[i]

        sum_up += self.bias
        self.__sigmoid(sum_up)
        return self.output


    def train_model(self, df):
        epoch = 0
        error = float('inf')
        prev_error = error
        houses = df['Hogwarts House']
        while error > self.max_error:
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
                error += (target - self.output) ** 2.0

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
            delta = prev_error - error
            stdout.write(   'Error = {0} | Delta = {1} | Epoch {2}           \r'
                            .format(error, delta, epoch))
            stdout.flush()
            prev_error = error
            epoch += 1
            #
