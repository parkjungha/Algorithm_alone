n=int(input())
i=1
numList=[]
while True:
    if '666' in str(i):
        numList.append(i)
    if len(numList)==n:
        break
    i += 1

print(numList[n-1])
