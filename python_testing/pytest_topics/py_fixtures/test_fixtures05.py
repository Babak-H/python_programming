"""
Parameterization with Fixtures
"""
import pytest


# we feed these two variables to test function via the params
# ids are optional, it is name of the variable we feed to test function
@pytest.fixture(params=[(3, 4), [3, 5]], ids=['tuple', 'list'])
def fixture01(request):
    # it will send each of the parameters to the test function, so here the test will be called TWO times (two asserts)
    return request.param


@pytest.fixture(params=["access", "slice", "assign"])
def fixture02(request):
    return request.param


def test_fix_param01(fixture01):
    assert type(fixture01) in [tuple, list]


# this test will run six times (all combination of variables between the two fixtures)
def test_two_fixtures(fixture01, fixture02):
    if fixture02 == "access":
        assert fixture01[0]
        assert fixture01[0] == 3
    elif fixture02 == "slice":
        assert fixture01[::-1]
    elif fixture02 == "assign":
        fixture01[0] = 99
        assert True
