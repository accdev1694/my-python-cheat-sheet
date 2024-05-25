# the continue statement is used within the loop to ask the program to retart the loop from the top

while True:    
    try:
        age = int(input("What is your age: "))
        if age <= 12:
            continue
        else:
            print("You are qualified")
            break
            
    except:
        pass
    
