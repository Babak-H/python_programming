"""
share fixtures across multiple tests.
can have single conftest.py in centralized directory for all tests to access the fixture
also, can have other conftest.py files in subdirectories (used locally only)

Fixture Scope
fixtures are created when first requested by a test, and are destroyed based on their scope:

function => default scope, fixture is destroyed at the end of test function
class => fixture is destroyed during teardown of the last test in the class
module => fixture is destroyed during teardown of the last test in the module
package => fixture is destroyed during teardown of the last test in the package
session => fixture is destroyed at the end of the test session
"""
import pytest


# this function is for initializing the variables that we use in several test methods
def pytest_configure():
    pytest.weekdays1 = ["mon", "tue", "wed"]
    pytest.weekdays2 = ["fri", "sat", "sun"]


@pytest.fixture(scope="module")
def setup01():
    # IDE might show an error related to the 'pytest.weekdays1', but it is actually fine
    wk1 = pytest.weekdays1.copy()
    wk1.append('thurs')
    yield wk1
    wk1.pop()


@pytest.fixture(scope="module")
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thurs")
    yield wk2


# "request" here refers to the test module (file) that is calling this fixture func
@pytest.fixture()
def setup04(request):
    months = getattr(request.module, "months")
    print("\n in Fixture setup04")
    print("\n Fixture scope: " + str(request.scope))
    print("\n Calling function: " + str(request.function.__name__))
    print("\n Calling module: " + str(request.module.__name__))
    months.append("April")
    yield months


@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == 'list':
            return [1, 2, 3]
        elif name == 'tuple':
            return (1, 3, 4)
    # here we return the reference to the function itself, it is a 'first class function'
    return get_structure

