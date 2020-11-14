def addPoints(plot, points, showlabels = False):
    for p in points:
        plot.plot(p.x, p.y, 'ro')
        if (showlabels):
            plot.text(p.x, p.y, 'P{} - ({}, {})'.format(p.id, p.x, p.y), horizontalalignment='center', verticalalignment='bottom')