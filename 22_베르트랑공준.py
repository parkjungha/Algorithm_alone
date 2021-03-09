
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

li = list(range(2,246912))
prime_li = []
for i in li:
    if isPrime(i):
        prime_li.append(i)

while True:
    n = int(input())
    if n==0:
        break
    cnt = 0
    for i in prime_li:
        if i>n and i=<2*+1:
            cnt+=1
    print(cnt)