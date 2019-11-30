numbers = []
new_num = int(input("nhap so:"))
numbers.append(new_num)

new_num = int(input("nhap so:"))
numbers.append(new_num)

new_num = int(input("nhap so:"))
numbers.append(new_num)

new_num = int(input("nhap so:"))
numbers.append(new_num)

print(*numbers, sep=',')

result = filter(lambda x: x%2 == 0, numbers) 
print(list(result)) 