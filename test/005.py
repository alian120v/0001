q=open('zadanie24_1.txt').readline()
s=[]
c=0
for a in range(1,len(q)):
    if q[a]=='A' and c%2==0 or q[a]=='B' and c%2==1:
        c+=1
        s.append(c)
    elif q[a]=='A':
        c=1
    else:
        c=0
print(max(s))