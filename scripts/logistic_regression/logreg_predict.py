from LRModel import LRModel
import pandas as pd
import numpy as np
from sys import argv, stderr, stdout

models =    {
                "Gryffindor": LRModel(  n_input=13,
                                        target="Gryffindor",
                                        max_error=13.1,
                                        weights_path='weights/G_model_weights.txt'),

                "Hufflepuff": LRModel(  n_input=13,
                                        target="Hufflepuff",
                                        max_error=16.5,
                                        weights_path='weights/H_model_weights.txt'),

                "Ravenclaw": LRModel(   n_input=13,
                                        target="Ravenclaw",
                                        max_error=19.1,
                                        weights_path='weights/R_model_weights.txt'),

                "Slytherin": LRModel(   n_input=13,
                                        target="Slytherin",
                                        max_error=11.1,
                                        weights_path='weights/S_model_weights.txt')

            }

# Something to iterate over...
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

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

def normalize(val, min_val, max_val):
    return (val - min_val) / (max_val - min_val)

def Average(lst):
    return sum(lst) / len(lst)

def main():
    if len(argv) != 2:
        stderr.write("usage: python3 logreg_train.py dataset_train.csv\n")
        exit(1)

    df = pd.read_csv(argv[1])

    df_num = df.select_dtypes(include=[np.number])

    df_num = (df_num - df_num.mean()) / df_num.std()

    df[df_num.columns] = df_num

    good = 0
    wrong = 0

    mean = []
    for student in df.iterrows():

        data = []
        for subject in student[1].keys():
            if subject in features:
                data.append(student[1][subject])

        if models["Gryffindor"].run_model(data) > 0.9:
            predict = 'Gryffindor'
        elif models["Hufflepuff"].run_model(data) > 0.9:
            predict = 'Hufflepuff'
        elif models["Ravenclaw"].run_model(data) > 0.9:
            predict = 'Ravenclaw'
        elif models["Slytherin"].run_model(data) > 0.9:
            predict = 'Slytherin'

        if student[1]['Hogwarts House'] == predict:
            good += 1
        else:
            print(student[1]['Hogwarts House'], predict)
            wrong += 1
    print(good, wrong)


if __name__ == "__main__":
    main()
