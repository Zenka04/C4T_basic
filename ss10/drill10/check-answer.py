i = {
    "q" : "mot ngay co bao nhieu gio :",
    "a" : [12,23,24,15],
    }
j = int(0)
while True:
    print(i["q"])
    for n,m in enumerate(i["a"]):
        print(n+1,m,sep=". ")
    k = int(input("cau tra loi:"))
    if k == 3 :
        print("dung")
        break
    else:
        print("sai")
        break