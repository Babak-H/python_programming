# https://realpython.com/command-line-interfaces-python-argparse/

import argparse
import os
import sys

# create parser
# my_parser = argparse.ArgumentParser(description="List the content of a folder")
# my_parser = argparse.ArgumentParser(prog='CLI', description='List the content of a folder')
# my_parser = argparse.ArgumentParser(prog="CLI", usage='%(prog)s [option] path', description='List the content of a folder', epilog="Enjoy the program!")

my_parser = argparse.ArgumentParser(prog="CLI",
                                    usage='%(prog)s [option] path',
                                    description='List the content of a folder',
                                    epilog="Enjoy the program!",
                                    prefix_chars='/')


# add the arguments
# if add -h to the command line it will show : the path to list
my_parser.add_argument('Path', metavar='path', type=str, help='the path to list')

# execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("the path does not exist")
    sys.exit()

print("\n".join(os.listdir(input_path)))

# how to run :  python argParse_console.py "FolderName"  => lists name of all folders

# ========================================
import argparse
import os
import sys

my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

my_parser.add_argument('a', help ='a first argument')
my_parser.add_argument('b', help='a second argument')
my_parser.add_argument('c', help='a third argument')
my_parser.add_argument('d', help='a fourth argument')
my_parser.add_argument('e', help='a fifth argument')

args = my_parser.parse_args()

print("its good!")

# how to run : python argParse_console.py x y z w y  => if all arguments are not available will give an error

# ========================================
import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()
print(args.input, args.id)

# how to run : python argParse_console.py --input 12 --id 13  => entering id is NOT required

# ========================================
import argparse

my_parser = argparse.ArgumentParser(description='List the contents of a folder', add_help=False)
agrs = my_parser.parse_args()

# if you write an argument for this code, it will return an error since we didnt add any args in the code

# ========================================
import argparse
import os
import sys

my_parser = argparse.ArgumentParser(description='List the contents of a folder')

my_parser.add_argument('Path', metavar='path', type=str, help='the path to a list')
my_parser.add_argument('-l', '--long', action='store_true', help='enable the long listing format')

args= my_parser.parse_args()
input_path = args.Path

if not os.path.isdir(input_path):
    print("error, no dir")
    sys.exit()

for line in os.listdir(input_path):
    if args.long:
        # get size of each file/folder
        size = os.stat(os.path.join(input_path, line)).st_size
        line = "%10d %s" % (size, line)
    print(line)

# python argParse_console.py folderName: just lists the folder/files
# python argParse_console.py folderName -l  : lists the folders/files and shows their sizes

# ========================================
import argparse

my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'

my_parser.add_argument('-a', action='store')
my_parser.add_argument('-b', action='store_true')
my_parser.add_argument('-c', action='store_false')
my_parser.add_argument('-d', action='append')
my_parser.add_argument('-e', action='append_const', const=3)  # max size of this argument is 42 characters
my_parser.add_argument('-f', action='count')
my_parser.add_argument('-j', action='version')

args = my_parser.parse_args()

print(vars(args))

# how to use:
# -a string : saves that string
# -b returns False | returns True if used
# -c returns True | returns False if used
# -f returns 1 |-ff returns 2
# -d a returns ['a']  | -d a,b,c returns ['a', 'b', 'c']
# -j returns version 1.0
# -e returns the constant 3

# ========================
import argparse

# custom action: it is done by subclassing the argparse.Action class and implementing a couple of methods

class VerboseStore(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(VerboseStore, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print(values, option_string)
        setattr(namespace, self.dest, values)


my_parser = argparse.ArgumentParser()
my_parser.add_argument('-i', '--input', action=VerboseStore, type=int)
args = my_parser.parse_args()
print(vars(args))

# how to use: python3 argParse_console.py -i 1357  returns {'input': 1357}

# =========================
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', nargs=3)

args = my_parser.parse_args()
print(args.input)

# how to use: here we force the user to enter at least 3 arguments without naming them in the code

# ========================
import argparse

my_parser = argparse.ArgumentParser()

# nargs= ? : only one or none
# nargs= * : a flexible number of values, which will ba gathered into a list
# nargs= + : at least one or more saved into a list

my_parser.add_argument('input', action='store', nargs='?', default='my default value')

args = my_parser.parse_args()
print(args.input)

# if user doesn't enter any values we will use the default

# ======================
import argparse

my_parser = argparse.ArgumentParser()

# nargs = argparse.REMAINDER : all the values that are remaining in the command line
my_parser.add_argument('first', action='store')
my_parser.add_argument('others', action='store', nargs=argparse.REMAINDER)

args = my_parser.parse_args()

print(args.first)
print(args.others)

# how to: the first argument user enters becomes first, rest of them will be added to a list as others

# ======================
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', default='42')

args = my_parser.parse_args()
print(vars(args))

# if user doesnt add any argument, a will become 42 by default

# ====================
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', choices=['head', 'tail'])

args = my_parser.parse_args()

# if you enter anything except head or tail after -a it will give an error

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', type=int, choices=range(1, 5))

args = my_parser.parse_args()
print(vars(args))

# if the input is anything outside 1-4 range, CLI will give back an error

# ==========================
import argparse

# you can only use -s or -v, can't use them both in same command
my_parser = argparse.ArgumentParser()
my_group = my_parser.add_mutually_exclusive_group(required=True)

my_group.add_argument('-v', '--verbose', action='store_true')
my_group.add_argument('-s', '--silent', action='store_true')

args = my_parser.parse_args()
print(vars(args))

# python3 argParse_console.py --silent : {'verbose': False, 'silent': True}




