from sys import stderr, argv
from StatsComputor import StatsComputor
import pandas as pd
import matplotlib.pyplot as plt


# Histograms matrix dimensions
hists_matrix_width = 13
hists_matrix_height = 13

# Something to iterate over...
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# This array contains the different colors for the histogram bars for each house.
houses_colors = {
                    "Gryffindor" : 'yellow',
                    "Hufflepuff" : 'orange',
                    "Ravenclaw" : 'blue',
                    "Slytherin" : 'green'
                }

def plot_scatter_matrix(df):
    """
        This function plots all the combination of subjects grades as scatter
        plots, with differents color points depending on the house.
        This scatter matrix allows us to see which causalty links will be
        usefuls for the logistic regression algorithm.
    """
    fig, axs = plt.subplots(hists_matrix_width, hists_matrix_height)
    for x, a in enumerate(df[1:]):
        for y, b in enumerate(df[1:]):
            if a == 'Hogwarts House' or b == 'Hogwarts House':
                continue

            axs[x - 1][y - 1].set_title(a + '-' + b, fontsize=1, pad=1)
            for house in houses:
                h = df.loc[df['Hogwarts House'] == house]
                axs[x - 1][y - 1].scatter(x=h[a], y=h[b], c=houses_colors[house], s=0.25)
            axs[x - 1][y - 1].xaxis.set_visible(False)
            axs[x - 1][y - 1].yaxis.set_visible(False)

    plt.savefig('fig.png', dpi=1600)


def main():
    if len(argv) != 2:
        stderr.write("usage: python scatter_plot.py dataset.csv\n")
        exit(1)

    sc = StatsComputor(argv[1])
    plot_scatter_matrix(sc.df)

if __name__ == "__main__":
    main()
