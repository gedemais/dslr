from sys import stdout, stderr, argv
import pandas

usage = "usage: python3 describe.py dataset.csv\n"

if len(argv) != 2:
    stderr.write(usage)
    exit(1)

try:
    df = pandas.read_csv(argv[1])
except:
    print("csv parsing failed.")
    exit(1)
