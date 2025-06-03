from assertpy import assert_that

def test_negative_sum_scenarios():
    x = 2
    y = 4
    assert x + y == 6

def test_negative_sum_scenarios_assertpy():
    x = 2
    y = 4
    print(f"\nTesting for {x} and {y} equals 6")
    assert_that(x + y).is_equal_to(6)