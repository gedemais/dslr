from LRModel import LRModel
import pandas as pd
from sys import argv, stderr

def main():
    if len(argv) != 2:
        stderr.write("usage: python3 logreg_train.py dataset_train.csv\n")
        exit(1)

    df = pd.read_csv(argv[1])
    df = df.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], 1)


    model = LRModel(13)
    model.train_model(df)

if __name__ == "__main__":
    main()
