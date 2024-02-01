autok=[]
f=open("fob2016.txt", "r")
for sor in f:
    #1 08:45 CEG306 501 23989 0
    
    tempSor=sor.strip().split(" ")
    #["1", "08:45", "CEG306", "501" , "23989" ,"0"]
    
   
    tempSor[3]=int(tempSor[3])
    tempSor[4]=int(tempSor[4])
    tempSor[5]=int(tempSor[5])
     #[1, "08:45", "CEG306", 501 , 23989 ,0 ]
    
    tempIdo=tempSor[1].split(":")
    #["08","15"]
    
    tempIdo[0]=int(tempIdo[0])
    tempIdo[1]=int(tempIdo[1])
    tempSor[1]=[tempSor[1],tempIdo[0],tempIdo[1], tempIdo[0]*60+tempIdo[1]]
    
    
    autok.append(tempSor)
f.close()
print(autok)