color = ["red", "green", "blue"]
print("our color list:")
print(*color,sep=", ")

a = input("chon mau theo ten hoac theo thu tu: ")

if a.isalpha():
    color.remove(a)
    print(*color,sep=", ")

if a.isdigit():
    b = int(a)
    color.pop(b - 1)
    print(*color,sep=", ")