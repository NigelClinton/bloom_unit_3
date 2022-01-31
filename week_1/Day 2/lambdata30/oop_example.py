""" Module that implements Car and Eletric Car classes """
"""Car class"""


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self):
        print('Driving...')

    def set_mileage(self, new_mileage):
        self.mileage = new_mileage

    def get_gas(self):
        print('Filling up on gas...')


"""Electric Car class"""


class EletricCar(Car):

    def __init__(self, make, model, year, battery_size=100):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_gas(self):
        print('I dont run on gas!')
