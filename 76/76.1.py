op=open("szyfr1.txt")
lx=[]
nn=0
for o in op:
    if nn == 6:
        lx.append(o.split())
    else:
        vo=o.rstrip()
        a=[]
        for voo in vo:
            a.append(voo)
        lx.append(a)
    nn+=1
for i in range(6):
    for c in range(50):
        t=lx[i][int(lx[6][c])-1]
        lx[i][int(lx[6][c]) - 1]=lx[i][c]
        lx[i][c]=t
for na in range(6):
    nu=""
    for l in lx[na]:
        nu+=l
    print(nu)