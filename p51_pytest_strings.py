# let us now create a program that returns a string, and test it
# always note that to make your code more testable, it needs to have a
# return value rather than just a side effect of printing to the terminal

def main():
    name = input("What is your name? ")
    print(hello(name))


def hello(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
    
# now lets create a test file for our code in test_p50_pytest_strings.py
