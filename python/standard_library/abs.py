import pytest
import logging


def _abs(x):
    """
     Return the absolute value of a number. The argument may be an integer, a floating point number, or an object
     implementing __abs__(). If the argument is a complex number, its magnitude is returned.
    """
    return abs(x)


def test_integer():
    value = 4
    print(type(value))
    a = _abs(value)
    assert a == 4, "Fix"


def test_floating_point_number():
    value = 10.35667
    a = _abs(value)
    assert a == value, "Fix"


def test_complex_number():
    value = 3 +6j
    print(type(value))
    a = _abs(value)
    print(a)

