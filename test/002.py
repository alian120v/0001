q=open('24_demo (4).txt').readline()
s=[]
c=1
for a in range(1,len(q)): 
    if q[a]=='Y'==q[a+1]:
        c+=1
    else:
        s.append(c)
        c=1
print(max(s))