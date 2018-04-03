a=input()
b=list(str(a))
for c in range(0,len(b)):
    if(((int(b[c]))%2)!=0):
        print(b[c])
