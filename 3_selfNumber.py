def d(n):
    return n+n//10+n%10
    
li = list(range(1,10001))

for i in li:
    d(i)