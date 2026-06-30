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
a = 0
m = 0
temp1 = 0
temp2 = 0
for i2 in l2:
    v = 0
    q1 = 0
    for i3 in i2:
        if q1 > 1:
            if not i3 - temp1 == temp2:
                v=1
                break
        q1 += 1
        temp2 = i3 - temp1
        temp1 = i3
    if v==0:
        a+=1
        if temp2>m:
            m=temp2

print("njwieszy odstemp: ",m)
print("ilosc ciagow arytmetycznych: ",a)