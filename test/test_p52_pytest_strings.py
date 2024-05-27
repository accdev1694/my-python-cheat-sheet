from p51_pytest_strings import hello
import pytest

def test_hello_arg():
    assert hello('Oloche') == "Hello, Oloche"
    
def test_hello_default():
    assert hello() == "Hello, World"
