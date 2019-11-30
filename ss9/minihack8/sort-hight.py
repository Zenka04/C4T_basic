diemcao = [12,32,56,63,83]
them = int(input('them diem moi: '))
diemcao.append(them)
b = sorted(diemcao, reverse= True)
for i,a in enumerate(b):
    print(i+1 ,a,sep = ' ')
