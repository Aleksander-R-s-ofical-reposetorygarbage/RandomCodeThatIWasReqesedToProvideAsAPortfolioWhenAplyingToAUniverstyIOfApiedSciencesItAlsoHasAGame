dat=open("liczby.txt")
td=[]
for inn in dat:
    td.append(int(inn.rstrip()))
a=0
v=[3]
##for ii in range(int(max(td)/4)):
##    c=1
##    for zx in v:
##        if (ii*2+3)%zx==0:
##            c=0
##            break
##    if c==1:
##        v.append(ii*2+3)
##print(v)
temp=0
for i in td:
    tim=0
    vx=3
    j=i
    while j/vx>1:
        if j%2==0:
            break
        if j%vx==0:
            while 0==0:
                temp=j
                j=j/vx
                if not j%vx==0:
                    j=temp
                    break
            tim+=1
        if tim==4:
            break
        vx+=2
    if tim==3:
        a+=1
print(a)