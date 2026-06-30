op=open("wspolrzedneTR.txt")
lx=[]
for i in op:
    lx.append(list(map(int,i.split())))
for x in lx:
    D1x=x[0]+x[4]-x[2]
    D1y=x[1]+x[5]-x[3]
    D2x=x[4]+x[0]-x[2]
    D2y=x[5]+x[1]-x[3]
    if D1x==D2x and D1y==D2y and D1y==D1x: ## odp poprawna tlko dla robow fajna tesc
        n=""
        for xp in x:
            n+=(str(xp)+"  ")
        n+=str(D1x)+"  "+str(D1y)
        print(n)