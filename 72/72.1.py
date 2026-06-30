op=open("napisy.txt")
lx=[]
for i in op:
    lx.append(i.split())
a=0
for x in lx:
    if len(x[0])/len(x[1])>=3 or len(x[1])/len(x[0])>=3:
        if a==0:
            print(x)
        a+=1
print("ilosc:",a)