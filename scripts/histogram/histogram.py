from sys import stdout, stderr, argv
import pandas as pd
import matplotlib.pyplot as plt
import math

def compute_count(column):
    count = 0
    for f in column:
        count += 1
    return count


def compute_mean(column):
    tmp = 0.0
    count = compute_count(column)
    for f in column:
        tmp += f
    return tmp / count


def coords(i, h):
    return int(i % h), int(i / h)


hists_matrix_width = 5
hists_matrix_height = 3
n = hists_matrix_width * hists_matrix_height


houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

houses_colors = {
                    "Gryffindor" : 'yellow',
                    "Hufflepuff" : 'orange',
                    "Ravenclaw" : 'blue',
                    "Slytherin" : 'green'
                }

matieres =      {
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


def get_grades(df):
    for house in houses:
        print(df)
        h = df.loc[df['Hogwarts House'] == house]
        print(len(h))
        for matiere in matieres.keys():
            matieres[matiere][house] = h[matiere]


def plot_histograms(df):
    fig, axs = plt.subplots(hists_matrix_height, hists_matrix_width)

    i = 0
    while i < n:
        if i >= len(matieres):
            axs[x][y].axis("off")
        else:
            matiere = list(matieres)[i]
            x, y = coords(i, hists_matrix_height)
            axs[x][y].set_title(matiere)
            print(matiere)
            for house in houses:
                print(house, ' : ', len(matieres[matiere][house]))
                axs[x][y].hist( matieres[matiere][house],
                                bins=30, alpha=0.75, color=houses_colors[house])
        
        i += 1
    plt.show()


def main():
    if len(argv) != 2:
        stderr.write("usage: python3 describe.py dataset.csv\n")
        exit(1)

    try:
        df = pd.read_csv(argv[1])
        df = df.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], 1)
        df = df.dropna()
    except:
        print("csv parsing failed.")
        exit(1)

    get_grades(df)
    plot_histograms(df)


if __name__ == "__main__":
    main()
