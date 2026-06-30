op=open("hasla.txt")
lx=[]
for i in op:
    lx.append(i.rstrip())
ll=[]
for il in range(10):
    ll.append(str(il))
a=0
for x in lx:
    tru=1
    for vx in x:
        br = 1
        for l in ll:
            if l==vx:
                br=0
        if br==1:
            tru=0
            break
    if tru==1:
        a+=1
print(a)