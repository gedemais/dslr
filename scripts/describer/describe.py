from sys import stderr, argv
from DatasetDescriber import DatasetDescriber

if len(argv) != 2:
    stderr.write("usage: python3 describe.py dataset.csv\n")
    exit(1)

describer = DatasetDescriber(argv[1])

describer.describe()

#print('-' * 80)
#print(describer.sd.df.describe())
