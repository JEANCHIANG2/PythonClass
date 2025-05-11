import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='Microsoft Jhenghei')
# Index(['年別', '亞洲地區', '日本', '韓國', '中國大陸', '越南', '泰國', '馬來西亞', '新加坡', '小計'], dtype='object')
datas = pd.read_csv('出國旅客按目的地統計.csv')
# labels = datas.columns[2:-1]
# data = datas.iloc[1][2:-1]
# print(data)
x = datas.columns[2:-1]
h = [int(h) for h in datas.iloc[1][2:-1]]
color = ['pink','#8ac4de','#d24b31','#c47bb4','#83ad28','#cda581','#9fd0de']
tick_label = ['Japan','Korea','China', 'Vietnam','Tailand','Malaysia','Singapore']
plt.bar(x,h,color=color,tick_label=tick_label)
plt.show()
