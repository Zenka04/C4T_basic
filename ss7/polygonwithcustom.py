from turtle import *
shape("turtle")
color("red")
speed(0)

i = int(input("so canh ma ban muon: "))

for j in range(i):
    fd(100)
    rt(360/i)

mainloop()
