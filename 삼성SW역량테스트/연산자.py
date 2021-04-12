import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
p,m,mul,div = map(int,input().split())

max_result = -1000000001
min_result = 1000000001

def dfs(cnt,result,p,m,mul,div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result,result)
        min_result = min(min_result,result)
        return
    else:
        if p:
            dfs(cnt+1,result+num[cnt],p-1,m,mul,div)
        if m:
            dfs(cnt+1,result-num[cnt],p,m-1,mul,div)
        if mul:
            dfs(cnt+1,result*num[cnt],p,m,mul-1,div)
        if div:
            dfs(cnt+1,-(-result//num[cnt]) if result<0 else result//num[cnt] ,p,m,mul,div-1)

dfs(1,num[0],p,m,mul,div)

print(max_result)
print(min_result) 
