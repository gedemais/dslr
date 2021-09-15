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

df = df.drop("Index", 1)
df = df.drop("First Name", 1)
df = df.drop("Last Name", 1)
df = df.drop("Birthday", 1)
df = df.drop("Best Hand", 1)

gryffondor = df.loc[df['Hogwarts House'] == 'Gryffindor']

for matiere in gryffondor:
    s = [x for x in gryffondor[matiere]]

