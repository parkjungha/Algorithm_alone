import sys
import copy

input = sys.stdin.readline
N,M = map(int,input().split())
NM = []
for i in range(N):
    NM.append(list(map(int,input().split())))
max_value = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
virus_list= []
for i in range(N):
    for j in range(M):
        if NM[i][j] == 2:
            virus_list.append([i,j])

def wall(start,count):
    global max_value
    if count == 3:
        sel_NM = copy.deepcopy(NM)
        for i in virus_list:
            virus(i[0],i[1],sel_NM)
        safe_counts = sum(i.count(0) for i in sel_NM)
        max_value = max(max_value,safe_counts)
        return True

    else:
        for i in range(start,N*M):
            y = i//M
            x = i%M
            if NM[y][x] == 0:
                NM[y][x] = 1
                wall(i,count+1)
                NM[y][x] = 0
    
def virus(y,x,sel_NM):
    if sel_NM[y][x] == 2:
        for dir in range(4):
            ny = y+dy[dir]
            nx = x+dx[dir]
            if ny>=0 and nx>=0 and ny<N and nx<M:
                if sel_NM[ny][nx] == 0:
                    sel_NM[ny][nx] = 2
                    virus(ny,nx,sel_NM)

wall(0,0)
print(max_value)
