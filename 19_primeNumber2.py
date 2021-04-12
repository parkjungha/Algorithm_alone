def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
    
M=int(input())
N=int(input())
primeList = []

for i in range(M,N+1):
    if isPrime(i):
        primeList.append(i)

if(len(primeList)==0):
    print(-1)
else:
    print(sum(primeList))
    print(min(primeList))