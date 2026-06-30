op=open("dane_ulamki.txt")
tb=[]
for i in op:
    tb.append(i.split())
ntb=[]
for i in tb:
    iv=float(i[0])/float(i[1])
    ntb.append(iv)
mz=9999999
g=[]
for ix in range(len(ntb)):
    if ntb[ix]<mz:
        mz=ntb[ix]
        g=[]
        g.append(ix)
    elif ntb[ix]==mz:
        g.append(ix)
vxx=9999999
fin=0
for a in g:
    if vxx>int(tb[a][0]):
        vxx=int(tb[a][0])
        fin=a
nx0=int(tb[fin][0])
nx1=int(tb[fin][1])
print(nx0,"",nx1)