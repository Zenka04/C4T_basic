import re

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        else:
            print("Your password seems fine")
            break

validate()