class Car:
    def __init__(self, color, door):
        self.color = color
        self.door = door

    def run(self):
        print(f'您的車顏色為{self.color}')


class Toyota(Car):
    # pass
    # brand = 'Toyota'
    def __init__(self, color, door):
        super().__init__(color, door)
        # self.brand = brand
        self.brand = 'Toyota'



class Tesla(Car):
    def __init__(self, color, door):
        super().__init__(color, door)
        self.brand = 'Tesla'
c1 = Toyota('white',4)
print(c1.brand)
print(c1.__dict__)

c2 = Tesla('red',4)
print(c2.__dict__)