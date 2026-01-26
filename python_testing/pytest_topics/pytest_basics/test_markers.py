import pytest

# we can also set markers for the whole module or class
pytestmark = [pytest.mark.smoke, pytest.mark.strtest]

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'pytest automation'
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'


@pytest.mark.sanity
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26


def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]


@pytest.mark.str
@pytest.mark.sanity
def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[10:] == 'klmnopqrstuvwxyz'
    assert letters [-3:] == 'xyz'


def test_strsplit():
    s1 = 'Python,Pytest and Automation'
    assert s1.split() == ['Python,Pytest', 'and', 'Automation']
    assert s1.split(',') == ['Python', 'Pytest and Automation']


@pytest.mark.str
def test_strjoin():
    pass

# pytest -m sanity
# pytest -m str
# pytest -v -m "sanity and not str"
# pytest -v -m "sanity and not str" .\test_markers.py
# pytest -v -m "sanity and str"
# pytest -v -m "sanity or str"
# pytest -v -m "smoke"

# Passed (.) : the test ran successfully
# Failed (F) : the test did Not run successfully
# Skipped (s) : the test was skipped
# XFail (x) : the test was not supposed to pass, ran and failed (good outcome)
# XPass (X) : the test was not supposed to pass, ran and passed (bad outcome)
# Error (E) : an Exception happened outside the test function

# fixtures : functions that are run by pytest before or after the actual test function (setup db connection, initialize webdriver,..)