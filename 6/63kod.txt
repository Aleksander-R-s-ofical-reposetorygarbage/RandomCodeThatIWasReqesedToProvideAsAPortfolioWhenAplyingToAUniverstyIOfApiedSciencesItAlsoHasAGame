op=open("anomalie.txt")
l=[]
for ld in op:
    l.append(list(map(int,ld.split())))
lflip=l[::-1]
min1opt=999999999
min2opt=999999999
min3opt=999999999
min4opt=999999999
n1=0
n2=0
n3=0
n4=0
for nl in range(4):
    for n in range(1000):
        f=0
        mi=0
        sk=0
        for i in range(1000):
            if nl==1:
                sk=n1
            elif nl==2:
                sk=n2
            elif nl==2:
                sk=n3
            if i>sk:
                if i==n:
                    f=1
                    mi += lflip[i][nl]
                mi+=lflip[i][f+nl]
        if min1opt > mi and nl==0:
            min1opt=mi
            n1 = n
        if min2opt > mi and nl==1 and n > n1:
            min2opt=mi
            n2 = n
        if min3opt > mi and nl==2 and n > n2:
            min3opt=mi
            n3 = n
        if min4opt > mi and nl==3 and n > n3:
            min4opt=mi
            n4 = n
ni=0
v=0
ml=[]
for ie in range(1000):
    if ie == n1 or ie == n2 or ie == n3 or ie == n4:
        ml.append([1000-ie,v])
        ni += lflip[ie][v]
        v+=1
    ni += lflip[ie][v]
    if not ie==0:
        ml.append([1000 - ie, v])
for z in ml:
    print(z)
print(ni-21)
