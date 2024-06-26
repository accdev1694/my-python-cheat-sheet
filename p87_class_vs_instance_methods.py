# instance methods are methods defined inside the class 
# class methods are special decorator methods that are defined at the class level

import clear

class Point():
    # instance attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # class method
    @classmethod
    def zero(cls):
        return cls(0,0)
    
    # instance method
    def draw(self):
        return f"Point {self.x}, {self.y}"
clear.clear()
point = Point.zero()
print(point.draw())