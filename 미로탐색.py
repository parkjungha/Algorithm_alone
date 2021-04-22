
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # 탐색 시작 노드를 큐에 삽입
    
    while queue: # queue가 빌 때 까지
        x,y = queue.popleft() # 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다

        for i in range(4): 
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m: # 범위 안에 있을 때
                if graph[nx][ny]==1: # 이동할 수 있는 칸일 때, 해당 노드를 처음 방문하는 경우에만 최단거리 기록
                    graph[nx][ny] = graph[x][y]+1 
                    queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
