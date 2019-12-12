import math


# Triangle area
class Triangle:
    
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2 
        return math.sqrt(s * (s - self.side1) * ( s - self.side2) * (s - self.side3)) 

# EquilateralTriangle area used also in Tetahendron class to calculate its volume
class EquilateralTriangle():

    def __init__(self, side):
        self.side = side 

    def get_area(self):
        return math.sqrt(3) * math.pow(self.side, 2) / 4 

# Rectangle area calculation
class Rectangle:
    
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def get_area(self):
        return self.width * self.height

# Square area calculation
class Square:

    def __init__(self, side):
        self.side=side

    def get_area(self):
        return math.pow(self.side,2)

# Ellipse area calculation
class Ellipse:

    def __init__(self, a_axis, b_axis):
        self.a_axis = a_axis
        self.b_axis = b_axis

    def get_area(self):
        return math.pi * self.a_axis * self.b_axis 

# Cube volume calculation
class Cube(Square):

    def __init__(self, side):
        super().__init__(side)

    def get_volume(self):
        return super().get_area() * self.side


# Tetahendron volume calculation
class Tetahedron(EquilateralTriangle):

    def __init__(self, side):
        super().__init__(side)

    def get_volume(self):
        return super().get_area() * math.sqrt(6) * self.side / 3 

# creating instances of objects of existed classes
t1 = Triangle(4,4,4)
t2 = EquilateralTriangle(4)
r1 = Rectangle(10,14)
s1 = Square(10)
e1 = Ellipse(10,14)

c1 = Cube(10)
te3 = Tetahedron(5)

# Calculating the area of different objects shapes
print(t1.get_area())
print(t2.get_area())
print(r1.get_area())
print(s1.get_area())
print(e1.get_area())


# Calculating the volume of 2 solids
print(c1.get_volume())
print(te3.get_volume())
