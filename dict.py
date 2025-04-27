#dict可以當成有屬性的list
#d1 ={
   # 'key':'value'
    #'屬性':'值'
#}


users = [
    {'name':'John',
    'mail':'john@gmail.com',
    'gender':'male',
    'skill':['Photoshop','python']
    },
    {'name':'Mary',
    'mail':'mary@gmail.com',
    'gender':'female',
    'skill':['Photoshop','python','HTML']
    }
]
#for data in users:
    #for k,v in data.items():
        #print(f'{k:10}:{v}')
    #print('--------------------------------------------------')
for idx in range(0,len(users)):
    for k,v in users[idx].items():
        print(f'{k:10}:{v}')