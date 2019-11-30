import re

def validate():
    while True:
        password = input("Enter a password: ")
        if re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        else:
            print("Your password seems fine")
            break

validate()