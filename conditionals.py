# python data types
'''
mutable(can change it) and immutable(can't change it) python data types:
mutable : list - set - dictionary
immutable: strings - numbers - tuples
'''

# Conditionals if-elif-else

# if else statement
# list commands : insert, remove, append, sort, pop, reverse

N = 10
a = []

for _ in range(N):
    line = input().split()
    if(len(line) == 1):
        command = line[0]
    elif(len(line) == 2):
        command = line[0]
        e = int(line[1])
    elif(len(line) == 3):
        command = line[0]
        i = int(line[1]) 
        e = int(line[2])   
    if command == 'insert':
        a.insert(i, e)
    elif command == 'print':
        print(a)
    elif command == 'remove':
        a.remove(e)
    elif command == 'append':
        a.append(e)
    elif command == 'sort':
        a = a.sort()
    elif command == 'pop' and len(a) != 0:
        a.pop()
    elif command == 'reverse':
        a = a.reverse()
    else:
        print("No idea!!")
        
## There is no switch-case statement in python!!
# use if-else instead

# and | or | not

user = "admin"
logged_in = True

if user == 'admin' and logged_in:
    print("Admin page")
elif user == 'admin' or logged_in:
    print("wrong page")
elif not logged_in:
    print("bad creds")
else:
    print("end")


a = [1,2,3]
b = [1,2,3]

print(a == b)  # checks if both objects have same value => True

print(id(a))
print(id(b))
print(a is b)  # checks if both objects are one in memory => False


# how to exit an if clause
# wrap the code in its own function. Instead of break, use return

condition_a, condition_b, outer_condition = True, False, True

def some_function():
    if condition_a:
        # do something and return early
        return
    if condition_b:
        # do something else and return early
        return

    return

if outer_condition:
    some_function()


# assert

'''
What is the use of “assert” in Python?
The assert statement exists in almost every programming language. It helps detect problems early in your program, where the cause is clear, rather than later as a side-effect of some other operation.
if not condition: 
    raise AssertionError()
'''

assert True # nothing happens
assert False  # crashes the code, AssertionError


