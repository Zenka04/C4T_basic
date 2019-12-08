i={
    'HP' : 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}
print(i)
j = input("hang may tinh muon kiem tra: ").lower()
if j=="hp":
    print("so luong",j,"la:",i['HP'])
if j=="dell":
    print("so luong",j,"la:",i['DELL'])
if j=="macbook":
    print("so luong",j,"la:",i['MACBOOK'])
if j=="asus":
    print("so luong",j,"la:",i['ASUS'])