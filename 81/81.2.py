op=open("wspolrzedne.txt")
lx=[]
for i in op:
    lx.append(list(map(int,i.split())))
a=0
for x in lx:
    if not x[0]-x[2]==0 and not x[2]-x[4]==0 and not x[0]-x[4]==0:
        if (x[1]-x[3])/(x[0]-x[2])==(x[3]-x[5])/(x[2]-x[4]) and (x[1]-x[5])/(x[0]-x[4])==(x[3]-x[5])/(x[2]-x[4]):
            a+=1
    else:
        if x[0]-x[2]==x[2]-x[4] and x[2]-x[4]==0:
            a+=1
print(a)