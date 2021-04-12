n = int(input())
plan = input().split()

dy = [-1,1,0,0] # L R U D , 0,1,2,3
dx = [0,0,-1,1] # L R U D
dir = ['L','R','U','D']

x=1
y=1

for p in plan:
    for d in range(len(dir)):
        if p == dir[d]:
            x += dx[d]
            y += dy[d]
        if x<1 or x>n or y<1 or y>n:
            x -= dx[d]
            y -= dy[d]
            continue
        
print(x,y)