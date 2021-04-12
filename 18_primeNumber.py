def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n=int(input())
count = 0 
li = input().split()
li = [int(x) for x in li]
for i in li:
    if isPrime(i):
        count+=1

print(count)