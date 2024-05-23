import sys

# on the command line, while running a program, you run the file name, this takes up the first argument
# anyhting else you type in, seperated by a space are ordered and can be accesses with the 0 index notation in python
# use the sys module to access them

print("my file name is", sys.argv[0])
print("hello, my name is", sys.argv[1])
print("-----")
# however, if the user doesnt type in anything after the file name, there comes an error

# this error can then be handled using an exception

try:
    print("Hello", sys.argv[1])    
except:
    print("You forgot the second argument")
print("-----")  

    
# another way to ensure the user types in something is to use an if statement as follows:

print("What is your name?")
if len(sys.argv) > 2:
    print("too many arguments")
elif len(sys.argv) < 2:
    print("too few arguments")
else:
    print("Your name is", sys.argv[1])
print("-----")