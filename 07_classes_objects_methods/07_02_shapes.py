'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math


class Rectangle():
    """Models the length and width of a rectangle"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Models area of rectangle"""
        rectangle_area = self.length * self.width
        print(f"The area of the rectangle is {rectangle_area}")

    def perimeter(self):
        """Models perimeter of rectangle"""
        rectangle_perimeter = (2*self.length) + (2*self.width)
        print(f"The perimeter of the rectangle is {rectangle_perimeter}")


class Circle():
    """Models the radius of a circle"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Models area of a circle"""
        circle_area = math.pi * (self.radius**2)
        print(f"The area of the circle is {circle_area}")

    def circumference(self):
        """Models the circumference of a circle"""
        circle_circumference = 2 * math.pi * self.radius
        print(f"The circumference of the circle is {circle_circumference}")
