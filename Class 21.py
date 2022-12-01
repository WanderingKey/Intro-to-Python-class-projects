import math

class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return (self.width + self.height) * 2

r1 = Rectangle(4, 40)
r2 = Rectangle(3.5, 35.7)
print(r1.width, r1.height, r1.getArea(), r1.getPerimeter())