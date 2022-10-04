q=open('inf_22_10_20_24.txt')
s=[]
c=0
for a in q:
    if  a.count('E')>a.count('A'):
        c+=1
print(c)