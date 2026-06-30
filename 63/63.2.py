op=open("ciagi.txt")
xv=0
t=0
for ni in op:
    i = ni.rstrip()
    li=len(i)
    for x in range(1,li):
        if i[x]==i[x-1] and i[x]=='1':
            t=1
            break
    if t==0:
        xv+=1
    t=0
print(xv)