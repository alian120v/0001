0000
q=open('24.2.txt').readline()
s=[1]
c=1
for a in range(1,len(q)):
    if q[a]=='X'==q[a+1]:
        c=c+1
    else:
        s.append(c)
        c=1
print(max(s))