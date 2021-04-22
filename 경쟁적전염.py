from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())
array = []
virusList = []
for i in range(n):
    array.append(list(map(int,input().split())))
    for j in range(n):
        if array[i][j] != 0:    
            virusList.append((array[i][j],0,i,j)) # virus 종류, 시간, x,y 좌표 (위치)

target_s,target_x,target_y = map(int,input().split())

virusList.sort()
q = deque(virusList)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    virus,s,x,y = q.popleft()
    if s==target_s:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and array[nx][ny]==0:
            array[nx][ny]=virus
            q.append((virus,s+1,nx,ny))

print(array[target_x-1][target_y-1])
