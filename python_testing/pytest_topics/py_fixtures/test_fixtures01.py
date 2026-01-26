import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixtures.. \n")
    city = ["New York", "London", "Riyadh", "Singapore", "Mumbai"]
    return city


def test_get_item(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == "New York"
    assert setup_list[::2] == ["New York", "Riyadh", "Mumbai"]


def my_reverse(lst):
    lst.reverse()
    return lst


def test_reverse_list(setup_list):
    assert setup_list[::-2] == ["Mumbai", "Riyadh", "New York"]
    assert setup_list[::-1] == my_reverse(setup_list)


@pytest.mark.xfail(reason="known issue: when we use 'usefixtures' annotation, we can Not access the return of the fixture method")
@pytest.mark.usefixtures("setup_list")
def test_use_fixture_demo():
    assert (setup_list[0] == "New York")
