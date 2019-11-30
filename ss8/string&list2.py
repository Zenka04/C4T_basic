import random
a = input("viet 1 thu: ")
b = list(a)
random.shuffle(b)
print(*b,sep='\n')