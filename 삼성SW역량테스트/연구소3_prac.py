from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
virus = []
notWall = 0

for i in range(n):
    a = list(map(int,input().split()))
    array.append(a)
    for j in range(n):
        if a[j] == 2:
            virus.append((i,j))
        if a[j] != 1:
            notWall += 1
            
mvirus = list(combinations(virus,m))

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0 and array[nx][ny]!=1:
                visit[nx][ny]=1
                cs[nx][ny] = cs[x][y]+1
                q.append((nx,ny))

res = sys.maxsize
for mv in mvirus:
    visit = [[0]*n for _ in range(n)]
    cs = [[-1]*n for _ in range(n)]
    q = deque()
    for i,j in mv:
        q.append((i,j))
        cs[i][j] = 0
        visit[i][j] = 1
    bfs()
    cnt = 0
    for j in visit:
        cnt += j.count(1)
    if notWall == cnt:
        max_val = 0
        for i in range(n):
            for j in range(n):
                if array[i][j] == 0:
                    max_val = max(max_val,cs[i][j])
        res = min(res,max_val)

print(res if res!=sys.maxsize else -1)