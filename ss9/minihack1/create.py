color = ["red", "green", "blue"]
print("Our color list:")
print(*color,sep=", ")

a = input("Enter a new colo: ")
color.append(a)
print("Our new color list: ")
print(*color,sep=", ")