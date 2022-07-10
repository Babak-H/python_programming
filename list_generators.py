a = [1, 2, 3]
a + a

# How can I compare two ordered lists in python?
print([0, 1, 2] == [0, 1, 2])
print([0, 1, 2] == [0, 2, 1])

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
old_l = [1, 2, 3]
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
x = [1, 2, 3, 4]
print(x[-1])  # last element
print(x[-3])  # third element from last

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
l = [1, 2, 3, 4, 6, 5, 7, 12, 9, 8]
l[1:-2:2]  # from second to last 2nd element with step 2 (skip one element each time)
l[-1:1:-1]  # iterating from last to second (-1 means going back)

# from last to first
l[::-1]

lst = [1, 2, 3, 4, 5, 5]

# from third to last
print(lst[2:])
# from third last element to last
print(lst[-3:])
# append to list (adds at end)
lst.append(6)
# inset to string (index, value)
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
print(sorted([3, 1, 2]), "sort without changing the original")
# find (first) index of a value inside list
print(lst.index(5), " index of value 5")
# check if a value is inside a list:
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
values = [1, 2, 3, 4]
min_idx = values.index(min(values))
max_idx = values.index(max(values))

# if else inside a list
y_raw = ['ham', 'spam', 'spam']
y = [1 if i == 'ham' else 0 for i in y_raw]


# generators
'''
generators have better performance than lists. because they don't put all the data into memory at once, instead they 
loop through data one by one.
generators are useful when the data includes hundreds of thousands or millions of records.
'''
def square_numbers(nums):
    for i in nums:
        yield i * i  # this yield keyword is what makes this function a generator

# when we call a generator it "doesn't" process anything, we have to call it to get the results
my_nums = square_numbers([1, 2, 3, 4, 5])

# here next() method calls each result from generator
print(next(my_nums))  # 1
print(next(my_nums))  # 2
print(next(my_nums))  # 3

for num in my_nums:
    print(num)

# generator comprehension (similar to list comprehension)
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)

for num in my_nums:
    print(num)

names = ['john', 'corey', 'adam', 'steve', 'Thomas']
majors = ['Math', 'Engineering', 'Compsci', 'Arts']

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

# here we create generator but since we haven't looped through it, we don't have to process anything
people = people_generator(10)
# here we process data
for peep in people:
    print(peep)
