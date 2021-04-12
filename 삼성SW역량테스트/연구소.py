'''
1. Select the wall to build
2. Spread Virus
3. Compute the saftey area

Repeat 1-3 for the every combination of wall selection 
Lastly, Repeat the max value of safety area.
'''

import copy # 딥카피 사용
import sys # 인풋 빠르게 받기

input = sys.stdin.readline

N,M = map(int,input().split())
NM = []
for i in range(N):
    NM.append(list(map(int,input().split())))

dy = [-1,1,0,0] # 상 하 좌 우 (row 단위)
dx = [0,0,-1,1] # 상 하 좌 우 (column 단위)

max_value = 0 # safety area

def wall(start,count):
    global max_value
    if count == 3: # 종료조건, 벽 3개 선택 완료
        sel_NM = copy.deepcopy(NM) # deepcopy로 벽 3개 모두 선택된 배열 복사
        for r in range(N): # 바이러스 퍼뜨리기
            for c in range(M):
                virus(r,c,sel_NM)
        safe_counts = sum(i.count(0) for i in sel_NM) 
        max_value = max(max_value,safe_counts)
        return True

    else: # 아직 벽 3개가 선택되지 않은 경우
        for i in range(start,N*M): # 2차원 배열에서 조합 구하기
            y = i//M # Row(y)는 i를 M(column의 수)으로 나눈 몫
            x = i%M # Column(x)는 i를 M(column의 수)으로 나눈 나머지
            if NM[y][x] == 0: # 안전 영역인 경우 벽으로 선택 가능
                NM[y][x] = 1 # 벽으로 변경
                wall(i,count+1) # 재귀적으로 벽 선택
                NM[y][x] = 0 # ???????????????????????????????

def virus(y,x,sel_NM):
    if sel_NM[y][x] == 2: # 선택된 셀이 바이러스면
        # 상하좌우 4방향을 확인하고 범위를 벗어나거나, 벽을 만날때까지 반복
        for dir in range(4):
            ny = y+dy[dir]
            nx = x+dx[dir]
            if ny>=0 and nx >= 0 and ny<N and nx<M: # 범위를 벗어나지 않을 때
                if sel_NM[ny][nx] == 0:
                    sel_NM[ny][nx] = 2 
                    virus(ny,nx,sel_NM) # 재귀적으로 바이러스 퍼뜨림

wall(0,0)
print(max_value)



