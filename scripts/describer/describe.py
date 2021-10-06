from sys import stderr, argv
from DatasetDescriber import DatasetDescriber


def main():

    if len(argv) != 2:
        stderr.write("usage: python describe.py dataset.csv\n")
        exit(1)

    describer = DatasetDescriber(argv[1])
    describer.describe()


if __name__ == "__main__":
    main()
