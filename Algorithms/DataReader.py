from Algorithms.Point2D import Point2D

def loadObjFile(filePath):
    datafile = open(filePath, 'r')
    lines = datafile.readlines()

    count = 0
    points = []

    for line in lines:
        tokens = line.split()
        if (len(tokens) == 3 and tokens[0] == 'v'):
            count += 1
            xCoord = float(tokens[1])
            yCoord = float(tokens[2])
            points.append( Point2D(xCoord, yCoord, count) )

    return points