i = int(input("thang bat ki: "))


if i <= 12:

    if i == 2:
        print("thang nay co 28 ngay")

    elif (( i % 2) == 1 and i < 8) or (( i % 2) == 0 and i >7)  :
        print("thang nay co 31 ngay")

    else:
        print("than nay co 30 ngay")

