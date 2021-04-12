li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = list(input()) 
time = 0
for i in s:
    for j in range(len(li)):
        if i in li[j]:
            time += j+3

print(time)