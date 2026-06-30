f1=open("dane_systemy1.txt")
f2=open("dane_systemy2.txt")
f3=open("dane_systemy3.txt")
f1p=[]
f2p=[]
f3p=[]
for i in f1:##copy
    f1p.append(i.rstrip().split())
for i in range(len(f1p)):
    mult=1
    a = f1p[i][0]
    temp1=0
    lna=len(a)
    for x in range(lna):
        temp1+=(int(a[lna-x-1])*mult)
        mult*=2
    f1p[i][0]=temp1
    mult=1
    b = str(f1p[i][1])
    neg=1
    if b[0]=="-":
        b=b[1:]
        neg=-1
    temp1=0
    lna=len(b)
    for x in range(lna):
        temp1+=(int(b[lna-x-1])*mult)
        mult*=2
    f1p[i][1] = temp1*neg
for i in f2:##copy
    f2p.append(i.rstrip().split())
for i in range(len(f2p)):
    mult=1
    a = f2p[i][0]
    temp1=0
    lna=len(a)
    for x in range(lna):
        temp1+=(int(a[lna-x-1])*mult)
        mult*=4
    f2p[i][0]=temp1
    mult=1
    b = str(f2p[i][1])
    neg=1
    if b[0]=="-":
        b=b[1:]
        neg=-1
    temp1=0
    lna=len(b)
    for x in range(lna):
        temp1+=(int(b[lna-x-1])*mult)
        mult*=4
    f2p[i][1] = temp1*neg
for i in f3:##copy
    f3p.append(i.rstrip().split())
for i in range(len(f3p)):
    mult=1
    a = str(f3p[i][0])
    temp1=0
    lna=len(a)
    for x in range(lna):
        temp1+=(int(a[lna-x-1])*mult)
        mult*=8
    f3p[i][0]=temp1
    mult=1
    b = str(f3p[i][1])
    neg=1
    if b[0]=="-":
        b=b[1:]
        neg=-1
    temp1=0
    lna=len(b)
    for x in range(lna):
        temp1+=(int(b[lna-x-1])*mult)
        mult*=8
    f3p[i][1] = temp1*neg

fu1=[]
fu2=[]
fu3=[]
for f in f1p:
    fu1.append(f[1])
for f in f2p:
    fu2.append(f[1])
for f in f3p:
    fu3.append(f[1])

ex=0
v1=0
v2=0
v3=0
for i in range(len(fu1)):
    z=0
    if (fu1[i]>v1):
        v1=fu1[i]
        z=1
    if (fu2[i]>v2):
        v2=fu2[i]
        z=1
    if (fu3[i]>v3):
        v3=fu3[i]
        z=1
    if (z==1):
        ex+=1
print(ex)