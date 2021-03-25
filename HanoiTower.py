import time

def hanoiTower(n, a, b, c):
    if n > 0:
        
        hanoiTower(n - 1, a, c, b)
        
        if a[0]:
            disk = a[0].pop()
            print( "Chuyen " + str(disk) + " tu " + a[1] + " den " + c[1])
            c[0].append(disk)
    
        hanoiTower(n - 1, b, a, c)
        
a = ([5,4,3,2,1], "a")
c = ([], "c")
b = ([], "b") 

print(a, b, c)

hanoiTower(len(a[0]),a,b,c)

print(a, b, c)