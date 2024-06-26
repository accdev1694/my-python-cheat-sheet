# Classes are blueprints for creating new objects, e.g  Human
# Objects are instances of a class, e.g John, Mary

# classes use Pascal convension (first word uppercase, no underscores)
# all functions in a class should have a self parameter

# Each class has attributes and methods
# Attributes are defined inside the constructor (they describe the object - nouns, descriptions, properties)
# methods are functions inside the object (they are verbs or actions that the object can perform)

class Car:
    # This the constructor. self refers to the Car class
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

        # methods, telling some actions
    def start(self):
        return f"Press {self.brand} Start Button"

    def stop(self):
        return f"Press {self.brand}Brake to Stop"

    def describe(self):
        return f"{self.color} {self.year} {self.brand}"


# notice you dont need to pass self in the argument
car1 = Car("BMW", 2025, "Blue")
car2 = Car("Mustang", 2026, "Green")
print()
print('-----------')
print(car1.color, car1.year, car1.brand)
print(car2.color, car2.year, car2.brand)

# we can print the methods
print('-----------')
print(car1.start())
print(car2.start())
print('-----------')
print()

# we can then print a detailed decription of the cars
print('-----------')
print(car1.describe())
print(car2.describe())
print('-----------')
print()
