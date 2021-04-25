import sys

def _min(q, d, s):
    min = sys.maxsize

    for i in q: 
        if d[i] != 0:
            if d[i] < min:
                min = d[i]
                min_i = i

    return min_i, min

def d_v(graph, v, s):
    d = dict()

    for i in range(v):
        if i != s:
            d[i] = graph[s][i]
    
    return d

def dijkstra(graph, v, s):
    d = d_v(graph, v, s)

    q = []

    S = {s:graph[s][s]}


    for i in range(v):
        if i != s:
            q.append(i)

    while len(q) != 0:
        u = _min(q, d, s)
        S.update({u[0]: u[1]})

        removeq = q.remove(u[0])

        for i in q:

            if graph[u[0]][i] != 0: 
                if d[i] == 0 or d[i] > d[u[0]] + graph[u[0]][i] and graph[u[0]][i] != 0:
                    d[i] = d[u[0]] + graph[u[0]][i]     
        
        del d[u[0]]

    return S
    

def _print(graph, v, s):
    print("Duong di ngan nhat tu dinh nguon:", s)
    print("Dinh den \tDuong di ngan nhat ")
    
    _dijkstra = dijkstra(graph, v, s)
    for i in _dijkstra:
        print(i, "\t\t", _dijkstra[i])

if __name__ == "__main__":
    # Co the thay doi do thi khac nhu duoi day 

    # vi du phan ly thuyet
    graph = [
        [0, 0, 9, 2, 5],
        [0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 8, 1, 0, 0]
    ]   

    # bai tap Exercises 9.3 bai 2 y b
#     graph = [
# #       [a, b, c, d, e, f, g, h, i, j, k, l]
#         [0, 3, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0], #a
#         [3, 0, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0], #b
#         [5, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0], #c
#         [4, 0, 2, 0, 1, 0, 0, 5, 0, 0, 0, 0], #d
#         [0, 3, 0, 1, 0, 2, 0, 0, 4, 0, 0, 0], #e
#         [0, 6, 0, 0, 2, 0, 0, 0, 0, 5, 0, 0], #f
#         [0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 6, 0], #g
#         [0, 0, 0, 5, 0, 0, 3, 0, 6, 0, 7, 0], #h
#         [0, 0, 0, 0, 4, 0, 0, 6, 0, 3, 0, 5], #i
#         [0, 0, 0, 0, 0, 5, 0, 0, 3, 0, 0, 9], #j
#         [0, 0, 0, 0, 0, 0, 6, 7, 0, 0, 0, 8], #k
#         [0, 0, 0, 0, 0, 0, 0, 0, 5, 9, 8, 0], #l
#     ]
    
    v = len(graph)
    s = 0
    S = dict()

    _print(graph, v, s)