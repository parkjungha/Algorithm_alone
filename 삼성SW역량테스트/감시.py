from copy import deepcopy
import sys
input = sys.stdin.readline

delta = [(0,1),(0,-1),(1,0),(-1,0)]
direction = {1:[[0],[1],[2],[3]],2:[[0,1],[2,3]],3:[[0,2],[1,3],[0,3],[1,2]],4:[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],5:[[0,1,2,3]]}

def dfs(n,arr):
    global min_sq
    if n == len(camera):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for idx,c in enumerate(camera):
            x = c[0] # camera가 있는 x좌표
            y = c[1] # camera가 있는 y좌표
            for element in arr[idx]:
                c = 1
                while True:
                    nx = x + delta[element][0]*c
                    ny = y + delta[element][1]*c
                    if 0<=nx<N and 0<=ny<M and office[nx][ny] != 6:
                        if office[nx][ny]==0 and visited[nx][ny] == False:
                            visited[nx][ny] = True
                            c+=1
                        else:
                            break
        cnt = 0
        for ii in range(N):
            for kk in range(M):
                if office[ii][jj] == 0 and visited[ii][jj] == False:
                    cnt += 1
        min_sq = min(min_sq,cnt)
        return
    for ele in direction[office[camera[n][0]][camera[n][1]]]:
        arr.apend(ele)
        dfs(n+1,arr)
        arr.pop()

N,M = map(int,input().split())
office = [list(map(int,input().split()) for _ in range(N)]
camera = []
min_sq = 0
for i in range(N):
    for j in range(M):
        if office[i][j] in range(1,6):
            camera.append((i,j))
        if office[i][j] == 0:
            min_sq += 1
dfs(0,[])
print(min_sq)