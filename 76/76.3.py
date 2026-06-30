op=open("szyfr3.txt")
lx=[]
for o in op:
    vo=o.rstrip()
    a=[]
    for voo in vo:
        a.append(voo)
    lx.append(a)
ax=[6,2,4,1,5,3]
lx=lx[0]
for c in range(50):
    t=lx[int(ax[(49-c)%6])-1]
    lx[int(ax[(49-c)%6])-1] = lx[49-c]
    lx[49-c] = t
nu=""
for l in lx:
    nu+=l
print(nu)