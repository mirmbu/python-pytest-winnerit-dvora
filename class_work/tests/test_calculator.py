from pages.calculateor import Calculator
import pytest
from assertpy import assert_that

test_data = [
    (1,1,2),
    (3,7,10),
    (5,1,6),
    (2,10,12),
    (10, 10, 20),
    (0,5,5),
    (-1,5,4),
    (-2,-2,-4)
]


@pytest.mark.parametrize("x, y, expected", test_data)
def test_add(x, y, expected):
    #send the x and y in the initializing the class.
    calc = Calculator(x,y)
    assert calc.add() == expected