op=open("tekst.txt")
lx=[]
for i in op:
    lx.append(i.split())
ml=0
mlc=0
fml=""
sam=["A","E","I","O","U","Y"]
for x in lx:
    for x2 in x:
        wm=0
        for v in x2:
            for s in sam:
                if s == v:
                    wm+=1
        if wm>ml:
            ml=wm
            fml=x2
            mlc=1
        elif wm==ml:
            mlc+=1
print("najwienksze pod slowo:",ml,"\nilossc takich slow:",mlc,"\nPierwsze takie slowo: ",fml)##<-- ??? jak zle