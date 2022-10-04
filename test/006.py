q=open('inf_26_04_21_24.txt').readline()
s=[0]
c=0
for a in q:
    if a.count('G') >= 25:
        x=len(a)
        for w in range(0,x):
            while a[c]==a[w]:
                s.append((x-w)-c+3)
            else:
                c+=1
print(max(s))