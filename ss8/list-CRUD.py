a = []
i = input("chon thao tac nao trong 4 thao tac duoi day C,R,U,D?  ")

while True:
    if i == "C" or i == "c":
        b = input("new item(s): ")
        a.append(b)
        print(*a,sep=", ")

    if i == 'R' or i == 'r':
        if len(i) >=1:
            print(*a,sep="\n")
        else:
            print("no item")

    if i == "U" or i == "u":
        c = int(input("chon thu ban muon thay the: ")) - 1
        d = input("doi thanh ")
        a[c] = d
        print(*a,sep=", ")

    if i == "D" or i == "d":
        e = int(input("chon thu ban muon xoa")) - 1
        a.pop(e)
        print(*a,sep=", ")
