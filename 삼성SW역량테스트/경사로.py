import sys

input = sys.stdin.readline

def check(li):
    sw = [0 for i in range(n)] # 경사로가 있는지 체크
    for i in range(n-1): 
        if li[i]==li[i+1]: # 높이가 같으면 계속 검사
            continue
        if abs(li[i]-li[i+1])>1: # 차이가 1보다 크면
            return False
        if li[i]>li[i+1]: # 높-낮
            low = li[i+1]
            for j in range(i+1,i+1+l): # 낮은 칸으로부터 L만큼 연속된 칸 검사
                if 0<=j<n: # j가 0보다 크고 n보다 작을 때
                    if li[j] != low: # L개만큼 연속 안되면, 즉 높이가 다르면
                        return False
                    if sw[j]==True: # 이미 그 칸에 경사로가 설치되어 있으면
                        return False
                    sw[j] = True # 해당 안되면 L개의 연속된 낮은 칸에 경사로 설치함
                else: # j가 0보다 작거나 n보다 클 때 ????
                    return False
        else: # 낮-높
            low = li[i]
            for j in range(i,i-l,-1): # 낮은 칸으로부터 왼쪽으로 L만큼 연속된 값 검사
                if 0<=j<n:
                    if li[j] != low:
                        return False
                    if sw[j]==True:
                        return False
                    sw[j]=True
                else:
                    return False
    return True

n, l = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
cnt = 0
for i in s:
    if check(i):
        cnt += 1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(s[j][i])
    if check(temp):
        cnt += 1
print(cnt)