import sys

from Algorithms.DataReader import loadObjFile
from Algorithms.GrahamScan import grahamScan

if __name__ == '__main__':
    dataFile = "TestData/UB1_einfach.obj"
    if (len(sys.argv) > 1):
        dataFile = str(sys.argv[1])

    data = loadObjFile(dataFile)
    
    print(grahamScan(data))