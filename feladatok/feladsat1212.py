adatok=[]
f=open("foglaltsag.txt", "r")
for sor in f:
    adatok.append(sor.strip())
f.close()
print(adatok)



kategoria=[]
f=open("kategoria.txt", "r")
for sor in f:
    kategoria.append(sor.strip())
f.close()
print(kategoria)