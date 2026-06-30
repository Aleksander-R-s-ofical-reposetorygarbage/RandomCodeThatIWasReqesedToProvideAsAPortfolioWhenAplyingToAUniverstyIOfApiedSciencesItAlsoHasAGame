op=open("probka.txt")
lx=[]
for i in op:
    lx.append(i.split())
print("kody szyfrujące:")
for x in lx:
    abr=0
    for A in range(26):
        for B in range(26):
            al=1
            for n in range(len(x[0])):
                l=((ord(x[0][n])-ord("a"))*A+B)%26-((ord(x[1][n]))-ord("a"))
                if not l==0:
                    al=0
                    break
            if al == 1:
                print(A,B)
                break
        if abr==1:
            break
print("kody deszyfrujące:")
for x in lx:
    abr=0
    for A in range(26):
        for B in range(26):
            al=1
            for n in range(len(x[0])):
                l=((ord(x[1][n])-ord("a"))*A+B)%26-((ord(x[0][n]))-ord("a"))
                if not l==0:
                    al=0
                    break
            if al == 1:
                print(A,B)
                break
        if abr==1:
            break