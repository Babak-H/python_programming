import logging

# square is a first class function because it can be passed as a 'variable' or to other functions
def square(x):
    return x * x

# assign function to variable
f = square
print(f)
print(f(5))

# map() is an example of higher-order function, since it accepts another function as input
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

# return a first class function as output of higher order function
def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message   # we return it as variable

print(logger('Hi!'))
log_hi = logger('Hi!')  # here we set the log_hi variable to be a function equal to log_message()
log_hi()  # here we execute it

# another example of return first class function as output from higher order function
def html_tag(tag):
    def wrap_text(msg):
        print(tag, msg)
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline')

print_p = html_tag('p')  # here we set print_p as a function equal to wrap_text()
print_p('Test paragraph')  # here we execute it with an argument

# Closure
'''
If function A is required only by function B should A be defined inside B?

def method_a(arg):
    some_data = method_b(arg)

def method_b(arg):
    return some_data

** In programming languages, a closure, (also lexical closure or function closure), is a technique for implementing 
lexically scoped name binding in a language with first-class functions. Operationally, a closure is a record storing 
a function
'''
def _sum(x, y):
    # closure
    def do_it():
        return x + y
    return do_it

a = _sum(1, 3)
print(a)
print(a())

def outer_func():
    message = 'Hi'  # this is called free variable, we can access it from inner function
    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()
print(my_func)
my_func()

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
by_func = outer_func('Bye')

hi_func()
by_func()

logging.basicConfig(filename='example.log', level=logging.INFO)

# get another function as an input
def logger(func):
    # gets argument related to that function
    def log_func(*args):
        logging.info("running '{}' with arguments '{}'".format(func.__name__, args))
        # run input function with input arguments
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)  # initialize outer function
sub_logger = logger(sub)
print(add_logger)

add_logger(3, 3)  # run the inner function
sub_logger(5, 2)

# Decorator
"""
Decorators, in the general sense, are functions or classes that wrap around another object, that extend, or decorate 
the object. The decorator supports the same interface as the wrapped function or object, so the receiver doesn't even 
know the object has been decorated.
A closure is an anonymous function that refers to its parameters or other variables outside its scope.
So basically, decorators uses closures.
"""

# we give *args, **kwargs argument to the decorator function, so we will be able to add arguments to wrapper function
# without raising errors
from functools import wraps


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed before', original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
print(decorated_display)
decorated_display()

'''
@decorator_function 

# the line above is same as two lines below
decorated_display = decorator_function(display)
decorated_display()
'''
# this @funcName will feed the below function to another function and that one will execute this
@decorator_function
def show():
    print("show something executed")

show()

@decorator_function
def display_info(name, age):
    print(name, age)

display_info("bob", 27)

# decorator class, this way we can easily check the arguments before feeding them to the function
class decorator_class(object):
    # get the method
    def __init__(self, original_function):
        self.original_function = original_function

    # get its arguments and run it with the args
    def __call__(self, *args, **kwargs):
        print('wrapper executed before', self.original_function.__name__)
        return self.original_function(*args, **kwargs)

@decorator_class
def display_inf(name, age):
    print(name, age)

display_inf("bob", 27)

def my_logger(orig_func):
    # import it inside the function, since we only need it here
    import logging
    logging.basicConfig(filename=orig_func.__name__+'.log', level=logging.INFO)

    @wraps(orig_func)  # @wraps does the work pf __inti__ and __call__ methods
    def wrapper(*args, **kwargs):
        logging.info("running '{}' with arguments '{}'".format(orig_func.__name__, args))
        return orig_func(*args, **kwargs)
    return wrapper

@my_logger
def display_inf(name, age):
    print(name, age)

display_inf("bob", 27)


def my_timer(orig_func):
    import time
    # we wrap this inside a logger, because we want to feed this decorator method, to another decorator later
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(t2, " seconds took")
        return result
    return wrapper


@my_timer
def display_inf(name, age):
    print(name, age)

display_inf("bob", 27)

# one function with two decorators
'''
Here how it works when you stack two decorators together:
        display_variable = my_logger(my_timer(display_inf))
        display_variable("Bob", 27)
so basically it chains the decorators together from top to bottom, since we want to use decorators in a chain we wrap 
the inner function inside a @wraps() function so it will preserve the original function
'''

@my_logger
@my_timer
def display_inf(name, age):
    print(name, age)

display_inf("Alex", 27)


# python @abstractmethod decorator
'''
You can apply the @abstractmethod decorator to methods such as draw() that must be implemented; Python will then raise 
an exception for classes that don’t define the method. Note that the exception is only raised when you actually try to 
create an instance of a subclass lacking the method.
'''
import abc

class AbstractClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abstractMethod(self):
        return

class ConcreteClass(AbstractClass):
    def __init__(self):
        self.me = "me"

# Will get a TypeError without the following two lines:
#   def abstractMethod(self):
#       return 0
c = ConcreteClass()
c.abstractMethod()

'''
If abstractMethod is not defined for ConcreteClass, the following exception will be raised when running the above code: 
   TypeError: Can't instantiate abstract class ConcreteClass with abstract methods abstractMethod
'''


