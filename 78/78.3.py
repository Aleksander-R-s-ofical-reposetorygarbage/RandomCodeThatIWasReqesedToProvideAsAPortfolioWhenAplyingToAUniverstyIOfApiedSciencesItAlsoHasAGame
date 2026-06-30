op=open("podpisy.txt")
lx=[]
for i in op:
    lx.append(i.split())
d=3
n=200
for x in range(len(lx)):
    for f in range(len(lx[x])):
        lx[x][f]=(int(lx[x][f])*d)%n
lst=[]
for a0 in lx:
    nw=""
    for a1 in a0:
        nw+=chr(a1)
    lst.append(nw)
opx=open("wiadomosci.txt")
ly=[]
for i in opx:
    ly.append(i.rstrip())
for t0 in range(len(ly)):
    while len(ly[t0])%8>0:
        ly[t0]+="."
tru_an=[]
an_0x=[]
an=[]
stup = "ALGORYTM"
for al in stup:
    an_0x.append(ord(al))
for y in ly:
    an=[]
    for x0 in an_0x:
        an.append(x0)
    z=0
    for i in y:
        an[z]=(an[z]+ord(i))%128
        z+=1
        z=z%8
    a = ""
    for ix in an:
        a += chr(65 + ix % 26)
    tru_an.append(a)
msg=""
lov=[]
for printer in range(len(tru_an)):
    if lst[printer]==tru_an[printer]:
        msg="wiarygodna"
        lov.append(printer+1)
    else:
        msg="modyfikowana"
    print(printer+1,"\t",lst[printer],"\t",msg)
print("wirygodne:",lov)