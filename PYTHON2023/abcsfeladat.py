import random

maganhangzo = 'aeiou'
massalhangzo = 'bcdfghjklmnpqrstvwxyz'
random.choice(massalhangzo)
betu=''
for i in range(5):
    if i % 2 ==0:
        betu += random.choice(massalhangzo)
    else:
        betu += random.choice(maganhangzo)
print(betu)
