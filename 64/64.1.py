op=open("dane_obrazki.txt")
a=[]
a1=[]
for i in op:
    if len(i)>19:
        a1.append(i.rstrip())
    else:
        a.append(a1)
        a1=[]
a.append(a1)
x=0
mx=0
for iv in a:
    bl=0
    for z in iv:
        if len(z)==20:
            break
        t=0
        for xz in z:
            if xz=="1":
                bl+=1
            t+=1
            if t==20:
                break
    if bl>200:
        x+=1
        if bl>mx:
            mx=bl
print("rewersy: ",x)
print("max czarnych: ",mx)