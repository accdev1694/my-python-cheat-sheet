# because manual testing casn be so verbose, we use a module pytest
# write code to test your code
# principally, write your test first
# lets explore our calculator program

def main():
    x = input("What's x? ")    
    print("x -", square(x))
    
    
def square(n):
    try:
        n = int(n)
        return n * n
    except ValueError:
        message = 'must be an int'
        return message


if __name__ == "__main__":
    main()
    
# we create a test file for this calculator naming it test_p50_pytest.py