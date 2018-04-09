a=input()
b=input()
c=[]
k=[]
for i in range(0,a):
        d=input()
        c.append(d)
for i in range(0,len(c)):
        if(i%2!=0):
            k.append(c[i-1])
print(k[b-1])
