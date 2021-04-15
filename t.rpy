px = sorted(points, key = lambda p: p.x)
py = sorted(points, key = lambda p: p.y)

# px : set of points sorted by x coordinates
# py: set of points sorted by y coordinates
def closest_pair(Px, Py):
    # base case
    if len(Px) < 4:
        return closest_pair_bruteforce(Px)

    # divide px into left and right halves
    Q = Px[:len(Px)/2]
    R = Px[len(Px)/2:]

    # sort Q and R both by x and y coordinates
    Qx = sorted(Q, key = lambda p: p.x) # complexity can be imporved
    Qy = sorted(Q, key = lambda p: p.y) # complexity can be imporved
    Rx = sorted(R, key = lambda p: p.x) # complexity can be imporved
    Ry = sorted(R, key = lambda p: p.y) # complexity can be imporved

    # conquer step, recursively find closest pairs on
    # left and right halves
    dl, p1, q1 = closest_pair(Qx, Qy)
    dr, p2, q2 = closest_pair(Rx, Ry)
    d = min(dl, dr)
    # closest pair split pair. One point is in left half
    # and other in right half
    dc, p3, q3 = closest_split_pair(Px, Py, d)

    # find the minimum and return the pair
    mind = min(dl, dr, dc)
    if mind == dl:
        return dl, p1, q1
    elif mind == dr:
        return dr, p2, q2
    else:
        return dc, p3, q3

# calculates distances from every point to every other point
# and compare the distance. Returns the minimum
def closest_pair_bruteforce(points):
    mind = sys.maxsize
    cpairs = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance_sq(points[i], points[j])
            if dist < mind:
                mind = dist 
                cpairs = (points[i], points[j])
    return mind, cpairs[0], cpairs[1]

# returns the closest pair of points between 
# the left and the right half
def closest_split_pair(Px, Py, d):
    # get the point in the boundary x-coordinate
    xbar = Px[len(Px)/2].x

    # get all the points between xbar - d and xbar + d
    # sorted by y-coordinates
    Sy = []
    for point in Py:
        if xbar - d <= point.x <= xbar + d:
            Sy.append(point)

    # compare each point with at most 7 neighboring points
    best = d
    best_pair = Px[0].x, Px[0].y

    for i in range(len(Sy)):
        for j in range(1, min(8, len(Sy) - i)):
            if distance_sq(Sy[i], Sy[i + j]) < best:
                best = distance_sq(Sy[i], Sy[i + j])
                best_pair = Sy[i], Sy[i + j]

    return best, best_pair[0], best_pair[1]