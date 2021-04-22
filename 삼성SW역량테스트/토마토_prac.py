from collections import deque

m,n = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

bfs()
result = -2
isTrue = False

for i in graph:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result,j)
if isTrue:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
