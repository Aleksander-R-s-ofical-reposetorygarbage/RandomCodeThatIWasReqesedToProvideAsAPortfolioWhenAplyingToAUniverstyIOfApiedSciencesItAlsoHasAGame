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
an=0
ans=[]
for z in a:
    tr=1
    r=0
    for v1 in range(10):
        for v2 in range(10):
            if z[v1][v2]!=z[v1+10][v2+10]:
                tr=0
                break
            if z[v1][v2]!=z[v1][v2+10]:
                tr=0
                break
            if z[v1][v2]!=z[v1+10][v2]:
                tr=0
                break
        if tr==0:
            break
    if tr==1:
        if an==0:
            ans=z
        an+=1
print("rek",an)
print("pierwszy:")
for x in ans:
    print(x)