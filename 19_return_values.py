# the print function has a side effect of printing something to the terminal

# however, you can implemet functions to have a return value or multiple return values,
# values which can then be used outside that function, whenever you call it

def main():
    width = int(input("What is width: "))
    width = square(width)
    print(width)


def square(x):
    return x**20
    


main()