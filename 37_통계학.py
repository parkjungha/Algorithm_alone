import sys
from collections import Counter

n=int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()

cnt = Counter(li)
mode = cnt.most_common()
if len(li)>1:
    if mode[0][1] == mode[1][1]:
        mod = mode[1][0]
    else:
        mod = mode[0][0]
else:
    mod = mode[0][0]
    
print(round(sum(li)/len(li)))
print(li[len(li)//2])
print(mod)
print(li[-1]-li[0])