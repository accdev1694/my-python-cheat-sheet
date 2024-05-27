from p30_custom_functions import get_int

# we will import a function from another file for use in this program
def main():
    calc = num_square()
    print(calc)
    
def num_square():
    num = get_int()
    return num * num


main()