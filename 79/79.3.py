op=open("okregi.txt")
lx=[]
for i in op:
    lx.append(list(map(float,i.split())))
a=0
for x in lx:
    for z in lx:
        if x[0]==z[1] and x[1]==-z[0] and x[2]==z[2]:
            a+=1
        if x[0]==-z[1] and x[1]==z[0] and x[2]==z[2]:
            a+=1
print("pary prostopadle:")
print(a/2)