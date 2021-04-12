from itertools import combinations
import sys

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if borad[i][j] == 1: house.append((i,j))
        if board[i][j] == 2: chicken.append((i,j))

minv = sys.maxsize
for ch in combinations(chicken,M): # 치킨집중에서 M개 조합
    sumv = 0
    for home in house: # 집마다
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv: break
    if sumv<minv:
        minv = sumv

print(minv)

from itertools import combinations

input = sys.stdin.readline
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
home, chicken = [],[]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home.append((i,j))
        if maps[i][j] == 2:
            chicken.append((i,j))
        
ans = 10000
for i in combinations(chicken,m):
    tmp = 0
    for j in home:
        minVal = 10000
        for k in i:
            distance = abs(k[0]-j[0])+abs(k[1]-j[1])
            minVal = min(minVal,distance)
        tmp += minVal
    ans = min(ans,tmp)

print(ans)


from collections import combinations
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append((i,j))
        if board[i][j]==2:
            chicken.append((i,j))

ans = sys.maxsize
for ch in combinations(chicken,m):
    tmp = 0
    for h in house:
        minVal = 10000
        for k in ch:
            distance = abs(k[0]-j[0])+abs(k[1]-k[1])
            minVal = min(minVal,distance)
        tmp += minVal
    ans = min(ans,tmp)

print(ans)











































