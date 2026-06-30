op=open("anomalie.txt")
l=[]
av=0
tot=0
ldif=[]
binar=[]
for ld in op:
    l.append(list(map(int,ld.split())))
for i in l:
    temp1 = []
    for x in range(4):
        nav=((i[x+1]-i[x])**2)**0.5
        tot+=1
        av+=nav
        temp1.append(nav)
    ldif.append(temp1)
av=av/tot
print(av)
for difc in ldif:
    temp2=0
    for c in difc:
        if c>av:
            temp2+=1
    if temp2==4:
        binar.append("1")
    else:
        binar.append("0")
bint=""
for xp in range(30):
    bint+=binar[len(binar)-30+xp]
lic=int(bint,2)
print(lic)
print("1"+bin(lic)[::2])