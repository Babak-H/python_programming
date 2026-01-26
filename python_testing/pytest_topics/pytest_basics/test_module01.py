# naming conventions: test_<module_name>.py

# naming conventions: def test_something():
# each test should only have one assert
def test_a1():
    assert 5 + 5 == 10


def test_a2():
    assert 5 * 5 == 25


# def test_a3():
#     assert 9/5 == 1.5, "failed test intentionally"


def test_a4():
    assert 9//5 == 1


def test_a5():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


# venv\scripts\activate

# pytest test_module01.py
# pytest
# pytest --cache-show

# By default, pytest captures standard-output while running tests. Only if a test fails, the captured output is shown.
# We can use -s option, toprint to stdout or to console in all cases:
# pytest -s test_module01.py
# verbose mode:
# pytest -v test_module01.py
# run a single class:
# pytest -v pytest_topics\test_module2.py::TestMyStuff
# run specific method:
# pytest -v pytest_topics\test_module2.py::TestMyStuff::test_strs

# either in module name or package name or testcase name we should have 'py_assertions':
# pytest -v -k "py_assertions"

# will only show the matched testcases, without executing them
# pytest -v -k "py_assertions" --collect-only

# will not show any tracebacks for errors:
# pytest -v -k "py_assertions" --tb=no

# # either in module name or package name or testcase name we should have 'case' or 'str'
# pytest -v -k "case or str" --tb=no

# will stop at the first FAILED testcase
# pytest -v -k "module" --tb=no -x

# will stop after 2 FAILED testcase
# pytest -v -k "module" --tb=no --maxfail=2

# quiet mode, will not show which exact testcase passed or failed
# pytest -v -k "module" --tb=no -q