class Car:
    def __init__(self, color, brand, door):
        # self.color = 'red'
        # self.brand = 'Tesla'
        # self.door = 4
        self.color = color
        self.brand = brand
        self.door = door

    def run(self):
        print(f'您的車品牌是{self.brand}，顏色為{self.color}')




c1 = Car('red','Tesla',4)

print(c1)
print(c1.color)
print(c1.brand)
print(c1.door)
print(c1.__dict__)
c1.run()

c2 = Car('white', 'Toyota', 5)
# c2.color = 'white'
# c2.brand = 'Toyota'
# c2.door = 5

print(c2)
print(c2.color)
print(c2.brand)
print(c2.door)
print(c2.__dict__)
c2.run()