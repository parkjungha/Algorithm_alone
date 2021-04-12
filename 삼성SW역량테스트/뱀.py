
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

# N = int(input())
# K = int(input())
# apples = []
# for i in range(K):
#     apples.append(list(map(int,input().split())))
# L = int(input())
# directions = []
# for i in range(K):
#     directions.append(input().split())

# board = [['X']*(N+2)] # 윗 벽 만들기
# for i in range(N): # board 행렬 만들기
#     board.append(['X']+[0]*N+['X'])
# board.append([['X']*(N+2)]) # 밑 벽 만들기

# for i in apples: # board에 사과 있는 곳 표시하기
#     board[i[0]][i[1]] = 1 

# print(board)

# 초기화
# length = 1
# headx = 1
# heady = 1
# tailx = 1
# taily = 1
# dx = 1 # 처음엔 오른쪽 방향으로 출발
# dy = 0

# def move(headx,heady,tailx,taily,dx,dy):
#     if board[headx+dx][heady+dy] == 1: #이동하는 칸이 1이면, 즉 사과가 있으면
#         headx += dx
#         heady += dy
#         board[headx+dx][heady+dy] = 0 # 사과 쳐먹음
#     elif board[headx+dx][heady+dy] == 0: # 사과가 없다면 꼬리도 이동
#         headx += dx 
#         heady += dy
#         tailx += dx
#         taily += dy

from collections import deque

def change(d,c):
    if c == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d

# 상 우 하 좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def start():
    direction = 1
    time = 1
    y,x = 0,0
    visited = deque([[y,x]])
    arr[y][x] = 2
    while True:
        y,x = y+dy[direction], x+dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:
                temp_y, temp_x = visited.popleft() # 꼬리가 있는 자리 queue에서 불러옴
                arr[temp_y][temp_x] = 0 # 보드에서 꼬리 제거
            arr[y][x] = 2 #뱀이 지난 곳 2로 저장
            visited.append([y,x]) # queue에 방문 기록 추가
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else: # 본인 몸에 부딪히거나 , 벽에 부딪힌 경우
            return time
    
if __name__ == '__main__':
    N = int(input())
    K = int(input())
    arr = [[0]*N for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        arr[a-1][b-1] = 1 #사과 있는 곳 표시
    L = int(input())
    times = {} 
    for i in range(L):
        X,C = input().split()
        times[int(X)] = C
    print(start())