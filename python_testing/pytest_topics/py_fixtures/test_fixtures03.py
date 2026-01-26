import pytest


def test_del_item(setup01):
    del setup01[-1]
    print(setup01)
    # IDE might show an error related to the 'pytest.weekdays1', but it is actually fine
    assert setup01 == pytest.weekdays1


def test_remove_item(setup02):
    setup02.remove('thurs')
    print(setup02)
    assert setup02 == pytest.weekdays2


# pytest -v -k test_fixtures03 --setup-show