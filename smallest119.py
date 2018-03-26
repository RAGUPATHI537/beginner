m=input()
n=input()
p=[]
for i in range(0,m):
    r=input()
    p.append(r)
    p.sort()
print(p[n-1])
