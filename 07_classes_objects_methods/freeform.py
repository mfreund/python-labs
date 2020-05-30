'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...
'''


class Connobation():

    language = 'English'  # class
    # population = 'Over 7 million'  # class

    """Models city with country"""
    def __init__(self, name, country, currency, population):
        self.name = name
        self.country = country
        self.currency = currency
        self.__population = population
        print("Im printing an init")

    def __str__(self):
        print("Im printing a str")
        return f"{self.name} is located in {self.country}"

    def __add__(self, other):
        return self.__population + other.__population

    def __gt__(self, other):
        return self.__population > other.__population

    def __lt__(self,other):
        return self.__population < other.__population

    def __eq__(self, other):
        return self.__population == other.__population

    def get_population(self):
        return self.__population

    def set_population(self, new_population):
        if isinstance(new_population, int):
            self.__population = new_population
        else:
            print("Population must be integer")

if __name__ == '__main__':
    ny = Connobation('New York City', 'United States of America', 'US dollars', 9)
    tokyo = Connobation('Tokyo', 'Japan', 'yen', 7)
    print(ny + tokyo)
    print(ny > tokyo)
    tokyo.set_population('two')
    print(ny > tokyo)

class Drink():

    package = 'bottle'

    """Models amount of liquid one has had in a day"""
    def __init__(self, brand, type, size, number):
        self.brand = brand
        self.type = type
        self.size = size
        self.number = number

    def __str__(self):
        return f"You have drank {self.size} fl oz of {self.brand} {self.number} times today"

    def amount(self):
        self.amount = self.size * self.number
        return self.amount

    def __add__(self, other):
        return self.amount + self.amount


if __name__ == '__main__':
    sat = Drink('Dasani', 'water', 8, 3)
    sun = Drink('Coke', 'soda', 8, 5)
    weekend = sat.amount() + sun.amount()
    print(weekend)

class People():

    nationality = 'American'

    """Models a person's name, age, favorite color"""
    def __init__(self, name, age, fave_color):
        self.name = name
        self.age = age
        self.fave_color = fave_color

    def __str__(self):
        return f"{self.name} is {self.age} years old and likes the color {self.fave_color}!"

    def birthday(self, birthdaymonth):
        self.birthdaymonth = birthdaymonth
        self.age += 1
        return f"{self.name} will be {self.age} in {birthdaymonth}"

    def education(self):
        if self.age >= 18:
            print(f"{self.name} is legally considered an adult")
        else:
            print(f"{self.name} is legally not considered an adult")


if __name__ == '__main__':
    mikiko = People('Mikiko', 23, 'red')
    bob = People('Bob', 40, 'blue')
    print(mikiko.birthday('September'))
