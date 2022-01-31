from mymodule import Car

tesla = EletricCar("Tesla", "S")


def test_ecar_info():
    assert tesla.make == 'Tesla'
    assert tesla.battery_size == 100
    assert tesla.model == 'S'


bmw = Car('bmw', 'fast model', 1999)


def test_car_info():
    assert bmw.make == 'bmw'
    assert bmw.mileage == 0
    assert bmw.year == 1999
    assert bmw.model == 'fast model'
