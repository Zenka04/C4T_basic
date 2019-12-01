i = {
    "name" : "son tung",
    "age" : "25",
    "job" : "ca si",
}
while True:
    c = input('ban muon xem gi: ')
    if c  in i:
        print(c,":",i[c])
    else:
        print(c ,'khong co') 