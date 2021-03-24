import time

s = ''

def reverse(s):
    return s[::-1]

def binary_1(n):
    global s

    if n == 0:
        return int(reverse(s))
    elif n > 0:
        s = s + str(n % 2)
        return binary_1(n // 2)
    
def binary_2(n):
    s = ''
    
    while n > 0:
        s = s + str(n % 2)
        # b.append(n % 2)
        n = n // 2

    return int(reverse(s))

n = int(input("Nhap so nguyen n: "))

time_start1 = time.time()
print("Phuong phap de quy:",binary_1(n))
time_end1 = time.time()

time1 = time_end1 - time_start1

print("Thoi gian de quy: ", time1, "s" )         

time_start2 = time.time()
print("Phuong phap vong lap:",binary_2(n))
time_end2 = time.time()

time2 = time_end2 - time_start2

print("Thoi gian vong lap : ", time2, "s" )         
