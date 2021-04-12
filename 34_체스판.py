N,M = map(int,input().split())
matrix = []
for i in range(N):
    matrix.append(list(input()))

cnt = 0
for i in range(N):
    for j in range(M):
        if j+1 != M:
            if matrix[i][j] == matrix[i][j+1]:
                cnt += 1
                matrix[i][j+1]
        if i+1 != N:
            if matrix[i][j] == matrix[i+1][j]:
                cnt += 1

print(cnt)