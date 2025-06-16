import pytest
from pages.calc_discount import calculate_discount

test_data = [
    (20,80),
    (25,75),
    (37, 63),
    (2, 98),
    (0, "Price and discount must be non-negative"),
    (3.5, 96.5),
    (-10, "Price and discount must be non-negative")
]

@pytest.mark.parametrize("discount_percent, expected", test_data)
def test_calculator_discount(base_price, discount_percent, expected):
    if isinstance(expected, str):
        with pytest.raises(ValueError, match=expected):
            calculate_discount(base_price, discount_percent)
    else:
        assert calculate_discount(base_price, discount_percent) == expected