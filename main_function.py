# you can use the main function and then call other functions inside it
def main():
    my_name = get_name()
    print('hello', my_name)
    
def get_name():
    user_name = input("What is your name: ")
    return user_name
    
    
main()