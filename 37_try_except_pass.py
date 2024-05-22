while True:    
    try:
        age = int(input("What is your age: "))
        break        
    except ValueError:
        pass        
    
    
# notice the pass statement, it is used when you dont want to print a message to the user
# but want to keep the loop on