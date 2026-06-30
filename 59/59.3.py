dat=open("liczby.txt")
td=[]
for inn in dat:
    td.append(int(inn.rstrip()))
temp=0
g=[]
an2=[]
for i in td:
    z=i
    temp = 0
    while z>9:
        c = 1
        for v in str(z):
            c=c*int(v)
        temp+=1
        z = c
    if temp==1:
        an2.append(i)
    g.append(temp)
print("min moc 1:",min(an2))
print("max moc 1:",max(an2))
for h in range(max(g)):
    temp=0
    for ii in g:
        if ii == h+1:
            temp+=1
    print("moc: ",h+1," ilosc: ",temp)