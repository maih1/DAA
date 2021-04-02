import random
import time

def binarySearch(a, x, l, r):
    
    # l=a[len(a)]
    if x < a[0] or x > a[len(a) - 1]:
        return -1
    elif l == r:
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

def inputArray(n):
    a = []
    
    for i in range(n):
        a.append(random.randint(1000, 10000))

    return sorted(a)

if __name__ == '__main__':
    
    n = int(input("Nhap so phan tu cua mang: "))    
    x = int(input("Nhap so can tim x: "))

    array = inputArray(n)

    # print("Mang array: ", array)

    timeStart = time.time()
    result = binarySearch(array, x, 0, len(array) - 1)
    timeEnd = time.time()

    time = timeEnd - timeStart

    if result != -1:
        print("So {} xuat hien tai vi tri: ".format(x), result)
    else:
        print('Khong co so {} trong mang'.format(x))

    print("Time:", round(time, 6))