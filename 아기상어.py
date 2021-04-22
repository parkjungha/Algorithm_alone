from collections import deque
INF = 1e9

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

now_size = 2
now_x, now_y = 0,0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x,now_y = i,j
            array[now_x][now_y] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 모든 위치까지의 최단거리만 계산하는 BFS함수
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1]*n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0 
    q = deque()
    q.append((now_x,now_y))
    dist[now_x][now_y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny]==-1 and array[nx][ny]<=now_size: # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1<=array[i][j]<now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x,y,min_dist # 먹을 물고기의 위치와 최단 거리
result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x,now_y = value[0],value[1]
        result+= value[2]

        array[now_x][now_y] = 0
        ate += 1

        if ate>now_size:
            now_size+= 1
            ate = 0

