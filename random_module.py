# Random module

# how to generate a random number in python
import random

for x in range(5):
    print(random.randint(1, 101)) # generates a number between 1 and 100

'''
range() and xrange() : xrange() was renamed to range() in Python 3.

In python, what is the difference between random.uniform() and random.random()?
random.random() gives you a random floating point number in the range [0.0, 1.0) (so including 0.0, but 
not including 1.0 which is also known as a semi-open range). 

random.uniform(a, b) gives you a random floating point number in the range [a, b], 
(where rounding may end up giving you b).
'''

def uniform(self, a, b):
    # Get a random number in the range [a, b) or [a, b] depending on rounding.
    return a + (b-a) * self.random()


print(random.uniform(1, 10)) # returns random float in  a range
print(random.randint(1, 10)) # returns random integer in  a range

# this function returns value in range of [0, 1)
print(random.random())

# =======================
# how to slice a list (indefinite length) randomly into 3 subgroups
l = [105, 167, 262, 173, 123, 718, 219, 272, 13, 21]

# random.shuffle() changes order of the list randomly
random.shuffle(l)
print(l)

# here we chunck the list into 3 random parts
[l[x::3] for x in range(3)]

print(l[::3])  
print(l[1::3])
print(l[2::3])
# ==========================
# range
for i in range(5):
    print(i * i)


for i in range(1, 6):
    print(i, sep='', end='', flush=True)


# write a program that prints numbers from 1 to 50, for multiples of 3 print "Fizz", for 
# mutilples of 5 print "Buzz" for both print "FizzBuzz"

for i in range(1, 51):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)