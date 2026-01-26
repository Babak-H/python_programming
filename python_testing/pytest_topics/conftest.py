import pytest, os

"""
    Reading commandline arguments from user when executing the test
"""

QA_CONFIG = "qa.prop"
PROD_CONFIG = "prod.prop"

# this method's name should be exactly "pytest_addoption"
def pytest_addoption(parser):
    parser.addoption("--cmdopt", default="QA")


@pytest.fixture
def cmd_opts(pytestconfig):
    print("\n In cmd_opt fixture function")
    opt = pytestconfig.getoption("cmdopt")
    if opt == "QA":
        # this way when code is executing, it will read the dir address of the 'conftest.py' file and not where the test itself is executing from
        f = open(os.path.join(os.path.dirname(__file__), QA_CONFIG), "r")
    elif opt == "PROD":
        f = open(os.path.join(os.path.dirname(__file__), PROD_CONFIG), "r")
    yield f
