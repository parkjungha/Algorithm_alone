n=int(input())
userlist= []
for i in range(n):
    userlist.append(input().split())

userlist.sort(key=lambda x: (int(x[0])))

for i in userlist:
    print(i[0],i[1])