l = open("ciagi.txt")
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
temp = 0
for i2 in l2:
    v = 0
    temp = 0
    for i3 in i2:
        for i4 in range(i3):
            if (i4 + 1) * (i4 + 1) * (i4 + 1) == i3:
                v = 1
                if i3 > temp:
                    temp = i3
            if (i4 + 1) * (i4 + 1) * (i4 + 1) > i3:
                break
    if v==1:
        l3.append(temp)

for p in l3:
    print(p)