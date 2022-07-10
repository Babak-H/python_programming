# if else statement
# list commands : insert, remove, append, sort, pop, reverse
N = 10
a = []

for _ in range(N):
    line = "1374".split()
    if len(line) == 1:
        command = line[0]
    elif len(line) == 2:
        command = line[0]
        e = int(line[1])
    elif len(line) == 3:
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

# There is no switch-case statement in python!!
# use if-else instead

# and | or | not
user = "admin"
logged_in = True

if user == 'admin' and logged_in:
    print('admin page')
elif user == 'admin' or logged_in:
    print('wrong page')
elif not logged_in:
    print('bad creds')
else:
    print('end')

# How to exit an if clause
# Wrap the code in its own function. Instead of break, use return
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

# Simplify Chained Comparison
if start <= x <= end:
    pass
# or
r = range(start, end + 1)  # (!) if integers
if x in r:
    pass