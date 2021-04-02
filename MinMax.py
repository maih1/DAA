import random
import time

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

def inputArray(n):
    a = []
    
    for i in range(n):
        a.append(random.randint(1000, 10000))

    return a

if __name__ == '__main__':
    
    n = int(input("Nhap so phan tu cua mang: "))    

    array = inputArray(n)

    print("Mang array: ", array)

    timeStart = time.time()
    result = minMax(array, 0, len(array) - 1)
    timeEnd = time.time()

    time = timeEnd - timeStart

    print("Min: {}, Max: {}".format(result[0], result[1]))
    print("Time:", round(time, 6))