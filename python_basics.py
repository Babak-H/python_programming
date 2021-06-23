###################### STRING AND TEXT DATA ######################
def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = "babak"
    last_name = "G"
    print_full_name(first_name, last_name)


# string split() and join() methods:
def split_and_join(line):
    a = line.split(" ")
    return "-".join(a)

line = "I like bbq"
result = split_and_join(line)
print(result)

# character methods
# .isalnum(), isalpha(), isdigit(), islower(), isupper()  : all return true or false
s = "Apple"
x = ["False", "False", "False", "False", "False"]

for i in range(len(s)):
    char = s[i]
    if char.isalnum() and x[0] == "False":
        x[0] = "True"

    if char.isalpha() and x[1] == "False":
        x[1] = "True"

    if char.isdigit() and x[2] == "False":
        x[2] = "True"

    if char.islower() and x[3] == "False":
        x[3] = "True"

    if char.isupper() and x[4] == "False":
        x[4] = "True"
     
for val in x:
    print(val)


# recieve an string and capitalize every word in it:
def solve(s):
    str_1 = ""
    l = s.split(" ")
    for word in l:
        str_1 += word.capitalize() + " "
    return str_1

s = "my name is babak"
result = solve(s)
print(result)


# sort all strings of a list based on their size
X = ["first", "Second", "Third"]
print(sorted(len(s) for s in X))
sorted_x = sorted(len(s) for s in X)
# print mode from the sorted list to find avg length of list
print(sorted_x[len(sorted_x) // 2]) # return middle value

l = [12, 14, 18, 28] # find mode
l = sorted(l)
mode = l[len(l) // 2]


# How to substring a string in Python?
x = "Hello World!"
x[2:]
# Get the last 4 characters of a string
mystr = "abcdefghijkl"
mystr[-4:]


# Splitting on delimiter in Python string
s = "a,b,c,d"
s.split(",")
# split only on last occurrence of ',' in string:
s.rsplit(',', 1)
# or
s.rpartition(',')

# split a word into a list
list("Word to Split")

# convert tuple to string
tup = ('a', 'b', 'c', 'd', 'g', 'x', 'r', 'e')
''.join(tup)

# How to sort the letters in a string alphabetically in Python
a = 'ZENOVW'
# sorted(a) ['E', 'N', 'O', 'V', 'W', 'Z']
print(''.join(sorted(a)))
b = '-'.join(sorted(a))
print(b.split('-'))

# replace a string in text with another string
str_0 = "hello world"
str_1 = str_0.replace('world', 'universe')
print(str_1)

# using .format() with strings
name = "Bob"
greeting = "Hello"

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)


import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    s = ""
    for word in word_list:
        s += word+"\n"
    return s

string, max_width = "hello", 6
result = wrap(string, max_width)
print(result)

###################### Numbers and numerical values ######################
import math

num = 3
num_1 = 3.14
print(type(num))
print(type(num_1))

print(3 * 2 + 1)
print(3 * (1 + 2))

# absolute value 
print(abs(-3))

# rounding number
print(round(3.14251, 2))

# if else statement with integers:
N = 25

if (N >= 1 or N <= 100):
    if (N % 2 != 0):
        print("strange")
    elif (N >=2 and N < 5):
        print("Not strange")
    elif(N >= 6 and N <= 20):
        print("strange")
    else:
        print("Not strange")


if __name__ == '__main__':
    a = 12
    b = 13

print(a + b)
print(a - b)
print(a * b)
print(a // b)  # floors to smaller int from float
print(float(a) / b)

# calculate leap year
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0):
        leap = True
    elif (year % 4 == 0 and year % 100 == 0 and year % 400 ==0):
        leap = True
    return leap

year = 2021
print(is_leap(year))

# Efficient way to convert string from split function to int in Python
test = '8743-12083-15'
lst_int = [int(x) for x in test.split("-")]

#  reverse an integer, and tell if palindrome (same number on both sides)
def palindrome(num):
    return str(num) == str(num)[::-1]

print(palindrome(121))


###################### List, Tuples, Sets, Dictionaries ######################
a = [1,2,3]
a+a

# How can I compare two ordered lists in python?
print([0,1,2] == [0,1,2])
print([0,1,2] == [0,2,1])

'''
in python you can't create an empty list and then assign a value by index to it.
j = []
j[0] = 1 this will return error

instead  => j.append(1)

How to clone or copy a list?
With "new_list = my_list", you don't actually have two lists. The assignment just copies the reference to
the list, not the actual list, so both new_list and my_list refer to the same list after the assignment
To actually copy the list, You can use the builtin list.copy() method (available since Python 3.3):
'''
old_l = [1,2,3]
new_l = old_l.copy()
# or
new_l = old_l[:]

# Difference between del, remove and pop on lists:
# 'remove' removes the first matching value, not a specific index
a = [0, 2, 3, 2]
a.remove(2)
print(a)

# del removes the item at a specific index
a = [3, 2, 2, 1]
del a[1]
print(a)

# and pop removes the item at a specific index and returns it
a = [4, 3, 5]
a.pop(1)

# negative index
x = [1,2,3,4]
print(x[-1]) # last element
print(x[-3]) # third element from last

# Append integer to beginning of list in Python
a = 5
li = [1, 2, 3]
[a] + li  # Don't use 'list' as variable name.

# How to randomly select an item from a list?
import random
foo = ["a", "b", "c", "d", "e"]
print(random.choice(foo))
# choose 3 random elements of list (can be repeated)
print(random.choices(foo, k=3))

# how to get an empty list of any size in python
a = [0] * 10
# or
a = [None] * 10

# find biggest / smallest string in the list
print(max(len(s) for s in X))
print(min(len(s) for s in X))

# list[start : end : step]
l = [1,2,3,4,6,5,7,12,9,8]  
l[1:-2:2] # from second to last 3rd element with step 2 (skip one element each time)
l[-1:1:-1]  # iterating from last to second (-1 means going back)

# from last to first
l[::-1]

lst = [1,2,3,4,5,5]

# from third to last
print(lst[2:]) 
# from third last element to last
print(lst[-3:]) 
# append to list (adds at end)
lst.append(6)
#inset to string (index, value)
lst.insert(0, 0)
# removes last value from list and return it
lst.pop()
print(lst)
# reverse the list (current list)
lst.reverse()
print(lst, "reversed")
print(lst[::-1])
# sort the list
lst.sort()
print(lst, "sorted")
# reverse-sort a list (biggest to smallest)
lst.sort(reverse=True)
print(lst, "reverse sorted")
# sort but not change the list
print(sorted([3,1,2]), "sort without changing the original")
# find (first) index of a value inside list
print(lst.index(5), " index of value")
#check if a value is inside a list:
print(7 in lst)
# add up all values inside an int list
numbers = [1, 2, 3]
sum(numbers)
# length of list
print(len(lst))

# check if all values in list are greater than a certain number
my_lst = [29, 500, 43]
all(i >= 300 for i in my_lst)

# List Unpacking
date, name, price = ['December 1', 'Bread gloves', 8.50]
print(date)
print(name)

# get average of all items in a list but drop the first and last one.
grades = [11, 44, 99, 88, 25]
def drop_first_last(grades):
    first, *middle, last = grades
    # sum(list) = adds all items in a list.
    # len(list) = gets the number of how many items in a list.
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last(grades)
drop_first_last([10, 5, 4, 7, 3])

# Getting the index of the returned max or min item using max()/min() on a list
values = [1,2,3,4]
if isMinLevel:
    return values.index(min(values))
else:
    return values.index(max(values))


# Convert list to tuple in Python
l = [4,5,6]
tuple(l)

# you can't add to tuple or remove from it when it is already created
tup = ('history', 'math', 'physics')

# Sort a list of tuples by 2nd item (integer value)
l = [('abc', 121),('abc', 231),('abc', 148), ('abc',221)]
'''
Try using the "key" keyword with sorted()
key should be a function that identifies how to retrieve the comparable element from your data structure. 
In your case, it is the second element of the tuple, so we access [1]
'''
sorted(l, key=lambda x: x[1])

# set : sets are used for membership testing and eliminating duplicate entries.
print(set('HackerRanks'))  # {'R', 's', 'n', 'H', 'a', 'c', 'r', 'e', 'k'}
print(set([1,1,4,5,12,1,6,6])) 
# dictionary to set
print(set({'Hacker' : 'DOSHI', 'Rank' : 616 }))

def averge(array):
    return sum(set(array)) / len(set(array))

s1 = {1,2,3,4,5}
s1.add(6)
s1.update([6,7,8])
print(s1)

# remove() and discard() both delete from set, but discard won't throw an error even when the value doesnt exist in the set
s1.remove(6)
s1.discard(7)
print(s1)

# there is no order for values in sets, so each time you run it, it will show new values
courses = {'one', 'two', 'three'}
# sets are optimized for membership sharing
print('one' in courses)
courses_2 = {'four', 'five', 'three'}

print(courses.intersection(courses_2), "similarity of sets")
print(courses.difference(courses_2), "differences of sets")
print(courses.union(courses_2), "mix two sets")

# generate empty list
empty_list = []
empty_list_2 = list()
# generate empty tuple
empty_tuple = ()
empty_tuple_2 = tuple()
# generate empty set
empty_set = set()


# create dictionary
student = {'name':'John', 'age':25, 'courses':['Math','CompSci']}
# both methods return the value for key, but when using get() it wont return error if key doesnt exist
print(student['name'], student.get('name'))
# delete key value pair from the dictionary
del student['age']
# another way (throws error since already deleted)
student.pop('age')
# length of dictionary
print(len(student))
# keys
print(student.keys())
# values
print(student.values())

# Check if a given key already exists in a dictionary
# this is the intended way to test for the existence of a key in a dict.
d = dict()

for i in range(100):
    key = i % 10
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print(d)

# How do you find the first key in a dictionary?
my_dict = {'foo': 'bar', 'too':'char'}
next(iter(my_dict)) # only shows first key

# How do you create nested dict in Python?
d = {}
d['dict1'] = {}
d['dict1']['innerkey'] = 'value'
d[32] = 'red'  
print(d)

# How to get a random value in python dictionary
d = {'VENEZUELA':'CARACAS', 'CANADA':'OTTAWA'}
random.choice(list(d.keys()))

# iteration through dictionary in python 2 vs python 3
# python 2  :  dict.iteritems() , dict.iterkeys()
# python 3
d.items() , d.keys()

# Converting Python Dictionary to List (with inner list)
dict = {1:1, 2:2, 3:3}
dictlist = []

for key, value in dict.items():
    temp = [key, value]
    dictlist.append(temp)
print(dictlist)

# named tuple : named tuples are similar to dictionaries, but with easier syntaxt that needs less writing
from collections import namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)
print(color.red)
white = Color(255,255,255)
print(white.blue)


# Sorting List of Dictionaries 
# itemgetter  (esasier to use than lambda, but slower)
from operator import itemgetter

users = [
    {'name': 'Anthony', 'join_date': '2017-03-09', 'age': 29},
    {'name': 'Britney', 'join_date': '2019-05-11', 'age': 21},
    {'name': 'Ned',     'join_date': '2016-01-29', 'age': 35}
]

print(users.sort(key=itemgetter('join_date')))
print(users.sort(key=itemgetter('age'), reverse=True))

# MUTABLE : can change it => list, dict, set, byteArray
# IMMUTABLE : can't change it => int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes
# a mutable object can change its state or contents and immutable objects cannot.

a = 12
b = a
b = 14
print(a, b)

###################### Random Module ######################
# range
if __name__ == '__main__':
    n = 12
# n is NOT included in the range
for i in range(n):
    print(i * i)

# range
n = 6
for i in range(1, n+1):
    print(i, sep='', end='', flush=True)  # prints everything in one line

# How to Generate a Random Number in Python
import random

for x in range(5):
    print(random.randint(1, 101))

'''
range() and xrange()
You are trying to run a Python 2 codebase with Python 3. xrange() was renamed to range() in Python 3.

In python, what is the difference between random.uniform() and random.random()?
random.random() gives you a random floating point number in the range [0.0, 1.0) (so including 0.0, but not including 1.0 which is also known as a semi-open range). 
random.uniform(a, b) gives you a random floating point number in the range [a, b], (where rounding may end up giving you b).
'''
def uniform(self, a, b):
    "Get a random number in the range [a, b) or [a, b] depending on rounding."
    return a + (b-a) * self.random()  # self.random => between 0 and 1 (smaller than 1)

print(random.uniform(1, 10)) # returns random float in  a range
print(random.randint(1, 100)) # returns random integer in  a range
# this function returns value in range of [0, 1)
print(random.random())

# How do you slice a list (indefinite length) randomly into 3 subgroups
l = [105, 167, 262, 173, 123, 718, 219, 272, 13, 21]
# random.shuffle() changes order of list randomly
random.shuffle(l)
print(l)

# l[0::3] => 105, 173, 718, 21 => get position 0, jump 3 steps ahead and get that position, repeat until end of list
print(l[::3])
print(l[1::3])
print(l[2::3])

[l[x::3] for x in range(3)]  

###################### Conditionals if-elif-else ######################
# if else statement
# list commands : insert, remove, append, sort, pop, reverse
N = 10
a = []

for _ in range(N):
    line = "1374".split()
    if(len(line) == 1):
        command = line[0]
    elif(len(line) == 2):
        command = line[0]
        e = int(line[1])
    elif(len(line) == 3):
        command = line[0]
        i = int(line[1]) 
        e = int(line[2])   
    if command == 'insert':
        a.insert(i, e)
    elif command == 'print':
        print(a)
    elif command == 'remove':
        a.remove(e)
    elif command == 'append':
        a.append(e)
    elif command == 'sort':
        a = a.sort()
    elif command == 'pop' and len(a) != 0:
        a.pop()
    elif command == 'reverse':
        a = a.reverse()
    else:
        print("No idea!!")
        
## There is no switch-case statement in python!!
# use if-else instead

# and | or | not
user= "admin"
logged_in = True

if user == 'admin' and logged_in:
    print('admin page')
elif yser == 'admin' or logged_in:
    print('wrong page')
elif not logged_in:
    print('bad creds')
else:
    print('end')


# How to exit an if clause
# Wrap the code in its own function. Instead of break, use return
def some_function():
    if condition_a:
        # do something and return early
        return
    if condition_b:
        # do something else and return early
        return
    return
if outer_condition:
    some_function()

####### SameValue  VS  Same Object #######

a = [1,2,3]
b = [1,2,3]
print(a == b) # checks if both objects have same value => True

print(id(a))
print(id(b))
print(a is b) # checks if both objects are one in memory => False

####### assert #######
'''
What is the use of “assert” in Python?
The assert statement exists in almost every programming language. It helps detect problems early in your program, 
where the cause is clear, rather than later as a side-effect of some other operation.
if not condition: raise AssertionError()
assert True # nothing happens
'''
assert False  # AssertionError

###################### loops ######################
# loop over an string
for letter in 'Hello':
    print(letter)

# Skip first entry in for loop in python
cars = [1,2,3,4]
itercars = iter(cars)
next(itercars) # jump first element
for car in itercars:
    print(car)

# while loop
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

# Fibonaci sequence
a, b = 0, 1
for _ in range(0, 10):
    print(a)
    a,b = b, a+b

'''
The enumerate() function adds a counter to an iterable. So for each element in cursor, a tuple is 
produced with (counter, element). the for loop binds that to row_number and row, respectively.
'''
elements = ('foo', 'bar', 'baz')
for elem in elements:
    print(elem)

for count, elem in enumerate(elements):
    print(count, elem)

## else clause after loop
my_list = [1,2,3,4]

for i in my_list:
    print(i)
    if i == 6:
        break
else:
    print("this will be executed if we didnt have any breaks")
  

j = 0
while j < 5:
    print(j)
    j += 1
    if j == 3:
        break
else:
    print("this will be executed if we didnt have any breaks")

###################### Iterators and Iterables ######################

# Iterable: something that can be looped over, all iterables have the iter() method
# Iterators : know their next state (next value to loop over) and contain next() method.

nums = [1,2,3]
print(nums.__iter__())

# itering over the list gives us an Iterator, and it contains __next__() method
i_nums = iter(nums)
print(i_nums.__next__())
print(i_nums.__next__())
print(i_nums.__next__())

# a class that works same as built-in range function
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 5)
print(next(nums))

for num in nums:
    print(num)

# Exhausting Iterators : in python3 you need to cast zip object as list to see all its values at once
names = ['Peter parker', 'Clark kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']

identities = zip(names, heroes)
print(identities)
print(list(identities))

###################### Itertools ######################
# itertools helps with iterating through sets of data
from itertools import *
import itertools
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b= ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# chain() function : group multiple lists together
for i in chain(a, b, c):
    print(i)
    
print (list(chain(a,b,c)))
print (list(chain(a[:2], b[:2], c[1:3])))

counter = itertools.count()
print(next(counter))
print(next(counter))
print(next(counter))

from collections import Counter
c = Counter('gallad')
print(c) 
print(c['a'])

c = Counter(['a', 'b', 'a', 'c', 'c'])
print(c)
print(list(c.elements()))

c = Counter(dogs=3, cats=4)
print(c) 
c.most_common(1) 
c.most_common(2) 

# combinations : order of a combo does not matter, a,b = b,a
# permutation : order does matter, a,b != b,
letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ['Corey', 'Nicole']

results = itertools.combinations(letters, 2)
print(list(results))

results_1 = itertools.permutations(letters, 2)
print(list(results_1))

# zip() functions ties two lists together in a new list of tuples
first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)

for a, b in names:
    print(a, b)


data = [100, 200, 300]
daily_data = zip(itertools.count(), data)

for a,b in daily_data:
    print(a,b)


counter = itertools.count(start=5, step=-2.5)
print(next(counter))
print(next(counter))
print(next(counter))


# all() : if all values in this list have this condition
# any() : if any value in this list has this condition

N = 3
list1 = [int(num) for num in "1 2 3 4 5 6 7".split(" ")]

if ((all(i > 0 for i in list1)) and (any(str(num)[::-1] == str(num) for num in list1))):
    print("True")
else:
    print("False")


############ reduce() ############
'''
reduce() function accepts a function and a sequence and returns a single value calculated as follows:
Initially, the function is called with the first two items from the sequence and the result is returned. 
The function is then called again with the result obtained in step 1 and the next value in the sequence. 
This process keeps repeating until there are items in the sequence. The syntax of the reduce() function 
is as follows:
Syntax: reduce(function, sequence[, initial]) -> value
'''
from functools import reduce

def do_sum(x1, x2): return x1 + x2
reduce(do_sum, [1, 2, 3, 4])  # 1+2  -> 3+3  -> 6+4


###################### Functions ######################
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
# you can send list as arg and dictionaries as kwarg
def student_info(*args, **kwargs):
    print(args) # positional arguments
    print(kwargs) # keyword argument
    
student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name':'john', 'age':22}
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
# you can see when we set it to None it doesnt change its value after being called
print(add_employee_fixed.__defaults__) 

# vars : It takes an object as a parameter which can be a module, a class, an instance, or any object having 
# __dict__ attribute.

# The method returns the __dict__ attribute for a module, class, instance, or any other object if the same 
# has a __dict__ attribute. If the object fails to match the attribute, it raises a TypeError exception.
class Geeks: 
    def __init__(self, name1 = "Bob", num2 = 26, name3 = "Gohardani"): 
        self.name1 = name1 
        self.num2 = num2 
        self.name3 = name3 
    
GeeksforGeeks = Geeks() 
print(vars(GeeksforGeeks))

##### Function Annotations ####
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

# as it can be seen here instead of generating new timestamp each time, the function uses first default assigned value for all 
# the function calls!
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

def display_time_fixed(time_to_print=None):
    if time_to_print == None:
        time_to_print=datetime.now()
    print(time_to_print.strftime("%b %d, %Y %H:%M:%S"))

display_time_fixed()
time.sleep(1)
display_time_fixed()

###################### Modules ######################

# how to import module or other python files
from custom_module import find_index, test
# import custom_module as cm  
# index = cm.find_index(courses, 'Math')

courses = ['History', 'Math', 'Physics']
index = find_index(courses, 'Math')
print(index)
print(test)

# using the "from module import *" is a really bad practice

###################### List Comprehensions , lambda fuctions, map ######################
nums = [1,2,3,4,5]
l_nums = [n*n for n in nums]
print(l_nums)

l_2 = [n for n in nums if n%2==0]
print(l_2)
# map applies a lambda function to list and returns result of lambda (here True / False)
print(list(map(lambda x: x%2==0, nums))) 
# filter applies lambda function but only returns value of elements that returned True
print(list(filter(lambda x: x%2==0, nums))) 
                     # outer loop         # inner loop
print([(letter, num) for letter in 'abcd' for num in range(4)])

# map function and tuples
n = 5
integer_list = map(int, "123".split())
print(hash(tuple(integer_list)))

# map and lambda for fibonacci
# The map() function applies a function to every member of an iterable and returns the result.
print(list(map(len, ['Tina', 'babak', 'Tom'])))

# Lambda is a single expression anonymous function often used as an inline function.
sum = lambda  a,b,c : a+b+c
sum(1,2,3)
cube = lambda x: x**3

def fibonacci(n):
    list = []
    for i in range(0, n):
        if(i == 0 or i == 1):
            list.append(i)
        else:
            list.append(list[i-1] + list[i-2])
    return list

n = 5
print(list(map(cube, fibonacci(n))))

# if else inside a list
y_raw = ['ham', 'spam', 'spam']
y = [1 if i=='ham' else 0 for i in y_raw]

# Extract first item of each sublist
lst = [["a","b","c"], [1,2,3], ["x","y","z"]]
lst2 = [item[0] for item in lst]
lst2

# access all list elements from last to first in python list
l = [4,3,2,1]
print([x for x in l[::-1]])

# Get the nth element from the inner list of a list of lists in Python
a = [ [1,2], [2,9], [3,7] ]
b = [el[1] for el in a]
print(b)

# lambda function:
answer = lambda x: print(x*7)
answer(5)

# using zip : zip will stop when shortest list stops
x = [1,2,3,4]
y = [1,4,6]

for i,j in zip(x, y):
    print(i / j)

# sort() / sorted() function with lambda expressions => using lambda to sort by last name
names = ['Alf Zed', 'Mike Mo', 'Steve Jobs']
names.sort(key=lambda x: x.split()[-1].lower)  # sorts based on the second part of each string

people = [('A', 28), ('B', 13), ('C', 58)]
people.sort(key=lambda x: x[1], reverse=True) # this will change the original list

###################### OS Module ######################
import os
from datetime import datetime

print(os.getcwd()) # current working directory
os.chdir('C:/Users/B/Desktop') # change directory
print(os.getcwd())
print(os.listdir())  # show all files and folders in current dir
os.mkdir('PythonMadeFolder') # create new folder
os.makedirs('outerFolder/innerFolder') # create nested folders (better way!
os.rmdir('PythonMadeFolder') # delete directory
os.removedirs('outerFolder/innerFolder')
os.rename('D3', 'D3.js')  # rename(original, new)
print(os.stat('XML.zip')) # get info about a file or folder
mod_time = os.stat('XML.zip').st_atime # find out last time a file/folder was modified
print(datetime.fromtimestamp(mod_time))

# os.walk() goes through all inner folder recursively
os.chdir('C:/Users/B/Desktop/SQL')
for dirpath, dirnames, filenames in os.walk("C:/Users/Bob/Desktop/SQL"):
    print(dirpath)
    print(dirnames)
    print(filenames)

# we use path.join() instead of just concating two strings because we don't want to get // or missing / in the 
# path string
file_path = os.path.join(os.getcwd(), "test.txt")
print(file_path)

print(os.path.basename("/tmp/test.txt")) # gives back filename from path
print(os.path.dirname("/tmp/txtfiles/test.txt")) # gives back folders name from path
print(os.path.split("/tmp/test.txt"))
print(os.path.exists("/tmp/txtfiles/test.txt"))  # check if the file actually exists
print(os.path.isdir("/tmp/txtfiles/test.txt")) # if it is folder ? (or file)

# Rename and Sort files/folders
os.chdir('C:/Users/Bob/Desktop/SQL/Files/sorted')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split("-")
    
    f_num = f_num.strip().zfill(2)
    f_ext = f_ext.strip()
    f_title = f_title.strip()
    
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)


###################### Datetime module ######################
import datetime
import calendar

d = datetime.date(2019, 5, 15) # create a date (don't write zero before single digit)
print(d)
# todays date
today = datetime.date.today() 
print(today)
print(today.day, today.month, today.year, today.weekday())   # weekday()  : Monday 0  sunday 6

# TimeDelta : find date of seven days from now in future
tdelta = datetime.timedelta(days=7)
print(today + tdelta)  # date2 = date1 + timedelta
# get what day of week it was 7 days ago
print((today - tdelta).weekday()) 

bday = datetime.date(2019, 9, 11) # timedelta = date1 - date2
till_bday = bday - today
print(till_bday.days)

t = datetime.time(9, 30, 45)  # hour - minute - second
print(t)

t = datetime.datetime(2019, 5, 18, 14, 51, 30)
print(t)
print(t.date(), "|=====|", t.time())

tdelta = datetime.timedelta(hours = 13)
print(t + tdelta)

# this is current time without any timezone
dt_today = datetime.datetime.today()
print(dt_today)
# this is same as dt_today but we can give it timezones
dt_now = datetime.datetime.now()
print(dt_now
# current utc time
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow)

# formating time to custom mode for printing : strftime
print(dt_today.strftime("%B %d %Y"))
# convert string to datetime : strptime
dt_str = "May 18, 2019"
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# dates and time in python : find day from the date
date = "9 18 1997"
month, day , year = date.split(" ")
l = list(calendar.day_name)
print(l[calendar.weekday(int(year), int(month), int(day))].upper())

# weight loss planning via datetime
current_weight = 79
goal_weight = 70
avg_loss_week = 1
start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_loss_week
print(f'reach goal in {(end_date - start_date).days} days')

###################### Context Managers ######################

# context managers deal with opening and closing files in python
# class context manager
class Open_file:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    # set up for context manger
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    # tear down of context manger
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close

# since we use with statement, it will call the __enter__() method
with Open_file('sample.txt', 'w') as f:
    f.write("Testing")
# when we exit the block it will call the __exit__() method
print(f.closed)


# contextmanger with function
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode) # __init__
        yield f # __enter__
    finally:
        f.close() # __exit__

with open_file('sample1.txt', 'w') as f:
    f.write("Lorem Epsium")
print(f.closed)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield # since we arent working with any object inside the block, we just yield empty
    finally:
        os.chdir()

with change_dir('Files'):
    print(os.listdir())
print(os.getcwd()) # gets back to previous directory


###################### PIP ######################
'''
pip help => shows all command options
pip help install => shows all command options for "install"
pip search packageName => tries to find if package with such name exists
pip install packageName
pip uninstall packageName
pip install -U packageName = updates the package
pip list => shows list of all installed packages
pip list -o => all outdated packages that need update
pip freeze > requirements.txt => get a list of all packages and their versions and send it to a file
pip install -r requirements.txt => read list of packages from a file and install them
'''

###################### Variable Scope ######################
# type of python variable scopes: 'Local', 'Enclosing', 'Global', 'Built-in'

x = 'variable x' # Global variable
def test():
    y = 'variable y'  # local variable
    print(y)

test()

# how to change global variable within a function
y = "global_y"
def test_1():
    global y # we have to use keyword global to make sure python understands we want to use the global variable
    y = "y_1"
    global x_1 # we can even define global variables within a function
    x_1 = 5

test_1()
print(y)
print(x_1)

import builtins
print(dir(builtins))  # dir() function returns all attributes of given variable

# Enclosing
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x) # here it checks if there is any local variables with name x so it will print them  
    inner()
    print(x) # here it will check for local variable for this scope (inside outer function) to print

outer()

###################### Exception Handling ######################
# all errors : https://www.tutorialspoint.com/python/python_exceptions.html

try:
    f = open('./Files/xxx.txt')
    # raise custom exception
    if f.name == "./Files/xxx.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e: # Exception covers every error
    print("XXX error")
else: # else clause only runs when we have NO exception
    print(f.read()) # this can also be inside the try block
    f.close()
# finally caluse always runs
finally:
    print("Final execution")


# Try - except - finally
while True:
    try: # try to do this. if something goes wrong do the except.
        number = int(input("what is your favorite number? \n"))
        print(18/number)
        break # when it breaks it means it ends the while loop.
    except ValueError:
        print("only enter a number!")
    except ZeroDivisionError:
        print("don't enter zero.")
    except: # this responds to any kind of error.
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
      
      
###################### GENERATORS ######################
'''
generators have better performance than lists. because they dont put all the data into memory at once, instead they 
loop through data one by one.
generators are useful when the data includes hundreds of thousands or millions of records.
'''
def square_numbers(nums):
    for i in nums:
        yield (i * i)  # this yield keyword is what makes this function a generator

# when we call a generator it "doesnt" process anything, we have to call it to get the results
my_nums = square_numbers([1,2,3,4,5])

# here next() method calls each result from generator
print(next(my_nums)) # 1
print(next(my_nums)) # 2
print(next(my_nums)) # 3

for num in my_nums:
    print(num)

# generator comprehension (similar to list comprehension)
my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)

for num in my_nums:
    print(num)


names = ['john', 'corey', 'adam', 'steve', 'Thomas']
majors = ['Math', 'Engineering', 'Compsci', 'Arts']

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
        }
        yield person

# here we create generator but since we haven't looped through it, we don't have to process anything
people = people_generator(10) 
for peep in people:
    print(peep)


###################### First Class Function ######################

# square is a first class function becuase it can be passed as a 'variable' or to other functions
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
    return log_message  # we return it as variable

print(logger('Hi!'))
log_hi = logger('Hi!')  # here we set the log_hi variable to be a function equal to log_message()
log_hi() # here we execute it

# another example of return first class function as output from higher order function
def html_tag(tag):
    def wrap_text(msg):
        print(tag, msg)
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline')

print_p = html_tag('p')  # here we set print_p as a function equal to wrap_text()
print_p('Test paragraph') # here we execute it with an argument

###################### CLOSURE ######################
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
def sum(x, y):
    # closure
    def do_it():
        return x + y
    return do_it
 
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


def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
by_func = outer_func('Bye')

hi_func()
by_func()


import logging
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


######################## DECORATORS ########################
'''
Decorators, in the general sense, are functions or classes that wrap around another object, that extend, or decorate 
the object. The decorator supports the same interface as the wrapped function or object, so the receiver doesn't even 
know the object has been decorated.
A closure is an anonymous function that refers to its parameters or other variables outside its scope.
So basically, decorators uses closures.
'''
# we give *args, **kwargs argument to the decorator function so we will be able to
# add arguments to wrapper function without raising errors
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
# this @funcName will feed the below function to another function and that one will process this
@decorator_function 
def show():
    print("show something executed")

show()

@decorator_function
def display_info(name, age):
    print(name, age)
    
display_info("bob", 27)

## decorator class, this way we can easily check the arguments before fedding them to the function
class decorator_class(object):
    # get the method
    def __init__(self, original_function):
        self.original_function = original_function
    # get it's arguments and run it with the args
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

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("running '{}' with arguments '{}'".format(
            orig_func.__name__, args))
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

######################## Object Oriented Programming  OOP ########################
'''
method => function that is associated with a class (difference between method and function)
attribute => variable that is associated with a class

when you create methods within class they recieve the instance as "first argument" automatically, by convention we call 
it self
'''

class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    # __init__(self) => is the constructor (initializer) for python classes, each time you create new instance it will run
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # this is class variable, won't be initialized via class instances (objects)
        Employee.num_of_emps += 1

    # you need to pass the "self" argument to the method to be able to access class properties inside it
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    # this is a class method, cls is similar to self, but here we feed the actual class to this method 
    # you can also use class methods from instances, but it is not reccomended
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    # here we use the class method as an alternative constructor, to make instances from string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # this is same as "Employee(first, last, pay)"
    
    # static method doesnt acces instance (self) or the class (cls). it is used just to do some operation related to this class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)

print(emp_1)
print(emp_2)

# you can use both of these ways below
print(emp_1.fullname())
print(Employee.fullname(emp_1))

'''
Employee.raise_amount => this is a class variable, if we change it, it will change for all instances
self.raise_amount => this is a instance variable, it will only change it for this instance of class
    
python will first check if an instance variable exists, if not it will proceed to find class variable
'''
# this is same as "Employee.raise_amount = 1.05"
Employee.set_raise_amount(1.05)  

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.raise_amount)

# since raise_amount is class variable we can't see it in properties of instance
print(emp_1.__dict__)

print(Employee.num_of_emps)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steven-Smith-30000'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
# using static method from class
my_date = datetime.date(2019, 7, 13)
print(Employee.is_workday(my_date))

# python Protected and Private methods
class Test:
    def __init__(self):
        self.foo = 11
        # variable with _ means it is better to be private _bar (similar to protected to c#), u still can access this 
        # from instances
        self._bar = 23  
        # variable with __ means it is actually private, cant be accessed from class instances nor can be accessed by 
        # class itself from outside
        self.__baz = 42
        
    def show(self):
        print("1")

t = Test()
t._bar
t.__baz  # throws an error

# inheritance => when you put argument after name of a class it means its another class that we want to inherit from

class Developer(Employee):
    # when you apply a parent method | property in child class, it doesnt affect instances of parent class
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
print(help(Developer))
dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("User", "Test", 60000, "Java")

print(dev_1.prog_lang)
print(dev_2.first)

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def rmv_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

mgr_1 = Manager("sue", "Smith", 90000, [dev_1])
print("name of manager : ", mgr_1.last)

mgr_1.add_employee(dev_2)
mgr_1.rmv_employee(dev_1)
mgr_1.employees

# check if object is instance of class :
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))


# check if class inherits from another class:
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))


## Magic / special Methods and overloading
class EmployeeX:
    # all these 3 methods are magic methods
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    # here we are overloading the default str method of this class   
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    # here we are overloading the default str method of this class
    def __str__(self):
        return '{}-{}'.format(self.first, self.last)
    
    # this special method adds two objects together (returns their combined pay)
    def __add__(self, other):
        return self.pay + other.pay


emp_1 = EmployeeX("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)
print(emp_1) # when we print this object this is calling emp_1.__repr__(self)
print(repr(emp_1)) # same as above
print(emp_2)

# both do same operation
print(1+2)
print(int.__add__(1,2))

print(len('test'))
print('test'.__len__())

print(emp_1 + emp_2)

# Getters, Setters, Deleters
class EmployeeY:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    # property decorators allow us to use the method like a propery of the class | getter
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    # with setter decorator you can overload the method and use it to set properties of the instance
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    # with deleter decorator you can overload the method and use it to set properties of the instance
    @fullname.deleter
    def fullname(self):
        print("Delete!")
        self.first = None
        self.last = None
    
emp_1 = EmployeeY('John', 'Smith', 40000)

print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = "Corey Schefer"
print(emp_1.first)

del emp_1.fullname
print(emp_1.first)


'''
whenever python runs a file, it first sets a few special variables, and one of those variables is __name__ and it
sets it to __main__, but if we import this module (file) in other file, it will be different.
therefore, we can use this idea to check if we are running it directly or running it by importing in another module
'''
print(__name__)

def main():
    print("running directly")

if __name__ == "__main__":
    main()
else:
    print("running from import")
      
######################## Working With Files #######################

# writing and reading from text file
fw = open('Files/sample.txt', 'w')
fw.write('writing some stuff on my text file\n')
fw.write('i like bacon\n n shit')
fw.close()
# read
fr = open('Files/sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

# How to read a text file into a list with Python
lines = text_file.read().split(',')
#or
lines = text_file.read().split('\n')

# this is called context manager, and it automatically closes the file (it's yielded inside the with clause)
with open('text.txt', 'r') as f:
    pass
print(f.closed)

# How can I open multiple files using “with open” in Python?
with open('a.txt', 'w') as a, open('b.txt', 'w') as b:
    print(a.name, b.name)  # print name of both files

with open("./Files/sample.txt", 'r') as f:
    # print(f.read())   => reads the whole text (if files are too big do not do this!!)
    # print(f.readline()) => reads one line of file
    # print(f.readline()) => reads the next line
    # print(f.readlines())  # reads all lines at once and puts them inside a list

    # this is most efficient way, because it does not read all lines of file at once
    for line in f:  
        print(line, end='')


with open("./Files/sample.txt", 'r') as f:
    contents = f.read(100) # reads first 100 characters of the file
    print(contents)
    size_to_read = 100
    contents = f.read(size_to_read) # this will read from characters 100 to 200
    size_to_read = 100
    contents = f.read(size_to_read) # reads the next 100 (or less remaining) characters

# optimized way for very large files:
with open("./Files/sample.txt", 'r') as f:
    size_to_read = 20
    contents = f.read(size_to_read)
    # continue until any unread characters are left in this file
    while len(contents) > 0:
        print(contents)
        contents = f.read(size_to_read)  # go 20 characters ahead
        print(f.tell()) # shows current position of reading

# if file doesnt exist, it will create it, but if it does, this method overwrites the file!!
# if file exists, use 'a' instead of 'w' to "append" to file
with open('./Files/test.txt', 'w') as f:
    f.write("Test")
    f.write("Test")
    f.writelines("\nHello this is a test")

# working with two files, read from one and write in the other:
with open('./Files/test.txt', 'r') as rf:
    with open('./Files/test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# working with non-text files, we use binary instead of string, rb, wb instead of r, w
with open('./Files/apple.jpg', 'rb') as rf:
    with open('./Files/apple_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)


# writing to non-text files in chuncks of bites
with open('./Files/apple.jpg', 'rb') as rf:
    with open('./Files/apple_copy_1.jpg', 'wb') as wf:
        chunk_size= 4096
        rf_chunk = rf.read(chunk_size)
        
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)  # go 4096 bytes ahead
      
# How to get rid of double backslash in python windows file path string?
# I have dict:
my_dictionary = {"058498":"table", "064165":"pen", "055123":"pencil"}
# iterate over it:
for item in my_dictionary:
    PDF = r'C:\Users\user\Desktop\File_%s.pdf' %item
    doIt(PDF)

def doIt(PDF):
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(PDF,"rb").read() )
# get this error:
IOError: [Errno 2] No such file or directory: 'C:\\Users\\user\\Desktop\\File_055123.pdf'
      
# SOLUTION:
'''
The double backslash is not wrong, python represents it way that to the user. In each double backslash \\, the first one escapes the second to imply an actual backslash. 
If a = r'raw s\tring' and b = 'raw s\\tring' (no 'r' and explicit double slash) then they are both represented as 'raw s\\tring'.
'''
# So in the PDF path+name:
item = 'xyz'
PDF = r'C:\Users\user\Desktop\File_%s.pdf' % item
print(PDF)  # the representation of the string, also in error messages
'C:\\Users\\user\\Desktop\\File_xyz.pdf'
print(PDF)  # "as used"
C:\Users\user\Desktop\File_xyz.pdf
      
######################## JSON ########################
# json = JavaScript object Notation
import json

people_string = '''
{
    "people": [
        {
            "name" : "john smith",
            "phone" : "123-456-7890",
            "email" : ["john@gmail.com", "smith@yahoo.com"],
            "has_licence" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "560-555-5153",
            "email" : null,
            "has_licence" : true
        }
    ]
}
'''

# a json object will be converted to python dictionary
data = json.loads(people_string)

print(type(data))
print(type(data['people']))

for person in data['people']:
    print(person['name'])

# here we delete phone number from data and then turn it back into a json object
for person in data['people']:
    del person['phone']

# indent will make the json file more readable
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

with open("./Files/states.json") as f:
    data = json.load(f)

for state in data['states']:
    #print(state['name'], state['abbreviation'])
    del state['abbreviation']

with open("./Files/new_states.json", "w") as f:
    json.dump(data, f, indent=2)


from urllib.request import urlopen
with urlopen("https://jsonplaceholder.typicode.com/todos") as response:
    source = response.read()

data = json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data))
# print(data[0])

compeleted_dict = {}
for dat in data:
    id = dat['id']
    if dat['completed'] == True:
        compeleted_dict[id] = dat['title']

# to save as json file it would be better to save as list, then each row would be its own dict
with open("./Files/to_do.json", "w") as f:
    json.dump(compeleted_dict, f, indent=2)

######################### Subprocess ##########################
# we can use subprocess module to run external commands via python it is very easy to handle shell scripting code 
# and linux command line via subprocess

import sys
import subprocess

subprocess.run("ls", shell=True)
subprocess.run("ls -la", shell=True) # get file 
subprocess.run(['ls', '-la'])  # without shell command
p1 = subprocess.run(['ls', '-la'])
print(p1.args)
print(p1.returncode) # return code 0 means ran successfully | return 1 means there was some error
p1 = subprocess.run(['ls', '-la'], capture_output=True) # capture output of subprocess to the variable p1
print(p1.stdout.decode()) # since p1 output is in bytes we use .decode() to convert it to utf-8
p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True) # capture it as text instead of bytes
print(p1.stdout)
p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True) # does same thing as above code
print(p1.stdout)
# write to text file
with open('output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)
# handling errors 
                                  # this stands for name of the folder
p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
print(p1.stderr) # show the error that we get
if p1.returncode != 0:
    sys.exit()

# check=True : throws an exception if we get an error
p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True, check=True)
# make output of one command input of another command
# cat command in linux looks at files
p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True) 
# grep command in linux searches the files
p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout) 
print(p2.stdout)
# same as above but in one line
p1 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)

###################### Pythonic Coding ######################
'''
Duck typing : if it behaves like a duck when asked to do so, it is a duck!
Asking Forgiveness, Not Permission : try doing something if it works, great. if not then handle the error 
(instead of doing several check ups before)
'''
class Duck():
    def quack(self):
        print('Quack')
        
    def fly(self):
        print('flap')

class Person:
    def quack(self):
        print('Quack like a duck')
        
    def fly(self):
        print('flap like a duck')   

# not Duck-typed(Non-Pythonic)
def quack_and_fly(thing):
    if isinstance(thing, Duck):
        # none pythonic way to check if we have a function in our class:
        if hasattr(thing, 'quack'):
            if callable(thing.quack):
                thing.quack()
            
        thing.fly()
    else:
        print("not a duck!")
        
d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
 
print(" ")
    
# Pythonic way
def quack_and_fly_fixed(thing): 
    #Asking Forgiveness, Not Permission (much more readable)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

quack_and_fly_fixed(d)
quack_and_fly_fixed(p)

person = {'name' : 'Jess', 'age' : 23, 'job' : 'Programmer'}

# non-pythonic way
if 'name' in person and 'age' in person and 'job' in person:
    print(person['name'], person['age'], person['job'])
else:
    print("missing some keys")
       
# pythonic way (Asking Forgiveness, Not Permission)
try:
    print(person['name'], person['age'], person['job'])
except KeyError as e:
    print("Missing {} key".format(e))


my_list = [1,2,3,4,5,6]

# non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])
    
# Pythonic way
try:
    print(my_list[5])
except IndexError:
    print("index not in the list")     
              
# How to activate an Anaconda environment?
# create an environment called py33 by using:
conda create -n py33 python=3.3 anaconda
# set the PATH as:
set PATH=C:\Anaconda\envs\py33\Scripts;C:\Anaconda\envs\py33;%PATH%
# inside the cmd:
activate py33
# in linux/mac:
source activate py33
    
# Check if a given key already exists in a dictionary
d = {"key1": 10, "key2": 23}

if "key1" in d:
    print("this will execute")

if "nonexistent key" in d:
    print("this will not")
              
# Creating password using Python passlib
# first install the package
sudo pip install passlib
# import the hash algorithm
from passlib.hash import sha256_crypt
# generate new salt, and hash a password
hash = sha256_crypt.encrypt("toomanysecrets")
print(hash)
      
# Are multiple classes in a single file recommended?
'''
Python is not exclusively class-based - the natural unit of code decomposition in Python is the module. Modules are just as likely to contain functions 
(which are first-class objects in Python) as classes. In Java, the unit of decomposition is the class. Hence, Python has one module=one file, and Java has one (public) 
class=one file.

Python is much more expressive than Java, and if you restrict yourself to one class per file (which Python does not prevent you from doing) you will end up with lots of very 
small files - more to keep track of with very little benefit.

even more important is that in Python, you don't use classes for every- thing; if you need factories, singletons, multiple ways to create objects, polymorphic helpers, etc, you use plain functions, not classes or static methods.

once you've gotten over the "it's all classes", use modules to organize things in a way that makes sense to the code that uses your components.
make the import statements look good.
'''

# where does anaconda python install in windows?
'''

To find where Anaconda was installed I used the "where" command on the command line in Windows.

C:\>where anaconda
which for me returned:

C:\Users\User-Name\AppData\Local\Continuum\Anaconda2\Scripts\anaconda.exe
'''

# Simplify Chained Comparison
if start <= x <= end:
    pass
# or
r = range(start, end + 1) # (!) if integers
if x in r:
    pass

# How to make a variable inside a try/except block public?
text = 'something'  # define it before the try-except or in else block
try:
    url = "http://www.google.com"
    page = urllib.request.urlopen(url)
    text = page.read().decode('utf8')
except (ValueError, RuntimeError, TypeError, NameError):
    print("Unable to process your request dude!!")

print(text)
              
              
# What is the meaning of “Failed building wheel for X” in pip install?
'''
If the package is not a wheel, pip tries to build a wheel for it (via setup.py bdist_wheel). If that fails for any reason, you get the "Failed building wheel for pycparser" message and pip falls back to installing directly (via setup.py install).

Once we have a wheel, pip can install the wheel by unpacking it correctly. pip tries to install packages via wheels as often as it can. This is because of various advantages of using wheels (like faster installs, cache-able, not executing code again etc).
'''

# how to specify new environment location for conda create?

# Will create the environment named /tmp/test-env which resides in /tmp/ instead of the default .conda
conda create --prefix /tmp/test-env python=3.7


#  How to group dataframe rows into list in pandas groupby?
'''
a b
A 1
A 2
B 5
B 5
B 4
C 6

A [1,2]
B [5,5,4]
C [6]
'''
df = pd.DataFrame( {'a':['A','A','B','B','B','C'], 'b':[1,2,5,5,4,6]})
df.groupby('a')['b'].apply(list)
df1 = df.groupby('a')['b'].apply(list).reset_index(name='new')
              

# python dataframe pandas drop column using int
df.drop(df.columns[i], axis=1)

# Add column in dataframe from list
import numpy as np
m = np.arange(16) * 10
m[df.A]
array([  0,  40,  50,  60, 150, 150, 140, 130])
df["D"] = m[df.A]

# How to change the Jupyter start-up folder
'''
Use the jupyter notebook config file:
Open cmd (or Anaconda Prompt) and run jupyter notebook --generate-config.
This writes a file to C:\Users\username\.jupyter\jupyter_notebook_config.py.
Browse to the file location and open it in an Editor
Search for the following line in the file: #c.NotebookApp.notebook_dir = ''
Replace by c.NotebookApp.notebook_dir = '/the/path/to/home/folder/'
Make sure you use forward slashes in your path and use /home/user/ instead of ~/ for your home directory, backslashes could be used if placed in double quotes even if folder name contains spaces as such : "D:\yourUserName\Any Folder\More Folders\"
Remove the # at the beginning of the line to allow the line to execute
'''

# python @abstractmethod decorator
'''
You can apply the @abstractmethod decorator to methods such as draw() that must be implemented; Python will then raise an exception for classes that don’t define the method. Note that the exception is only raised when you actually try to create an instance of a subclass lacking the method.
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
If abstractMethod is not defined for ConcreteClass, the following exception will be raised when running the above code: TypeError: Can't instantiate abstract class ConcreteClass with abstract methods abstractMethod
'''          
              
              
# fnmatch => unix filename pattern matching
'''
This module provides support for Unix shell-style wildcards, which are not the same as regular expressions (which are documented in the re module). The special characters used in shell-style wildcards are:

Pattern     Meaning

*  =>  matches everything
?  => matches any single character
[seq]  => matches any character in seq
[!seq]  =>matches any character not in seq
'''

import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
