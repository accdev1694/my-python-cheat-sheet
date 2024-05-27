# we have seen default parameters to the print function before
print("Hello", "Oloche", sep='-')
# this sets sep as a default parameter

# the same way we can set a default parameter to our own functions
# just in case the user doesnt pass in any argument as a parameter
def greet(to="world"):
    print("Hello", to)
    
greet()
# notice how hello world gets printed