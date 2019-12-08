a = {
    "name" : "tackle",
    "min lv" : 1,
    "damage" : 5,
    "hit rate" : 0.3,
}
b = {
    "name" : "quick atk",
    "min lv" : 2,
    "damage" : 3,
    "hit rate" : 0.5,
}
c = {
    "name" : "strong kick",
    "min lv" : 4,
    "damage" : 9,
    "hit rate" : 0.2,
}
skills = [a["name"], b["name"], c["name"]]
atk = [a["damage"], b["damage"], c["damage"]]
while True:
    print("lever: 3", '\n', "skillS :")
    for m,n in enumerate(skills):
        print(m + 1, n, sep='. ')
    a = input("chon skill:")
    if a == '1':
        print("damage :", atk[0])
    elif a == '2':
        print("damage :", atk[1] )
    elif a == '3':
        print("khong du lever")
    else:
        print("khong co skill")
        break