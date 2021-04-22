from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
dx= [-1,1,0,0]
dy= [0,0,-1,1]
n,m = map(int,input().split())
array = []
virus = []
notWall = 0
result = sys.maxsize
for i in range(n):
    array.append(list(map(int,input().split())))
    for j in range(n):
        if array[i][j] == 2:
            virus.append((i,j))
        if array[i][j] != 1:
            notWall += 1
def bfs():
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0 and array[nx][ny] != 1: # 벽이 아닌 곳
                visit[nx][ny]=1
                cs[nx][ny]=cs[x][y]+1
                q.append((nx,ny))
                
cq = list(combinations(virus,m))
for i in cq:
    q= deque()
    visit = [[0]*n for _ in range(n)]
    cs = [[-1]*n for _ in range(n)]
    for x,y in i:
        visit[x][y] = 1
        cs[x][y] = 0
        q.append((x,y))
    bfs()
    cnt = 0
    for j in visit:
        cnt += j.count(1)
    if cnt == notWall:
        max_value = 0
        for j in range(n):
            for k in range(n):
                max_value = max(max_value,cs[j][k])
        result = min(max_value,result)
        
print(result if result!=sys.maxsize else -1)