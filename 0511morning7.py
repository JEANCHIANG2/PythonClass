class Car:
    def __init__(self, color, door):
        self.color = color
        self.door = door

    def run(self):
        print(f'您的車顏色為{self.color}')

class Toyota(Car):
    pass

class Tesla(Car):
    pass

c1 = Toyota('white',4)
print(c1.__dict__)

c2 = Tesla('red',5)
print(c2.__dict__)