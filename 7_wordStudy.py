s=input().upper()
unique = list(set(s))
cnt = []
for i in unique:
    cnt.append(s.count(i))

if cnt.count(max(cnt))>1:
    print('?')
else:
    max = cnt.index(max(cnt))
    print(unique[max])