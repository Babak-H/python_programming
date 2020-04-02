# List, Tuples, Sets, Dictionaries

import random

# doubling a list
a = [1, 2, 3]
print(a + a)  # [1, 2, 3, 1, 2, 3]

# =====================================
# How can I compare two ordered lists in python
print([0, 1, 2] == [0, 1, 2])  # True
print([0, 1, 2] == [0, 2, 1])  # False

"""
in python you can't create an empty list and then assign a value by index to it.
j = []
j[0] = 1 this will return error

instead:
j.append(1)
"""

# =====================================
# how to clone or copy a list
"""
With new_list = my_list, you don't actually have two lists. The assignment just copies the reference to the list, not the actual list, so both 'new_list' and 'my_list' refer to the same object after the assignment.
To actually copy the list, you have various possibilities:
You can use the builtin list.copy() method (available since Python 3.3):
"""

old_list = [1, 2, 3]
new_list = old_list.copy()
# or
new_list = old_list[:]

# =====================================
# Difference between del, remove and pop on lists

# remove: removes the first matching value, not an specfic index:
a = [0,2,3,2]
a.remove(2)
print(a)

# del removes item at specific index
a = [3,2,2,1]
del a[1]
print(a)

# pop removes the item at an specific index and returns it
a = [4,3,5]
x = a.pop(1)

# =====================================
# negative index
x = [1,2,3,4]

print(x[-1])    # 4
print(x[-3])    # 2


# Append integer to beginning of list in Python
a = 5
li = [1, 2, 3]
[a] + li  # Don't use 'list' as variable name.


# How to randomly select an item from a list?
foo = ['a', 'b', 'c', 'd']
print(random.choice(foo))   # b

# choose 3 random elements of list (can be repeated)
print(random.choice(foo, k=3))  # ['b', 'b', 'e']


# How do I get an empty list of any size in python?
a = [0] * 10
# or
a = [None] * 10


# find biggest/smallest item in a list of strings:
x = ['a', 'apple', 'pie']

print(max(len(s) for s in X))
print(min(len(s) for s in X))


#==================================
# list[start:end:step] traversing a list

l = [1,2,3,4,6,5,7,12,9,8]

l[1:-2:2]   # from second to last third element with step 2 (skip one element each time)

# iterating from last to second (-1 means going back)
l[-1:1:-1]

# deom last to first
l[::-1]


lst = [1,2,3,4,5,5]

print(lst[2:]) # from third to last
print(lst[-3:]) # from third last element to last
lst.append(6) # append to list (adds at end)
lst.insert(0, 0) # inset to string (index, value)
lst.pop() # removes last element from list

# reverse the list (current list)
lst.reverse()
print(lst, "reversed")

# sort the list
lst.sort()
print(lst, "sorted")

# reverse sort a list
lst.sort(reverse=True)
print(lst, "reverse sorted")

# sort but not change the list
print(sorted([3,2,1]), "sort without changing the original")

# find (first) index of a value inside list
print(lst.index(5), "index of value")

# check if a value is inside a list:
print(7 in lst)

# add up all values inside a numerical list
numbers = [1,2,3]
print(sum(numbers))

# length of list
print(len(lst))

#==================================
# find second smallest number in a inner list

# create a list with inner lists from user input
p_list = []
for _ in range(0, int(input())):
    p_list.append([input(), float(input())])

# for name, marks in p_list : this is how we iterate inner lists with two array
# then we select mark
# and use set to remove duplicates
second_low = sorted(list(set[marks for name, marks in p_list]))[1]

print('\n'.join([a for a,b in sorted(p_list) if b == second_low]))

#==================================
# Check if all values in list are greater than a certain number

my_list1 = [29, 500, 43]
all(i > = 30 for i in my_list1)


items = ['December 1', 'Bread gloves', 8.50]
print(items[0])
print(items[1])

# simple unpacking
date, name, price = ['December 1', 'Bread gloves', 8.50]
print(date)
print(name)

grades = [11, 44, 99, 88, 25]
# get avg of all items in a list but drop the first and last one

def drop_first_last(grades):
    first, *middle, last = grades
    
    avg = sum(middle) / len(grades)

drop_first_last(grades)
drop_first_last([10, 5, 4, 7, 3])

# Getting the index of the returned max or min item using max()/min() on a list

values = [1,2,3,4]
if isMinLevel:
    return values.index(min(values))
else:
    return values.index(max(values))

#========================================
# convert list to tuple in python
l = [4,5,6]
tuple(l)

# you can't add to tuple or remove from it when it is already created
tuple = ('history', 'math', 'physics')


# Sort a list of tuples by 2nd item (integer value)
l = [('abc', 121),('abc', 231),('abc', 148), ('abc',221)]

'''
Try using the "key" keyword with sorted()
key should be a function that identifies how to retrieve the comparable element from your data structure. 
In your case, it is the second element of the tuple, so we access [1]
'''
sorted(l, key = lambda x: x[1])

#========================================
# set : sets are used for membership testing and eliminating duplicate entries.

print(set('HackerRanks')) # {'R', 's', 'n', 'H', 'a', 'c', 'r', 'e', 'k'}

print(set([1,1,4,5,12,1,6,6])) # {1, 4, 5, 6, 12}

print(set({'Hacker' : 'DOSHI', 'Rank' : 616 })) # {'Hacker', 'Rank'}

def averge(array):
    return sum(set(array) / len(set(array)))


s1 = {1,2,3,4,5}

s1.add(6)
s1.update([6,7,8])
print(s1)   # {1, 2, 3, 4, 5, 6, 7, 8}

# remove() and discard() both delete from set, but discard won't throw an error even when the 
# value doesnt exist in the set

s1.remove(6)
s1.discard(7)
print(s1)   # {1, 2, 3, 4, 5, 8}


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

#========================================
# create a dictionary
students = {'name': 'John', age: '22', 'courses': ['Math', 'CompSci']}

# both methods return the value for key, but when u use get() it wont return error if key doesnt exist
print(students['name'], students.get('name'))

# delete key value pair from the dictionary
del students('age')

# another way
students.pop('age')

# length of dictionary
print(len(students))
# get all keys
print(students.keys())
# get all values
print(students.values())

# check if a given key already exists in the dictionary
# "in" is the intended way to test for the existence of a key in a dict.

d = dict()

for i in range(100):
    key = i % 10
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


# How do you find the first key in a dictionary?
my_dict = {'foo': 'bar', 'too':'char'}
next(iter(my_dict)) # shows only first key


# How do you create nested dict in Python?
d = {}
d['dict1'] = {}
d['dict1']['innerkey'] = 'value'


# How to get a random value in python dictionary
d = {'Venezuela': 'Caracas', 'Canada': 'Ottawa'}
random_key = random.choice(list(d.keys()))


# iteration through dictionary in python 2 vs python 3

# python 2
dict.iteritems() , dict.iterkeys()
# python 3
dict.items() , dict.keys()


# Converting Python Dictionary to List (with inner list)
dict = {1:1, 2:2, 3:3}
dictList = []

for key, value in dict.items():
    temp = [key, value]
    dictList.append(temp)


#========================================
# named tuple: named tuples are similar to dictionaries, but with easier syntaxt that needs less writing

from collections import namedtuple

Color = namedtuple('color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)
print(color.red)    # 55

#========================================

# if else inside a list
y = [1 if i=='ham' else 0 for i in y_raw]

# extract first item of each sublist
lst = [['a','b', 'c'], [1,2,3], ['x', 'y', 'z']]

lst2 = [item[0] for item in lst]

# access all list elements from last to first in python list
l = [1,2,3,4]
print([x for x in l[::-1]])

# iterating through 2 dimensional lists in 1 line
sandwiches = [["bacon", "banana"], ["ham", "salami", "cheese"]]
prefs = {"bacon": 5, "ham": -2, "salami": 1}

scores = [ [ ", ".join(i), sum( prefs[j] for j in i if j in prefs) ] for i in sandwiches ]
print(scores)