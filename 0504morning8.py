import pandas as pd
datas =pd.read_csv('Restaurant_C_f.csv')
condition = datas['Add'].str.contains('中壢')
result = datas[condition]
result = result.drop(['Id','Px','Py'], axis = 1)
result.to_excel('chungli.xlsx')

