# use f-strings or format strings to combine text, variables and even code expressions within a string
#guy = 'oloche' 
#print(f"Hello {guy}")

# you can use f strings to specify thousandth seperators with comas
#num = int(input("What's num: "))
#print(f"{num:,}") 

# you can format decimal points in an f string as well
#gpa = float(input("What your gpa: "))
#print(f"{gpa:.1f}")
# rounds to 1 decimal place

# you can pad your f string with characters before
age = int(input("Whats your age: "))
print(f"{age:05}")
# here i am padding with 0's in front until all the caharcters become 5