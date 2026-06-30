op=open("hasla.txt")
lx=[]
for i in op:
    lx.append(i.rstrip())
a=0
for x in lx:
    j=0
    for v in range(len(x)-3):
        ln=[ord(x[v]),ord(x[v+1]),ord(x[v+2]),ord(x[v+3])]
        ln.sort()
        if ln[0]+3==ln[1]+2 and ln[1]+2==ln[2]+1 and ln[2]+1==ln[3]:
            j=1
    if j==1:
        a+=1
print(a)