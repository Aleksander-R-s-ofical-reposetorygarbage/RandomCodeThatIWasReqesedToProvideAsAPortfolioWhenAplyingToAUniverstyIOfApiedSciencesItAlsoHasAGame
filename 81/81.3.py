op=open("wspolrzedneTR.txt")
lx=[]
for i in op:
    lx.append(list(map(int,i.split())))
a=[]
ob=0
for x in lx:
    o=0
    if not x[0]-x[2]==0 and not x[2]-x[4]==0 and not x[0]-x[4]==0:
        if not (x[1]-x[3])/(x[0]-x[2])==(x[3]-x[5])/(x[2]-x[4]) and not (x[1]-x[5])/(x[0]-x[4])==(x[3]-x[5])/(x[2]-x[4]):
            o=(((x[0]-x[2])**2+(x[1]-x[3])**2)**0.5+((x[0]-x[4])**2+(x[1]-x[5])**2)**0.5+((x[4]-x[2])**2+(x[5]-x[3])**2)**0.5)
    else:
        if not x[0]-x[2]==0 and not x[2]-x[4]==0:
            o=(((x[0]-x[2])**2+(x[1]-x[3])**2)**0.5+((x[0]-x[4])**2+(x[1]-x[5])**2)**0.5+((x[4]-x[2])**2+(x[5]-x[3])**2)**0.5)
    if o>ob:
        ob=o
        a=x
print(a)
print(ob-ob%0.01)