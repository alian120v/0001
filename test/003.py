q=open('24_demo (5).txt').readline()
s=[]
c=0
for a in range(1,len(q)):
    if q[a]=='X' and c%3==0 or q[a]=='Y' and c%3==1 or q[a]=='Z' and c%3==2:
        c+=1
        s.append(c)
    elif q[a]=='X':
        c=1
    else:
        c=0
print(max(s))