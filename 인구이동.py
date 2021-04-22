from collections import deque
import sys

input = sys.stdin.readline

n,l,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

ans = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    move_q = deque()
    q.append((x,y))
    c[x][y] = 1
    people,cnt = 0,0
    while q:
        x,y = q.popleft()
        move_q.append((x,y))
        people += a[x][y]
        cnt += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and c[nx][ny]==0:
                if l <= abs(a[x][y]-a[nx][ny])<=r:
                    c[nx][ny] = cnt
                    q.append((nx,ny))

    while move_q:
        x,y = move_q.popleft()
        a[x][y] = people//cnt
    
    if cnt == 1:
        return 0
    return 1

while True:
    q = deque()
    c = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if c[i][j] == 0:
                cnt += bfs(i,j)
    if cnt == 0:
        break
    ans += 1

print(ans)