
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()

        for i in range(4):
            
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]== 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
                
    return graph[n-1][m-1]