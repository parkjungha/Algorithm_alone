from collections import deque    
import copy
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def bfs():
    global ans
    q = deque()
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 2:
                q.append((i,j)) # virus 좌표 다 queue에 담음

    w = copy.deepcopy(array)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and w[nx][ny] == 0:
                w[nx][ny] = 2
                q.append((nx,ny))
    
    
    for i in range(n):
        for j in range(m):
            if w[i][j] == 0:
                cnt += 1
        
    ans = max(ans,cnt)

def wall(x):
    if x == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if array[i][j] == 0:
                    array[i][j] = 1
                    wall(x+1)
                    array[i][j] = 0

wall(0)
print(ans)