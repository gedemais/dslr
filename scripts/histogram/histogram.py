from sys import stderr, argv
import pandas as pd
import matplotlib.pyplot as plt


def coords(i, h):
    return int(i % h), int(i / h)


# Histograms matrix dimensions
hists_matrix_width = 5
hists_matrix_height = 3

# Something to iterate over...
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# This array contains the different colors for the histogram bars for each house.
houses_colors = {
                    "Gryffindor" : 'yellow',
                    "Hufflepuff" : 'orange',
                    "Ravenclaw" : 'blue',
                    "Slytherin" : 'green'
                }

# This dict contains dict-fields for each subject studied in Hogwarts.
# Each of thoses dicts have four array-fields containing grades of each student
# of every house in the concerned subject. This way we can access the grades of a
# specific house in a specific subject, e.g matieres['Arithmancy']['Gryffindor']
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
    """ 
        This function fills the matieres dict by conditionally selecting
        students houses and grades with df.loc() in the dataset.
    """
    for house in houses:
        h = df.loc[df['Hogwarts House'] == house]
        for matiere in matieres.keys():
            matieres[matiere][house] = h[matiere]


def plot_histograms(df):
    """
        This function plots a histograms matrix, containing histograms for
        each Hogwarts subject, showing the repartition of all houses grades in
        the concerned subject. This plot allows us to spot the subject with the
        best grades repartition in Hogwarts.
    """
    fig, axs = plt.subplots(hists_matrix_height, hists_matrix_width)

    for i, matiere in enumerate(matieres.keys()):
        x, y = coords(i, hists_matrix_height)
        axs[x][y].set_title(matiere)
        for house in houses:
            axs[x][y].hist( matieres[matiere][house],
                            bins=30, alpha=0.75, color=houses_colors[house])

    axs[1][hists_matrix_width - 1].axis("off")
    axs[2][hists_matrix_width - 1].axis("off")
    plt.show()


def main():
    if len(argv) != 2:
        stderr.write("usage: python histogram.py dataset.csv\n")
        exit(1)

    try:
        df = pd.read_csv(argv[1])
        df = df.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], 1)
    except:
        print("csv parsing failed.")
        exit(1)

    get_grades(df)
    plot_histograms(df)


if __name__ == "__main__":
    main()
