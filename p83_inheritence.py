class Staff():
    year = 2024
    shift = "Night"
    
    def __init__(self, name):
        self.name = name
        
class Manager(Staff):
    def working(self):
        return f"{self.name} is Working!"
    
    def not_working(self):
        return f"{self.name} is not Working!!!" 
        
manager1 = Manager("Gabs")
manager2 = Manager("Dan")
print(manager1.working())
print(manager1.not_working())

