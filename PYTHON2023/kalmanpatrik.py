lista=[]
f=open("fob2016.txt","r")
for sor in f:
    lista.append(sor.strip().split(" "))

f.close()
print(lista)

csapat=lista[::3]
eletkor=lista[1::3]
nev=lista[2::3]

