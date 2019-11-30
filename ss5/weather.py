import random

r1 = random.randint(1,100)
print("random number betwen 1 and 100 is % s" %(r1))

if r1<30:
    print("rainy")
elif r1<60:
    print("cloudy")
else:
    print("sunny")