# lets try out arithmetic operatos on methods

class Numbers():
    def __init__(self, x):
        self.x = x

        
    def __add__(self, num2):
        return self.x + num2.x
    
    def __sub__(self, num2):
        return self.x - num2.x
    
    def __mul__(self, num2):
        return self.x * num2.x
    
    
num1 = Numbers(7)
num2 = Numbers(5)

print(num1 + num2, '(exepects 12 for addition)')
print(num1 - num2, '(exepects 2 for subtraction)')
print(num1 * num2, '(exepects 35 for subtraction)')

# check out other magic methods here https://realpython.com/python-magic-methods/