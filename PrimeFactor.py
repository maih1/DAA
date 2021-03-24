import time
import math

a = []
prime = 2

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    
    return True

def intPrime_1(n):
    global prime, a

    if n == 1:
        return a
    elif n % prime == 0:
        a.append(prime)
        return intPrime_1(n // prime)
    else: 
        prime += 1
        return intPrime_1(n)

def intPrime_2(n):
    a = []
    prime = 2
    
    while n > 1:
        if n % prime == 0 :
            a.append(prime)
            n = n // prime
        else:
            prime = prime + 1
    
    return a

n = int(input("Nhap so nguyen n: "))

time_start1 = time.time()
print("Phuong phap de quy:",intPrime_1(n))
time_end1 = time.time()

time1 = time_end1 - time_start1

print("Thoi gian de quy: ", time1, "s" )         

time_start2 = time.time()
print("Phuong phap vong lap:",intPrime_2(n))
time_end2 = time.time()

time2 = time_end2 - time_start2

print("Thoi gian vong lap : ", time2, "s" )