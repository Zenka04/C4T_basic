skill1={    
    'Skill': 1,
    'Name': 'Tackle',
    'Minimum level': 1,
    'Damage': 5,
    'Hit rate': 0.3,
}
skill2={
    'Skill': 2,
    'Name': 'Quick attack',
    'Minimum level': 2,
    'Damage': 3,
    'Hit rate': 0.5,
}
skill3={
    'Skill': 3,
    'Name': 'Strong Kick',
    'Minimum level': 4,
    'Damage': 9,
    'Hit rate': 0.2,
}
a=[skill1, skill2, skill3]
for i in range(3):
    print(a[i])
b=[skill1['Name'],skill2['Name'],skill3['Name']]
print('Skill:')
for i,k in enumerate(b):
    print(i+1,k,sep='.')