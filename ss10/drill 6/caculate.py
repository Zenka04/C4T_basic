
i = {'name' : 'HUY',
    'role' : 'waiter',
    'hour' : 12,
    'salary per hours($)' : 0.8}                        
l = {'name' : 'TUNG',
    'role' : 'cook',
    'hour' : 24,
    'salary per hours($)' : 1.5}                                        
k = {'name' : 'MDUC',
    'role' : 'manager',
    'hour' : 20,
    'salary per hours($)' : 2}
a = {
    'luong thang HUY' : 0.8*12,
    'luong thang TUNG' : 1.5*12,
    'luong thang MDUC' : 2*12
}
a = {
    a['luong thang HUY'] + a['luong thang TUNG'] + a['luong thang MDUC']
}
print('so luon chi nhanh phai tra cho nv la: ',a)