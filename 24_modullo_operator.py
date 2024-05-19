# modullo operators finds the remainder of a division

# lets imlements a program to find out if a number is even or odd
# remember that even numbers are divisible by 2 with remainder of 0
# and odd numbers are divisible by 2 with remainders more than 0

def main():
    num = int(input("Type in your number: "))
    if is_even(num):
        print("Number is even")
    else:
        print("Number is odd")
        
def is_even(x):
    #return True if x % 2 == 0 else False
    return x % 2 == 0
    # this line above is termed a pythonic way of writing code
        
main()
