li = input().split()
a = int(''.join(reversed(li[0])))
b = int(''.join(reversed(li[1])))

if a>b:
    print(a)
else:
    print(b)