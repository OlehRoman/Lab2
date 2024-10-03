import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def area_without_triangle(self, triangle):
        circle_area = self.area()
        triangle_area = triangle.area()
        return circle_area - triangle_area

    def length_of_circle(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        info = ("\n"
            f"Circle Information:\n"
            f"-------------------\n"
            f"Radius: {self.radius:.2f}\n"
            f"Diameter: {2 * self.radius:.2f}\n"
            f"Area: {self.area():.2f}\n"
            f"Lenght of circle: {self.length_of_circle():.2f}"
        )
        return info
