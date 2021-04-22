from collections import deque
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx= [0,0,-1,1]
dy= [-1,1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((y,x))
    
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx]==1:
                    graph[ny][nx] = graph[y][x]+1
                    queue.append((ny,nx))

    return graph[n-1][m-1]

print(bfs(0,0))