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

def compute_count(column):
    count = 0
    for f in column:
        if pd.isna(f):
            continue
        count += 1
    return count

def compute_mean(column):
    tmp = 0.0
    count = compute_count(column)
    for f in column:
        if pd.isna(f):
            continue
        tmp += f
    return tmp / count

df = df.drop("Index", 1)
df = df.drop("First Name", 1)
df = df.drop("Last Name", 1)
df = df.drop("Birthday", 1)
df = df.drop("Best Hand", 1)

df = df.dropna()

matieres =  {
            "Arithmancy": {},
            "Astronomy": {},
            "Herbology": {},
            "Defense Against the Dark Arts": {},
            "Divination": {},
            "Muggle Studies": {},
            "Ancient Runes": {},
            "History of Magic": {},
            "Transfiguration": {},
            "Potions": {},
            "Care of Magical Creatures": {},
            "Charms": {},
            "Flying":{}
            }


houses =    [
                "Gryffindor",
                "Hufflepuff",
                "Ravenclaw",
                "Slytherin",
            ]


for house in houses:
    h = df.loc[df['Hogwarts House'] == house]
    for matiere in matieres.keys():
        #print("{0}, {1} :".format(house, matiere), h[matiere].values)
        matieres[matiere][house] = [x for x in h[matiere].values]

w = 5
h = 3

fig, axs = plt.subplots(h, w)

i = 0
for matiere in matieres.keys():
    x = int(i % h)
    y = int(i / h)
    axs[x][y].set_title(matiere)
    axs[x][y].hist(matieres[matiere]['Gryffindor'], bins=25, alpha=1, label='Gry', color='r')
    axs[x][y].hist(matieres[matiere]['Hufflepuff'], bins=25, alpha=1, label='Huf', color='g')
    axs[x][y].hist(matieres[matiere]['Ravenclaw'], bins=25, alpha=1, label='Rav', color='b')
    axs[x][y].hist(matieres[matiere]['Slytherin'], bins=25, alpha=1, label='Sly', color='y')
    i += 1

plt.show()
