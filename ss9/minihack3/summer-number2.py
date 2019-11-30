numbers = []
new_num = int(input("nhap so:"))
numbers.append(new_num)

new_num = int(input("nhap so:"))
numbers.append(new_num)

new_num = int(input("nhap so:"))
numbers.append(new_num)

new_num = int(input("nhap so:"))
numbers.append(new_num)

print(*numbers, sep=' ')

Sum = sum(numbers)
print(Sum)