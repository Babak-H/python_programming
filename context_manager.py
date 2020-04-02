# Context Managers

# class context manager
class Open_file:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    # setup for context manager:
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    # tear down of context manager:
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

# since we use "with" statement, it will call the __enter__() method
with Open_file('sample.txt', 'w') as f:
    f.write("Testing")

# when we exit the block it will call the __exit__() method
print(f.closed) # True

#==========================
# context manager with function

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode) # __init__
        yield f   # __enter__  | yield is what makes the program stay in this state
    
    finally:
        f.close()  # __exit__

with open_file("sample1.txt", "w") as f:
    f.write("Lorem Epsium")

print(f.closed)

#=======================
import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield # since we arent working with any object inside the block, we just yield empty
    finally:
        os.chdir(cwd)


with change_dir('Files'):
    print(os.listdir())

print(os.getcwd())