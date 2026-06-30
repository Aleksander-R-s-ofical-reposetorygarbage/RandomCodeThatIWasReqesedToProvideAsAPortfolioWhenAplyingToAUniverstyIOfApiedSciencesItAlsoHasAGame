op=open("ciagi.txt")
w1=""
w2=""
xv=[]
for ni in op:
    i = ni.rstrip()
    li=len(i)
    if li%2==0:
        for c1 in range(int(li/2)):
            w1+=i[c1]
        for c2 in range(int(li/2),li):
            w2+=i[c2]
        print(i)
        print(w1)
        print(w2)
        print("")
        if w1==w2:
            xv.append(i)
    w1=""
    w2=""
print(xv)