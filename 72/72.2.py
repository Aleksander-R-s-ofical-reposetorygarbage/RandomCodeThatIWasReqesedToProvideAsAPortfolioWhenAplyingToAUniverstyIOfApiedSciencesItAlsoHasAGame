op=open("napisy.txt")
lx=[]
for i in op:
    lx.append(i.split())
for x in lx:
    if len(x[0])<len(x[1]):
        n=0
        b=0
        nap=""
        for vx in range(len(x[0])):
            if not x[0][vx]==x[1][vx]:
                n=1
                break
            b+=1
        if n==0:
            for o in range(len(x[1])):
                if b-1<o:
                    nap+=x[1][o]
            print(x[0],"  ",x[0],"",nap)