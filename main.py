from classes.circle import Circle
from classes.ring import Ring
from classes.triangle import Triangle

def main():
    circle = Circle(10)
    print(circle)

    ring = Ring(outer_radius=15, inner_radius=5, name="Sweet Donut", flavor="Chocolate", price_per_unit=1.5)
    print(ring)

    triangle = Triangle(point1=(0, 0), point2=(6, 0), point3=(3, 5))
    print(triangle)

    triangle_area = triangle.area()
    print(f"Triangle Area: {triangle_area:.2f} square units")

    remaining_circle_area = circle.area_without_triangle(triangle)
    print(f"Circle Area without Triangle: {remaining_circle_area:.2f} square units")

    a, b, c = 3, 4, 5
    is_triangle_valid = Triangle.is_valid_triangle(a, b, c)
    print(f"Can sides {a}, {b}, and {c} form a valid triangle? {'Yes' if is_triangle_valid else 'No'}")

    total_cost = ring.cost(ring.area())
    print(f"Total cost of the donut: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
