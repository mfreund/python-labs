'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car():

    wheels = 4 # class

    """Models a car including model, year, and max speed"""
    def __init__(self, model, year, max_speed):  # three attributes
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        """Increases max_speed of the car by 5"""
        self.max_speed += 5

    def __str__(self):
        return f"The {self.model} {self.year} has a maximum speed of {self.max_speed} km/h"

honda = Car('Honda Accord', '2018', 200) # instance of Car class
toyota = Car('Toyota Camry', '2019', 215)
print(honda.wheels)
Car.wheels = 5 # class level
print(toyota.wheels)
print(honda.wheels)
