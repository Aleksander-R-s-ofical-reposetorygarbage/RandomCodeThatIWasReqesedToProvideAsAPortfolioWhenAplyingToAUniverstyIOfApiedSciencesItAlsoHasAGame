op=open("hasla.txt")
lx=[]
for i in op:
    lx.append(i.rstrip())
a=0
l1=[]
l2=[]
l3=[]
for il in range(10):
    l1.append(str(il))
for vo in range(26):
    l2.append(chr(ord("a") + vo))
    l3.append(chr(ord("A") + vo))
for x in lx:
    v1=0
    v2=0
    v3=0
    for v in x:
        if v1==0:
            for l1a in l1:
                if l1a==v:
                    v1=1
                    break
        if v2==0:
            for l2a in l2:
                if l2a==v:
                    v2=1
                    break
        if v3==0:
            for l3a in l3:
                if l3a==v:
                    v3=1
                    break
    if v1+v2+v3==3:
        a+=1
print(a)