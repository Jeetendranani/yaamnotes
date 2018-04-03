"""
66. Plus One

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""


class Solution:
    def plussOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
            if carry == 0:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits


"""
11.1. Output Formatting

The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested 
containers:

The pprint module offers more sophisticated control over printing both built-in and user defined objects in a way that 
is readable by the interpreter. When the result is longer than one line, the "pretty printer" adds line breaks and 
indentation to more clearly reveal data structure:

The textwrap module formats paragraphs of text to fit a given screen width:

The local module accesses a database of culture specific data formats. The grouping attribute of locale's format 
function provides a direct wa of formatting numbers with group separators:

11.2. Templating

The string module includes a versatile Template class with a simplified syntax suitable for editing by end-user. This 
allows users to customize their applications without having to alter the application. 

The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores).
Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening
spaces. Writing $$ creates a single escaped $:

The substitute() method raise a KeyError when a placeholder is not supplied in a dictionary or a keyword argument. For
mail-merge style applications, user supplied data may be incomplete and the safe_substitute() method may be more 
appropriate - it will leave placeholders unchanged if data is missing:

Template subclasses can specify a custom delimiter. For example, a batch renaming utility for a photo browser may elect 
to use percent signs for placeholders such as the current date, image, sequence number, or file format:

Another application for templating is separating program logic from the details of multiple output formats. This makes 
it possible to substitute custom templates for XML files, plain text reports, and HTML web reports.

11.3. Working with binary dta record layouts

The struct module provides pack() and unpack() functions for working with variable length binary record formats. The 
following example shows how to loop through header information in a ZIP file without using the zipfile module. Pack
codes 'H' and 'I' represent two and four byte unsigned numbers respectively. The '<' indicates that they are standard 
size and in little-endian byte order:
"""


import struct



with open("myfile.zip", 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size


"""
11.4. Multi-threading

Threading is a technique for decoupling tasks which are not sequentially dependent. Threads can be used to improve the 
responsiveness of applications that accept user input while other tasks run in the background. A related use case is 
running I/O in parallel with computations in another threadd.

The following code shows how the high level threading module can run tasks in background while the main program 
continues to run:
"""

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w' zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of :', self.infile)

background = AsyncZip('mydata.txt', 'my.zip')
background.start()
print("The main program continues to run in foreground.")

background.join()
print("Main program waited until background was done.")


"""
The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. To 
that end, the threading module provides a number of synchronization primitives including locks, events, condition 
variables, and semaphores.

While those tools are powerful, minor design erros can result in problem that are difficult to reproduce. So, the 
preferred approach to task coordination is to concentrate all access to resource in a single thread and then use the 
queue module to feed that thread with requests from other threads. Applications using Queue Objects for inter-thread 
communication and coordination are easier to design, more readable, and more reliable.

11.5. Logging

The logging module offers a full featured and flexible logging system. At its simplest, log messages are sent to a file
or sys.stderr:
"""


import logging
logging.debug("Debugging information")
logging.info("Informational message")
logging.warning("Warning: config file %s not found", 'server.config')
logging.error("Error occurred")
logging.critical("Critical error -- shutting down")


"""
by default, informational and debugging message are suppressed and the output is send to standard error. Other output
options include routing messages through email, datagrams, sockets, or to an HTTP Server, new filters can select 
different routing based on message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

The logging system can be configured directly from Python or can be loaded from a user editable configuration file for
customized logging without altering the application.

11.6. Weak References

Python does automatic memory management (reference counting for most objects and garbage collection to eliminate 
cycles). The memory is freed shortly after the last reference to it has ben eliminated. 

This approach works fine for most applications but occasionally there is a need to track objects only as long as they
are being used by something else. Unfortunately, just tracking them creates a reference that makes them permanent. 
The weakref module previous tools for tracking objects without creating a reference, when the object is no longer 
needed, it is automatically removed from a weekref table and a callback is triggered for weekref objects. Typical 
applications include caching objects that are expensive to create:

11.7. Tools for working with lists

Many data structure needs can be met with the built-in list type. However, sometimes there is a need for alternative 
implementations with different performance trade-offs.

The array module provides an array() object that is like a lit that store only homogeneous data and stores it more 
compactly. the following example shows an array of numbers stored as two byte unsigned binary numbers (typecode "H")
rather than the usual 16 bytes per entry for regular lists of Python int objects:

The collections module provides a deque() object that is like a list with faster appends and pops from the left side 
but slower lookups in the middle. These objects are well suited for implementing queues and breadth first tree searches:

In addition to alternative list implementations, the library also offers other tools such as the bisect module with
functions for manipulating sorted lists:

the heapq module provides functions for implementing heaps based on regular lists. The lowest valued entry is always 
kept at position zero. This is useful for applications which repeatedly access the smallest element but do not want to
run a full list sort:

11.8. Decimal floating point arithmetic

The decimal module offers a Decimal datatype for decimal floating point arithmetic. Compared to the the built-in float
implementation of binary floating point, the class is especially helpful for:
    - financial applications and other uses which require exact decimal representation.
    - control over precision
    - control over rounding to meet legal or regulatory requirements.
    - Tracking of significant decimal places. or
    - applications where the user expects the results to match calculations done by hand.
    
For example, calculating a 5% tax on a 70 cent phone charge gives different result in decimal floating point and binary
floating point. The different becomes significant if the results are rounded to the nearest cent:

The decimal result keeps a trailing zero, automatically inferring four place significance from multiplicands with two
place significance. Decimal reproduces mathematics as done by hand and avoids issues that can arise when binary floating
point cannot exactly represent decimal quantities.

Exact representation enables the decimal class to perform modulo calculations and equality tests that are unsuitable 
for binary floating point.

The decimal module provides arithmetic with as much precision as needed:

12. Virtual Environments and packages

12.1. Introduction

Python applications will often use packages and modules tht dont' come as part of the standard library. Applications 
will sometimes need a specific version of a library, because the application may require that a particular bug has 
been fixed or the application may be written using an obsolete version of the library's interface.

This means it may not be possible fo one Python installation to meet the requirements of every application. If 
application A needs version 1.0 of particular module but application B needs version 2.0, then the requirements are in 
conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

The solution for this problem is to create a virtual environment (often shortened to "virtualenv"), a self-contained 
directory tree that contains a Python installation for a particular version of Python, plus a number of additional 
packages.

Different applications can then use different virtual environments.  To resolve the earlier example of conflicting 
requirements, application A can have its own virtual environment with version 1.0 installed while application B has 
another virtualenv with version 2.0. If application B requires a library be upgraded to version 3.0, this will not  
affect application A's environment.

12.2. Creating Virtual Environment

The script used to create and manage virtual environments is called pyvenv, pyvenv will usually installed the most 
version of Python that you have available; the script is also installed with a version number, so if you have multiple 
versions of python on your system you cna select a specific Python version by running pyvenv-3.4 or whichever version 
you want.

To create a virtualenv, decide upon a directory where you want to place it and run pyvenv withe the directory path:

pyvenv tutorial-env

This will create the tutorial-env directory if it doesn't exist, and also create directories inside it containing a 
copy of the Python interpreter, teh standard library, and various supporting files.

Once you've created a virtual environment, you need to activate it.

On windows, run: 

tutorial-env/scripts/activate

On unix or maxos, run:

source tutorial-env/bin/activate

This script is written for the bash shell. If you use csh or fish shells, there are alternate activate.csh and 
activate.fish script you should use instead.)

Activating the virtualenv will change your shell's prompt to show what virtualenv you're suing, and modify the
environment so that running pathon will get you that particular version and installation of Python. For example:

12.3. Managing Packages with pip

Once you've activated a virtual environment, you can install, upgrade and remove packages using a program called pip.
By default pip will install packages from the Python package index. you can browser the Python package index by going
to it in your web browser, or you can use pip's limited search feature:

pip has a number of subcommands: "search", "install", "uninstall", "freeze", etc

you can install the latest version of package by specifying a packages's name:

You can also install a specific version of package by giving the package name followed by == and the version number:

If you re-run this command, pip will notice that the requested version is already installed and do nothing. You can 
supply a different version number to get that version, or you can run pip install --upgrade to ugrade the package the 
latest version:

Pip uninstall followed by one or more package names will remove the packages form the virtual environment.

pip show will display information about a particular package from the virtual environment.

pip show will display information about a particular package:

pip list will display all of teh packages installed in the virtual environment:

pip freeze will produce a similar list of the installed packages, but the output uses the format that pip install 
expects. A common convention is to put this list in a requirements.txt file:

The requirements.txt can then be committed to version control and sipped as part of an application. User can then 
install all the necessary packages with install -r.

pip has many more options. consult the Installing Python Modules guide for complete documentation for pip. When you've
written a package and want to make it available on the Python Package Index, consult the Distributing Python Modules 
guide.

13. What Now?

Reading this tutorial has probably reinforced your interest in using Python - You should be eager to apply Python to 
solving your real-world problems. Where should you go to learn more?

This tutorial is part of Python's documentation set. Some other documents in the set are:

    - The Python standard Library:
    You should browse through this manual, which gives complete (though terse) reference material about types, 
    functions, and modules in the standard library. The standard Python distribution includes a lot of additional code.
    There are modules to read Unix mailboxes, retrieve documents via HTTP, generate random numbers, parse command-line
    options, write CGI programs, compress data, and many other tasks. Skimming through the Library Reference will give 
    you an idea of what's available. 
    
    - Installing Python modules explains how to install additional modules written by other Python users.
    - The Python language Reference: A detailed explanation of python's syntax and semantics. It's heavy reading, but 
    is useful as a complete guide to the language itself.
    
More Python resources:
    
    - https://www.python.org: The major Python Web site. It contains code, documentation, and pointers to 
    Python-related pages around the Web. This Web site is mirrored in various places around the world, such as Europe,
    Japan, and Australia; a mirror may be faster than the main site, depending on your geographical location.
    
    - https://docs.python.org: Fast access to Python's documentation.
    
    - https://pypi.python.rog/pypi: The Python package index, previously also nicknamed the Cheese Shop, is an index of
    user-created Python modules that are available for download. Once you begin releasing code, you can register it 
    here so that others can find it.
    
    - https://code.actiestate.com/recipes/langs/python/: The python cookbook is a sizable collection of code examples,
    large modules, and useful scripts. particularly notable contributions are collected in a book also titled Python
    Cookbook.
    
    - http://www.pyvideo.org collects links to Python related videos from conferences and user-group meetings.
    
    - https://scipy.org: The scientific Python project includes modules for fast array computations and manipulations
    plus a host of packages for such things as linear algebra, Fourier transforms, non-linear solvers, random number 
    distributions, statistical analysis and the like. 
    
for Python -related question and problem reports, you can posted to teh newsgroup comp.lang.python, or send them to the
mailing list at python-list@python.org. The newsgroup and mailing list are gatewayed, so messages posted to one will 
automatically be forwarded to the other. There are hundreds of postings a day, asking (and answering) questions, 
suggesting new features, and announcing new modules. Mailing list archives are available at 
http://mail.python.org/pipermail/.

14. Interactive input editing and history substitution

Some version of the python interpreter support editing of the current input line and history substitution, similar to
facilities found in the korn shell and ghe GNU bash shell. This is implemented using the GUN Raedline library, which 
supports various styles of editing. This library has its own documentation which we won't duplicate here.

14.1. Tab completion and History Editing

Completion of variable and module name is automatically enabled at interpreter startup so that the Tab key invokes the 
completion function; it looks at Python statement names, the current local variables and the available module names. 
For dotted expression such as string.a, it will evaluate the expression up to the final '.' and then suggest completions 
from the attributes of the resulting object. Note that this amy execute application-defined code if an object with a 
__getattr__() method is part of the expression. The default configuration also saves your history into a file named 
.python_history in your user directory. The history will be available again during the next interactive interpreter 
session.

14.2. Alternatives to the interactive interpreter

This facility is an enormous step forward compared to earlier versions of the interpreter; however, some wishes are 
left: It would be nice if the proper indentation were suggested on continuation lines (the parser knows if an indent 
token is required next). The completion mechanism might use the interpreter's symbol table. A command to check (or even 
suggest) matching parentheses, quotes, etc., would also be useful.

One alternative enhanced interactive interpreter has been around for quite some time is Ipython, which features tab 
completion, object exploration and advanced history management. It can also be thoroughly customized and embedded 
into other applications. Another similar enhanced interactive environment is bpython.

15. Floating Point Arithmetic: Issues and Limitations

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions, For example, the decimal 
fraction

0.125

has value 1/10 + 2/100 + 5/1000, and in the same way the binary fraction

0.001

has value 0/2 + 0/4 + 1/8. This two fraction have identical values, the only real difference being that the first is 
written in base 10 fractional notation, and the second in base 2.

Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. A consequence is that, in 
general, the decimal floating-point numbers you enter are only approximated by the binary floating-point numbers 
actually stored in the machine.

The problem is easier to understand at first in base 10, Consider the fraction 1/3. you can approximate that as a base
10 fraction:

0.3

or, better

0.33

or better

0.333

and so on. No matter how many digits you're willing to write down, the result will never be exactly 1/3, but will be 
an increasingly better approximation of 1/3.

In the same way, no matter how many base 2 digits you're willing to use, the decimal value 0.1 can't be represented 
exactly as a base 2 fraction. In base 2, 1/10 is the infinitely repeating fraction

0.000110011001100110011...

Stop at any finite number of bits, and you get an approximation. On most machines today, floats are approximate using
a binary fraction with the numerator using the first 53 bits starting with the most significant bit and with the 
denominator as a power of two. In the case of 1/10, the binary fractioin is 3602879701896397 / 2 ** 55 which is close
to but not exactly equal to the true value of 1/10.

Many users are not aware of the approximation because of the way values are displayed. Python only prints a decimal 
approximation to the true decimal value of the binary approximation stored by the machine. On most machines, if Python
were to print hte true decimal value of the binary approximation stored for 0.1, it would have to display

>>> 0.1
0.1000000000000000055511151231257827021181583404541015625

That is more digits than most people find useful, so Python keeps the number of digits manageable by displaying a 
rounded value instead.

Just remember, even though the printed result looks like the exact value 1/10, the actual stored value is the nearest 
representation binary fraction.

Interestingly, there are many different decimal number that share the same nearest approximate binary fraction. For 
example the number 0.1 and 0.10000000000000000001 are all approximated by 3602879701896397 / 2 ** 55. Since all of these
decimal values share the same approximation, andy one of them could be displayed while still preserving the invariant 
eval(repr(x)) == x.

Historically, the python prompt and built-in repr() function would choose the one with 17 significant digits. Starting 
with Python 3.1, python (on most systems) is now to choose the shortest of these and simply display 0.1.

Note that this is the very nature of binary floating-point: this is not a bug in Python, and it is not a bug in your 
code either. you'll see the same kind of thins in all languages that support you hardware's floating-point arithmetic
(although some language may not display the difference by default, or in all output modes).

For more pleasant output, you may wish to use string formatting to produce a limited number of significant digits:

It is important to realize that this is, in a real sense, an illusion: you're simply rounding the display of the true 
machine value.

One illusion may beget another. For example, since 0.1 is not exactly 1/10, summing three values of 0.1 may not yield 
exactly 0.3, either:

>>> .1 + .1 + .1 == .3
False

Also, since the 0.1 cannot get any closer to the exact value of 1/10 and 0.3 can't get any closer to the exact value 
of 3/10, then pre-rounding with round() function cannot help:

>>> round(.1, 1) + round(.1, 1) + round(.1 1) == round(.3, 1)
False

Though the number can't be made close to their intended exact values, the round() function can be useful for 
post-rounding so that results with inexact value become comparable to one another:

>>> round(.1 + .1 + .1, 10) == round(.3, 10)
True

Binary floating-point arithmetic holds many surprises like this. the problem with "0.1" is explained in precise detail
below, in the "representation error" section. see the perils of floating point for a more complete account of other 
common surprises.

As that sys near the end, "there are no easy answers." Still, don't be unduly wary of floating-point! The errors in 
Python float operations are inherited from teh floating-point hardware, and on most machines are on the order of no
more than 1 part in 2 ** 53 per operation. That's more than adequate for most tasks, but you do need to keep in mind
that it's not decimal arithmetic and that every float operation can suffer a new rounding error.

While pathological cases do exist, for most casual use of floating-point arithmetic you'll see the result you expect in 
the end if you simply round the display of your final results to the number of decimal digits you expect. str() usually
suffices, and for finer control see teh str.format() method's format specifiers in Format String Syntax.

For use cases which require exact decimal representation, try using the decimal module which implements decimal 
arithmetic suitable for accounting applications, and high precision applications.

Another form of exact arithmetic is supported by the fractions module which implements arithmetic based on rational 
numbers (so the number like 1/3 can be represented exactly).

If you are heavy user of floating point operations you should take a look at the Numerical Python package and many other
packages for mathematical and statistical operations supplied by the SciPy project.

Python provides tools that may help on those rare occasions when you really do want to know the exact value of a float.
The float.as_integer_ratio() method expresses the value of a float as a fraction:

Since th ratio is exact, it can be used to losslessly recreate the original value:

The float.hex() method expresses a float in hexadecimal (base 16) again giving the exact value stored by your computer:

This precise hexadecimal representation can be used to reconstruct the float value exactly.

Since the representation is exact, it is useful for reliably porting values across different versions of Python 
(platform independence) and exchanging data with other languages that support the same format (such as Java and C99).

Another helpful tool is math.fsum() function which helps mitigate loss-of-precision during summation. It tracks "lost
digits" as values are added onto a running total. That can make a difference in overall accuracy so that the error
do not accumulate to the point where they affect the final total:

15.1. Representation Error
"""