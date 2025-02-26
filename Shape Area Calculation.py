'''
 Shape Area Calculation (Polymorphism)
Create a base class Shape with an abstract method area(). Then, create the following subclasses:

Circle (with radius).
Rectangle (with length and width).
Triangle (with base and height). Each subclass should implement the area() method. Write code to calculate the area of each shape.
'''

from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

for shape in shapes:
    print(f"Area is :{shape.area()}")