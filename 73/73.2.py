op=open("tekst.txt")
lx=[]
for i in op:
    lx.append(i.split())
al=[["A",0],["B",0]]
ap=0
for x in lx:
    for x2 in x:
        for v in x2:
            ap+=1
            num=0
            tol=0
            for a in al:
                if a[0]==v:
                    al[num][1]+=1
                    tol=1
                num+=1
            if tol==0:
                al.append([v,1])
dc=1
while dc>0:
    dc=0
    for asor in range(len(al)-1):
        if ord(al[asor][0])>ord(al[asor+1][0]):
            dc+=1
            altm=al[asor][0]
            al[asor][0] = al[asor+1][0]
            al[asor + 1][0] = altm
for ia in al:
    print(ia[0],ia[1]," ",int((ia[1]/ap)*10000)/100,"%")