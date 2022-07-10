"""
Duck typing : if it behaves like a duck when asked to do so, it is a duck!
Asking Forgiveness, Not Permission : try doing something if it works, great. if not then handle the error
(instead of doing several check ups before)
"""

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
    # Asking Forgiveness, Not Permission (much more readable)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

quack_and_fly_fixed(d)
quack_and_fly_fixed(p)


person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}

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

my_list = [1, 2, 3, 4, 5, 6]

# non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])

# Pythonic way
try:
    print(my_list[5])
except IndexError:
    print("index not in the list")


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
df = pd.DataFrame({'a': ['A', 'A', 'B', 'B', 'B', 'C'], 'b': [1, 2, 5, 5, 4, 6]})
df.groupby('a')['b'].apply(list)
df1 = df.groupby('a')['b'].apply(list).reset_index(name='new')

# python dataframe pandas drop column using int
df.drop(df.columns[i], axis=1)

# Add column in dataframe from list
import numpy as np

m = np.arange(16) * 10
m[df.A]
array([0, 40, 50, 60, 150, 150, 140, 130])
df["D"] = m[df.A]
