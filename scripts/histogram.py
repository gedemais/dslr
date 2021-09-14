import matplotlib.pyplot as plt

x = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
plt.hist(x, range = (0, 5), bins = 5, color = 'yellow', edgecolor = 'red')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')
plt.show()
