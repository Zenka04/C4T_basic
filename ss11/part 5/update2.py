i = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}
i['FUJITSU'] = 15
i['ALIENWARE'] = 5
i['DELL'] += 10
i['MACBOOK'] -=2
print(i)
a = input("hay may ")
a = a.upper()
b = int(input("so luong "))
print(i[a]-b)