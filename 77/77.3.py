op=open("szyfr.txt")
lx=[]
for i in op:
    lx.append(i.rstrip())
x = lx[0]
key=lx[1]
dtl=[["A",0],["B",0]]
n=0
for iap in range(len(x)):
    if (ord(x[iap])-ord("A")) >= 0 and (ord(x[iap])-ord("A")) <= 26:
        z=0
        r=0
        for dt in dtl:
            if dtl[z][0]==x[iap]:
                dtl[z][1]+=1
                r=1
            z+=1
        n+=1
        if r==0:
            dtl.append([x[iap],1])
for janser in range(26):
    for dt1 in dtl:
        if dt1[0]==chr(ord("A")+janser):
            print(dt1[0],"-",dt1[1])
k0=0
for dt2 in dtl:
    k0 += dt2[1]*(dt2[1]-1)
k0t=k0/(n*(n-1))
d=0.0285/(k0t-0.0385)
print(d-(((d*1000)%10)/1000))
print(len(key))