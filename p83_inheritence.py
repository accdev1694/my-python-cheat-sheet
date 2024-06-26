class Staff():
    year = 2024
    shift = "Night"
    
    def __init__(self, name):
        self.name = name
        
class Manager(Staff):
    
    def working(self):
        return "is Working!"
    def not_working(self):
        return "is not working!!!"   
        
manager1 = Manager("Gabs")
manager2 = Manager("Dan")
print(f"{manager1.name} {manager1.working()}")
print(f"{manager2.name} {manager1.not_working()}")

