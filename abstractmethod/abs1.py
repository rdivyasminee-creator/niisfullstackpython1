from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

33
# Derived class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Taking input
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Creating object
r = Rectangle(length, width)

# Display result
print("Perimeter of Rectangle =", r.perimeter())