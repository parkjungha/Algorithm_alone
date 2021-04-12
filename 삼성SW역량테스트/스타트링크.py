from itertools import combinations
import sys

input = sys.stdin.readline

def dfs(idx,cnt): # N/2명 모든 조합
    global ans,select
    if cnt == N/2: 
        start,link = 0,0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    start += mat[i][j]
                elif not select[i] and select[j]:
                    link += mat[i][j]
        ans = min(ans,abs(start-link))

    else:
        for i in range(idx,N):
            if select[i]:
                continue
            select[i] = 1
            dfs(i+1,cnt+1)
            select = 0

N = int(input()) # N은 짝수
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))
select = [0 for i in range(N)]
ans = sys.maxsize
dfs(0,0)
print(ans)