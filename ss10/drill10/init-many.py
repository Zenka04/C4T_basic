i = {
    "q1" : "mot ngay co bao nhieu gio :",
    "q2" : "mot tuan co bao nhieu ngay :",
    "a1" : [12,23,24,15],
    "a2" : [3,7,31,30],
    }
j = int(0)
while True:
    print(i["q1"])
    for n,m in enumerate(i["a1"]):
        print(n+1,m,sep=". ")
    k = int(input("cau tra loi:"))
    if k == 3 :
        print("dung")
        break
    else:
        print("sai")
        break
while True:
    print(i["q2"])
    for n,m in enumerate(i["a2"]):
        print(n+1,m,sep=". ")
    k = int(input("cau tra loi:"))
    if k == 2 :
        print("dung")
        break
    else:
        print("sai")
        break