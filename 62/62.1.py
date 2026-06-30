f1=open("liczby1.txt")
f1p=[]
for i in f1:
    f1p.append(int(i.rstrip(),8))
n=10000000
m=0
for xi in f1p:
    if  xi>m:
        m=xi
    if xi<n:
        n=xi
print(oct(n))
print(oct(m))