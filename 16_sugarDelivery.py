n=int(input())
box = 0

while True:
    if n%5 == 0:
        box += (n//5)
        print(box)
        break
    box += 1
    n -= 3
    if n<0:
        print(-1)
        break