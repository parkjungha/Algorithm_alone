n = int(input())
inputList = []
for i in range(n):
    quiz = input()
    inputList.append(quiz)
    
for quiz in inputList:
    count = 0
    sum = 0
    for j in quiz:
        if j =='O':
            count += 1
        else:
            count = 0
        sum += count
    print(sum)