l = ['SD','BD','BTL','CG','BD','HBT']
j = [150300, 247100, 333300, 266800, 420900, 318000]
x = j[0]
for i in j:
    if x < i:
        x = i
    else:
        pass
print('Quan co dan so cao nhat:', x)
y = j[0]
for k in j:
    if y > k:
        y = k
    else:
        pass
print('Quan co dan so thap nhat:', y)   