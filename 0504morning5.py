import pandas as pd

# 一維資料
data = pd.Series([10,20,22,7,68,55])

# 二維資料
data2 = pd.DataFrame(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

data3 = pd.DataFrame(
    {
        'name':['Zac','Andy','Tim'],
        'age':[30,32,28]
    },
    index=['A','B','C']
)
# print(data3)
# print(data3.size)
# print(data3.shape)
# print(data3.columns)
# print(data3.index)

# print(data3['name'])
# print(data3.iloc[0])
# print(data3.loc['C'])


data4 = pd.DataFrame(
    [
        {'name':'Zac','age':32,'gender':'M'},
        {'name':'Max','age':28,'gender':'M'},
        {'name':'Andy','age':30,'gender':'M'},
        {'name':'Amy','age':22,'gender':'F'},
        {'name':'Laura','age':26,'gender':'F'},
    ]
)
# print(data4['age'].max())
# print(data4['age'].min())
# print(data4['age'].mean())
# print(data4['age'].std())
# print(data4['age'].describe())

# condition = data4['age'] >= 30
# print(data4[condition])
# print(data4[data4['age'] >= 30])

condition = data4['gender'].str.contains('F')
print(data4[condition])
