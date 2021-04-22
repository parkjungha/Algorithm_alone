n,m = map(int,input().split())
r,c,d = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean(x,y,d):
    global ans
    if arr[x][y] ==0:
        arr[x][y] = 2
        ans += 1
    for i in range(4):
        nd = (d+3)%4
        nx = x+dx[nd]
        ny = y+dy[nd]
        if arr[nx][ny] == 0:
            clean(nx,ny,nd)
            return
        d = nd
    nd = (d+2)%4
    nx = x+dx[nd]
    ny = y+dy[nd]
    if arr[nx][ny] ==1:
        return 
    clean(nx,ny,d)
    
    
clean(r,c,d)
print(ans)