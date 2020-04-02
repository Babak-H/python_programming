# Variable Scope
# type of python variable scopes: Local, Enclosing, Gloabal, Built-in

x = 'variable x'  # Global variable

def test():
    y = 'variable y'  # local variable
    print(y)

test()

#=====================
# how to change a global variable within a function

y = "global_y"

def test_1():
    global y # we have to use keyword global to make sure python understands we want to use the global variable
    y = "y_1"
    
    global x # we can even define global variables within a function
    x= 5

test_1()
print(y)
print(x)

#=========================
import builtins

print(dir(builtins))  # dir() function returns all attributes of given variable

#=======================

# Enclosing 

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)  # here it checks if there is any local variables with name 'x' so it will print them

    inner()
    print(x)  # here it will check for local variable for this scope (inside outer function) to print
