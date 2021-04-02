def binarySearch(a, x, l, r):
    if l == r:
        if a[l] == x:
            return l
        else:
            return -1
    else:
        m = (l+r) // 2
        y=a[m]
        if a[m] == x:
            return m
        elif a[m] > x:
            return binarySearch(a, x, l, m - 1)
        elif a[m] < x:
            return binarySearch(a, x, m + 1, r)

a = [1, 2, 3, 4, 5, 10, 20, 40, 50]
x = 20

result = binarySearch(a, x, 0, len(a) - 1)

if result != -1:
    print(result)
else:
    print('not')