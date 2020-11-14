import sys
import matplotlib.pyplot as plt

from Algorithms.DataReader import loadObjFile

if __name__ == '__main__':
    dataFile = "TestData/UB1_einfach.obj"
    if (len(sys.argv) > 1):
        dataFile = str(sys.argv[1])

    data = loadObjFile(dataFile)
    for item in data:
        item.show(plt, True)
    plt.show()