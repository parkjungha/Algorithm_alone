import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
array = []
for i in range(3): # 3*3 배열 입력
    array.append(list(map(int,input().split())))

def operation(array):
    if len(array)>100: # array의 행 개수가 100보다 크면
        array = array[:100]
    if len(array[0])>100: # array의 열의 개수가 100보다 크면
        for a in array:
            a = a[:100]

    new_array = []
    for row in array:
        d = {}
        for i in row:
            if i!=0 and i not in d.keys():
                d[i] = row.count(i)
        sorted_d = sorted(d.items(),key=lambda x:(x[1],x[0])) # 값을 기준으로 dictionary 정렬
        new = []
        for i in sorted_d:
            new.append(i[0])
            new.append(i[1])

        new_array.append(new)

    #행 또는 열의 크기가 커진 곳에는 0이 채워진다
    max_len= max(len(x) for x in new_array)
    for row in new_array: 
        if len(row)<max_len:
            for i in range(max_len-len(row)):
                row.append(0)

    return new_array

def transpose(array):
    row = len(array) # row
    col = len(array[0]) # col
    new = [[0]*row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            new[j][i] = array[i][j]
    return new

cnt = 0
while True:
    col = len(array[0]) # 2
    row = len(array) # 3
    if 0<=r-1<row and 0<=c-1<col and array[r-1][c-1] == k:
        print(cnt)
        break
    if cnt>=100:
        print(-1)
        break
    cnt += 1
    if row>=col: # 행의 개수 ≥ 열의 개수인 경우
        array = operation(array)
    elif row<col: # 행의 개수 < 열의 개수인 경우
        array = transpose(operation(transpose(array)))

