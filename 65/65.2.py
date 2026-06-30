op=open("dane_ulamki.txt")
tb=[]
for i in op:
    tb.append(i.split())
ntb=[]
x=0

def xnvd(x,y):
    if x>y:
        return xnvd(y,x)
    if x==0:
        return y
    return xnvd(x,y%x)


for i in tb:
    if xnvd(float(i[1]), float(i[0]))==1:
        x+=1
print(x)