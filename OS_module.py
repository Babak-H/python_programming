# Modules

# how to import module or other python files
from custom_module import find_index, test
# import custom_module as cm
# index = cm.find_index(courses, 'Math')

courses = ['History', 'Math', 'Physics']
index = find_index(courses, 'Math')
print(index)
print(test)

# using the "from module import *" is a really bad practice

# OS Module

import os
from datetime import datetime

print(os.getcwd())  # current working directory
os.chdir('C:/Users/B/Desktop')  # change directory
print(os.getcwd())
print(os.listdir())  # show all files and folders in current dir
os.mkdir('PythonMadeFolder')  # create new folder
os.makedirs('outerFolder/innerFolder')  # create nested folders (better way!
os.rmdir('PythonMadeFolder')  # delete directory
os.removedirs('outerFolder/innerFolder')
os.rename('D3', 'D3.js')  # rename(original, new)
print(os.stat('XML.zip'))  # get info about a file or folder
mod_time = os.stat('XML.zip').st_atime  # find out last time a file/folder was modified
print(datetime.fromtimestamp(mod_time))

# os.walk() goes through all inner folder recursively
os.chdir('C:/Users/B/Desktop/SQL')
for dirpath, dirnames, filenames in os.walk("C:/Users/Bob/Desktop/SQL"):
    print(dirpath)
    print(dirnames)
    print(filenames)

# we use path.join() instead of just concatenating two strings because we don't want to get // or missing / in the
# path string
file_path = os.path.join(os.getcwd(), "test.txt")
print(file_path)

print(os.path.basename("/tmp/test.txt"))  # gives back filename from path
print(os.path.dirname("/tmp/txtfiles/test.txt"))  # gives back folders name from path
print(os.path.split("/tmp/test.txt"))
print(os.path.exists("/tmp/txtfiles/test.txt"))  # check if the file actually exists
print(os.path.isdir("/tmp/txtfiles/test.txt"))  # if it is folder ? (or file)

# Rename and Sort files/folders
os.chdir('C:/Users/Bob/Desktop/SQL/Files/sorted')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split("-")

    f_num = f_num.strip().zfill(2)
    f_ext = f_ext.strip()
    f_title = f_title.strip()

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)


# fnmatch => unix filename pattern matching
'''
This module provides support for Unix shell-style wildcards, which are not the same as regular expressions (which are 
documented in the re module). The special characters used in shell-style wildcards are:

Pattern     Meaning

*  =>  matches everything
?  => matches any single character
[seq]  => matches any character in seq
[!seq]  =>matches any character not in seq
'''

import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)
