def printArray(a):
    for i in range(len(a)):
        print(a[i], end="")
    print()

def binary(a, i):
    if i == len(a):
        printArray(a)
        return
    
    a[i] = 0
    binary(a, i + 1)

    a[i] = 1
    binary(a, i + 1)

if __name__ == "__main__":
    n = int(input("Nhap so day nhi phan n = "))
    a = [0] * n

    print("Day nhi phan duoc tao co do dai la",n )
    binary(a, 0)