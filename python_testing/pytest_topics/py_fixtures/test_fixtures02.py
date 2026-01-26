import os
import pytest

weekdays1 = ["mon", "tue", "wed"]
weekdays2 = ["fri", "sat", "sun"]
filename = 'file1.txt'

@pytest.fixture()
def setup01():
    print("\n SetUp: before yield setup01 fixture")
    wk1 = weekdays1.copy()
    wk1.append('thurs')
    # we run the test function at this moment
    yield wk1
    print("\n TearDown: after yield setup01 fixture")
    wk1.pop()


@pytest.fixture()
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0, "thurs")
    yield wk2
    # we are Not required to do tear down after setting up variables


@pytest.fixture()
def setup03():
    # set up the file before test
    with open(filename, 'w') as f:
        f.write("Pytest is good")
    with open(filename, 'r+') as f:
        # this is when the test function is called
        yield f
    # tear down the file after test
    os.remove(filename)


def test_extended_list(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ["mon", "tue", "wed", "thurs", "fri", "sat", "sun"]


def test_len(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)


def test_file_read(setup03):
    assert (setup03.readline() == "Pytest is good")