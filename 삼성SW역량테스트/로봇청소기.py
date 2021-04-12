import sys
input = sys.stdin.readline

dr = [-1,0,1,0] # 북 동 남 서 0 1 2 3   -1 -2 -3 -4
dc = [0,1,0,-1]

def clean(r,c,d):
    global cnt
    if NM[r][c] == 0: # 현재 위치가 0이면
        NM[r][c] = 2 # 청소함 (2로 바꿈)
        cnt += 1 # 청소 횟수
    for dir in range(4): # 모든 방향에 대해서
        nd = (d+3)%4 # 현재 방향 기준으로 왼쪽으로 이동할 것임
        nr = r+dr[nd] 
        nc = c+dc[nd]
        if NM[nr][nc] == 0: # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
            clean(nr,nc,nd) # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다
            return
        d = nd # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    
    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는
    nd = (d+2)%4 # 뒤쪽 방향으로
    nr = r+dr[nd]
    nc = c+dc[nd]
    if NM[nr][nc] == 1: # 뒤 쪽 방향이 벽이면
        return # 작동 중지
    clean(nr,nc,d) # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.

N,M = map(int,input().split())
r,c,d = map(int,input().split())
NM = []
for i in range(N):
    NM.append(list(map(int,input().split())))
cnt = 0 
clean(r,c,d)
print(cnt)