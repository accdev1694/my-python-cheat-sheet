# because manual testing casn be so verbose, we use a module pytest
# write code to test your code
# principally, write your test first
# lets explore our calculator program

def main():
    x = int(input("What's x? "))
    print("x is", square(x))
    
    
def square(n):
    return n * n


if __name__ == "__main__":
    main()
    
# we create a test file for this calculator naming it test_p50_pytest.py