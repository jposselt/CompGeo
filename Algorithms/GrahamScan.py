import operator

def direction(p1, p2, p3):
    '''
    Returns in which direction the line segment defined by three points is turning at the middle point

        Parameters:
                p1 (point): Start point of the line segment
                p2 (point): Middle point of the line segment
                p3 (point): End point of the line segment

        Returns:
                turn direction (float):
                                        > 0 if right turn
                                        < 0 if left turn
                                        == 0 if collinear
    '''
    v1 = (p3.x - p2.x, p3.y - p2.y) # vector p1->p3
    v2 = (p2.x - p1.x, p2.y - p1.y) # vector p1->p2
    return v1[0]*v2[1] - v1[1]*v2[0] # cross product

def distanceSquare(p1, p2):
    '''
    Returns the squared distance between two points
    '''
    return (p2.x - p1.x)**2 + (p2.y - p1.y)**2

def grahamScan(points):
    '''
    Calculates the convex hull of a set of 2D points using Graham's scan algorithm

        Parameters:
                points (list): The
        Returns:
                result (tuple): First element is a list of points that form the convex hull.
                                Second element is a list of lists of points that each represent
                                a processing step of the algorithm.
    '''
    n = len(points)
    steps = []

    if (n > 2):
        # Sort points lexically by by x- and y-coordinates (items 1 and 2 in the named tuple)
        points.sort(key = operator.itemgetter(1, 2))

        Lupper = [points[0], points[1]]
        for i in range(2,n):
            Lupper.append(points[i])
            steps.append(Lupper.copy())
            
            while(len(Lupper) > 2):
                d = direction(Lupper[-3], Lupper[-2], Lupper[-1])
                if (d < 0): # left turn
                    Lupper.remove(Lupper[-2])
                    steps.append(Lupper.copy())
                elif (d == 0): # collinear
                    if (distanceSquare(Lupper[-3], Lupper[-2]) <= distanceSquare(Lupper[-3], Lupper[-1]) ):
                        Lupper.remove(Lupper[-2])
                    else:
                        Lupper.remove(Lupper[-1])
                else:
                    break

        Llower = [points[-1], points[-2]]
        for i in range(n-3, -1, -1):
            Llower.append(points[i])
            step = Lupper.copy()
            step.extend(Llower[1:])
            steps.append(step)

            while(len(Llower) > 2):
                d = direction(Llower[-3], Llower[-2], Llower[-1])
                if (d < 0): # left turn
                    Llower.remove(Llower[-2])
                    step = Lupper.copy()
                    step.extend(Llower[1:])
                    steps.append(step)
                elif (d == 0): # collinear
                    if (distanceSquare(Llower[-3], Llower[-2]) <= distanceSquare(Llower[-3], Llower[-1]) ):
                        Llower.remove(Llower[-2])
                    else:
                        Llower.remove(Llower[-1])
                    step = Lupper.copy()
                    step.extend(Llower[1:])
                    steps.append(step)
                else:
                    break

        if (len(Llower) > 2):
            Lupper.extend(Llower[1:-1])

        return (Lupper, steps)

    else:
        return (points, [])