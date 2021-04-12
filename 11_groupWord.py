n=int(input())

count=0
for i in range(n):
    s = input()
    letters=[]
    b=True
    for j in s:
        if j not in letters:
            letters.append(j)
        else:
            if j == letters[-1]:
                continue
            else:
                b = False
    if b==True:
        count += 1

print(count)
