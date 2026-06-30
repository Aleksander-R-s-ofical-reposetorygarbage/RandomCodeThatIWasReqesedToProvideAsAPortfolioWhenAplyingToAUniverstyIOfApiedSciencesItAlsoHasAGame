op=open("hasla.txt")
lx=[]
for i in op:
    lx.append(i.rstrip())
ld=[]
for x1 in lx:
    a=0
    for x2 in lx:
        if x1==x2:
            a+=1
    if a>1:
        ld.append(x1)
ld=set(ld)
for d in ld:
    print(d)