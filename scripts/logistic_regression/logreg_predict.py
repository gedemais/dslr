from LRModel import LRModel
import pandas as pd
import numpy as np
from sys import argv, stderr, stdout

# Prediction models generated with weights files contents
models =    {
                "Gryffindor": LRModel(  n_input=13,
                                        target="Gryffindor",
                                        weights_path='weights/G_model_weights.txt'),

                "Hufflepuff": LRModel(  n_input=13,
                                        target="Hufflepuff",
                                        weights_path='weights/H_model_weights.txt'),

                "Ravenclaw": LRModel(   n_input=13,
                                        target="Ravenclaw",
                                        weights_path='weights/R_model_weights.txt'),

            }

# Something to iterate over...
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# Dataset features taken into account
features =  [
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


def one_vs_all(data):
    """
        This function is the one-vs-all algorithm implementation. It iterates
        through the models results to spot the first positive prediction,
        resolving our multi-binary classification problem, allowing us to deliver
        a pertinent classification.
        Parameters:
            - data (list) : Input data for binary prediction models.
                            (Features of one student in the dataset)
    """

    for house in houses[:len(houses) - 1]:
        if models[house].run_model(data) > 0.9:
            return house
    return houses[-1]


def gen_prediction_csv(df):
    """
        This function iterates through the whole dataset to predict a house
        classification for each student. Then it exports the results of thoses
        predictions into a file named houses.csv.
        Parameters:
            - df (Pandas DataFrame) : Normalized dataset.
    """

    csv_data =  {
                    'Index': [],
                    'Hogwarts House': []
                }

    for i, student in enumerate(df.iterrows()):
        data = []
        for subject in student[1].keys():
            if subject in features:
                data.append(student[1][subject])

        csv_data['Index'].append(i)
        csv_data['Hogwarts House'].append(one_vs_all(data))

    pd.DataFrame(csv_data).to_csv(r'houses.csv', index=False)
    

def main():
    # Parameters check
    if len(argv) != 2:
        stderr.write("usage: python logreg_predict.py dataset_test.csv\n")
        exit(1)

    # Loading and normalizing the dataset
    df = pd.read_csv(argv[1])
    df_num = df.select_dtypes(include=[np.number])
    df_num = (df_num - df_num.mean()) / df_num.std()
    df[df_num.columns] = df_num

    # Generation of houses.csv
    gen_prediction_csv(df)

if __name__ == "__main__":
    main()
