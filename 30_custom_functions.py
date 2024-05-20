# main function
# function to get a positive integer
# function to say hello number of times

def main():
    number = get_int()
    hello(number)
    
def get_int():
    while True:        
        n = int(input("Type a number: "))
        if n >= 0:
            break
    return n
    
def hello(i):
    for _ in range(i):
        print("Hello")
main()