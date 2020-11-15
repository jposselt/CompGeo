import sys
import matplotlib.pyplot as plt

from Algorithms.DataReader import loadObjFile
from Algorithms.GrahamScan import grahamScan

def switch_scene(event):
    # counter stays between [-1, len(steps) + 1]
    if (event.key == 'left'):
        if (switch_scene.counter >= 0):
            switch_scene.counter -= 1
    elif (event.key == 'right'):
        if (switch_scene.counter < len(switch_scene.steps)):
            switch_scene.counter += 1

    # clear figure but keep window open
    plt.clf()

    if (switch_scene.counter == len(switch_scene.steps)):
        # algorithm finished: draw hull lines
        if (len(switch_scene.hull) > 0):
            x = [p.x for p in switch_scene.hull]
            y = [p.y for p in switch_scene.hull]
            x.append(switch_scene.hull[0].x)
            y.append(switch_scene.hull[0].y)
            plt.plot(x, y)
    elif (switch_scene.counter >= 0):
        # draw current state of the algorithm
        state = switch_scene.steps[switch_scene.counter]
        if (len(state) > 0):
            x = [p.x for p in state]
            y = [p.y for p in state]
            plt.plot(x, y)

    # always draw input data
    for item in data:
        item.show(plt)

    # draw hull points with labels and different color
    if (switch_scene.counter == len(switch_scene.steps)):
        for item in switch_scene.hull:
                item.show(plt,True,'r')

    # update display
    plt.draw()

switch_scene.counter = -1
switch_scene.data = []
switch_scene.hull = []
switch_scene.steps = []

if __name__ == '__main__':
    dataFile = "TestData/UB1_einfach.obj"
    if (len(sys.argv) > 1):
        dataFile = str(sys.argv[1])
    data = loadObjFile(dataFile)

    # calculate convex hull
    hull, steps = grahamScan(data)

    # configure callback function
    switch_scene.counter = -1
    switch_scene.data = data
    switch_scene.hull = hull
    switch_scene.steps = steps

    # register callback
    cid = plt.figure().canvas.mpl_connect('key_press_event', switch_scene)

    # initial display
    for item in data:
        item.show(plt)
    plt.show()