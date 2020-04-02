# Strings and text data

def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()  # input get the data from the console
    last_name = input()
    print_full_name(first_name, last_name)


# =====================================
# string split() and join() methods:

def split_and_join(string):
    a = string.split(" ")
    return "-".join(a)


line = "I love Apple Pie"
res = split_and_join(line)
print(res)


# =====================================
# how many times a substring occurs in an string

# dumb way
def count_substring(string, sub_string):
    count = 0
    num = 0
    for i in range(len(string)):
        if string[i] == sub_string[num]:
            num = num + 1
        else:
            num = 0
        if num == len(sub_string):
            count = count + 1
            num = 0
    return count


# smart way
message = "Hello my Friend, hello there"
print(message.lower().count('hello'))

# ================================
# character methods : .isalnum(), isalpha(), isdigit(), islower(), isupper()  : all return true or false

myString = "Hello There whats up?"
print(myString.isalnum())
print(myString.isalpha())
print(myString.isdigit())
print(myString.islower())
print(myString.isupper())


# ========================
# receive an string and capitalize every word in it

def solve(s):
    string = ""
    l = s.split(" ")
    for word in l:
        string += word.word.capitalize() + " "
    return string


s = "hello world"
result = solve(s)


# ============================
# if a character in string is lower case make it upper and vice versa then return the string

def swap_case(s):
    l = list(s)
    for i in range(len(s)):
        if l[i].isupper():
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()
    return "".join(l)


print(swap_case("ApplePie"))

# =============================
# sort all strings of a list based on their size

X = ["apple", "pie", "Bob"]
print(sorted(len(s) for s in X))
sorted_x = sorted(len(s) for s in X)

# average length in the list, find the middle value, it is avg length
print(sorted_x[len(sorted_x)] // 2)

# find mode
l = [12, 14, 18, 28]
l = sorted(l)
model = l[len(l) // 2]

# ============================

# How to substring a string in Python?
x = "Hello World"
x1 = x[2:]

# get the last 4 characters of a string
mystr = "abcdefghijkl"
mystr[-4:]

# split a word into a list
list("Word to split")

# Splitting on last delimiter in Python string
s = "a,b,c,d"
s.rsplit(',', 1)
# or
s.rpartition(',')

# convert a tuple into an string
tup = ('a', 'b', 'c', 'd')
x = ''.join(tup)

# ============================
#  How to sort the letters in a string alphabetically in Python
a = 'ZENOVW'  # sorted(a) ['E', 'N', 'O', 'V', 'W', 'Z']

b = '-'.join(sorted(a))
print(b.split('-'))

# ============================
# replace a string in text with another string

string = "hello babak"
string_1 = string.replace('babak', 'caleb')

# ============================
# using .format() with strings

name = "hunter"
greeting = "Hello"

message = f'{name}, {greeting}'.format()  # only works with python > 3
print(message)

# ================================
# textwrap can separate strings based on the given length
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)

    s = ""
    for word in word_list:
        s += word + " "
    return s

wrap("hello my name is apple pie", 3)  # hel lo my  nam e is  app le pie