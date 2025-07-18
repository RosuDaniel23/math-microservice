import pytest
from app.services import factorial, fibonacci, power

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_fibonacci_base():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_positive():
    assert fibonacci(7) == 13

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-5)

def test_power():
    assert power(2) == 4
    assert power(10) == 100
