'''
Polymorphism

Polymorphism is the ability of an object to take on multiple forms, depending on the context in which it is used.

Properties of Polymorphism:

1 Method Overriding: A subclass can provide a different implementation of a method that is already defined in its superclass.
2 Method Overloading: Multiple methods with the same name but different parameters can be defined.
3 Operator Overloading: Operators such as +, -, *, etc. can be redefined for custom classes.'''


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Method overriding
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # Method overriding
        return self.width * self.height

# Create a list of shapes
shapes = [Circle(5), Rectangle(4, 6)]

# Iterate over the shapes and calculate their areas using polymorphism
for shape in shapes:
    print(shape.area())

# Output:
# 78.5
# 24