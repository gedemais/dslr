from LRModel import LRModel
import pandas as pd
from sys import argv, stderr, stdout
from time import sleep

# Something to iterate over...
models =    {
                "Gryffindor": LRModel(13, "Gryffindor", 13.1),
                "Hufflepuff": LRModel(13, "Hufflepuff", 16.5),
                "Ravenclaw": LRModel(13, "Ravenclaw", 19.1),
                "Slytherin": LRModel(13, "Slytherin", 11.1)
            }

weights =   {
                "Gryffindor": [],
                "Hufflepuff": [],
                "Ravenclaw":  [],
                "Slytherin":  []
            }

def export_weights(weights, house):
    path = 'weights/' + house[0] + '_model_weights.txt'
    n = len(weights)
    try:
        with open(path, 'w+') as f:
            for i, w in enumerate(weights):
                f.write(str(w))
                if i < n - 1:
                    f.write(',')
    except:
        stderr.write('Failed to export weights. Abort.')
        exit(1)

def main():
    if len(argv) != 2:
        stderr.write("usage: python3 logreg_train.py dataset_train.csv\n")
        exit(1)

    df = pd.read_csv(argv[1])
    df = df.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], 1)

    for model_feature in models:
        stdout.write('\n')
        print("Training model {0}".format(model_feature))
        models[model_feature].train_model(df)
        weights[model_feature] = [x for x in models[model_feature].weights]
        weights[model_feature].append(models[model_feature].bias)
        export_weights(weights[model_feature], model_feature)

if __name__ == "__main__":
    main()
