import math
import copy

def dist(p1, p2):
    return math.sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2))

def burte_force(a):
    min_d = dist(a[0], a[1])
    pairs = (a[0], a[1])

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if dist(a[i], a[j]) < min_d:
                min_d = dist(a[i], a[j])
                pairs = (a[i], a[j])

    return min_d, pairs

def arr_min(p, n, d):
    mim_d = d[0]
    pairs = d[1]

    for i in range(n):
        j = i + 1
        while j < n and (p[j][1] - p[i][1]) < mim_d:
            mim_d = dist(p[i], p[j])
            pairs = (p[i], p[j])
            j += 1
		
    return mim_d, pairs

def closestPair(p, q, n):
    if n <= 3:
        return burte_force(p)

    m = n // 2
    m_p = p[m]

    dl = closestPair(p[:m], q, m)
    dr = closestPair(p[m:], q, n - m)

    d = min(dl, dr)

    strip = []

    for i in range( n ):
        
        if abs(q[i][0] - m_p[0]) < d[0]:
            strip.append(q[i])
    # print(d)
    return min(d, arr_min(strip, len(strip), d))

def sorts(p, n):
	p.sort(key = lambda point: point[0])
	q = copy.deepcopy(p)
	q.sort(key = lambda point: point[1])	

	return closestPair(p, p, n)

if __name__ == "__main__":
    point = [(2, 3), (12, 30), (0, 1), (12, 50), (6, 7), (5, 1), (12, 10), (3, 4)]
    n = len(point)

    result = sorts(point, n)
    
    print("Cap diem co khoang cach nho nhat: d{} = {}".format(result[1], result[0]))
