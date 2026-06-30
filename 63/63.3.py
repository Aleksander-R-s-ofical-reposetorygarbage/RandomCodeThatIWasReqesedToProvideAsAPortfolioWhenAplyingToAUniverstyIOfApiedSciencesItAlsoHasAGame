op=open("ciagi.txt")
xv=[]
for ni in op:
    xv.append(int(ni.rstrip(),2))
a=0
aps=[]
for vt in xv:
    v=vt
    io=2
    xr=0
    while v+1>io:
        if v%io==0:
            v=v/io
            xr+=1
            if xr==3:
                break
        else:
            io+=1
    if xr==2:
        a+=1
        aps.append(vt)
print(a)
print("max:",max(aps))
print("min:",min(aps))