import random

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# both methods return the value for key, but when using get() it won't return error if key doesn't exist
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
my_dict = {'foo': 'bar', 'too': 'char'}
next(iter(my_dict))  # only shows first key

# How do you create nested dict in Python?
d = {}
d['dict1'] = {}
d['dict1']['inner_key'] = 'value'
d[32] = 'red'
print(d)

# How to get a random value in python dictionary
d = {'VENEZUELA': 'CARACAS', 'CANADA': 'OTTAWA'}
random.choice(list(d.keys()))

# iteration through dictionary in python 2 vs python 3
# python 2  :  dict.iteritems() , dict.iterkeys()
# python 3
d.items(), d.keys()

# Converting Python Dictionary to List (with inner list)
dict = {1: 1, 2: 2, 3: 3}
dictlist = []

for key, value in dict.items():
    temp = [key, value]
    dictlist.append(temp)
print(dictlist)

# Sorting List of Dictionaries
# itemgetter  (easier to use than lambda, but slower)
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


# Check if a given key already exists in a dictionary
d = {"key1": 10, "key2": 23}

if "key1" in d:
    print("this will execute")

if "nonexistent key" in d:
    print("this will not")
