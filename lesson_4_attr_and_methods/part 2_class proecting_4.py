import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * self.radius
        self.area = math.pi * radius ** 2

circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)