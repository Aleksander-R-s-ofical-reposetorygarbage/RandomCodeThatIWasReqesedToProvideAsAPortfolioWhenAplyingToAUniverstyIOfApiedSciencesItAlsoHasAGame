op=open("wspolrzedne.txt")
lx=[]
for i in op:
    lx.append(list(map(int,i.split())))
a=0
for x in lx:
    n=1
    for xp in x:
        if not xp>0:
            n=0
            break
    if n==1:
        a+=1
print(a)