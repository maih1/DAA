import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nhap so n: "))

timeStart = time.time() 
print("So fibonacci thu {}:".format(n),fibonacci(n))
timeEnd = time.time()

time = timeEnd - timeStart

print("Thoi gian:", time)
