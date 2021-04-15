def sumA(a,L,R):
    sumA = a[L]
    i = L
    for i in range(R):
        sumA = sumA + a[i]

    return sumA

def fakeCoin(a,L,R):
    M = (L + R) // 3
    if (sumA(a,L,R) == 0):
        return (L,R)
    if (sumA(a,L,M) > sumA(a,M,2 * M)):
        return fakeCoin(a,M,2 * M)
    elif (sumA(a,L,M) < sumA(a,M,2 * M )):
        return fakeCoin(a,L,M)
    else:
        return fakeCoin(a,2 * M, R)

#authCoin: 1, fakeCoin : 0
def inputCoin(a,n):
    i = 0
    for i in range (n):
        a.append(int(input()))
    
    return a

n = int(input('Nhap n:'))
a = []
inputCoin(a,n)
print(fakeCoin(a,0,n - 1))


        