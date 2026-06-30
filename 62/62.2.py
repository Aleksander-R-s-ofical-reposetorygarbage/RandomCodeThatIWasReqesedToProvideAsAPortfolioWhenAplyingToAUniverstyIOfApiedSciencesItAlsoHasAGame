f1=open("liczby2.txt")
f1p=[]
for i in f1:
    f1p.append(int(i.rstrip()))
cb=0
fst=0
t1=0
tims=1
star=0
for ii in f1p:
    if ii>t1:
        if tims==1:
            star=t1
        tims+=1
        if cb<tims:
            cb=tims
            fst=star
    else:
        tims=1
    t1=ii
print("pierwszy:",fst,"\ndlugosc:",cb)