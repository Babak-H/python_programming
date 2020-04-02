# Functions

# function that does nothing!!

def hello_func():
    pass

def hello_function():
    return "Hello"

print(hello_function())

# argument name has a default value (keyword argument)
# argument with default value should come after normal arguments (positional argument)

def func(greeting, name='Bob'):
    return f'{greeting} {name}'.format()

print(func("hi", "Corey"))

# *args = you can send as many arguments to the function, we don't know how many
# you can send list as arg and dictionaries as kwarg

def student_info(*args, **kwargs):
    print(args) # positional arguments
    print(kwargs) # keyword arguments


student_info('Math', 'Art', name='John', age=22)

# another way
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
# putting * behind list and ** behind dictionary will unpack them to become arguments of the function
student_info(*courses, **info)

# ========================
# Mutable Default function Argument problem

def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

'''
in above function we give an empty (mutable) object when the argument is empty, but here we see when
we use it several times, instead of creating new lists, it adds to the same list
this problem arises in lists because they are mutable, strings don't have such problems
'''

print(add_employee.__defaults__)  # ([],) each time it will add it to this default empty list

add_employee('Corey')
add_employee('John')
add_employee('Jane')
print(add_employee.__defaults__)  # all the values are added to default list and list is no longer empty


def add_employee_fixed(emp, emp_list=None):
    if emp_list is None:
        emp_list = []

    emp_list.append(emp)
    print(emp_list)

print(add_employee_fixed.__defaults__)

add_employee_fixed('Corey')
add_employee_fixed('John')

print(add_employee_fixed.__defaults__)  # when we set it to None it doesnt change its value after being called


# Mutable Default function Argument problem
import time
from datetime import datetime

def display_time(time_to_print=datetime.now()):
    print(time_to_print.strftime("%b %d, %Y %H:%M:%S"))

# instead of generating new timestamp each time, the function uses first default assigned 
# value for all.
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()


def display_time_fixed(time_to_print=None):
    if time_to_print == None:
        time_to_print = datetime.now()
    print(time_to_print.strftime("%b %d, %Y:%H:%M:%S"))

display_time_fixed()
time.sleep(1)
display_time_fixed()

'''
a mutable object can change its state or contents and immutable objects can't
mutable: list, dict, set, byte array
immutable: int, float, complex, string, tuple, frozenset  [note: immutable version of set], bytes
'''
# ========================
# it takes an object as a parameter which can be a module, a class, an instance or any object that has __dict__ attribute
class Geeks:
    def __init__(self, name1= "Bob", num2= 26, name3 = "Gohardani"):
        self.name1 = name1
        self.num2 = num2
        self.name3 = name3


GeeksforGeeks = Geeks()
print(vars(GeeksforGeeks))  # {'name1': 'Bob', 'num2': 26, 'name3': 'Gohardani'}

# ========================
# Function Annotation

# without annotation
def foo(prefix, suffix):
    return prefix + " " + suffix

result = foo("foo", "bar")
print(result)

# with annotation
# annotations are the doc/info that gives information about the function and its variables

def foo_ann(prefix: "the first word", suffix: "the last word") -> "the two words with and between them":
    return prefix + " and " + suffix

print(foo_ann("foo", "bar"))
print(help(foo_ann))
print(foo_ann.__annotations__)

# ========================

'''
whenever python runs a file, it first sets a few special variables, and one of those variables is __name__ and it
sets it to __main__, but if we import this module (file) in other file, it will be different.

therefore, we can use this idea to check if we are running it directly or running it by importing in another module
'''

def main():
    print("running directly")

if __name__ = "__main__":
    main()
else:
    print("running from import")



















