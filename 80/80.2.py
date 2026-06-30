op=open("dane_trojkaty.txt")
lx=[]
for i in op:
    lx.append(int(i.rstrip()))
mx=0
for a in range(len(lx)):
    for b in range(len(lx)):
        for c in range(len(lx)):
            if lx[a] + lx[b] > lx[c] and lx[a] + lx[c] > lx[b] and lx[b] + lx[c] > lx[a]:
                if not a-b==0 and not a-c==0 and not c-b==0:
                    if lx[a]+lx[b]+lx[c]>mx:
                        mx=lx[a]+lx[b]+lx[c]
print(mx)