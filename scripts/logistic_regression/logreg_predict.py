from LRModel import LRModel
import pandas as pd
from sys import argv, stderr, stdout

models =    {
                "Gryffindor": LRModel(  n_input=13,
                                        target="Gryffindor",
                                        max_error=14.0,
                                        weights_path='weights/G_model_weights.txt'),

                "Hufflepuff": LRModel(  n_input=13,
                                        target="Hufflepuff",
                                        max_error=18.0,
                                        weights_path='weights/H_model_weights.txt'),

                "Ravenclaw": LRModel(   n_input=13,
                                        target="Ravenclaw",
                                        max_error=19.0,
                                        weights_path='weights/R_model_weights.txt'),

                "Slytherin": LRModel(   n_input=13,
                                        target="Slytherin",
                                        max_error=12.0,
                                        weights_path='weights/S_model_weights.txt'),
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

    good = 0
    wrong = 0

    mean = []
    for student in df.iterrows():
        data = []
        for subject in student[1].keys():
            if subject in features:
                data.append(normalize(student[1][subject], df[subject].min(), df[subject].max()))
        g = models["Gryffindor"].run_model(data)
        h = models["Hufflepuff"].run_model(data)
        r = models["Ravenclaw"].run_model(data)
        s = models["Slytherin"].run_model(data)

        max_val = 0
        predict = 0
        for i, score in enumerate([g, h, r, s]):
            if score > max_val:
                max_val = score
                predict = i

        print(student[1]['Hogwarts House'], ' : ', houses[predict])
        if student[1]['Hogwarts House'] == houses[predict]:
            good += 1
        else:
            wrong += 1

    print(good, wrong)


if __name__ == "__main__":
    main()
