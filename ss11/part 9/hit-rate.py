import random
skill = {
"a" : {
    "name" : "tackle",
    "min lv" : 1,
    "damage" : 5,
    "hit rate" : 0.3,
},
"b" : {
    "name" : "quick atk",
    "min lv" : 2,
    "damage" : 3,
    "hit rate" : 0.5,
},
"c" : {
    "name" : "strong kick",
    "min lv" : 4,
    "damage" : 9,
    "hit rate" : 0.2,
}
}

for i,a in enumerate(skill):
    print(i+1,skill[a])
j = random.randint(0,1)   
l = int(input("ban chon skill nao: "))
if l == 1:
    if j > skill['a']['hit rate']:
        print('trung,sat thuong gay ra la:',skill['a']['damage']) 
    else:
        print('truot')     

if l == 2:
    if j > skill['b']['hit rate']:
        print('trung,sat thuong gay ra la:',skill['b']['damage']) 
    else:
        print('truot')   

if l == 3:
    if j > skill['a']['hit rate']:
        print('trung,sat thuong gay ra la:',skill['c']['damage']) 
    else:
        print('truot')   
