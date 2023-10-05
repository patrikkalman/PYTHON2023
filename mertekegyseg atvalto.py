hossz = ["mm", "cm", "dm", "m", "km"]
#a következőbe (jobbra lévőbe) mennyi a valtószám
hosszertek = [10, 10, 10, 1000, 1]
        
terulet = ["mm2", "cm2", "dm2", "m2","km2"]
#a következőbe (jobbra lévőbe) mennyi a valtószám
teruletertek = [100, 100, 100, 1000000,1]

#szam bekeres
#szam ellenorzes 
rossz=True
while rossz:
    try:
        szam=float(input("irj be egy szamot: "))
        rossz=False
    except:
        print("ez nem jo!!")
       
#mertekegyseg bekeres

rossz=True
while rossz:
    mertekEgyseg=input("kerem a mertekegyseget: ")
    #mertekegyseg ellenorzes, tipus kideritese
    if mertekEgyseg in hossz:
        rossz=False
    else:
        print("ismeretlen mertekegyseg:"+mertekEgyseg)


#mertekegyseg2 bekeres

rossz=True
while rossz:
    mertekEgyseg2=input("kerem a cel mertekegyseget: ")
    #mertekegyseg ellenorzes, az 1. tipusbol 
    if mertekEgyseg in hossz:
        rossz=False
    else:
        print("ismeretlen mertekegyseg:"+mertekEgyseg2)        

#kiszamitas

me1Index = hossz.index(mertekEgyseg)
me2Index = hossz.index(mertekEgyseg2)
#print(me1Index,me2Index)

#print(hosszertek[me1Index:me2Index])

szorzo=1
for ertek in hosszertek[me1Index:me2Index]:
    szorzo = szorzo * ertek

szam = szam/ertek

#kiiras
print(szam,mertekEgyseg2)    
    #ujra?
    
    
