c = int(input())

for i in range(c):
    s = list(map(int,input().split()))
    n = s[0]
    s = s[1:]
    
    avg = sum(s)/len(s)
    num = 0
    for j in s:
        if j>avg:
            num+=1
    rate = float(num/len(s))*100
    print('%.3f%%' % rate)