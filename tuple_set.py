# Convert list to tuple in Python
l = [4, 5, 6]
tuple(l)

# you can't add to tuple or remove from it when it is already created
tup = ('history', 'math', 'physics')

# Sort a list of tuples by 2nd item (integer value)
l = [('abc', 121), ('abc', 231), ('abc', 148), ('abc', 221)]

'''
Try using the "key" keyword with sorted()
key should be a function that identifies how to retrieve the comparable element from your data structure. 
In your case, it is the second element of the tuple, so we access [1]
'''
sorted(l, key=lambda x: x[1])

# set : sets are used for membership testing and eliminating duplicate entries.
print(set('HackerRanks'))  # {'R', 's', 'n', 'H', 'a', 'c', 'r', 'e', 'k'}
print(set([1, 1, 4, 5, 12, 1, 6, 6]))  # {1, 4, 5, 12, 6}
# dictionary to set
print(set({'Hacker': 'DOSHI', 'Rank': 616}))


# this is mean not median
def averge(array):
    return sum(set(array)) / len(set(array))


s1 = {1, 2, 3, 4, 5}
s1.add(6)
s1.update([6, 7, 8])
print(s1)

# remove() and discard() both delete from set, but discard won't throw an error even when the value doesnt exist in
# the set
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

# named tuple : named tuples are similar to dictionaries, but with easier syntax that needs less writing
from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
print(color.red)
white = Color(255, 255, 255)
print(white.blue)