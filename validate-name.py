while True:
    txt = input("enter your name? ")
    print(txt)
    if txt.isdigit():
        print("is not your name")
    else:
        print("is your name")
        break