while True:
    txt =  input("emter your name: ")
    print(txt)
    if txt.isalpha():
        print("is your name")
        break
    else:
        print("is not your name")