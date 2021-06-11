# pip install pytest
# convention is to name the test file as  "test_toBeTestedName.py"

import mathlib
import pytest
import sys

# give test_ prefix to the method that you want to test
def test_calc_total():
    assert mathlib.calc_total(4, 5) == 9
    assert mathlib.calc_total(7, 3) == 10
    assert mathlib.calc_total(10, 10) >= 15

# how to skip a test
@pytest.mark.skip(reason="I want to skip this test for now")
def test_calc_muliply():
    assert mathlib.calc_multiply(10, 3) == 30
    assert mathlib.calc_multiply(5, 5) == 25

@pytest.mark.skipif(sys.version_info < (3,3), reason="checking os version")
def test_calc_total_string():
    result = mathlib.calc_total('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result

def test_calc_muliply_string():
    assert mathlib.calc_multiply('Hello ', 3) == 'Hello Hello Hello '
    res = mathlib.calc_multiply('Hello ', 2)
    assert res == 'Hello Hello '
    assert type(res) is str
    assert 'Hello' in res


'''
v = verbose, for details
k = keyword
m = marks


how to run it => pytest test_mathlib.py

how to only run one of the tests => pytest test_mathlib.py::test_calc_total

run all tests that contain keyword 'calc' => pytest -v -k "calc"

run all tests that contain keyword 'calc' or 'windows' => pytest -v -k "calc or windows"

stop the testing process when there is a failure => pytest -v -x

stop testing process after a number of fails => pytest -v --maxfail=2

show the prints => pytest -v -s
'''