import sys
from collections import deque

input = sys.stdin.readline

n,l,r = map(int,input().split())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q= deque()
    q.append((i,j))
    unit = []
    unit.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
                if l<=abs(A[nx][ny]-A[x][y])<=r:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    unit.append((nx,ny)) # 유닛 정보 저장
    return unit

cnt = 0
while True:
    visit = [[0]*n for _ in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                unit = bfs(i,j)
                if len(unit)>1:
                    isTrue = True
                    unit_mean = sum([A[x][y] for x,y in unit])//len(unit)
                    for x,y in unit:
                        A[x][y] = unit_mean
    if isTrue == False:
        break
    cnt += 1

print(cnt)