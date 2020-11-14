from Algorithms.DataReader import loadObjData
from Algorithms.Drawing import addPoints

import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = loadObjData("TestData/UB1_einfach.obj")
    addPoints(plt, data, True)
    plt.show()