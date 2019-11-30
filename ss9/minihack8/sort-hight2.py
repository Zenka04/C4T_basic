j = [12,32,56,63,83]
l = int(input('them diem moi: '))
j.append(l)
b = sorted(j, reverse = True)
a = len(j)
for i in range(5):
    print(b[i])