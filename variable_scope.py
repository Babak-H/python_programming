# type of python variable scopes: 'Local', 'Enclosing', 'Global', 'Built-in'

x = 'variable x'  # Global variable
def test():
    y = 'variable y'  # local variable
    print(y)

test()

# how to change global variable within a function
y = "global_y"
def test_1():
    global y  # we have to use keyword global to make sure python understands we want to use the global variable
    y = "y_1"
    global x_1  # we can even define global variables within a function
    x_1 = 5

test_1()
print(y)
print(x_1)

import builtins
print(dir(builtins))   # dir() function returns all attributes of given variable

# Enclosing
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x) # here it checks if there is any local variables with name x, so it will print them
    inner()
    print(x)  # here it will check for local variable for this scope (inside outer function) to print

outer()


# SameValue  VS  Same Object

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # checks if both objects have same value => True

print(id(a))
print(id(b))
print(a is b)  # checks if both objects are one in memory => False

