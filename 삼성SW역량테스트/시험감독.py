n= int(input())
a = list(map(int,input().split()))
b, c = map(int,input().split())
count = 0

#총 감독관 1명씩
for i in range(len(a)):
    a[i] -= b
    count += 1

for k in range(len(a)):
    if a[k]<=0:
        continue
    if a[k]%c == 0:
        count += a[k]//c
    elif a[k]%c != 0:
        count += a[k]//c + 1

print(count)