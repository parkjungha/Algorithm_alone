from collections import deque

n = int(input())
s = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []
for i in range(n):
    s.append(list(input()))
    
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    s[x][y] = "0"
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and s[nx][ny] == "1":
                s[nx][ny] = "0"
                queue.append([nx, ny])
                count += 1
    cnt.append(count)

for i in range(n):
    for j in range(n):
        if s[i][j] == "1":
            bfs(i, j)
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)