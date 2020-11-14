from collections import namedtuple

def loadObjData(filePath):
    datafile = open(filePath, 'r')
    lines = datafile.readlines()

    count = 0
    dataPoints = []
    Point = namedtuple('Point', ['id', 'x', 'y'])

    for line in lines:
        tokens = line.split()
        if (len(tokens) == 3 and tokens[0] == 'v'):
            count += 1
            p = Point(count, float(tokens[1]), float(tokens[2]))
            dataPoints.append(p)

    return dataPoints