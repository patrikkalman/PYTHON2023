start=5
stop=100
oszthat=10

for x in range(start,stop):
    if x%oszthat==0:
        print(x)



for x in range(start,stop, oszthat):
   print(x-start%oszthat)
