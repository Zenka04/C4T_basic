import random
a = ['game']
b = list(a)
c = random.choice(b)

print("doan tu") 

if c == "game":
    d = list(c)
    random.shuffle(d)
    print(*d,sep='\n')
    
    e = input("cau tra loi cua ban ") 
    if e == "game":
        print("dung roi")
    else:
        print("sai roi")


