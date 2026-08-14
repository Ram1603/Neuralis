from abc import ABC, abstractmethod
import math


# Abstract Base Class acting as a blueprint
class Shape(ABC):

    # Abstract method: Must be defined by any subclass that inherits from Shape
    @abstractmethod
    def calculate_area(self):
        pass


# Subclass 1: Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    # Specific area formula for Circle: π * r²
    def calculate_area(self):
        return math.pi * (self.radius**2)


# Subclass 2: Rectangle
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Specific area formula for Rectangle: width * height
    def calculate_area(self):
        return self.width * self.height


# --- Test Run ---
if __name__ == "__main__":
    # Create instances of Circle and Rectangle
    circle_item = Circle(radius=7)
    rectangle_item = Rectangle(width=5, height=10)

    # Display calculated areas
    print(
        f"Circle Area (radius=7)    : {circle_item.calculate_area():.2f} sq units"
    )
    print(
        f"Rectangle Area (5x10)     : {rectangle_item.calculate_area():.2f} sq units"
    )