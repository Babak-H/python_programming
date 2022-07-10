def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = "babak"
    last_name = "G"
    print_full_name(first_name, last_name)

# string split() and join() methods:
def split_and_join(line):
    a = line.split(" ")
    return "-".join(a)

line = "I like bbq"
result = split_and_join(line)
print(result)

# character methods
# .isalnum(), isalpha(), isdigit(), islower(), isupper()  : all return true or false
s = "Apple"
x = ["False", "False", "False", "False", "False"]

for i in range(len(s)):
    char = s[i]
    if char.isalnum() and x[0] == "False":
        x[0] = "True"

    if char.isalpha() and x[1] == "False":
        x[1] = "True"

    if char.isdigit() and x[2] == "False":
        x[2] = "True"

    if char.islower() and x[3] == "False":
        x[3] = "True"

    if char.isupper() and x[4] == "False":
        x[4] = "True"
     
for val in x:
    print(val)

# recieve an string and capitalize every word in it:
def solve(s):
    str_1 = ""
    l = s.split(" ")
    for word in l:
        str_1 += word.capitalize() + " "
    return str_1

s = "my name is babak"
result = solve(s)
print(result)

# sort all strings of a list based on their size
X = ["first", "Second", "Third"]
print(sorted(len(s) for s in X))
sorted_x = sorted(len(s) for s in X)
# print mode from the sorted list to find avg length of list
print(sorted_x[len(sorted_x) // 2]) # return middle value

l = [12, 14, 18, 28] # find mode
l = sorted(l)
mode = l[len(l) // 2]

# How to substring a string in Python?
x = "Hello World!"
x[2:]
# Get the last 4 characters of a string
mystr = "abcdefghijkl"
mystr[-4:]

# Splitting on delimiter in Python string
s = "a,b,c,d"
s.split(",")
# split only on last occurrence of ',' in string:
s.rsplit(',', 1)
# or
s.rpartition(',')

# split a word into a list
list("Word to Split")

# convert tuple to string
tup = ('a', 'b', 'c', 'd', 'g', 'x', 'r', 'e')
''.join(tup)

# How to sort the letters in a string alphabetically in Python
a = 'ZENOVW'
# sorted(a) ['E', 'N', 'O', 'V', 'W', 'Z']
print(''.join(sorted(a)))
b = '-'.join(sorted(a))
print(b.split('-'))

# replace a string in text with another string
str_0 = "hello world"
str_1 = str_0.replace('world', 'universe')
print(str_1)

# using .format() with strings
name = "Bob"
greeting = "Hello"

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)


import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    s = ""
    for word in word_list:
        s += word+"\n"
    return s

string, max_width = "hello", 6
result = wrap(string, max_width)
print(result)