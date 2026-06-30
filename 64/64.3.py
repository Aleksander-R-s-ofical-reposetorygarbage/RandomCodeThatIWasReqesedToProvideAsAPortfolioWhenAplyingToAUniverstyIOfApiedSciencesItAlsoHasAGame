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
c=0
f=0
b=0
mx=0
for z in a:
    colx=0
    coly=0
    for v1 in range(20):
        cx=0
        cy = 0
        for v2 in range(20):
            cx+=int(z[v1][v2])
            cy += int(z[v2][v1])
        if cx%2!=int(z[v1][20]):
            colx+=1
        if cy%2!=int(z[20][v1]):
            coly+=1
    if coly==0 and colx==0:
        c+=1
    elif coly<2 and colx<2:
        f+=1
    else:
        b+=1
        if mx<coly+colx:
            mx=(coly+colx)
print("poprawne:",c,"\nnaprawialne:",f,"\nnienaprawialne:",b,"\nnjwienksza ilosc blendow:",mx)