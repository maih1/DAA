import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))

def cost(points, n, m, k):
    p1 = points[n]
    p2 = points[m]
    p3 = points[k]
    
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1)

def mTC(points, n, m):
     
    if (m < n + 3):
        return 0
              
    for k in range(n + 1, m):
        res = (mTC(points, n, k) + mTC(points, k, m) + cost(points, n, k, m ))
     
    return round(res, 4)
 
 
points = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
n = len(points)
print(mTC(points, 0, n-1))
 