import random
import time

def min_a(a, k):
    i_min = k

    for i in range(k + 1, len(a)):
       
        if a[i] < a[i_min]:
            i_min = i

    return i_min
    
def sort(a):
    for i in range(0, len(a) - 1):
        min_i = min_a(a, i)

        temp = a[i]
        a[i] = a[min_i]
        a[min_i] = temp
        
    return a

def array_a(n):
    a = []
    
    for i in range(n):
        a.append(random.randint(-100, 100))

    return a

n = int(input("Nhap so phan tu mang n:"))
array = array_a(n)
print(array)

time_start = time.time()
ss = sort(array)
time_end = time.time()

time = time_end - time_start

print(ss)    
print("Time: ", time, "s" )