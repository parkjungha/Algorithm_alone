from itertools import combinations
from copy import deepcopy

n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

chicken = []
houses = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            chicken.append((i,j))
        elif array[i][j] == 1:
            houses.append((i,j))

mchicken = list(combinations(chicken,m))
ans = 10000000

for mk in mchicken: # m개의 뽑힌 치킨집 목록
    temp = deepcopy(array) # array 깊은 복사. m개의 치킨집 조합에 대해서만 사용할 temp matrix 복사
    city_dist = 0 # 도시의 치킨거리    
    for h in houses: # 한 집집 마다 돌면서
        min_dist = 100000
        for j in mk: # 특정 집에서 치킨집 마다 돌면서 거리 계산
            dist = abs(h[0]-j[0])+abs(h[1]-j[1]) # 거리
            min_dist = min(min_dist,dist) # 작은 거리만 저장
        city_dist += min_dist # 가장 작은 치킨거리 도시의 치킨거리 변수에 더해줌
    ans = min(ans,city_dist)

print(ans)