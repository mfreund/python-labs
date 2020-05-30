'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

from freeform import Connobation


class City(Connobation):
    def __init__(self, name, country, currency, population, mayor):
        super(City, self).__init__(name, country, currency, population)
        self.mayor = mayor

class AmericanCity(City):
    def __init__(self, name, population, mayor):
        super(AmericanCity, self).__init__(name, 'USA', 'US Dollars', population, mayor)  # some vars stay the same


from freeform import Drink


class Soda(Drink):
    def __init__(self, brand, type, size, number, flavor):
        super(Soda, self).__init__(brand, type, size, number)
        self.flavor = flavor

class Diet(Soda):
    def __init__(self, brand, size, number, flavor):
        super(Diet, self).__init__(brand, 'diet soda', size, number, flavor)


from freeform import People


class Adult(People):
    def __init__(self, name, age, fave_color, occupation):
        super(Adult, self).__init__(name, age, fave_color)
        self.occupation = occupation

class Hours(Adult):
    def __init__(self, name, age, fave_color, occupation, hours):
        super().__init__(name, age, fave_color, occupation)
        self.hours = hours
