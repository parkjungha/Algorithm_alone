s = input()
alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
for i in alphabet:
    if i in s:
        count += s.count(i)
        s = s.replace(i,'_')

print(count+len(s.replace('_','')))