import pytest
import mathlib


# parametrize will let you call the function once, but give it different arguments
@pytest.mark.parametrize('num1, num2, res',
                        [
                            (4, 5, 9),
                            (10, 10, 20),
                            ('Hello', ' World', 'Hello World'),
                            (10.5, 25.5, 36)
                        ])
def test_calc_total_par(num1, num2, res):
    assert mathlib.calc_total(num1, num2) == res