# polymorphism_demo.py
import math  # Needed for Circle area calculation

class Shape:
    """Base class for all shapes"""
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Rectangle shape"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    """Circle shape"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
