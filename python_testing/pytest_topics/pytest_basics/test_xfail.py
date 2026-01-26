import pytest
import sys

def test_strjoin():
    s1 = 'Python,Pytest and Automation'
    l1= ['Python,Pytest', 'and', 'Automation']
    l2= ['Python', 'Pytest and Automation']
    assert  ' '.join(l1) == s1

# we expect this test function to fail, with this marker it will not throw an error
# XFAIL will only apply if the raised error is index error
@pytest.mark.xfail(raises=IndexError ,reason="idx out of range")
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]


@pytest.mark.xfail
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'


@pytest.mark.xfail
def test_str06():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[10]


# if the OS is linux (or any other non-windows) it will not use xfail marker, and it will throw an error, since the idx is out of range
@pytest.mark.xfail(sys.platform == 'win32', reason="should only work in linux OS")
def test_str07():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]