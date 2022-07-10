# function that does nothing!!
def hello_func():
    pass

def hello_function():
    return "Hello"

print(hello_function())

# argument name has a default value (keyword argument)
# argument with default value should come after normal arguments (positional argument)
def func(greeting, name='Bob'):
    return '{}, {}'.format(greeting, name)

print(func('hi', 'Corey'))

# *args = you can send as many arguments to the function, we don't know how many
# **kwargs = you can send list as arg and dictionaries as kwarg
def student_info(*args, **kwargs):
    print(args)  # positional arguments
    print(kwargs)  # keyword argument

student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'john', 'age': 22}
# putting * behind list and ** behind dictionary will unpack them to become arguments of the function
student_info(*courses, **info)

# Mutable Default function Argument problem
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

# in above function we give an empty (mutable) object when the argument is empty, but here we see when
# we use it several times, instead of creating new lists, it adds to the same list
# this problem arises in lists because they are mutable, strings don't have such problems

print(add_employee.__defaults__)  # ([],) each time it will add it to this default empty list
add_employee('Corey')
add_employee('John')
add_employee('Jane')

# you can see that all the values are added to default list and list is no longer empty
print(add_employee.__defaults__)

def add_employee_fixed(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

print(add_employee_fixed.__defaults__)
add_employee_fixed('Corey')
add_employee_fixed('John')
# you can see when we set it to None it doesn't change its value after being called
print(add_employee_fixed.__defaults__)




class Geeks:
    def __init__(self, name1="Bob", num2=26, name3="Gohardani"):
        self.name1 = name1
        self.num2 = num2
        self.name3 = name3
'''
vars : It takes an object as a parameter which can be a module, a class, an instance, or any object having  __dict__ 
attribute.
The method returns the __dict__ attribute for a module, class, instance, or any other object if the same 
has a __dict__ attribute. If the object fails to match the attribute, it raises a TypeError exception.'''
GeeksforGeeks = Geeks()
print(vars(GeeksforGeeks))

# Function Annotations
# without annotation
def foo(prefix, suffix):
    return prefix + " " + suffix

result = foo("foo", "bar")
print(result)

# with annotation
# annotations are the doc / info that gives information about the function and its variables
def foo(prefix: "The first word", suffix: "The last word") -> "the two words with and between them":
    return prefix + " and " + suffix

result = foo("foo", "bar")
print(result)
print(help(foo))
print(foo.__annotations__)

# Mutable Default function Argument problem
import time
from datetime import datetime

def display_time(time_to_print = datetime.now()):
    print(time_to_print.strftime("%b %d, %Y %H:%M:%S"))

# as it can be seen here instead of generating new timestamp each time, the function uses first default assigned value
# for all the function calls!
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

def display_time_fixed(time_to_print=None):
    if time_to_print is None:
        time_to_print = datetime.now()
    print(time_to_print.strftime("%b %d, %Y %H:%M:%S"))

display_time_fixed()
time.sleep(1)
display_time_fixed()