# context managers deal with opening and closing files in python
# class context manager
import os
from contextlib import contextmanager
from email.mime.base import MIMEBase


class Open_file:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # set up for context manger
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # tear down of context manger
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


# since we use with statement, it will call the __enter__() method
with Open_file('sample.txt', 'w') as f:
    f.write("Testing")
# when we exit the block it will call the __exit__() method
print(f.closed)


# contextManger with function
@contextmanager
def open_file(file, mode):
    global f
    try:
        f = open(file, mode)  # __init__
        yield f  # __enter__
    finally:
        f.close()  # __exit__


with open_file('sample1.txt', 'w') as f:
    f.write("Lorem Epsium")
print(f.closed)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield  # since we aren't working with any object inside the block, we just yield empty
    finally:
        os.chdir()


with change_dir('Files'):
    print(os.listdir())
print(os.getcwd())  # gets back to previous directory

# writing and reading from text file
fw = open('Files/sample.txt', 'w')
fw.write('writing some stuff on my text file\n')
fw.write('i like bacon\n n shit')
fw.close()

# read
fr = open('Files/sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

# How to read a text file into a list with Python
lines = text_file.read().split(',')
# or
lines = text_file.read().split('\n')

# this is called context manager, and it automatically closes the file (it's yielded inside the with clause)
with open('text.txt', 'r') as f:
    pass
print(f.closed)

# How can I open multiple files using “with open” in Python?
with open('a.txt', 'w') as a, open('b.txt', 'w') as b:
    print(a.name, b.name)  # print name of both files

with open("./Files/sample.txt", 'r') as f:
    # print(f.read())   => reads the whole text (if files are too big do not do this!!)
    # print(f.readline()) => reads one line of file
    # print(f.readline()) => reads the next line
    # print(f.readlines())  # reads all lines at once and puts them inside a list
    # this is the most efficient way, because it does not read all lines of file at once
    for line in f:
        print(line, end='')

with open("./Files/sample.txt", 'r') as f:
    contents = f.read(100)  # reads first 100 characters of the file
    print(contents)
    size_to_read = 100
    contents = f.read(size_to_read)  # this will read from characters 100 to 200
    contents = f.read(size_to_read)  # reads the next 100 (or less remaining) characters

# optimized way for very large files:
with open("./Files/sample.txt", 'r') as f:
    size_to_read = 20
    contents = f.read(size_to_read)
    # continue until any unread characters are left in this file
    while len(contents) > 0:
        print(contents)
        contents = f.read(size_to_read)  # go 20 characters ahead
        print(f.tell())  # shows current position of reading

# if file doesn't exist, it will create it, but if it does, this method overwrites the file!!
# if file exists, use 'a' instead of 'w' to "append" to file
with open('./Files/test.txt', 'w') as f:
    f.write("Test")
    f.write("Test")
    f.writelines("\nHello this is a test")

# working with two files, read from one and write in the other (copy content):
with open('./Files/test.txt', 'r') as rf:
    with open('./Files/test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# working with non-text files, we use binary instead of string, rb, wb instead of r, w
with open('./Files/apple.jpg', 'rb') as rf:
    with open('./Files/apple_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

# writing to non-text files in chunks of bites
with open('./Files/apple.jpg', 'rb') as rf:
    with open('./Files/apple_copy_1.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)  # go 4096 bytes ahead

# How to get rid of double backslash in python Windows file path string?
# I have dict:
my_dictionary = {"058498": "table", "064165": "pen", "055123": "pencil"}

def doIt(PDF):
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(PDF,"rb").read())

# iterate over it:
for item in my_dictionary:
    PDF = r'C:\Users\user\Desktop\File_%s.pdf' % item
    doIt(PDF)
# get this error:
# IOError: [Errno 2] No such file or directory: 'C:\\Users\\user\\Desktop\\File_055123.pdf'

# SOLUTION:
'''
The double backslash is not wrong, python represents it way that to the user. In each double backslash \\, the first 
one escapes the second to imply an actual backslash. 
If a = r'raw s\tring' and b = 'raw s\\tring' (no 'r' and explicit double slash) then they are both represented as 
'raw s\\tring'.
'''
# So in the PDF path+name:
item = 'xyz'
PDF = r'C:\Users\user\Desktop\File_%s.pdf' % item
print(PDF)  # the representation of the string, also in error messages
'C:\\Users\\user\\Desktop\\File_xyz.pdf'
print(PDF)  # "as used"
# C:\Users\user\Desktop\File_xyz.pdf




