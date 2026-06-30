op=open("tekst.txt")
lx=[]
for i in op:
    lx.append(i.split())
a=0
for x in lx:
    for x2 in x:
        n=""
        g=0
        u=0
        for v in x2:
            if g>0:
                if n==v:
                    u=1
            g+=1
            n=v
        if u==1:
            a+=1
print(a)