import pytest

def test_case01():
    # catches all errors
    with pytest.raises(Exception):
        assert (1/0)
    # catches specific error, better approach
    with pytest.raises(ZeroDivisionError):
        assert (5/0)


def test_case02():
    with pytest.raises(Exception) as ex_info:
        assert (1,2,3) == (1,2,4)
    print(ex_info)  # AssertionError


def func1():
    raise ValueError("Exception func1 raised.")


def test_func1():
    with pytest.raises(ValueError) as ex_info:
        func1()
    assert str(ex_info.value) == 'Exception func1 raised.'
