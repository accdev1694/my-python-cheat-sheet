from timeit import timeit


code1 = '''
def xfactor(income):
    if income <= 0:
        raise ZeroDivisionError("Income cannot be 0 or less")
    return 10 / income

try:
    xfactor(100)
except ZeroDivisionError as e:
    print(e)
    '''
    

code2 = '''
def xfactor(income):
    try:
        return 10 / income
    except ZeroDivisionError:
        print("Income cannot be 0 or less")
xfactor(100)
    '''
    

code3 = '''
def xfactor(income):
    if income <= 0:
        print("Income cannot be 0 or less")
    else:
        return 10 / income
xfactor(100)
    '''
    
print("raise:", timeit(code1, number = 100000)) # most time
print("try except:", timeit(code2, number = 100000)) #this took the least time, try except
print("if else:", timeit(code3, number = 100000)) # most time, same as first
