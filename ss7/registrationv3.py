i = input("your user name: ")

while True:
    j = input("your email: ")

    regex = compile('[@]') 
    
    if(regex.search(j) == None): 
        print("email cua ban sai")
            
    else: 
        break

while True:
    k = input("mat khau cua ban ")
    if len(k) >= 8 and k.isalnum():
        break
    else:
        print("mật khẩu của bạn phải có ít nhất 8 ký tự và một chữ cái / số")


while True:
    l = input("dien lai mat khau ")
    if k == l:
        print("mat khau cua ban dung")
        break
    else:
        print("mat kha cua ban sai")