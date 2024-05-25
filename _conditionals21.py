# if statements are used to execute some code if some condition is true

age = int(input("How old are you? "))

if age <= 12:
    print("you are young")
elif age <= 19:
    print("You are a teenager")
elif age <= 21:
    print("You are a young adult")
elif age <= 50:
    print("You are an adult")
else:
    print("You are old!!!")
    
# this is called a control flow
