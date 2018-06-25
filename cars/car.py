class Car:
    def __init__(self, color, doors):
        self.color = color
        self.number_of_doors = doors
        self.number_of_wheels = 4

    def __str__(self):
        return f'Color: {self.color}\nDoors: {self.number_of_doors}\nWheels: {self.number_of_wheels}\n'

    def honk(self):
        print('Honk!')
