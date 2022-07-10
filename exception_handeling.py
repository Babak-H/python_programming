# all errors : https://www.tutorialspoint.com/python/python_exceptions.html

try:
    f = open('./Files/xxx.txt')
    # raise custom exception
    if f.name == "./Files/xxx.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:  # Exception covers every error
    print("XXX error")
else:  # else clause only runs when we have NO exception
    print(f.read())  # this can also be inside the try block
    f.close()
# finally caluse always runs
finally:
    print("Final execution")

# Try - except - finally
while True:
    try:  # try to do this. if something goes wrong do the except.
        number = int(input("what is your favorite number? \n"))
        print(18 / number)
        break  # when it breaks it means it ends the while loop.
    except ValueError:
        print("only enter a number!")
    except ZeroDivisionError:
        print("don't enter zero.")
    except:  # this response to any kind of error.
        break
    # the code inside finally will be shown no matter what. (even after the break)
    finally:
        print("loop complete.")

# Catch multiple exceptions in one line (except block)
except (IDontLikeYouException, YouAreBeingMeanException) as e:
    pass

# How to properly assert that an exception gets raised in pytest?
import pytest

def test_passes():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0

def test_passes_without_info():
    with pytest.raises(Exception):
        x = 1 / 0

def test_fails():
    with pytest.raises(Exception) as e_info:
        x = 1 / 1

def test_fails_without_info():
    with pytest.raises(Exception):
        x = 1 / 1

# assert
'''
What is the use of “assert” in Python?
The assert statement exists in almost every programming language. It helps detect problems early in your program, 
where the cause is clear, rather than later as a side-effect of some other operation.
if not condition: raise AssertionError()
assert True # nothing happens
'''
assert False  # AssertionError
assert 2 == 2  # nothing happens

# Don't do this. Assertions are caught as exceptions.
def test_passes_but_should_not():
    try:
        x = 1 / 1
        assert False
    except Exception:
        assert True

# Even if the appropriate exception is caught, it is bad style,
# because the test result is less informative
# than it would be with pytest.raises(e)
# (it just says pass or fail.)
def test_passes_but_bad_style():
    try:
        x = 1 / 0
        assert False
    except ZeroDivisionError:
        assert True

def test_fails_but_bad_style():
    try:
        x = 1 / 1
        assert False
    except ZeroDivisionError:
        assert True


# How to make a variable inside a try/except block public?
text = 'something'  # define it before the try-except or in else block
try:
    url = "http://www.google.com"
    page = urllib.request.urlopen(url)
    text = page.read().decode('utf8')
except (ValueError, RuntimeError, TypeError, NameError):
    print("Unable to process your request dude!!")
print(text)



