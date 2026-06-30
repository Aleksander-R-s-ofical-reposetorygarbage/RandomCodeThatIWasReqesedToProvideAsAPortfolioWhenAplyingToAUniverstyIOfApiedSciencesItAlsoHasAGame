op=open("szyfr2.txt")
lx=[]
nn=0
for o in op:
    if nn == 1:
        lx.append(o.split())
    else:
        vo=o.rstrip()
        a=[]
        for voo in vo:
            a.append(voo)
        lx.append(a)
    nn+=1
for c in range(50):
    t=lx[0][int(lx[1][c%15])-1]
    lx[0][int(lx[1][c%15]) - 1]=lx[0][c]
    lx[0][c]=t
nu=""
for l in lx[0]:
    nu+=l
print(nu)