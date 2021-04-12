def hansu(n):
    if n<100:
        return True
    li = list(str(n))
    diff = []
    for i in range(len(li)-1):
        diff.append(int(li[i+1])-int(li[i]))
    for j in range(len(diff)-1):
        if diff[j] != diff[j+1]:
            return False
        else:
            return True

def hansu2(n):
    if n<100:
        return True
    if (n//100-n%100//10) == (n%100//10-n%10):
        return True
    else: return False

n = int(input())
count=0
for k in range(1,n+1):
    if hansu2(k)==True:
       count+=1
print(count)