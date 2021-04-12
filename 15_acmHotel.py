t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split())
    li = []
    for j in range(1,w+1):
        for i in range(1,h+1):
            if len(str(j))==1:
                li.append(str(i)+'0'+str(j))
            else:
                li.append(str(i)+str(j))

    print(li[n-1])