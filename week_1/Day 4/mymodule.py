def inc(x):
    return x + 1

""" Module that implements Car and Eletric Car classes """


class Car:
    """ Car class for creating car objects. """
    def __init__(self, make, model, year):
        """ Initializing attreibutes """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    
    def drive(self):
        """ Drives the car """
        print('Driving...')

    def set_mileage(self, new_mileage):
        """Sets milage to the specified milage"""
        self.mileage = new_mileage

    def get_gas(self):
        """ Filling up the tank"""
        print('Filling up on gas...')


"""Electric Car class"""


class EletricCar(Car):
    
    def __init__(self, make, model, year, battery_size=100):
        """ Inherit from other class + bat size """
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_gas(self):
        """ Gas Meme """
        print('I dont run on gas!')
