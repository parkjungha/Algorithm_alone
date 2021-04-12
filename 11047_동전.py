N,K=map(int,input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
coins.reverse()

count = 0 

for coin in coins:
    count += K//coin #젤 큰 단위의 동전으로 나눈 몫을 더함
    K %= coin #나머지

print(count)