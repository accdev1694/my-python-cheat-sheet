# exceptions arent really good things in code. they mean something unexpected has happened that has the capacity to break your code

# let us create a program to collect a number from a  user and print it to the terminal
# the try block should only contain the only code that might raise an error
def main():
    age = get_age()
    print(f"You will be {age + 1} years old next year")
    
def get_age():
    while True:
        user_age = input("What is your age: ")
        try:
            return int(user_age)
        except ValueError:
            print("You must type a number")        

main()