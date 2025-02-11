"""
Parametrized tests for the Operations class.
"""

import pytest
from app.operations import Operations  # Adjust this import if needed

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3.5, 4.5, 8.0),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_addition(a, b, expected):
    """
    Test that addition of a and b returns the expected sum.
    """
    result = Operations.addition(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3.5, 1.5, 2.0),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtraction(a, b, expected):
    """
    Test that subtraction of b from a returns the expected difference.
    """
    result = Operations.subtraction(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (3.5, 2, 7.0),
    (-1, -1, 1),
    (0, 10, 0),
])
def test_multiplication(a, b, expected):
    """
    Test that multiplication of a and b returns the expected product.
    """
    result = Operations.multiplication(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (3.5, 1.75, 2.0),
    (-4, -2, 2),
    (9, 3, 3),
])
def test_division(a, b, expected):
    """
    Test that division of a by b returns the expected quotient.
    """
    result = Operations.division(a, b)
    assert result == expected

def test_division_by_zero():
    """
    Test that dividing by zero raises a ValueError with the correct message.
    """
    with pytest.raises(ValueError, match="Division By zero is not allowed."):
        Operations.division(5, 0)
