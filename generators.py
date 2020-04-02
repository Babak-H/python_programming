# Generators

'''
generators have better performance than lists. because they dont put all the data into memory at once, 
instead they loop through data one by one. generators are useful when the data includes hundreds of 
thousands or millions of records
'''


def square_numbers(nums):
    for i in nums:
        yield (i*i)  # this yield keyword is what makes this function a generator


# when we call a generator it doesnt process anything, we have to call it to get the results
my_nums = square_numbers([1, 2, 3, 4, 5])

# here next() method calls each result from generator
print(next(my_nums))  # 1
print(next(my_nums))  # 2
print(next(my_nums))  # 3

for num in my_nums:
    print(num)


# generator comprehension (similar to list comprehension)
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)  # <generator object <genexpr> at 0x10870f5f0>

for num in my_nums:
    print(num)


# =========================
import random

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

# this is were we finally do the processing
for peep in people:
    print(peep)

