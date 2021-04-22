from collections import deque

m,n,k = map(int,input().split())
s= [[0]*n for _ in range(m)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = []
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            s[j][k] = 1
for i in range(m):
    for j in range(n):
        if s[i][j] == 0:
            count = 1
            s[i][j] = 1
            q= deque()
            q.append((i,j))
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx<m and 0<=ny<n and s[nx][ny] == 0:
                        s[nx][ny] = 1
                        count += 1
                        q.append((nx,ny))
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i,end= ' ')