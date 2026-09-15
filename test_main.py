import pytest
from main import add, subtract, multiply, divide, is_even

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_is_even():

 def test_is_even():
    assert is_even(4) == True