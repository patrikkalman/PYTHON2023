f=open("sanyi.txt","w")

for i in range(100):
    f.write(str(i)+"\n")
f.close()



f=open("sanyi.txt","r")

szoveg=f.read()
szoveg=szoveg.strip()
lista=szoveg.split("\n")

f.close()
print(lista)

osszeg=0
for egySzam in lista:
    osszeg+=int(egySzam)

print(osszeg)

lista2=[]
f=open("sanyi.txt","r")
for egySzam in f:
    lista.append(int(egySzam))

f.close()
print(lista2, sum(lista2))

