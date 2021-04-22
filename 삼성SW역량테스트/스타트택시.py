import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1] 
n,m,r = map(int,input().split()) # 손님 m명, 남은 연료의 양 r
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
tx,ty = map(int,input().split()) # 택시의 시작 위치
tx -= 1
ty -= 1
src = []
dest = []
for i in range(m):
    src_x,src_y,dest_x,dest_y = map(int,input().split())
    src.append((src_x-1,src_y-1)) 
    dest.append((dest_x-1,dest_y-1))


def bfs(x,y): # 현재 위치가 주어질 때, 나머지 모든 칸에 대한 최단거리 탐색
    dist = [[-1]*n for _ in range(n)] # 최단거리 저장할 어레이
    visit = [[0]*n for _ in range(n)]
    q = deque()
    q.append((x,y)) # 시작노드 queue에 넣기
    visit[x][y] = 1
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0: # 범위안에 속하면서 방문하지 않은 노드이고 벽이 아니면
                visit[nx][ny] = 1
                if array[nx][ny]!=1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))

    return dist

isTrue = False

for i in range(m): # 손님 m명에 대해서 반복
    temp = bfs(tx,ty) # 택시의 위치에서 모든 칸 최단거리를 담고있는 array 리턴
    min_dist = 1000000000000
    min_x,min_y = 0,0
    min_idx = 0
    for x,y in src:
        if temp[x][y] == -1: # 손님 자리가 -1이면
            isTrue = True
        if min_dist>temp[x][y]:
            min_dist = temp[x][y] # 최단거리 손님의 거리 저장
            min_x,min_y = x,y # 최단거리 손님의 좌표 저장
            min_idx = src.index((x,y)) # 최단거리 손님의 인덱스값 저장
        elif min_dist == temp[x][y]: # 최단거리가 같으면
            if min_x > x: # 행번호가 작은걸로
                min_dist = temp[x][y]
                min_x,min_y = x,y 
                min_idx = src.index((x,y)) 
            elif min_x == x: # 행번호도 같으면
                if min_y > y: # 열번호가 작은걸로
                    min_dist = temp[x][y]
                    min_x,min_y = x,y 
                    min_idx = src.index((x,y)) 
                    
            
    r -= min_dist # 연료에서 손님한테 간 거리만큼 빼기
    if r<0: # 연료가 바닥나면
        isTrue = True
    tx,ty = min_x,min_y # 택시 최단거리 손님이 있던 좌표로 이동

    # 이제 목적지로
    temp = bfs(tx,ty) # 현재 택시 위치에서부터 또 다시 최단거리 계산한 array 리턴
    used = temp[dest[min_idx][0]][dest[min_idx][1]]
    r -= used  # 연료에서 그 손님한테로 가는 거리만큼 빼줌
    if r<0:
        isTrue = True
    tx,ty = dest[min_idx][0],dest[min_idx][1] # 목적지의 x좌표, y좌표로 택시 좌표 옮겨줌
    r += used*2 # 소모한 연료의 양의 두배를 더해줌! 연료 충전
    src.pop(min_idx)
    dest.pop(min_idx)

if isTrue:
    print(-1)
else:
    print(r)