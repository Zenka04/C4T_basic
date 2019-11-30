import random

while True:
    s1 = random.randint(0,100)
    print("Random number between 0 and 100 is % s" % (s1)) 

    s2 = random.randint(0,100)
    print("Random number between 0 and 100 is % s" % (s2)) 

    result_num = random.randint(0,1)
    final_result=0
    opt_num = random.randint(0,3)
    opt = ''
    if opt_num==0:
        opt = "+"
        if result_num==0:
            final_result=s1+s2
    elif opt_num==1:
        opt = "-"
        if result_num==0:
            final_result=s1-s2
    elif opt_num==2:
        opt = "*"
        if result_num==0:
            final_result=s1*s2
    else :
        opt = "/"
        if result_num==0:
            final_result=s1/s2

    if result_num==1:
        final_result-=1

    print("phep tinh", s1,opt,s2,"=",final_result )

    ans = int(input("Nhap ket qua: 0. Dung 1. Sai"))

    if ans==result_num:
        print("cau tra loi dung")

    else:
        print("cau tra loi sai")
        break


