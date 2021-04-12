import sys

input = sys.stdin.readline

def check(li):
    sw = [0 for i in range(N)]
    for i in range(N-1):
        if li[i] == li[i+1]:
            continue
        if abs(li[i]-li[i+1])>1:
            return False
        if li[i]>li[i+1]: # 높 낮
            low = li[i+1]
            for j in range(i+1,i+1+L):
                if 0<=j<N:
                    if li[j] != low:
                        return False
                    if sw[j] == 1:
                        return False
                    sw[j] = 1
                else:
                    return False
        if li[i]<li[i+1]:
            low = li[i]
            for j in range(i,i-L,-1):
                if 0<=j<N:
                    if li[j] != low:
                        return False
                    if sw[j] == 1:
                        return False
                    sw[j] = 1
                else:
                    return False
    return True
        
N,L = map(int,input().split())
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))
ans = 0
for i in mat:
    if check(i):
        ans += 1

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(mat[j][i])
    if check(temp):
        ans += 1

print(ans)