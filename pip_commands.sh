### PIP ###

pip help  # shows all command options
pip help install  # shows all command options for "install"
pip search packageName  # tries to find if package with such name exists
pip install packageName
pip uninstall packageName
pip install -U packageName   # updates the package
pip list  # shows list of all installed packages
pip list -o  # all outdated packages that need update
pip freeze > requirements.txt  # get a list of all packages and their versions and send it to a file
pip install -r requirements.txt  # read list of packages from a file and install them


# How to activate an Anaconda environment?
# create an environment called py33 by using:
conda create -n py33 python=3.3 anaconda
# set the PATH as:
set PATH=C:\Anaconda\envs\py33\Scripts;C:\Anaconda\envs\py33;%PATH%
# inside the cmd:
activate py33
# in linux/mac:
source activate py33

# Creating password using Python passlib
# first install the package
sudo pip install passlib
# import the hash algorithm
from passlib.hash import sha256_crypt
# generate new salt, and hash a password
hash = sha256_crypt.encrypt("toomanysecrets")
print(hash)

# where does anaconda python install in windows?
'''
To find where Anaconda was installed I used the "where" command on the command line in Windows.
C:\>where anaconda
which for me returned:
C:\Users\User-Name\AppData\Local\Continuum\Anaconda2\Scripts\anaconda.exe
'''

# What is the meaning of “Failed building wheel for X” in pip install?
'''
If the package is not a wheel, pip tries to build a wheel for it (via setup.py bdist_wheel). If that fails for any
reason, you get the "Failed building wheel for pycparser" message and pip falls back to installing directly
(via setup.py install).
Once we have a wheel, pip can install the wheel by unpacking it correctly. pip tries to install packages via wheels as
often as it can. This is because of various advantages of using wheels (like faster installs, cache-able, not executing
 code again etc).
'''

# how to specify new environment location for conda create?
# Will create the environment named "test-env" which resides in /tmp/ instead of the default .conda
conda create --prefix /tmp/test-env python=3.7

# How to change the Jupyter start-up folder
'''
Use the jupyter notebook config file:
Open cmd (or Anaconda Prompt) and run jupyter notebook --generate-config.
This writes a file to C:\Users\username\.jupyter\jupyter_notebook_config.py.
Browse to the file location and open it in an Editor
Search for the following line in the file: #c.NotebookApp.notebook_dir = ''
Replace by c.NotebookApp.notebook_dir = '/the/path/to/home/folder/'
Make sure you use forward slashes in your path and use /home/user/ instead of ~/ for your home directory, backslashes could be used if placed in double quotes even if folder name contains spaces as such : "D:\yourUserName\Any Folder\More Folders\"
Remove the # at the beginning of the line to allow the line to execute
'''