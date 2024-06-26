# there is a method used in checking if an object is an instance of a class
import clear

class Point():
    def draw(self):
        print("draw")
clear.clear()
point = Point()
print(isinstance(point, Point))