import matplotlib.pyplot as plt
plt.rc('font',family='Microsoft Jhenghei')

datas=[20,68,88]
labels = ['大學','高中','國中']
plt.pie(
    datas,
    labels = labels,
    radius = 1,
    labeldistance = .3,
    textprops = {'size':10,'weight':'bold'},
    autopct = '%.1f%%'

)
data = [30,70,120]
total = sum(data)
data_2 = [str(round(100 * d / total))+'%'for d in data]
print(data_2)
plt.legend()
# plt.show()
