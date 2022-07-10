# range
if __name__ == '__main__':
    n = 12
# n is NOT included in the range
for i in range(n):
    print(i * i)

# range
n = 6
for i in range(1, n + 1):
    print(i, sep='', end='', flush=True)  # prints everything in one line

# How to Generate a Random Number in Python
import random

for x in range(5):
    print(random.randint(1, 101))

'''
range() and xrange()
xrange() was renamed to range() in Python 3.

In python, what is the difference between random.uniform() and random.random()?
random.random() gives you a random floating point number in the range [0.0, 1.0) (so including 0.0, but not including 1.0 which is also known as a semi-open range). 
random.uniform(a, b) gives you a random floating point number in the range [a, b], (where rounding may end up giving you b).
'''


def uniform(self, a, b):
    """Get a random number in the range [a, b) or [a, b] depending on rounding."""
    return a + (b - a) * self.random()  # self.random => between 0 and 1 (smaller than 1)

print(random.uniform(1, 10))  # returns random float in a range
print(random.randint(1, 100))  # returns random integer in a range
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

var = [l[x::3] for x in range(3)]
print(var)