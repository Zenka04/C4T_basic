l = {
    "q1" : "mot ngay co bao nhieu gio :",
    "q2" : "mot tuan co bao nhieu ngay :",
    "a1" : [12,23,24,15],
    "a2" : [3,7,31,30],
    }
i = int(0)
d = int(0)
p = float
while True:
    print(l["q1"])
    for n,m in enumerate(l["a1"]):
        print(n+1,m,sep=". ")
    ans = int(input("cau tra loi:"))
    if ans == 3 :
        print("dung")
        d = d + 1
        i = i + 1
        print("diem:", i)
        break
    else:
        print("sai ")
        d = d + 1
        print("diem:", i)
        break
while True:
    print(l["q2"])
    for n,m in enumerate(l["a2"]):
        print(n+1,m,sep=". ")
    ans = int(input("cau tra loi:"))
    if ans == 2 :
        print("dung")
        break
    else:
        print("sai")
        break