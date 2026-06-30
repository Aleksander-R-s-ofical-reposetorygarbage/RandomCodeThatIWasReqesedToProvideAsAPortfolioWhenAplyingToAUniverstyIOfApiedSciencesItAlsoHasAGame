op=open("okregi.txt")
lx=[]
for i in op:
    lx.append(list(map(float,i.split())))
al=[0,0,0,0]
L=0
for x in lx:
    j=0
    n1=0
    n2=0
    print(x)
    while 1:
        if x[0]==0 or x[1]==0:
            j=1
            break
        if x[0]>0:
            if x[0]<x[2]:
                j = 1
                break
        else:
            if -x[0]<x[2]:
                j = 1
                break
            n1 = 1
        if x[1]>0:
            if x[1]<x[2]:
                j = 1
                break
        else:
            if -x[1]<x[2]:
                j = 1
                break
            n2 = 4
        break
    if j==0:
        if n1+n2==0:
            al[0]+=1
        elif n1+n2==1:
            al[1]+=1
        elif n1+n2==4:
            al[3]+=1
        else:
            al[2]+=1
    if j==1:
        L+=1
for e in range(4):
    print("cw",e+1)
    print(al[e])
print("reszta\n",L)