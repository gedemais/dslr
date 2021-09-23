from sys import stderr
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

    def __init__(self, n_input, weights_path=""):
        try:
            self.weights = [0.0 for x in range(n_input)]
            self.output = 0.0
            self.n_input = n_input
        except:
            stderr.write('Failed to create linear regression model: invalid input/output size\n')
            exit(1)


    def __sigmoid(self, x):
        self.output = 1.0 / (1.0 + math.exp(-x))


    def run_model(self, input_data):
        if len(input_data) != self.n_input:
            stderr.write('Invalid input data for linear regression model.')

        i = 0
        sum_up = 0.0
        while i < self.n_input:
            sum_up += input_data[i] * self.weights[i]
            i += 1

        self.__sigmoid(sum_up)
        return self.output

    def train_model(self, df):
        updates = [0.0 for x in range(self.n_input)]
        for student in df.iterrows():
            self.run_model(student[1].values[1:])
            print(self.output)
            print('-' * 80)
                
