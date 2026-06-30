dtbad=open("liczby.txt")
dat=[]
for v in dtbad:
    dat.append(int(v.rstrip()))
x1=1
x2=1
a=0
for i in dat:
    if i<1000:
        x1=x2
        x2=i
        a+=1
print("liczba liczb mnieszch od 1000: ",a,"\n dwie ostanie iczby: ",x1,x2)