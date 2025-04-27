import matplotlib.pyplot as plt

listx = [16, 26, 38, 15, 22, 30]
listy = [1, 3, 5, 7, 9, 11]
plt.title('test')
plt.xlabel('degree')
plt.ylabel('day')
plt.plot(listx, listy, marker='o', color='green')

plt.show()
