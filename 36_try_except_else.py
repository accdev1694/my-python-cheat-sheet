# the else statement is used here to execute a code if there is no error to catch on the except block
# the same code from the previous module can be expressed thus:
while True:    
    try:
        age = int(input("What is your age: "))        
    except ValueError:
        print("You must type in a number")        
    else:
        print(f"You will be {age + 1} years old next year")
        break
    
# notice the break statement, it is used to break out of the loop once the code runs successfully