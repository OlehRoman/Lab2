from classes.circle import Circle
from classes.sweets import Sweets
import math

class Ring(Circle, Sweets):
    def __init__(self, outer_radius, inner_radius, name, flavor, price_per_unit):
        Circle.__init__(self, outer_radius)
        Sweets.__init__(self, flavor, price_per_unit)
        self.inner_radius = inner_radius
        self._name = name

    def area(self):
        outer_area = super().area()
        inner_area = math.pi * self.inner_radius ** 2
        return outer_area - inner_area

    def __str__(self):
        info = (
            f"This {self.name} has the following characteristics:\n"
            f"--------------------------------------------\n"
            f"Outer radius: {self.radius:.2f} units\n"
            f"Inner radius: {self.inner_radius:.2f} units\n"
            f"Radius difference: {self.radius_difference():.2f} units\n"
            f"Outer area: {super().area():.2f} square units\n"
            f"Inner area: {self.inner_area():.2f} square units\n"
            f"Ring area (Outer - Inner): {self.area():.2f} square units\n"
            f"Flavor: {self.flavor}\n"
            f"Price per unit area: {self.price_per_unit:.2f}\n"
            f"Total cost: {self.cost(self.area()):.2f}\n"
        )
        return info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 1:
            raise ValueError("Too short name")
        self._name = value

    def inner_area(self):
        return math.pi * self.inner_radius ** 2

    def radius_difference(self):
        return self.radius - self.inner_radius
