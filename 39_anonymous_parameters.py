# you can create functions with anonymous parameters that can be called with any argument whatsoever

def main():    
    name = get_name()
    age = get_age()
    
    greet_user("Hello user")   
    greet_user(f"hi {name}, you are {age} years old") 
    
def greet_user(prompt):
    print(prompt)
    
def get_name():
    user_name = input("What is your name: ")
    return user_name

def get_age():
    user_age = int(input("What is your age: "))
    return user_age
    
    
    
main()