test=int(input())
for i in range(test):
    k = int(input())
    n = int(input())
    f = [x+1 for x in range(n)]

    for j in range(k):
        for x in range(1,n):
            f[x] += f[x-1]

    print(f[-1])
