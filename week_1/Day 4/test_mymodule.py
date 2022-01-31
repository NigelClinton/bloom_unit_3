import pytest
from mymodule import inc, Car

def test_inc_pn():
    assert inc(11) == 12
    assert inc(3) == 4

def test_inc_z():
    assert inc(0) == 1

def test_inc_nn():
    assert inc(-1) == 0

def test_inc_fn():
    assert inc(1.5) == 2.5

ford = Car("Ford","Focus",2021)

def test_car_info():
    assert ford.make == 'Ford'
    assert ford.mileage == 0