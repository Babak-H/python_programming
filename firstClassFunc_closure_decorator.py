# First Class function

# square is a first class function becuase it can be passed as a variable or to other functions


from functools import wraps
import logging


def square(x):
    return x*x


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
        print('log:', msg)

    return log_message  # we return it as variable


print(logger('Hi'))
# here we set the log_hi variable to be a function equal to log_message()
log_hi = logger("Hi")
log_hi()  # execute the inner function


# another example of return first class function as output
def html_tag(tag):
    def wrap_text(msg):
        print(tag, msg)

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test headline')

# here we set print_p as a function equal to wrap_text()
print_p = html_tag('p')
print_p('Test paragraph')  # here we execute it with an argument


# Closure
'''
if function A is required only by function B, should A be defined inside B?
def method_a(arg):
    some_data = method_b(arg)

def method_b(arg):
    return some_data

In programming languages, a closure, also lexical closure or function closure,
is a technique for implementing lexically scoped name binding in a language 
with first-class functions. Operationally, a closure is a record storing a function.
'''


def sum(x, y):
    # closure
    def do_it():
        return x + y

    return do_it()


a = sum(1, 3)

print(a)
print(a())


def outer_func():
    message = 'Hi'  # this is called free variable, we can acess it from inner function

    def inner_func():
        print(message)

    return inner_func


my_func = outer_func()
print(my_func)

my_func()


def outer_func1(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func1('Hi')
bye_func = outer_func1('Bye')

hi_func()
bye_func()

#==================
# feed another function as an argument
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger1(func):
    def log_func(*args):
        logging.info("running '{}' with arguments '{}'".format(
            func.__name__, args))
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger1(add)  # initialize outer function
sub_logger = logger1(sub)
print(add_logger)

add_logger(3, 3)  # run the inner function
sub_logger(5, 2)


# ============================================
# Decorators

'''
Decorators, in the general sense, are functions or classes that wrap around another 
object, that extend, or decorate the object. The decorator supports the same interface 
as the wrapped function or object, so the receiver doesn't even know the object has been decorated.

A closure is an anonymous function that refers to its parameters or other variables outside its scope.

So basically, decorators use closure
'''

# we give *args, **kwargs argument to the wrapper function so we will be able to add arguments
# without raising errors


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed before', original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()

'''
@decorator_function 

# the line above is same as two lines below

decorated_display = decorator_function(display)
decorated_display()
'''


@decorator_function
def show():
    print("show something executed")


show()


@decorator_function
def display_info(name, age):
    print(name, age)


# the two arguments will be fed to wrapper function, first we execute decorator func then wrapper will execute this
# func with same arguments
display_info("bob", 28)

# ====================
# Decorator Class
# decorator class can wrap itself around a function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('wrapper executed before', self.original_function.__name__)
        return self.original_function(*args, **kwargs)


@decorator_class
def display_inf(name, age):
    print(name, age)

display_inf("bob", 27)


# ===========================
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=orig_func.__name__+'.log', level=logging.INFO)

    # since we want to use decorators in a chain we wrap the inner function 
    # inside a @wraps() function so it will preserve the original function
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("running '{}' with arguments '{}'".format(
            orig_func.__name__, args))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_inf1(name, age):
    print(name, age)

display_inf1("bob", 27)



def my_timer(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(t2, " seconds took")
        return result
    return wrapper

@my_timer 
def display_inf2(name, age):
    print(name, age)
    
display_inf2("bob", 27)

# =============================
# function with two decorators

'''
Here how it works when you stack two decorators together
display_variable = my_logger(my_timer(display_inf))
display_variable("Bob", 27)

so basically it chains the decorators together from top to bottom

since we want to use decorators in a chain we wrap the inner function
inside a @wraps() function so it will preserve the original function
'''

@my_logger
@my_timer
def display_inf3(name, age):
    print(name, age)

display_inf3("Alex", 27)

# =========================
# decorator functions that take in arguments (similar to Flask router decorator)

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'wrapper executed before', original_function.__name__)
            return original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function

@prefix_decorator("/about")
def display1(name, age):
    print(name, age)
    
display1("bob", 27)

