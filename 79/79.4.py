op=open("okregi.txt")
lx=[]
b=1000
for i in op:
    lx.append(list(map(float,i.split())))
    b-=1
    if b==0:
        break
a=1
mx=0
for e in range(len(lx)-1):
    br=0
    d2=(lx[e][0]-lx[e+1][0])**2+(lx[e][1]-lx[e+1][1])**2
    d=d2**0.5
    if lx[e][2]-lx[e+1][2]>0:
        if d>=(lx[e][2]+lx[e+1][2]) or d<=(lx[e][2]-lx[e+1][2]):
            br=1
    else:
        if d >= (lx[e][2] + lx[e+1][2]) or d <= -(lx[e][2] - lx[e+1][2]):
            br=1
    if br==1:
        print("dlugosc lancucha:",a)
        if a>mx:
            mx=a
        a=1
    else:
        a+=1
print("dlugosc lancucha:",a)
print("najdluszy:",mx)