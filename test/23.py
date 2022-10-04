s=[]
k=m=m1=a1=0
q=list(map(int,(open('17.txt').readlines())[1:]))
while a1<=len(q)-30:
    for a in range(a1,len(q)):
        if k<30:
            if q[a]%2==1 and q[a]>0:k+=1
            m+=q[a]
        elif k==30:
            s.append(m)
            m1=max(m,m1)
            m=k=0
            break
    a1+=1
    print(m1)
print(max(s))