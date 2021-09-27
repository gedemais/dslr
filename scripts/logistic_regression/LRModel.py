from sys import stderr
import pandas as pd
import math

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
    __learning_rate = 0.0005

    def __init__(self, n_input, target, weights_path=""):
        try:
            self.target = target
            self.weights = [0.0 for x in range(n_input)]
            self.output = 0.0
            self.n_input = n_input
        except:
            stderr.write('Failed to create linear regression model: invalid input/output size\n')
            exit(1)


    def __normalize(self, val, min_val, max_val):
        return (val - min_val) / (max_val - min_val)


    def __sigmoid(self, x):
        try:
            self.output = 1.0 / (1.0 + math.exp(-x))
        except OverflowError:
            print(-x)


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

        self.__sigmoid(sum_up)
        return self.output


    def gradient_descent(self, student, target):
        updates = []
        for grade in student:
            change = (target - self.output) * self.output * (1.0 - self.output)
            updates.append(change * self.__learning_rate)
        return updates


    def train_model(self, df):
        error = float('inf')
        prev_error = error
        threshold = 10.0
        while error > threshold:
            error = 0.0
            updates = [0.0 for x in range(self.n_input)]
            for student in df.iterrows():
                house = student[1].values[0]
                student = student[1].values[1:]
                target = 1.0 if house == self.target else 0.0
                self.run_model(student)
                error += (self.output - target) ** 2.0
                updates = self.gradient_descent(student, target)

            for i, u in enumerate(updates):
                self.weights[i] += updates[i] * self.__learning_rate
            #
            print("Error : ", error)
            print("Delta : ", prev_error - error)
            prev_error = error
            print(self.weights)
            print('-' * 80)
            #
        print('__________________\n' * 3)

