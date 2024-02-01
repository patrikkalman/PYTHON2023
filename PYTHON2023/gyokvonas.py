import math

a=int(input("a:"))
b=int(input("b:"))

c=math.sqrt(a*a+b*b)
print(c)

for a in range(a, 100):
    for b in range(a,100):
        c=math.sqrt(a*a+b*b)
        if c%1==0:
            print(a,b,c)
