# Abstract classes are classes that are incomplete
# they have some define attributes but are not instantiated.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def move(self):
        pass
    def brake(self):
        pass
    
class Cars(Vehicle):
    def move(self):
        print("You Move")
    def brake(self):
        print("You brake")
        
car = Cars()
car.move()
car.brake()