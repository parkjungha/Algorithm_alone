testcase = int(input())
for i in range(testcase):
    a = input().split()
    n = int(a[0])
    for j in a[1]:
        print(j*n,end='')
    print()