import sys
input = sys.stdin.readline
N,M=map(int,input().split())
r,c,d=map(int,input().split())
NM=[]
for i in range(N):
    NM.append(list(map(int,input().split())))

dy = [-1,0,1,0] # 북 동 남 서 
dx = [0,1,0,-1]

cnt = 0

def clean(r,c,d):
    global cnt
    if NM[r][c] == 0:
        NM[r][c] = 2 # 현재 위치를 청소한다.
        cnt += 1 
    for dir in range(4): # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다
        nd = (d+3)%4
        nr = r+dy[nd]
        nc = c+dx[nd]
        if NM[nr][nc] == 0: # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
            clean(nr,nc,nd) # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            return
        d = nd # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.

    nd = (d+2)%4 # 후진
    nr = r+dy[nd]
    nc = c+dx[nd]  
    if NM[nr][nc] == 1: # 뒤쪽 방향이 벽인 경우
        return # 중지
    clean(nr,nc,d) # 벽이 아니면 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    
clean(r,c,d)
print(cnt)