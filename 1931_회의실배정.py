N=int(input())
times = []
for i in range(N):
    times.append(list(map(int,input().split())))

t=0
count=0

for time in times:
    if time[0] >= t:
        count += 1
        t = time[1]

print(count)