f1=open("liczby1.txt")
f1p=[]
for i1 in f1:
    f1p.append(int(i1.rstrip(),8))
f2=open("liczby2.txt")
f2p=[]
for i2 in f2:
    f2p.append(int(i2.rstrip()))
a=0
b=0
for i in range(1000):
    if f2p[i]==f1p[i]:
        a+=1
    if f2p[i]<f1p[i]:
        b+=1

print(a)
print(b)