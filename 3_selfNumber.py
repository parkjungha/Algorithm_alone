def d(n):
    if n<=99:
        return n+n//10+n%10
    elif n<=999:
        return n+n//100+n%100//10+n%10
    elif n<=9999:
        return n+n//1000+n%1000//100+n%100//10+n%10
    else:
        return 10001
    
li = list(range(1,10001))
nonSelfNum = []
for i in li:
    nonSelfNum.append(d(i))

result = [x for x in li if x not in nonSelfNum]

for i in result:
    print(i)