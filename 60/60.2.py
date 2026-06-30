dtbad=open("liczby.txt")
dat=[]
for v in dtbad:
    dat.append(int(v.rstrip()))
a=[]
temp=0
b=[]
for i in dat:
    temp=0
    for i2 in range(i):
        if i%(i2+1)==0:
            temp+=1
            b.append(i2+1)
    if temp == 18:
        a.append(i)
        a.append(b)
    b=[]
for c in a:
    print(c)