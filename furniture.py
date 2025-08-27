# Parent class
class Furniture:
    def __init__(self, name, material, color, price):
        self.name = name
        self.material = material
        self.color = color
        self.price = price

    def describe(self):
        return f"{self.name} made of {self.material}, color {self.color}, priced at ${self.price}"

    def discount(self, percentage):
        """Apply a discount and return new price"""
        discounted_price = self.price - (self.price * percentage / 100)
        return f"Discounted price: ${discounted_price:.2f}"


# This shows inheritance for class chair
class Chair(Furniture):
    def __init__(self, name, material, color, price, legs, has_cushion):
        super().__init__(name, material, color, price)
        self.legs = legs
        self.has_cushion = has_cushion

    # This shows polymorphism for the chair
    def describe(self):
        cushion_status = "with cushion" if self.has_cushion else "without cushion"
        return f"{self.name} ({self.color}, {self.material}) - {self.legs} legs, {cushion_status}, costs ${self.price}"


# This shows inheritance for class table
class Table(Furniture):
    def __init__(self, name, material, color, price, shape, seats):
        super().__init__(name, material, color, price)
        self.shape = shape
        self.seats = seats

    # This shows polymorphism for the table
    def describe(self):
        return f"{self.name}: A {self.shape} table in {self.color}, seats {self.seats} people, costs ${self.price}"


# Usage examples
f1 = Furniture("Generic Furniture", "Wood", "Brown", 150)
c1 = Chair("Office Chair", "Leather", "Black", 120, 5, True)
t1 = Table("Dining Table", "Oak Wood", "Dark Brown", 500, "Rectangle", 6)

print(f1.describe())
print(c1.describe())
print(t1.describe())

print(c1.discount(10))   # Discount on chair
print(t1.discount(20))   # Discount on table
