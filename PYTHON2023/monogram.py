import transzformaciok
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x550")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, background="#00ffff")
canvas.pack(fill=BOTH,expand=1)

#betuk=[
        #[10,10,20,10,15,5,10,10],#tető
        #[10,10,20,10,20,20,10,20,10,10],#fal
        #[13,20,13,15,17,15,17,20]#ajtó
#    ]

alakzat=[
    [0,0,0,100,100,100,100,0],
    [30,30,30,70,70,70,70,30],
    [150,0,150,100,250,100,250,0],
    [180,30,180,70,220,70,220,30]
]
szinek=["red","#00ffff", "blue","#00ffff", ]

#konfigurálás
meret=1
meret2=1
fok=0
dX=0
dY=0

for i in range(len(alakzat)):
    alakzat[i]=transzformaciok.nagyit(alakzat[i],meret,meret2)

xy=transzformaciok.kozepPont(alakzat)

for i in range(len(alakzat)):
    alakzat[i]=transzformaciok.forgat(alakzat[i],fok,xy[0],xy[1])

#teto=nagyit(teto,meret,meret2)
#fal=nagyit(fal,meret,meret2)

for i in range(len(alakzat)):
    alakzat[i]=transzformaciok.eltol(alakzat[i],dX,dY)        


for i in range(len(alakzat)):
    canvas.create_polygon(alakzat[i], fill=szinek[i],) 
    #canvas.create_line(betuk[i],fill="brown",width=3)



win.mainloop()