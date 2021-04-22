from copy import deepcopy
import sys

input = sys.stdin.readline
r,c,t = map(int,input().split())
array = []
cl = [] # 공기청정기의 행 번호 저장 (원소 두개)
for i in range(r):
    a = list(map(int,input().split()))
    array.append(a)
    if array[i][0]==-1:
        cl.append(i)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def spread():
    global array
    array2 = deepcopy(array)
    for x in range(r):
        for y in range(c):
            if array[x][y]>=5: # 미세먼지가 있는 칸
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<r and 0<=ny<c and array[nx][ny] != -1: # 범위안에 있으면서 공기청정기가 아닌 칸에
                        array2[nx][ny] += array[x][y]//5
                        array2[x][y] -= array[x][y]//5
    array = array2

def clean():
    global array
    array2 = deepcopy(array)

    # 상단 cl[0]
    array2[cl[0]][1] = 0 
    for i in range(1,c-1):
        array2[cl[0]][i+1] = array[cl[0]][i] # 오른쪽으로 
    for i in range(cl[0],0,-1):
        array2[i-1][c-1] = array[i][c-1] # 위쪽으로
    for i in range(c-1,0,-1):
        array2[0][i-1] = array[0][i] # 왼쪽으로
    for i in range(0,cl[0]-1): 
        array2[i+1][0] = array[i][0] # 아래쪽으로
    # array2[cl[0]][0] = -1

    # 하단 cl[1]
    array2[cl[1]][1] = 0
    for i in range(1,c-1):
        array2[cl[1]][i+1] = array[cl[1]][i] # 오른쪽으로     
    for i in range(cl[1],r-1):
        array2[i+1][c-1] = array[i][c-1] # 아래쪽으로
    for i in range(c-1,0,-1):
        array2[r-1][i-1] = array[r-1][i] # 왼쪽으로
    for i in range(r-1,cl[1],-1):
        array2[i-1][0] = array[i][0]
    array2[cl[1]][0] = -1
    array = array2

for i in range(t):
    spread()
    clean()

ans = 0
for i in range(r):
    for j in range(c):
        if array[i][j]>0:
            ans+= array[i][j]

print(ans)
