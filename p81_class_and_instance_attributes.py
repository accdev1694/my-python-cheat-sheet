# class attributes are defined inside the class
# instance attributes are defined as arguments while creating the instances

class Birds():
    # class attributes. they stay the same for all instances of this class
    legs = 2
    wings = 2

    def __init__(self, type, color, gender):
        self.type = type
        self.color = color
        self.gender = gender


        # instance parameters
bird1 = Birds("Chicken", "White", "Female")
bird2 = Birds("Dove", "Grey", "Male")

print(bird1.legs)
print(bird2.legs)

# we can modify the class parameters

Birds.legs = 4
# notice how it changes
print()
print(bird1.legs)
print(bird2.legs)