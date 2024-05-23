import sys

# used to exit early from a program and could take an argument which is printed to the user

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
print("Hello,", sys.argv[1])