adatok=[]
f=open("tancrend.txt", )
for sor in f:
    adatok.append(sor.strip())
f.close()
print(adatok)
#egyik megoldas
tancok=adatok[::3]
fiuk=adatok[2::3]
lanyok=adatok[1::3]
#print(tancok)

#masik megoldas
#adatok3=[]
#for i in range(0,len(adatok/3,3))
