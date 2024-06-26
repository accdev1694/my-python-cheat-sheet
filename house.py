class House():
    is_roof = True
    kitchen = 1
    def __init__(self, rooms, is_dining, baths, color, price):
        self.rooms = rooms
        self.is_dining = is_dining
        self.baths = baths
        self.color = color
        self.price = price
        
    def describe(self):
        print(f"{self.rooms} bedroom house with {self.baths} bathrooms, {self.color} color. Its price is {self.price} and Dining is {self.is_dining}")
        
    def warming(self):
        print("Warming is switched on")
        