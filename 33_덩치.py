n= int(input())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))

result = []
for j in li:
    count = 0
    for k in li:
        if j[0]<k[0] and j[1]<k[1]:
            count += 1
    result.append(count+1)

for _ in result:
    print(_,end=' ')