# Iterators and Iterables
'''
iterable: something that can be looped over, all iterables have the iter() method
iterator: know their next state(next value to loop over) and contain next() method
'''

from itertools import *
nums = [1, 2, 3]
print(nums.__iter__())  # <list_iterator object at 0x000001DD7372A0B8>

# iterating over the list gives us an iterable, and it contains __next()__ method
i_nums = iter(nums)
print(i_nums.__next__())    # 1
print(i_nums.__next__())    # 2

# =============================
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
print(next(nums))   # 1

# =============================
# Exhausting Iterators: in Python3 you need to cast zip objects as list to see all values at once

names = ['Peter parker', 'Clark kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']

identities = zip(names, heroes)
print(identities)   # <zip object at 0x1103d6d40>
# [('Peter parker', 'spiderman'), ('Clark kent', 'superman'), ('Wade Wilson', 'deadpool'), ('Bruce Wayne', 'batman')]
print(list(identities))


# zip() functions ties two lists together in a new list of tuples
first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)
# names = [("Bucky", "Roberts"), ("Tom", "Hanks"), ("Taylor", "Swift")]

for a, b in names:
    print(a, b)
# =============================
# Itertools
# itertools help with iterating through sets of data


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['zero', 'one', 'two', 'three', 'four',
     'five', 'six', 'seven', 'eight', 'nine']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# chain() function: group multiple lists together
for i in chain(a, b, c):
    print(i)

print(list(chain(a, b, c)))  # turns 3 lists into one giant list
print(list(chain(a[:2], b[:2], c[1:3])))

# count: comes from itertools, and counts from zero, upwards
counter = count()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2


# Combinations: order of a combo does not matter: a,b = b,a
# permutation: order does matter: a,b != b,a

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

results = combinations(letters, 2)
# ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
print(list(results))

results_1 = permutations(letters, 2)
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]
print(list(results_1))


l = [100, 200, 300]
daily_data = zip(count(), l)

for a, b in daily_data:
    print(a, b)

counter = count(start=5, step=-2.5)

print(next(counter))    # 5
print(next(counter))    # 2.5
print(next(counter))    # 0.0

#==================

# all(): if all values in this list have this condition
# any(): if any value in this list has this condition

N = int(input())

list1 = [int(num) for num in input().split(" ")]
                            # int(str(num)[::-1]) == num : if the number is palindrome
if all(i > 0 for i in list1) and any(int(str(num)[::-1]) == num for num in list1):
    print(True)
else:
    print(False)
