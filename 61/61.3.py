l = open("bledne.txt")
l2 = []
o = 0
for i in l:
    o += 1
    if o % 2 == 0:
        l2.append(i.split())
qqq1 = 0
qqq2 = 0
for oi in l2:
    qqq1 = 0
    for oi2 in oi:
        l2[qqq2][qqq1] = int(oi2)
        qqq1 += 1
    qqq2 += 1
l3 = []
l4 = []
temp = 0
tempD = 0
for i2 in l2:
    qqq3=0
    for i3 in i2:
        tempD=i3-temp
        temp=i3
        if qqq3>0:
            l3.append(tempD)
        qqq3=1
    l4.append(l3)
    l3=[]
x1=0
x2=0
x3=0
l5=[]
axis=0
for j in l4:
    t=0
    for h in j:
        if t==3:
            if h==x3:
                if not h==x1:
                    l5.append(l2[axis][2])
            if not h==x3:
                if h==x2:
                    l5.append(l2[axis][0])
                else:
                    if h==x1:
                        l5.append(l2[axis][1])

        if t>3:
            if x3==h:
                if not x2 == x1:
                    l5.append(l2[axis][t-1])
        if t == (len(j)-1):
            if x3 == x2:
                if x3 == x1:
                    if not x3==h:
                        l5.append(l2[axis][t + 1])
                else:
                    if not  x1 == h:
                        l5.append(l2[axis][t])
        x3=x2
        x2=x1
        x1=h
        t+=1
    axis+=1
for c in l5:
    print(c)