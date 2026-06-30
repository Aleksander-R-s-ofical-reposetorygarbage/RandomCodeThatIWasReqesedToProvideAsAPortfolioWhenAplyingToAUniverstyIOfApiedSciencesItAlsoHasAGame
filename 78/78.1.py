op=open("wiadomosci.txt")
lx=[]
for i in op:
    lx.append(i.rstrip())
x=lx[0]
while len(x)%8>0:
    x+="."
an=[]
stup="ALGORYTM"
for al in stup:
    an.append(ord(al))
z=0
for i in x:
    an[z]=(an[z]+ord(i))%128
    z+=1
    z=z%8
a=""
for ix in an:
    a+=chr(65+ix%26)
print("dlugosc:",len(x),"\ntablica:",an,"\nskrut:",a)