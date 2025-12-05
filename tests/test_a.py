import pytest
from src.a import div

@pytest.mark.parametrize('a, b, excpected', [
    (1, 2, 0.5),
    (2, 3, 0.6666666666666666),
    (3, 4, 0.75),
    (4, 5, 0.8),
    (5, 6, 0.83333333333333333),
    (6, 7, 0.8571428571428571),
    (7, 8, 0.875),
    (8, 9, 0.8888888888888888),
])
def test_division(a, b, excpected):
    assert div(a, b) == excpected

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_infinity_division():
    assert div(float('inf'), 1) == float('inf')
    assert div(1, float('inf')) == 0.0
'''
def test_faulty():
    assert div(2, 5) == 4
'''