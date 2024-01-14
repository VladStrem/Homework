import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


circle_1 = Circle(2)
circle_2 = Circle(3)

print(circle_1)
print(circle_2)

area_circle_1 = circle_1.area()
print(f"Area of circle_1: {area_circle_1:.2f}")

circumference_circle_2 = circle_2.circumference()
print(f"Circumference of circle_2: {circumference_circle_2:.2f}")