from turtle import *
import random

color = ["red", "green", "blue"]
print("danh sach mau: ")
print(*color,sep=", ")



while True:
    a = random.choice(color)
    print(a)
    fillcolor(a)
    begin_fill()
    forward(10)
    end_fill()

mainloop()