# calling_process.py
# The following modules must be imported


import os
import sys


# this is the code to execute
program = "python"
print("Process calling")
arguments = ["called_process.py"]

# we cal the called_process.py script todo
os.execvp(program, (program, ) + tuple(arguments))
print("Good bye!!")

