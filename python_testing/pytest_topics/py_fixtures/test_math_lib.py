
import math_lib as mathlib
import pytest
import sys


def test_calc_total():
    assert mathlib.calc_total(4, 5) == 9
    assert mathlib.calc_total(7, 3) == 10
    assert mathlib.calc_total(10, 10) >= 15


@pytest.mark.skip(reason="I want to skip this test for now")
def test_calc_multiply():
    assert mathlib.calc_multiply(10, 3) == 30
    assert mathlib.calc_multiply(5, 5) == 25

@pytest.mark.skipif(sys.version_info < (3,3), reason="checking os version")
def test_calc_total_string():
    result = mathlib.calc_total('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result

def test_calc_multiply_string():
    assert mathlib.calc_multiply('Hello ', 3) == 'Hello Hello Hello '
    res = mathlib.calc_multiply('Hello ', 2)
    assert res == 'Hello Hello '
    assert type(res) is str
    assert 'Hello' in res


'''
v = verbose, for details
k = keyword
m = marks


how to run it => pytest test_math_lib.py
how to only run one of the tests => pytest test_math_lib.py::test_calc_total
run all tests that contain keyword 'calc' => pytest -v -k "calc"
run all tests that contain keyword 'calc' or 'windows' => pytest -v -k "calc or windows"
stop the testing process when there is a failure => pytest -v -x
stop testing process after a number of fails => pytest -v --maxfail=2
show the prints => pytest -v -s
'''