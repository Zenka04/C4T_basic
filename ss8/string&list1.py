a = input("nhap thu ban thic,ngan cach bang dau,: ")
c = a.split(",")
b = len(c)
for i in range(b):
    print(*c[i])