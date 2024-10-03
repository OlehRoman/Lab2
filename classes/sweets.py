class Sweets:
    def __init__(self, flavor, price_per_unit):
        self.flavor = flavor
        self.price_per_unit = price_per_unit

    def cost(self, area):
        return area * self.price_per_unit

    def __str__(self):
        return (f"Sweets with flavor: {self.flavor}\n"
                f"Price per unit area: {self.price_per_unit:.2f}")