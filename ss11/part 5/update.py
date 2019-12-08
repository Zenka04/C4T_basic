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
a = sum(i.values())
b = int(input("so luong may da mua la :"))
print("tong so may :", a)
print("so luong may con lai la :", a-b)
