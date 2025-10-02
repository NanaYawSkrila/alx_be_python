# polymorphism_demo.py
import math

class Shape:
    """Base class representing a generic shape."""
    
    def area(self):
        """Calculate the area of the shape. Must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Represents a rectangle shape."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    """Represents a circle shape."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
