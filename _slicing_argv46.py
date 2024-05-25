import sys
# we can get access to multiple prompts passed at the command prompt using a for loop

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    
for arg in sys.argv[1:]:
    print("Welcome", arg)
