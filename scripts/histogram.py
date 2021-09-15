from sys import stdout, stderr, argv
import pandas as pd
import matplotlib.pyplot as plt
import math

usage = "usage: python3 describe.py dataset.csv\n"

if len(argv) != 2:
    stderr.write(usage)
    exit(1)

try:
    df = pd.read_csv(argv[1])
except:
    print("csv parsing failed.")
    exit(1)

