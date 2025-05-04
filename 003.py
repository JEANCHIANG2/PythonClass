import matplotlib.pyplot as plt
plt.rc('font',family='Microsoft Jhenghei')
listx = [1, 2, 3, 4, 5, 6]
listy = [16, 26, 38, 15, 22, 30]
plt.title('test')
plt.xlabel('日')
plt.ylabel('氣溫(攝氏)')

plt.plot(listx, listy, marker='s',color='#ff8c00', linestyle='-',linewidth=1,markersize=5,label='五月')
plt.xlim(1,7)
plt.ylim(1,50)
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.yticks(range(1,51,3))
plt.legend()
plt.show()
