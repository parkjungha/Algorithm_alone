import sys

input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
order = list(map(int,input().split()))

dx = [0,0,-1,1] # 동 서 북 남 1 2 3 4
dy = [1,-1,0,0] 

dice = [0,0,0,0,0,0] # 주사위 초기화

def rotate(i):
    if i==1:
        dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif i==2:
        dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
    elif i==3:
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
    elif i==4:
        dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]
    return dice

for i in order:
    nx = x+dx[i-1]
    ny = y+dy[i-1]
    if 0<=nx<n and 0<=ny<m:
        dice = rotate(i)
        if array[nx][ny] == 0:
            array[nx][ny] = dice[5]
        else:
            dice[5] = array[nx][ny]
            array[nx][ny] = 0
        x,y = nx,ny
        print(dice[0])
    

