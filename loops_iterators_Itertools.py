# loop over an string
for letter in 'Hello':
    print(letter)

# Skip first entry in for loop in python
cars = [1, 2, 3, 4]
iter_cars = iter(cars)
next(iter_cars)  # jump first element
for car in iter_cars:
    print(car)

# while loop
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

# Fibonacci sequence
a, b = 0, 1
for _ in range(0, 10):
    print(a)
    a, b = b, a+b

'''
The enumerate() function adds a counter to an iterable. So for each element in cursor, a tuple is 
produced with (counter, element). the for loop binds that to row_number and row, respectively.
'''
elements = ('foo', 'bar', 'baz')
for elem in elements:
    print(elem)

for count, elem in enumerate(elements):
    print(count, elem)

# else clause after loop
my_list = [1, 2, 3, 4]

for i in my_list:
    print(i)
    if i == 6:
        break
else:
    print("this will be executed if we didn't have any breaks")

j = 0
while j < 5:
    print(j)
    j += 1
    if j == 3:
        break
else:
    print("this will be executed if we didn't have any breaks")

# Iterable: something that can be looped over, all iterables have the iter() method
# Iterators : know their next state (next value to loop over) and contain next() method.

nums = [1, 2, 3]
print(nums.__iter__())

# iterating over the list gives us an Iterator, and it contains __next__() method
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
heroes = ['spiderMan', 'superman', 'deadpool', 'batman']

identities = zip(names, heroes)
print(identities)
print(list(identities))

# itertools helps with iterating through sets of data
from itertools import *
import itertools

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# chain() function : group multiple lists together
for i in chain(a, b, c):
    print(i)

print(list(chain(a, b, c)))
print(list(chain(a[:2], b[:2], c[1:3])))

counter = itertools.count()
print(next(counter))
print(next(counter))
print(next(counter))

from collections import Counter

c = Counter('galled')
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
numbers = [0, 1, 2, 3]
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

for a, b in daily_data:
    print(a, b)

counter = itertools.count(start=5, step=-2.5)
print(next(counter))
print(next(counter))
print(next(counter))

# all() : if all values in this list have this condition
# any() : if any value in this list has this condition

N = 3
list1 = [int(num) for num in "1 2 3 4 5 6 7".split(" ")]

if (all(i > 0 for i in list1)) and (any(str(num)[::-1] == str(num) for num in list1)):
    print("True")
else:
    print("False")

# using zip : zip will stop when shortest list stops
x = [1, 2, 3, 4]
y = [1, 4, 6]

for i, j in zip(x, y):
    print(i / j)


