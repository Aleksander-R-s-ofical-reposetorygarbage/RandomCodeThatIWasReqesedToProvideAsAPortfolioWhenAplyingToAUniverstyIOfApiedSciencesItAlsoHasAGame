dat=open("liczby.txt")
td=[]
for inn in dat:
    td.append(int(inn.rstrip()))
a=0
temp=0
temp1=0
temp2=0
for i in td:
    temp = int(str(i)[::-1])
    temp1 = i+temp
    temp2 =str(temp1)[::-1]
    if str(temp1) == temp2:
        a+=1
print(a)