# Subprocess
# we can use subprocess module to run external commands via python, it is very easy to handle shell scripting code
# and linux command line via subprocess
import sys
import subprocess

subprocess.run("ls", shell=True)
subprocess.run("ls -la", shell=True)  # get file
subprocess.run(['ls', '-la'])  # without shell command

p1 = subprocess.run(['ls', '-la'])
print(p1.args)
print(p1.returncode)  # return code 0 means ran successfully | return 1 means there was some error

p1 = subprocess.run(['ls', '-la'], capture_output=True)  # capture output of subprocess to the variable p1
print(p1.stdout.decode())  # since p1 output is in bytes we use .decode() to convert it to utf-8

p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)  # capture it as text instead of bytes
print(p1.stdout)

p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)  # does same thing as above code
print(p1.stdout)

# write to text file
with open('output.txt', 'w') as f:
    p1 = subprocess.run(['ls', '-la'], stdout=f, text=True)

# handling errors
# this stands for name of the folder
p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)
print(p1.stderr)  # show the error that we get
if p1.returncode != 0:
    sys.exit()

# check=True : throws an exception if we get an error
p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True, check=True)

# make output of one command input of another command
# cat command in linux looks at files
p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
# grep command in linux searches the files
p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

# same as above but in one line
p1 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)
