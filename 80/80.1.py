op=open("dane_trojkaty.txt")
lx=[]
for i in op:
    lx.append(int(i.rstrip()))
for x in range(len(lx)-2):
    if lx[x]+lx[x+1]>lx[x+2] and lx[x]+lx[x+2]>lx[x+1] and lx[x+1]+lx[x+2]>lx[x]:
        if lx[x]**2+lx[x+1]**2==lx[x+2]**2 or lx[x]**2+lx[x+2]**2==lx[x+1]**2 or lx[x+1]**2+lx[x+2]**2==lx[x]**2:
            print(lx[x],lx[x+1],lx[x+2])