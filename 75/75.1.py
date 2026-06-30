op=open("tekst.txt")
lx0=[]
for i in op:
    lx0.append(i.split())
lx=lx0[0]
for x in lx:
    if x[0]==x[len(x)-1]:
        if x[0]=="d":
            print(x)