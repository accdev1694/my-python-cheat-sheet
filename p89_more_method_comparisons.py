# lets look at more method comparison operators

class Numbers():
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, num2):
        return self.x == num2.x
    
    def __ne__(self, num2):
        return self.x != num2.x
    
    def __gt__(self, num2):
        return self.x > num2.x
    
    def __lt__(self, num2):
        return self.x < num2.x
    
num1 = Numbers(5)
num2 = Numbers(2)

print(num1 > num2, 'expects True')
print(num1 < num2, 'expects False')
print(num1 == num2, 'expects False')
print(num1 != num2, 'expects True')
