op=open("napisy.txt")
lx=[]
for i in op:
    lx.append(i.split())
ml=[]
m=0
for x in lx:
    tm=0
    if len(x[0])<len(x[1]):
        aps=len(x[1])-len(x[0])
        for s in range(len(x[0])):
            if x[0][s]==x[1][s+aps]:
                tm+=1
            else:
                tm=0
    else:
        aps=len(x[0])-len(x[1])
        for s in range(len(x[1])):
            if x[1][s]==x[0][s+aps]:
                tm+=1
            else:
                tm=0
    if tm>m:
        m=tm
        ml=[x]
    elif tm == m:
        ml.append(x)
print("max kncowa",m)
for mop in ml:
    print(mop)