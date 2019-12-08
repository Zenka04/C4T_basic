i={
    'HP' : 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}
i["TOSHIBA"] = 10
for m,n in i.items():
    print(m,n,sep=':')
a = sum(i.values())
print(a)

print('\n')
i["FUJITSU"] = 15
i["ALIENWARE"] = 5
for m,n in i.items():
    print(m,n,sep=':')
print(a)