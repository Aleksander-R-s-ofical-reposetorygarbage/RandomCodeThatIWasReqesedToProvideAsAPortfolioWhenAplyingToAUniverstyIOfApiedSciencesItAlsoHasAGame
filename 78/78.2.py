op=open("podpisy.txt")
lx=[]
for i in op:
    lx.append(i.split())
d=3
n=200
for x in range(len(lx)):
    for y in range(len(lx[x])):
        lx[x][y]=(int(lx[x][y])*d)%n
for a0 in lx:
    nw=""
    for a1 in a0:
        nw+=chr(a1)
    print(nw)