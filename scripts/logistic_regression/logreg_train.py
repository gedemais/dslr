from LRModel import LRModel
import pandas as pd
import numpy as np
from sys import argv, stderr, stdout
import os

# Something to iterate over...
models =    {
                "Gryffindor": LRModel(13, "Gryffindor", 13.2),
                "Hufflepuff": LRModel(13, "Hufflepuff", 15.01),
                "Ravenclaw": LRModel(13, "Ravenclaw", 20.01),
            }

# Weights storage
weights =   {
                "Gryffindor": [],
                "Hufflepuff": [],
                "Ravenclaw":  [],
            }

def export_weights(weights, house):
    """
        This function exports the weights of a trained classification model,
        identified by its house prediction name.
        Parameters:
            - weights (float array) : Weights and bias array.
            - house (str) : Model identifier.
    """
    path = 'weights/' + house[0] + '_model_weights.txt'
    n = len(weights)

    try:
        os.mkdir('weights/')
    except FileExistsError:
        pass

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
        stderr.write("usage: python logreg_train.py dataset_train.csv\n")
        exit(1)

    # Loading and normalization of test dataset
    try:
        df = pd.read_csv(argv[1])
        df = df.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], axis=1)
        df_num = df.select_dtypes(include=[np.number])
        df=(df-df.min())/(df.max()-df.min())
        df[df_num.columns] = df_num
    except:
        stderr.write('CSV parsing failed. Abort.')
        exit(1)

    # Iteration through models for training
    for model_feature in models:
        stdout.write("\nTraining model {0}\n".format(model_feature))
        models[model_feature].train_model(df)
        # Copying weights and bias
        weights[model_feature] = [x for x in models[model_feature].weights]
        weights[model_feature].append(models[model_feature].bias)
        # Exporting them
        export_weights(weights[model_feature], model_feature)


if __name__ == "__main__":
    main()
