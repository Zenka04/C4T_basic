i = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,  
    "ACER" : 25,  
}
i["TOSHIBA"] = 10
i["FUJITSU"] = 15
i["ALIENWARE"] = 5

j = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 300,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}
for o in j:
    k = i[o] * j[o]
    print(k)
for o in j:
    print(o)