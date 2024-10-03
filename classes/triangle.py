import math
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def __str__(self):
        x_coords = [self.point1[0], self.point2[0], self.point3[0], self.point1[0]]
        y_coords = [self.point1[1], self.point2[1], self.point3[1], self.point1[1]]

        plt.plot(x_coords, y_coords, marker='o', color='green')
        plt.fill(x_coords, y_coords, 'skyblue', alpha=0.3)
        plt.title("Triangle")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
        info = ("\n"
            f"Triangle coordinates\n"
            f"--------------------\n"
            f"-----> {self.point1} <-----\n"
            f"-----> {self.point2} <-----\n"
            f"-----> {self.point3} <-----\n")
        return info

    def area(self):
        a = math.dist(self.point1, self.point2)
        b = math.dist(self.point2, self.point3)
        c = math.dist(self.point3, self.point1)

        semi_perimeter = (a + b + c) / 2
        return math.sqrt(
            semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)
        )

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a