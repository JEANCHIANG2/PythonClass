import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='Microsoft Jhenghei')
# Index(['年別', '亞洲地區', '日本', '韓國', '中國大陸', '越南', '泰國', '馬來西亞', '新加坡', '小計'], dtype='object')
datas = pd.read_csv('出國旅客按目的地統計.csv')
labels = datas.columns[2:-1]
data = datas.iloc[1][2:-1]
print(data)
plt.pie(
    data,
    labels=labels,
    radius=1,
    labeldistance=1.1,
    textprops={'size':10, 'weight':'bold'},
    autopct='%.1f%%'
)
plt.legend()
plt.show()
