from collections import deque
import sys

input = sys.stdin.readline

def change(d,c):
    if c=='L':
        d = (d-1)%4
    elif c=='D':
        d = (d+1)%4
    return d

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def start():
    direction = 1
    time = 1
    x,y = 0,0
    visited = deque([[y,x]])
    arr[x][y] = 2
    while True:
        x,y = x+dx[direction],y+dy[direction]
        if 0<=y<n and 0<=x<n and arr[x][y] != 2:
            if not arr[x][y] != 1:
                temp_x,temp_y = visited.popleft()
                arr[temp_x][temp_y] = 0
            arr[x][y] = 2
            visited.append([x,y])
            if time in times.keys():
                direction = change(direction,times[time])
            time+=1
        else:
            return time

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = [[0]*n for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        arr[a-1][b-1] = 1
    l = int(input())
    times ={}
    for i in range(l):
        x,c = input().split()
        times[int(x)] = c
    print(start())