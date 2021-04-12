n=int(input())
room = 1
rule = 1
num = 1

if n ==1:
    print(1)
else:
    while True:
        num += 6*rule
        room += 1
        if (n<=num):
            break
        rule+=1
    print(room)