l = ['SD','BD','BTL','CG','BD','HBT']
j = [150300, 247100, 333300, 266800, 420900, 318000]
k = [117.43,9.224,43.35,12.04,9.96,10.09]
o = [j[0]/k[0],j[1]/k[1],j[2]/k[2],j[3]/k[3],j[4]/k[4],j[5]/k[5]]
a = sum(o)
b = len(l)

print('Mat do dan cu TB:', a/b)