from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = []

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4): 
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    count.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)

count.sort()
print(len(count))
for i in count:
    print(i)
