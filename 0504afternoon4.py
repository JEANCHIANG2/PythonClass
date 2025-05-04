import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='Microsoft Jhenghei')


pets = pd.read_csv('COA_OpenData.csv')
# animal_kind(動物的類型)、animal_Variety(動物品種)

total = pets['animal_id'].count()

cats = pets[pets['animal_kind'].str.contains('貓')]
cats_total = cats['animal_id'].count()

dogs = pets[pets['animal_kind'].str.contains('狗')]
dogs_total = dogs['animal_id'].count()

other = pets[pets['animal_kind'].str.contains('貓|狗') == False]

other_total = total - cats_total - dogs_total

print(other['animal_kind'])

plt.pie([dogs_total, cats_total, other_total],
        labels=['狗','貓','其他'],
        autopct='%.1f%%',
        explode=[.1, .1, .5]
        )
plt.legend()
plt.show()