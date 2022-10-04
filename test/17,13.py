q=open('17.txt').readline()
q.replace('\n','',99999)
for a in (range(0,len(q)+1)):
    if int(int(q[a-1]))%160!=int(q[a])%160 and (int(q[a-1])%7==0 or int(q[a])%7==0):
        c=c+1
        m=max(m,(int(q[a-1])+int(q[a])))
print(c,m)