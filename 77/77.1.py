op=open("dokad.txt")
lx=[]
for i in op:
    lx.append(i.rstrip())
x = lx[0]
key="LUBIMYCZYTAC"
ans=""
key_run=0
key_dt=0
for iap in range(len(x)):
    if (ord(x[iap])-ord("A")) >= 0 and (ord(x[iap])-ord("A")) <= 26:
        ans+=chr((ord(x[iap])+ord(key[key_dt])-(ord("A")*2))%26+ord("A"))
        key_dt+=1
        if key_dt == 1:
            key_run+=1
        if key_dt >= len(key):
            key_dt=0
    else:
        ans+=x[iap]
print(ans)
print("powturzenie klucza:",key_run)