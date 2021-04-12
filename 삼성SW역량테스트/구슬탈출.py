from collections import deque

n,m = map(int,input().split())
dx=[1,-1,0,0] # 오 왼 아래 위
dy=[0,0,-1,1]
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
s = []

def move(i,j,dx,dy):
    c = 0
    while s[i+dx][j+dy]!='#' and s[i][j]!='O':
        i += dx
        j += dy
        c += 1
    return i,j,c

def bfs():
    while q:
        ri,rj,bi,bj,d = q.popleft()
        if d>10:
            break
        for i in range(4):
            nri,nrj,rc = move(ri,rj,dx[i],dy[i]) # 빨간 구슬과 파란 구슬 똑같이 상,하,좌,우 O 또는 #를 만나기 전까지 이동시켜준다. 
            nbi,nbj,bc = move(bi,bj,dx[i],dy[i])
            if s[nbi][nbj] != "O": # 파란 구슬이 O를 만나지 않을 때!
                if s[nri][nrj] == "O": # 빨간 구슬이 O를 만난다면
                    print(d)
                    return
                if nri == nbi and nrj == nbj: # 빨간 구슬과 파란 구슬이 겹쳐있다면 더 많이 이동한 구슬을 그 한칸 전으로 다시 이동
                    if rc>bc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visit[nri][nrj][nbi][nbj]: # 이동한 위치가 아직 방문하지 않은 곳이라면 q에 좌표와 d(이동 횟수)를 넣어준다
                    visit[nri][nrj][nbi][nbj] = True
                    q.append([nri,nrj,nbi,nbj,d+1])
    print(-1)

for i in range(n):
    a = list(input())
    s.append(a)
    for j in range(m):
        if a[j] == "R":
            ri,rj = i,j
        if a[j] == "B:
            bi,bj = i,j

q = deque()
q.append([ri,rj,bi,bj,1])
visit[ri][rj][bi][bj] = True
bfs()