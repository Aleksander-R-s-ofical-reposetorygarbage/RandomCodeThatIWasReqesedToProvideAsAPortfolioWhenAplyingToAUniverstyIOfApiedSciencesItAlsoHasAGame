op=open("anomalie.txt")
l=[]
a=0
for ld in op:
    l.append(list(map(int,ld.split())))
for i in l:
    ar=0
    for x in range(4):
        if not i[x+1]>=i[x]:
            ar=1
            break
    if ar==0:
        a+=1
print(a)