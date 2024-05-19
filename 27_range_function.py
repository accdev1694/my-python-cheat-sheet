# the range function returns a range of numbers form 0 to the argument specified in the function, but exluding the end argument


for char in range(0, 6, 2):
    print(char)
    
# above, the first parameter is the start, the second is the end, the third is the step
    
    
# you can use the _ to define the variable if you are never going to use it again

for _ in range(10):
    print("Hello")
