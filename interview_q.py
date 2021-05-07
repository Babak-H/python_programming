# Frequency Counter (inside an String)
from collections import Counter

def freq_counter_a(s) -> str:
    """function that finds most frequent letters, then joins it together in most common order and
    returns it as string"""
    try:
        # I assume that we are interested in characters, regardless of the capitalization
        s = s.lower()
        # sort s string based on repetition of each value from least repeated to most
        return ''.join(sorted(s, key=lambda c: s.count(c), reverse=True)).replace(" ", "")
    except (AttributeError, TypeError) as e:
        print(e)


def freq_counter_b(s) -> str:
    """function that finds most frequent letters, returns them by most common order, without repetition"""
    try:
        s = s.lower()
        counter = Counter(s)
        return ''.join(char for char, freq in counter.most_common()).replace(" ", "")
    except (AttributeError, TypeError) as e:
        print(e)




####################### tests for the two functions above ##########################
import pytest
from frequency_counter import *


@pytest.mark.parametrize('inp, res', [
    ("a bb ccc", "cccbba"),
    ("hh b zzz 454", "zzzhh44b5"),
    ("11 222 5", "222115"),
    ("!!!!!####$$$$$$$%%%%&&*(*)*()", "$$$$$$$!!!!!####%%%%***&&()()")
])
def test_counter_freq_a_is_correct(inp, res):
    assert freq_counter_a(inp) == res


@pytest.mark.parametrize('inp, res', [
    ("a bb ccc", "cba"),
    ("hh b zzz 454", "zh4b5"),
    ("11 222 5", "215"),
    ("!!!!!####$$$$$$$%%%%&&*(*)*()", "$!#%*&()")
])
def test_counter_freq_b_is_correct(inp, res):
    assert freq_counter_b(inp) == res


@pytest.mark.parametrize('inp, res', [
    ("Happy HH", "HHHaypp"),
    ("BaBak", "bbaak"),
    (" 33 8 0", "3380   ")
])
def test_counter_freq_a_is_wrong(inp, res):
    assert freq_counter_a(inp) != res


@pytest.mark.parametrize('inp, res', [
    ("a bb ccc", "cccbba"),
    ("x y z ", "xyz   "),
])
def test_counter_freq_b_is_wrong(inp, res):
    assert freq_counter_b(inp) != res


def test_counter_freq_a_handle_exception():
    assert freq_counter_a(12345) is None


def test_counter_freq_b_handle_exception():
    assert freq_counter_b(45632) is None


# testing to make sure it does raise an exception
def test_counter_freq_a_raise_exception():
    with pytest.raises(TypeError) as e:
        freq_counter_a(12123123 + "453453")


def test_counter_freq_b_raise_exception():
    with pytest.raises(TypeError) as e:
        freq_counter_b(879787 + "-=65756")


'''
*** What is Python?
Python is a programming language with objects, modules, threads, exceptions, and automatic memory management. The
benefits of pythons are that it is simple and easy, portable, extensible, build-in data structure, and it is open-source.


*** What is PEP8?
PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.


*** What is pickling and unpickling?
Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using 
dump function. This process is called pickling. While the process of retrieving original Python objects from the stored 
string representation is called unpickling.


*** How is Python interpreted?
Python language is an interpreted language. Python program runs directly from the source code. It converts the source code
that is written by the programmer into an intermediate language, which is again translated into machine language that 
has to be executed.


*** How is memory managed in python?
Python memory is managed by Python private heap space. All Python objects and data structures are located in a private 
heap. The programmer does not have an access to this private heap, and the interpreter takes care of this Python private 
heap.
The allocation of Python heap space for Python objects is done by the Python memory manager. The core API gives access to
some tools for the programmer to code.
Python also has an inbuilt garbage collector, which recycles all the unused memory and frees the memory and makes it 
available to the heap space.


*** How are arguments passed by value or by reference?
Everything in Python is an object, and all variables hold references to the objects. The reference values are according to the functions. 
Therefore, you cannot change the value of the references. However, you can change the objects if it is mutable.


*** Explain namespace in Python
In Python, every name introduced has a place where it lives and can be hooked for. This is known as a namespace. It is like a box where a 
variable name is mapped to the object placed. Whenever the variable is searched out, this box will be searched to get the corresponding 
object.
local => enclosed => global => built-in


*** Python Scopes?
- local scope refers to the local objects available in the current function.
- global scope refers to the objects available throught the code execution since their inception.
- module-level scope refers to the global objects of the current module accessible in the program.
- outermost scope refers to all the built-in names callable in the program. The objects in this scope are searched last to find the 
name referenced.


*** In Python what are iterators?
In Python, iterators are used to iterate a group of elements, containers like a list.


*** What is docstring in Python?
A Python documentation string is known as docstring, it is a way of documenting Python functions, modules, and classes.


*** What is negative index in Python?
Python sequences can be index in positive and negative numbers. For positive index, 0 is the first index, 1 is the second index, 
and so forth. For the negative index, (-1) is the last index, and (-2) is the second last index, and so forth.


*** What is module and package in Python?
In Python, module is the way to structure a program. Each Python program file is a module, which imports other modules like objects 
and attributes.
The folder of Python program is a package of modules. A package can have modules or subfolders.


*** Enumerate
use a for loop over a collection

Months = ["Jan","Feb","Mar","April","May","June"]
for i, m in enumerate (Months):
        print(i,m)


*** Explain membership operators with example?
These operators test for membership in a sequence such as lists, strings, or tuples. Two membership operators are used in Python. 
(in, not in). It gives the result based on the variable present in a specified sequence or string.

x = 4
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")


*** Explain arrays in Pythons with example?
A Python Array is a collection of a common type of data structures having elements with the same data type. It is used to store collections 
of data. In Python programming, arrays are handled by the "array" module. If you create arrays using the array module, elements of the 
array must be of the same numeric type.

import array as myarray
abc = myarray.array('d', [2.5, 4.9, 6.7])
balance = array.array('i', [300,200,100])
print(abc[0])


*** What are the common examples of exceptions in Python?
- Division by Zero
- Accessing a file that does not exist.
- Addition of two incompatible types
- Trying to access a nonexistent index of a sequence
- Removing the table from the disconnected database server.


*** Dictionary Comprehension ?
my_list = [2, 3, 5, 7, 11]
squared_dict = {x : x**2 for x in my_list} 

my_list = [2, 3, 5, 7, 11]
squared_dict = {x : x**2 for x in my_list if x%2 != 0} 


*** Flatten multi-dimensional list?
my_list = [[10,20,30],[40,50,60],[70,80,90]]

flattened = [x for temp in my_list for x in temp]
# output => [10, 20, 30, 40, 50, 60, 70, 80, 90]


*** Python Package vs Module?
Modules, in general, are simply Python files with a .py extension and can have a set of functions, classes or variables defined and 
implemented. They can be imported and initialized once using the import statement. If partial functionality is needed, import the 
requisite classes or functions using from foo import bar.

Packages allow for hierarchial structuring of the module namespace using dot notation. As, modules help avoid clashes between global 
variable names, in a similary manner, packages help avoid clashes between module names.


*** What is self in Python?
Self is a keyword in Python used to define an instance or an object of a class. In Python, it is explicity used as the first paramter, 
unlike in Java where it is optional. It helps in disinguishing between the methods and attributes of a class from its local variables.


*** Python Break, Continue, Pass?
break => The break statement terminates the loop immediately and the control flows to the statement after the body of the loop.

continue => The continue statement terminates the current iteration of the statement,skips the rest of the code in the current 
iteration and the control flows to the next iteration of the loop.

pass => pass keyword in Python is generally used to fill-up empty block


*** help() and dir() ?
help => help() function in Python is used to display the documentation of modules, classes, functions, keywords, etc. If no parameter is 
passed to the help() function, then an interactive help utility is launched on the console.

dir => dir() function tries to return a valid list of attributes and methods of the object it is called upon. It behaves differently 
with different objects, as it aims to produce the most relevant data, rather than the complete information.


*** .py vs .pyc ?
.py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program. We get bytecode after 
compilation of .py file (source code). .pyc files are not created for all the files that you run. 
It is only created for the files that you import.


Decorators 
tuples
map
lambda
copy
class, inheritance
generators
iterators
*arg **kwarg
'''