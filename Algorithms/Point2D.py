class Point2D:
    def __init__(self, x, y, identifier):
        self.x = x
        self.y = y
        self.id = identifier
        
    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.id)

    def __repr__(self):
        return 'Point2D({}, {}, {})'.format(self.x, self.y, self.id)

    def show(self, context, showLabels=False):
        context.plot(self.x, self.y, 'ro')
        if (showLabels):
            context.text(self.x, self.y, 'P{} - ({}, {})'.format(self.id, self.x, self.y), horizontalalignment='center', verticalalignment='bottom')