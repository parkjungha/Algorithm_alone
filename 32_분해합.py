n = int(input())
for i in range(1,n):
    sum = i
    for k in str(i):
        sum += int(k)
    if sum == n:
        print(i)
        break
    if i == n:
        print(0)