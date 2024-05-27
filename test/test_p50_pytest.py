import pytest
from p50_pytest import square

# this program is specifically to test the square function
# note the naming convensions for the test file name and test function names
# prefixing the actual files with 'test'
# its common practice to mannually write code to test each casein wwhich the test might fail
# use pytest and the try assert and printing error is handled automatically
# just assert the correct cases
# seperate each function for each use case
    
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
# you have to test strings, smaller numbers, larger numbers
# 
def test_str():
    with pytest.raises(TypeError):
        square("cat")


