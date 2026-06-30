f1=open("liczby2.txt")
f1p=[]
for i in f1:
    f1p.append(i.rstrip())
a10=0
a8=0
for ii in f1p:
    v = str(oct(int(ii)))
    for x in ii:
        if x == '6':
            a10 += 1
    for x2 in v:
        if x2 == '6':
            a8 += 1
print("6 w dec:",a10)
print("6 w oct:",a8)