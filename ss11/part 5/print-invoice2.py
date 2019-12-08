i = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 300,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}
j = input("hang may ma ban muon mua: ")
j = j.upper()
l = int(input("so luong may ban muon mua: "))
a = i[j] * l
print("tong so tien:", a)