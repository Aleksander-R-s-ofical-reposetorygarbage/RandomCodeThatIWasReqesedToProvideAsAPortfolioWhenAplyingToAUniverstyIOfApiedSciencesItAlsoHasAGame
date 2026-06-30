op=open("tekst.txt")
lx0=[]
for i in op:
    lx0.append(i.split())
lx=lx0[0]
A=5
B=2
for x in lx:
    if len(x)>9:
        L=""
        for c in x:
            L+=(chr(((ord(c)-ord("a"))*A+B)%26+ord("a")))
        print(L)