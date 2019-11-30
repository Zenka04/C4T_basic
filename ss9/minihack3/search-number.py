numbers = ['7','13','19','61','73']
print(numbers)
x = input("So can tim: ")

if x in numbers:
    print('Tim thay',',','vi tri so:',numbers.index(x))
else:
    print("Khong tim thay ")