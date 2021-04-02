def minMax(a, l, r):
    if (r - l) <= 1:
        a1 = a[l]
        a2 = a[r]
        return (min(a[l], a[r]), max(a[l], a[r]))
    else:
        m = (l + r) // 2
        x = minMax(a, l, m)
        y = minMax(a, m, r)

        return (min(x[0], y[0]), max(x[1], y[1]))

a = [3, 5, 2, 60, -3, 9, 12, 1, 5, 70, 23, 23, 2]

result = minMax(a, 0, len(a) - 1)
print(result)