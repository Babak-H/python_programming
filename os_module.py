# modules

# # import custom_module as cm  how to import module or other python files
# from custom_module import find_index, test

# courses = ['History', 'Math', 'Physics']

# # index = cm.find_index(courses, 'Math')
# index = find_index(courses, 'Math')
# print(index)
# print(test)

# # using the "from module import *" is a really bad practice

#=================================
# OS module
import os
from datetime import datetime

print(os.getcwd()) # current working directory

os.chdir('C:/Users/Bob/Desktop')  # change directory
print(os.getcwd())

print(os.listdir())  # show all files and folders in current dir

os.mkdir('PythonMadeFolder') # create new folder

os.makedirs('outerFolder/innerFolder') # create nested folders (better way!)

os.rmdir('PythonMadeFolder')

os.removedirs('outerFolder/innerFolder')

os.rename('D3', 'D3.js')  # rename(original, new)

print(os.stat('XML.zip')) # get info about a file or folder

# find out last time a file/folder was modified
mod_time = os.stat('strings.py').st_atime
print(datetime.fromtimestamp(mod_time))

# =================================
os.chdir('C:/Users/Bob/Desktop/SQL')

# goes through every subfolder and file under current folder, in an reccursive manner
for dirpath, dirnames, filenames in os.walk('C:/Users/Bob/Desktop/SQL'):
    print(dirpath)
    print(dirnames)
    print(filenames)
    print()


# we use path.join() instead of just concating two strings because we don't want to get // or / missing in the path string
file_path = os.path.join(os.getcwd(), "test.txt")
print(file_path)

# =======================
print(os.path.basename("/temp/test.txt"))  # gives back filename from path
print(os.path.dirname("/tmp/txtfiles/test.txt"))  # gives back folders name from path
print(os.path.split("/tmp/test.txt"))  # ('/tmp', 'test.txt')
print(os.path.exists("/tmp/txtfiles/test.txt")) # checks if file actually exists (True/False)
print(os.path.isdir("/tmp/txtfiles/test.txt"))  # if path is a folder (or it is a file?)

# =======================
# Rename and Sort files/folders

import os

os.chdir("C:/Users/Bob/Desktop/SQL/Files/sorted")
print(os.getcwd())

for f in os.listdir(): # get name of all the files inside this folder
    f_name, f_ext = os.path.splitext(f)   # name, extension
    f_title, f_num = f_name.split("-") 

    f_num = f_num.strip().zfill(2)
    f_ext = f_ext.strip()
    f_title = f_title.strip()

    new_name = f'{f_num}-{f_title}{f_ext}'.format()
    os.rename(f, new_name)